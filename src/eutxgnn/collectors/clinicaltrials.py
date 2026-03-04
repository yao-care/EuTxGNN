"""ClinicalTrials.gov evidence collector using API v2."""

import json
import re
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode

from .base import BaseCollector, CollectorResult


class ClinicalTrialsCollector(BaseCollector):
    """Collector for ClinicalTrials.gov clinical trial data."""

    source_name = "clinicaltrials_gov"

    # API v2 endpoint
    BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

    # Fields to retrieve
    FIELDS = [
        "NCTId",
        "BriefTitle",
        "OfficialTitle",
        "OverallStatus",
        "Phase",
        "StudyType",
        "EnrollmentCount",
        "StartDate",
        "CompletionDate",
        "Condition",
        "InterventionName",
        "InterventionType",
        "PrimaryOutcomeMeasure",
        "LocationCountry",
        "LeadSponsorName",
    ]

    def __init__(self, max_results: int = 50):
        """
        Initialize the collector.

        Args:
            max_results: Maximum number of results to return per query
        """
        self.max_results = max_results

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """
        Search ClinicalTrials.gov for trials involving a drug-disease pair.

        Args:
            drug: Drug name (generic or brand name)
            disease: Disease/indication name

        Returns:
            CollectorResult with trial data
        """
        query = {"drug": drug, "disease": disease}

        try:
            # Build search query
            search_terms = [drug]
            if disease:
                search_terms.append(disease)

            # API v2 query parameters
            params = {
                "query.term": " AND ".join(search_terms),
                "pageSize": min(self.max_results, 100),
                "fields": ",".join(self.FIELDS),
                "format": "json",
            }

            url = f"{self.BASE_URL}?{urlencode(params)}"
            req = Request(url, headers={"User-Agent": "EuTxGNN-Collector/1.0"})

            with urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))

            # Parse results
            trials = []
            for study in data.get("studies", []):
                protocol = study.get("protocolSection", {})
                id_module = protocol.get("identificationModule", {})
                status_module = protocol.get("statusModule", {})
                design_module = protocol.get("designModule", {})
                desc_module = protocol.get("descriptionModule", {})
                conditions_module = protocol.get("conditionsModule", {})
                arms_module = protocol.get("armsInterventionsModule", {})
                outcomes_module = protocol.get("outcomesModule", {})
                contacts_module = protocol.get("contactsLocationsModule", {})
                sponsor_module = protocol.get("sponsorCollaboratorsModule", {})

                # Extract phase
                phases = design_module.get("phases", [])
                phase = phases[0] if phases else "N/A"

                # Extract conditions
                conditions = conditions_module.get("conditions", [])

                # Extract interventions
                interventions = []
                for intervention in arms_module.get("interventions", []):
                    interventions.append({
                        "name": intervention.get("name", ""),
                        "type": intervention.get("type", ""),
                    })

                # Extract primary outcomes
                primary_outcomes = []
                for outcome in outcomes_module.get("primaryOutcomes", []):
                    primary_outcomes.append(outcome.get("measure", ""))

                # Extract countries
                locations = contacts_module.get("locations", [])
                countries = list(set(loc.get("country", "") for loc in locations if loc.get("country")))

                # Extract sponsor
                lead_sponsor = sponsor_module.get("leadSponsor", {})

                trial = {
                    "nct_id": id_module.get("nctId", ""),
                    "title": id_module.get("briefTitle", ""),
                    "official_title": id_module.get("officialTitle", ""),
                    "status": status_module.get("overallStatus", ""),
                    "phase": phase,
                    "study_type": design_module.get("studyType", ""),
                    "enrollment": design_module.get("enrollmentInfo", {}).get("count", 0),
                    "start_date": status_module.get("startDateStruct", {}).get("date", ""),
                    "completion_date": status_module.get("completionDateStruct", {}).get("date", ""),
                    "conditions": conditions,
                    "interventions": interventions,
                    "primary_outcomes": primary_outcomes[:3],  # Limit to 3
                    "countries": countries,
                    "sponsor": lead_sponsor.get("name", ""),
                    "url": f"https://clinicaltrials.gov/study/{id_module.get('nctId', '')}",
                }
                trials.append(trial)

            return self._make_result(query, trials)

        except (URLError, HTTPError) as e:
            return self._make_result(
                query, [], success=False, error_message=str(e)
            )
        except Exception as e:
            return self._make_result(
                query, [], success=False, error_message=f"Unexpected error: {e}"
            )

    def get_phase_score(self, phase: str) -> int:
        """
        Get a numeric score for trial phase (higher = stronger evidence).

        Args:
            phase: Phase string (e.g., "PHASE3", "Phase 2/Phase 3")

        Returns:
            Score from 0-4
        """
        phase_lower = phase.lower()
        if "phase 4" in phase_lower or "phase4" in phase_lower:
            return 4
        elif "phase 3" in phase_lower or "phase3" in phase_lower:
            return 4
        elif "phase 2" in phase_lower or "phase2" in phase_lower:
            return 3
        elif "phase 1" in phase_lower or "phase1" in phase_lower:
            return 2
        elif "early" in phase_lower:
            return 1
        return 0

    def evaluate_evidence_level(self, trials: list[dict]) -> str:
        """
        Evaluate evidence level based on clinical trials.

        Args:
            trials: List of trial dictionaries

        Returns:
            Evidence level (L1-L5)
        """
        if not trials:
            return "L5"  # No evidence

        # Count completed Phase 3 trials
        phase3_completed = sum(
            1 for t in trials
            if self.get_phase_score(t.get("phase", "")) >= 4
            and t.get("status", "").upper() == "COMPLETED"
        )

        # Count completed Phase 2 trials
        phase2_completed = sum(
            1 for t in trials
            if self.get_phase_score(t.get("phase", "")) == 3
            and t.get("status", "").upper() == "COMPLETED"
        )

        # Count any Phase 1/2 trials
        phase1_2_any = sum(
            1 for t in trials
            if self.get_phase_score(t.get("phase", "")) >= 2
        )

        if phase3_completed >= 2:
            return "L1"  # Multiple Phase 3 RCTs
        elif phase3_completed >= 1 or phase2_completed >= 2:
            return "L2"  # Single Phase 3 or multiple Phase 2
        elif phase2_completed >= 1:
            return "L3"  # Phase 2 evidence
        elif phase1_2_any >= 1:
            return "L4"  # Early phase evidence
        else:
            return "L5"  # No significant evidence
