---
layout: default
title: Talazoparib
parent: High Evidence (L1-L2)
nav_order: 565
evidence_level: L2
indication_count: 10
---

# Talazoparib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Talazoparib: From gBRCA-Mutated HER2-Negative Breast Cancer to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Talazoparib is a PARP inhibitor originally used to treat germline BRCA1/2-mutated, HER2-negative advanced or metastatic breast cancer. The TxGNN model's top-ranked prediction is **HER2-Positive Breast Carcinoma**, supported by **10 clinical trials** and **13 publications** in the Evidence Pack — however, closer inspection shows that most of this evidence actually describes **HER2-negative** patient populations, suggesting the top prediction is likely an ontology/label mismatch rather than a genuine new signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | gBRCA-mutated, HER2-negative locally advanced or metastatic breast cancer (as described in cited literature; no structured license data available) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not marketed (per data on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack. Based on the supporting literature, Talazoparib is a poly(ADP-ribose) polymerase (PARP) inhibitor that exploits **synthetic lethality** in tumors with homologous recombination deficiency (HRD), most commonly BRCA1/2-mutated tumors. Its proven efficacy is in HER2-negative, gBRCA-mutated breast cancer (established via the Phase 3 EMBRACA trial referenced in the literature), where blocking base-excision repair is lethal to cells already deficient in double-strand break repair.

Superficially, the original and predicted indications both fall under "breast cancer," which is why the TxGNN model may have linked them through shared knowledge-graph nodes. However, the approved indication is explicitly restricted to a **HER2-negative** population, while the top prediction proposes a **HER2-positive** population — a direct contradiction at the biomarker level, since HER2-driven tumors are typically treated with HER2-targeted therapy (e.g., trastuzumab-based regimens) rather than PARP inhibitors, and there is no established mechanistic link between PARP inhibition and HER2 signaling.

This concern is reinforced by the supporting evidence itself: several of the "supporting" clinical trials (e.g., NCT06735742, NCT03911973, NCT02401347) explicitly enroll **HER2-negative** or BRCA-mutant/triple-negative populations, and are flagged in the evidence annotations as likely ontology-matching errors ("label directly contradicts trial population"). One cited trial (NCT04508803) does not even involve talazoparib. Taken together, this indication should be treated as a **candidate requiring manual curation and re-verification** rather than a validated repurposing signal — the underlying mechanistic and trial-level evidence more strongly support extension into **HER2-negative, PR-negative/triple-negative breast cancer** (see rank 3 in the full prediction set, evidence level L2, "Proceed with Guardrails"), not HER2-positive disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | Neoadjuvant talazoparib in germline BRCA1/2-mutated **HER2-negative** early breast cancer — population is HER2-negative, not positive |
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | ctDNA-guided treatment-switch trial in HR-positive metastatic breast cancer; talazoparib's role is not the primary focus |
| [NCT06735742](https://clinicaltrials.gov/study/NCT06735742) | N/A (post-marketing) | Active, not recruiting | 3 | TALZENNA special investigation in BRCA-mutated, **HER2-negative** unresectable/recurrent breast cancer — directly contradicts the "HER2-positive" label (flagged as ontology mismatch) |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 + talazoparib in triple-negative or hormone-resistant/**HER2-negative** metastatic breast cancer; HER2 status ambiguous |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Recruiting | 36 | Talazoparib in advanced solid tumors with DNA damage response gene alterations; not HER2-specific |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib + talazoparib in triple-negative or BRCA1/2-positive, **HER2-negative** breast cancer — population contradicts predicted label |
| [NCT02401347](https://clinicaltrials.gov/study/NCT02401347) | Phase 2 | Completed | 21 | Talazoparib in BRCA wild-type TNBC/HRD or HER2-negative breast cancer/solid tumors with HR pathway mutations — BRCA wild-type, HER2 status not confirmed positive |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY 2 platform trial spanning multiple breast cancer subtypes (including HER2-positive arms), but not a talazoparib-specific design |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH basket trial exploring approved oncology drugs in biomarker-guided solid tumor patients; not talazoparib/HER2-specific |
| [NCT04508803](https://clinicaltrials.gov/study/NCT04508803) | Phase 2 | Completed | 37 | HX008 + niraparib (not talazoparib) in germline-mutated metastatic breast cancer — likely irrelevant to this indication pairing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | Review (ASCO Guideline) | J Clin Oncol | ASCO guideline update on systemic therapy for HR-positive, **HER2-negative** metastatic breast cancer |
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | Review/Meta-analysis (GRADE) | Breast (Edinburgh) | PARP inhibitors (olaparib, talazoparib) for BRCA1/2-related, **HER2-negative** advanced breast cancer — approval basis reiterated as HER2-negative |
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | Retrospective cohort | Frontiers in Immunology | Compares talazoparib vs. conventional chemotherapy; abstract text refers to "HER2-negative advanced BC," inconsistent with the title's "HER2-positive" wording |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | Real-world/observational | The Oncologist | Real-world US outcomes of talazoparib in gBRCA-mutated, **HER2-negative** advanced breast cancer |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase 1/2 trial report | Breast Cancer Res Treat | Gedatolisib + talazoparib in advanced triple-negative or BRCA1/2-positive, **HER2-negative** breast cancer |
| [35343197](https://pubmed.ncbi.nlm.nih.gov/35343197/) | 2022 | Review | Indian J Cancer | Role of PARP inhibitors in management of **HER2-negative** metastatic breast cancer |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | Real-world/observational | Clin Breast Cancer | Mayo Clinic real-world prescribing patterns and outcomes of PARP inhibitors in metastatic breast cancer |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | Retrospective | Mol Diagn Ther | Clinical actionability of molecular targets (incl. PARPi) in multi-ethnic breast cancer patients |
| [36202026](https://pubmed.ncbi.nlm.nih.gov/36202026/) | 2022 | Network meta-analysis | Cancer Treat Rev | Bayesian network meta-analyses of therapeutic sequencing in metastatic **triple-negative** breast cancer |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | Review | Oncology (Williston Park) | Overview of novel therapies (immunotherapy, ADCs) in metastatic **triple-negative** breast cancer |

---

## EU Market Information

No marketing authorization records are available in this Evidence Pack (`taiwan_regulatory.total_licenses = 0`, `licenses = []`), and market status is recorded as **Not marketed**. Licensing information should be re-verified directly against the EMA product database before proceeding further.

---

## Cytotoxicity

Talazoparib is a PARP inhibitor used as an oncology therapy and is classified here as an antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor, synthetic-lethality mechanism) |
| Myelosuppression Risk | High — PARP inhibitors, including talazoparib, are well known to cause anemia, neutropenia, and **thrombocytopenia**; this class-level toxicity was specifically flagged elsewhere in the Evidence Pack as a safety concern to weigh against any new indication |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete blood count (CBC) with differential (particularly platelet count), renal function |
| Handling Protection | Should be handled per institutional hazardous/cytotoxic drug handling protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (HER2-Positive Breast Carcinoma) is contradicted by the majority of its own supporting clinical trial and literature evidence, which actually describes **HER2-negative** patient populations — this pattern is consistent with an ontology/label-matching error rather than a genuine pharmacological signal. Combined with a blocking data gap on drug labeling/safety information (DG001) and the absence of any EU marketing authorization on file, there is insufficient basis to advance this specific indication.

**To proceed, the following is needed:**
- Manual re-verification of the disease-label mapping for "HER2 positive breast carcinoma" against the cited trials/publications to confirm or rule out the ontology mismatch
- Official drug labeling / safety data (TFDA or EMA SmPC) to complete the blocking safety review (DG001)
- Mechanism-of-action confirmation (DG002) from DrugBank or equivalent source
- If the label-mismatch is confirmed, redirect evaluation toward the mechanistically consistent, higher-quality signal identified elsewhere in the prediction set — **PR-negative/triple-negative breast cancer** (evidence level L2, decision stage S3, "Proceed with Guardrails") — which aligns with talazoparib's established gBRCA/HRD-driven mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

