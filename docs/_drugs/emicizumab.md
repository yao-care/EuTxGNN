---
layout: default
title: Emicizumab
parent: High Evidence (L1-L2)
nav_order: 213
evidence_level: L1
indication_count: 10
---

# Emicizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Emicizumab: From Congenital Hemophilia A to Acquired Coagulation Factor Deficiency (Acquired Hemophilia A)

## One-Sentence Summary

Emicizumab (Hemlibra) is a bispecific monoclonal antibody originally developed for congenital Hemophilia A, where it bridges Factor IXa and Factor X to mimic the cofactor function of activated Factor VIII. The TxGNN model predicts efficacy in **"acquired coagulation factor deficiency"** — a term that maps clinically to **Acquired Hemophilia A (AHA)** — and this direction is unusually well supported for a TxGNN candidate, with **2 relevant studies identified in the trial registry search and 20 PubMed publications**, including multiple completed Phase 2/3 studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Hemophilia A (with/without FVIII inhibitors) — not extractable from Taiwan regulatory data; drug is not TFDA-licensed |
| Predicted New Indication | Acquired coagulation factor deficiency (Acquired Hemophilia A) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data from DrugBank is currently a data gap (DG002). Based on the mechanistic description embedded in the evidence pack, emicizumab is a bispecific antibody that binds both Factor IXa and Factor X, spatially bridging them to restore the enzymatic function normally performed by activated Factor VIII (FVIIIa) — independent of endogenous FVIII levels or the presence of FVIII inhibitors. This is why it works in congenital Hemophilia A regardless of inhibitor status.

Acquired coagulation factor deficiency, in this predicted indication, corresponds to Acquired Hemophilia A — a disorder in which autoantibodies neutralize a patient's own Factor VIII, producing the same downstream coagulation defect seen in congenital disease (impaired FIXa/FX-driven thrombin generation), even though the underlying cause (autoimmune vs. genetic) differs.

Because emicizumab's mechanism bypasses FVIII entirely, it is mechanistically indifferent to *why* FVIII activity is low — whether from a congenital mutation or an acquired inhibitory autoantibody. This explains why the prediction is biologically plausible and, unlike most of the other TxGNN candidates for this drug (e.g., Glanzmann thrombasthenia, Scott syndrome, TTP — all platelet or non-FVIII pathway disorders with explicitly weak mechanistic links per the evidence pack), this one has already moved from theory into real-world clinical use as an off-label bridging/prophylactic therapy in AHA, pending immunosuppressive therapy taking effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | Recruiting | 3000 | ATHN Transcends — multicenter natural history cohort of non-neoplastic hematologic disorders, including acquired coagulation factor deficiencies; provides real-world safety/effectiveness observation rather than an emicizumab-specific interventional design. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase III (single-arm, open-label) | J Thromb Haemost | First prospective Phase III study of emicizumab prophylaxis in patients with Acquired Hemophilia A (PwAHA); no prior prospective data existed before this trial. |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | RCT (open-label), Phase 2 | Lancet Haematol | GTH-AHA-EMI study: emicizumab protected AHA patients from bleeding and allowed immunosuppression to be deferred during the first 12 weeks. |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase III (final analysis) | Thromb Haemost | AGEHA study final analysis: favorable benefit-risk profile for emicizumab prophylaxis in AHA, including immunosuppression-ineligible patients and long-term use data. |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus/Guideline | Hamostaseologie | GTH-AHA Working Group consensus recommendations on using emicizumab in AHA, based on the GTH-AHA-EMI results. |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Cohort | Blood Adv | Real-world US multicenter cohort (62 patients, 12 centers) treated off-label with emicizumab for a median of 10 weeks. |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohort/follow-up | Blood Adv | 2-year follow-up of GTH-AHA-EMI patients showing sustained survival benefit and postponed immunosuppression. |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Comparative study | J Thromb Haemost | Direct comparison of emicizumab versus immunosuppressive therapy for AHA management. |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Review | J Thromb Haemost | Narrative review of AHA management approaches in the "emicizumab era." |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review | Blood Transfus | Reviews pros and cons of emicizumab as a new approach to AHA bleeding prevention and treatment. |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | Case series | Haemophilia | Case series describing emicizumab use in AHA, noting no randomized trials existed at the time of writing. |

---

## Taiwan Market Information

Emicizumab is **not currently marketed in Taiwan** — 0 TFDA authorizations are on record, and no licensed dosage forms or approved indication text are available.

---

## Safety Considerations

Please refer to the SmPC for safety information. TFDA label warnings, contraindications, and drug interaction data are currently unavailable (flagged as a **Blocking** data gap, DG001) and must be obtained before any formal safety assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among emicizumab's TxGNN candidates, "acquired coagulation factor deficiency" (Acquired Hemophilia A) is the only one with genuine clinical validation — three completed/near-complete Phase 2–3 studies (GTH-AHA-EMI, AGEHA, and the single-arm Phase III study) plus consensus guidelines already support off-label-to-guideline-level use. However, the drug is not TFDA-licensed in Taiwan, and safety labeling data is a **Blocking** gap, so this cannot yet advance past initial evidence review.

**To proceed, the following is needed:**
- TFDA-approved label / SmPC (warnings, contraindications, DDI) to clear the Blocking data gap (DG001)
- Formal DrugBank MOA confirmation (DG002)
- A regulatory pathway assessment for Taiwan market entry or named-patient/off-label use, since there are currently 0 local authorizations
- Confirmation of AHA diagnostic overlap with the TxGNN-labeled term "acquired coagulation factor deficiency" to ensure correct clinical scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

