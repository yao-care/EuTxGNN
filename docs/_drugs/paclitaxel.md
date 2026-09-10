---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From an Unspecified Original Indication to Female Breast Carcinoma

## One-Sentence Summary

> Paclitaxel is a taxane-class chemotherapy agent; however, this evidence pack does not contain its documented original indication (data gap) or EU marketing/label data.
> The TxGNN model's top prediction is **Female Breast Carcinoma**, supported by more than 50 clinical trials and 20 publications —
> but the evidence pack's own mechanistic analysis flags this as very likely a **re-confirmation of Paclitaxel's already-established standard indication**, not a genuine repurposing discovery.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no EMA license records in this evidence pack) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is marked as a data gap in this evidence pack. Based on the mechanistic rationale attached to the top prediction, Paclitaxel acts as a **microtubule-stabilizing agent**: it binds β-tubulin and inhibits microtubule depolymerization, arresting cells in the M phase of mitosis. This produces cytotoxic effects preferentially in rapidly proliferating cells, including breast carcinoma cells.

However, a critical caveat must be flagged: the evidence pack's own rationale for this candidate states explicitly that this is **not actually a novel repurposing signal**. Paclitaxel is a globally established standard chemotherapy for breast cancer, and the "prediction" appears here only because the `original_indications` field in the source drug record was empty (a data pipeline gap), causing an already-known indication to be scored as if it were new. The same issue affects several other top-ranked candidates in this evidence pack (e.g., ER-negative breast cancer, ER-positive breast cancer, hormone-resistant breast carcinoma), which are simply clinical subtypes/contexts of the same established indication rather than independent repurposing opportunities.

Because the mechanism (microtubule inhibition via β-tubulin binding) does not depend on hormone-receptor status, it mechanistically explains efficacy across ER-positive, ER-negative, and hormone-resistant breast cancer subtypes alike — which is consistent with why the model scores these subtypes so highly. This strengthens the plausibility of the *biology*, but does not change the conclusion that this is a known-indication reconfirmation rather than a new discovery requiring separate regulatory pursuit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A (translational) | Completed | 3,677 | Landmark analysis of breast cancer intrinsic subtypes and paclitaxel benefit, using CALGB 9344/9741 trial samples — foundational evidence for paclitaxel's role in adjuvant therapy. |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recruiting | 54 | MRI-guided neoadjuvant de-escalation trial in stage II–III triple-negative breast cancer (TNBC). |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Double-blind RCT of paclitaxel + trastuzumab ± lapatinib in ErbB2-overexpressing metastatic breast cancer; stopped early. |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy (incl. weekly paclitaxel) alone vs. plus trastuzumab in node-positive/high-risk HER2-low breast cancer. |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Active, not recruiting | 2,000 | EC→paclitaxel vs. FEC→paclitaxel (q3w or q2w with pegfilgrastim support) in node-positive breast cancer. |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2,005 | Sequential doxorubicin/paclitaxel/cyclophosphamide vs. concurrent AC→paclitaxel at different intervals in node-positive stage II/IIIA breast cancer. |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense, dose-intensified neoadjuvant regimens (incl. paclitaxel) in high-risk early breast cancer. |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Completed | 725 | Double-blind biosimilar comparison (ABP 980 vs. trastuzumab, paclitaxel backbone) in HER2-positive early breast cancer. |
| [NCT00915018](https://clinicaltrials.gov/study/NCT00915018) | Phase 2 | Completed | 479 | Neratinib + paclitaxel vs. trastuzumab + paclitaxel as first-line therapy for ErbB2-positive metastatic breast cancer. |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab, and their combination, all plus paclitaxel, in HER2-positive primary breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms. |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort/Comparative | Cancer | Phase II trial: doxorubicin + paclitaxel efficacy/toxicity in advanced breast carcinoma; role of prior adjuvant anthracycline exposure. |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review documenting extension of taxane licensure to first-line breast and ovarian cancer treatment. |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | — | Chem Biol Drug Des | Explores paclitaxel combination therapies against breast carcinoma and identifies in vivo biomarkers using patient-derived models. |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | — | J Immunother Cancer | Paclitaxel's effect on tumor-associated macrophages to enhance PD-1 blockade efficacy in TNBC. |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | — | Nature Communications | Identifies TEKT4 germline variants enriched in breast cancer resistant to paclitaxel. |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | — | BioMed Research International | Real-world study: neoadjuvant epirubicin/cyclophosphamide + weekly paclitaxel + trastuzumab in HER2+ breast carcinoma. |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | — | Molecular Pharmacology | Mechanistic study on reversing stathmin-mediated resistance to paclitaxel and vinblastine in breast carcinoma cells. |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | — | J Clin Oncol | ECOG Phase II trial of biweekly paclitaxel + cisplatin in advanced breast carcinoma. |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | — | Cancer | Role of paclitaxel in multimodality treatment for inflammatory breast carcinoma. |

---

## EU Market Information

No EMA marketing authorization records are present in this evidence pack (`taiwan_regulatory.total_licenses = 0`, market status: Not Marketed). No product-level authorization table can be generated.

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent, β-tubulin binding) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

*Note: Detailed toxicity/monitoring data are subject to a Blocking data gap in this evidence pack (missing TFDA/EMA product label) and cannot be sourced beyond the general drug-class classification above.*

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence pack flags a **Blocking** data gap (missing TFDA/EMA label — warnings, contraindications, DDI), which by definition prevents completion of the S1 safety evaluation regardless of clinical efficacy evidence.
- The evidence pack's own mechanistic rationale indicates the top-ranked candidate (and several related subtype candidates: ER-negative, ER-positive, and hormone-resistant breast cancer) most likely represents Paclitaxel's **already-established standard indication**, misclassified as a "new prediction" due to a missing `original_indications` field — not a genuine repurposing discovery.
- The drug currently has no EU marketing authorization on record in this dataset (0 licenses), so no regulatory pathway context is available for a "Go" decision.

**To proceed, the following is needed:**
- Obtain the official TFDA/EMA-approved product label (warnings, contraindications, drug interactions) to complete the S1 safety evaluation.
- Retrieve the formal DrugBank mechanism-of-action record to replace the current data gap.
- Re-verify the `original_indications` field against an authoritative source; if Paclitaxel's approved breast cancer indication is confirmed, reclassify this candidate as "known indication" rather than a repurposing opportunity, and re-run TxGNN scoring excluding already-approved indications.
- Prioritize evaluation of the genuinely novel, evidence-free candidates in this pack (e.g., parameningeal embryonal rhabdomyosarcoma, botryoid-type embryonal rhabdomyosarcoma of the vagina — both L5, zero trials/literature) only after preclinical mechanistic validation, given they currently have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

