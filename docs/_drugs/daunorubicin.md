---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Daunorubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is an anthracycline antibiotic that has been a cornerstone of acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL) induction therapy for decades.
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma (HL)**, supported by strong anthracycline class evidence and one early pilot study of liposomal daunorubicin in relapsed/refractory lymphoma.
Evidence is graded **L3**, reflecting substantial indirect class-level support but the absence of a dedicated daunorubicin Phase 2/3 RCT in HL.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia (AML / ALL) — EU authorization data not captured in current dataset |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| EU Market Status | Not marketed (no EU authorizations found in current dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Daunorubicin is one of the founding members of the anthracycline class of chemotherapeutics. Its mechanism centres on DNA intercalation and inhibition of topoisomerase II (Topo II), which stalls replication forks and triggers apoptosis in rapidly dividing cancer cells. Detailed formal MOA data is not available in the current regulatory dataset; however, this mechanism is well-established in the pharmacological literature and confirmed by references within the evidence pack itself (PMID 14584273, which explicitly describes daunorubicin and cytarabine as the foundational AML induction combination).

Hodgkin's lymphoma is uniquely sensitive to anthracycline-based chemotherapy. The ABVD regimen — the global standard first-line therapy for HL — anchors on **doxorubicin** (hydroxydaunorubicin), a close structural analogue of daunorubicin that shares the same DNA-intercalation and Topo II inhibition mechanism. This pharmacological kinship is not incidental: daunorubicin and doxorubicin differ by a single hydroxyl group at C-14, producing overlapping cytotoxic profiles against lymphoid malignancies. Multiple completed Phase 3 trials in HL (NCT00678327, n=1,202; NCT00049595, n=552; NCT00025259, n=1,734) have validated anthracycline-containing regimens as the therapeutic backbone for this disease.

Critically, liposomal daunorubicin (DaunoXome) was directly evaluated in 19 patients with relapsed or refractory lymphoma in a 1997 pilot study (PMID 9387047). At the higher dose schedule (120 mg/m²), objective responses were observed (1 CR + 2 PRs) with a favourable cardiac safety profile — providing direct proof-of-concept that daunorubicin reaches and is active in lymphoma tissue. Modern targeted liposomal co-delivery formulations incorporating daunorubicin (PMID 31239668) further demonstrate ongoing translational interest in repurposing this agent with improved delivery strategies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678327](https://clinicaltrials.gov/study/NCT00678327) | Phase 3 | Completed | 1,202 | Randomised PET-adapted therapy in newly diagnosed advanced HL using ABVD; FDG-PET/CT assessed response to anthracycline-containing chemotherapy |
| [NCT00049595](https://clinicaltrials.gov/study/NCT00049595) | Phase 3 | Completed | 552 | BEACOPP (escalated+baseline) vs ABVD in Stage III–IV HL; head-to-head comparison of two anthracycline-based strategies |
| [NCT00025259](https://clinicaltrials.gov/study/NCT00025259) | Phase 3 | Completed | 1,734 | Response-based dose-intensive chemotherapy ± radiotherapy in children and adolescents with intermediate-risk Hodgkin's disease |
| [NCT00736320](https://clinicaltrials.gov/study/NCT00736320) | Phase 3 | Unknown | 1,150 | HD16 treatment optimisation for early-stage HL using FDG-PET stratification; large-scale ABVD-based trial |
| [NCT01777152](https://clinicaltrials.gov/study/NCT01777152) | Phase 3 | Completed | 452 | Brentuximab vedotin + CHP (cyclophosphamide-doxorubicin-prednisone) vs CHOP in CD30+ mature T-cell lymphomas; strongest evidence for doxorubicin-backbone in CD30+ disease |
| [NCT00025064](https://clinicaltrials.gov/study/NCT00025064) | Phase 2 | Unknown | 260 | Multi-arm chemotherapy ± radiotherapy ± stem cell transplant protocol for children and adolescents with Hodgkin's disease; includes anthracycline-based induction |
| [NCT01771107](https://clinicaltrials.gov/study/NCT01771107) | Phase 1/2 | Completed | 41 | AVD (doxorubicin-vinblastine-dacarbazine) + brentuximab vedotin in Stage II–IV HIV-associated HL; demonstrates AVD tolerability in immunocompromised HL patients |
| [NCT00654732](https://clinicaltrials.gov/study/NCT00654732) | Phase 2 | Completed | 58 | Rituximab + ABVD vs ABVD alone in high-risk (IPS >2) advanced-stage classical HL; anthracycline backbone maintained |
| [NCT00797472](https://clinicaltrials.gov/study/NCT00797472) | Phase 2 | Unknown | 120 | R-mabHD monoclonal antibody vs ABVD in Hodgkin's disease; randomised comparison with standard anthracycline-based chemotherapy as control arm |
| [NCT06377566](https://clinicaltrials.gov/study/NCT06377566) | Phase 2 | Recruiting | 71 | BV-AVD (brentuximab vedotin + doxorubicin-vinblastine-dacarbazine) in newly diagnosed early-stage bulky HL using PET-adapted approach |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT Phase 3 | N Engl J Med | Nivolumab + AVD vs BV-AVD vs ABVD in advanced-stage classic HL; PD-1 blockade added to anthracycline backbone improves outcomes in adults and children |
| [29224502](https://pubmed.ncbi.nlm.nih.gov/29224502/) | 2018 | RCT Phase 3 | N Engl J Med | Brentuximab vedotin + AVD vs ABVD in Stage III–IV HL; BV-AVD demonstrated superior progression-free survival, validating doxorubicin-based platform |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT Follow-up | N Engl J Med | 5-year follow-up of BV-AVD trial showing durable overall survival benefit; longest-term anthracycline-based HL trial outcome data |
| [36322844](https://pubmed.ncbi.nlm.nih.gov/36322844/) | 2022 | RCT | N Engl J Med | Brentuximab vedotin + multiagent chemotherapy in high-risk pediatric HL; established BV-AVD efficacy and safety in children |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Early Phase/Pilot | Investig New Drugs | **Direct daunorubicin evidence**: Liposomal daunorubicin (DaunoXome) in 19 relapsed/refractory lymphoma patients; 120 mg/m² achieved 1 CR + 2 PRs with no clinical cardiac deterioration |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Review | Cancer Treat Rep | Comparative analysis of daunorubicin and doxorubicin (adriamycin) in cancer treatment; defines pharmacological similarities and clinical differentiation between the two anthracyclines |
| [30139285](https://pubmed.ncbi.nlm.nih.gov/30139285/) | 2018 | Review | Expert Rev Hematol | Sequencing of novel therapies in relapsed HL; anthracycline-based salvage context with CR rates up to 94% in frontline ABVD |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Risk-adapted and response-adapted treatment strategies for early-stage HL; discusses role of anthracycline dose reduction vs intensification |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Cancer Chemother | Confirms daunorubicin + cytarabine as foundational AML therapy; also notes ABVD as the Phase 3-validated standard for advanced HL, establishing the anthracycline class bridge |
| [6085157](https://pubmed.ncbi.nlm.nih.gov/6085157/) | 1984 | Review | Pediatr Med Chir | Historical 15-year data on childhood Hodgkin's disease outcomes; 90% 5-year survival with anthracycline-inclusive regimens, establishing long-term benefit benchmark |

---

## EU Market Information

No EU marketing authorizations for Daunorubicin were identified in the current dataset. Daunorubicin is used in clinical practice under hospital exemptions and national authorizations (e.g., as liposomal formulation DaunoXome in some markets), but formal EMA-level marketing authorization data was not captured for this candidate. Please consult the EMA product database for the most current regulatory status.

---

## Cytotoxicity

Daunorubicin is an anthracycline antibiotic and a classical cytotoxic chemotherapy agent. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (Topo II inhibitor / DNA intercalator) |
| Myelosuppression Risk | High — Severe myelosuppression is the primary dose-limiting toxicity; neutropenia and thrombocytopenia are expected and typically reach nadir at 10–14 days post-dose |
| Emetogenicity Classification | Moderate to High — Risk is dose-dependent; prophylactic antiemetics recommended per institutional protocol |
| Monitoring Items | CBC with differential (pre-dose and at nadir), cardiac function (LVEF by echocardiogram or MUGA scan at baseline and after cumulative dose thresholds), hepatic function (bilirubin, transaminases), renal function |
| Handling Protection | Must be handled as a cytotoxic agent — closed-system drug transfer devices, biological safety cabinet preparation, PPE including gloves and gown; disposal per cytotoxic waste regulations |

> Note: Formal safety data was not available in the current dataset. The information above reflects established pharmacological knowledge for the anthracycline class. Please refer to the SmPC for product-specific warnings and dose adjustments.

---

## Safety Considerations

Please refer to the SmPC for safety information. No formal key warnings, contraindications, or drug–drug interaction data were captured for this candidate in the current dataset.

> As an anthracycline, clinicians should be particularly attentive to **cumulative cardiotoxicity**: the risk of congestive heart failure rises substantially above cumulative daunorubicin doses of 550 mg/m², and prior anthracycline exposure must be considered in lifetime cumulative dose calculations.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Daunorubicin's mechanism is pharmacologically congruent with the anthracycline backbone of HL therapy, and the 1997 DaunoXome pilot study provides direct proof-of-concept for lymphoma activity. However, the L3 evidence rating reflects a fundamental gap: no dedicated Phase 2/3 RCT has tested daunorubicin (or its liposomal formulation) specifically in Hodgkin's lymphoma, and modern HL therapy has consolidated around doxorubicin + novel agents (BV, nivolumab) rather than exploring anthracycline substitution.

**To proceed, the following is needed:**
- Retrieval of formal MOA and safety data from DrugBank (data gap DG001 and DG002 must be resolved before any S1 safety screening)
- Assessment of whether liposomal daunorubicin (DaunoXome, if available) represents a more competitive formulation than standard daunorubicin given the existing doxorubicin-dominated landscape
- Identification of a specific unmet niche within HL where daunorubicin could be differentiated — for example, patients with prior doxorubicin-induced cardiomyopathy where a liposomal formulation with a distinct cardiac profile might be advantageous
- Preclinical confirmation of daunorubicin activity in HL cell lines (L428, KMH2) or patient-derived xenograft models to build translational rationale before clinical development investment
- Clarification of EU/EMA regulatory status and pathway for a potential indication extension or new formulation approval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

