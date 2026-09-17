---
layout: default
title: Topotecan
parent: High Evidence (L1-L2)
nav_order: 607
evidence_level: L2
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a topoisomerase I inhibitor originally approved for platinum-refractory ovarian cancer, small cell lung cancer, and cervical cancer. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **5 clinical trials** and **20 publications** currently identified in support of this direction — though most of the trial-level evidence involves combination regimens or adjacent tumor types rather than confirmatory breast cancer monotherapy studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this regulatory dataset; per established pharmacology, Topotecan (Hycamtin) is originally indicated for platinum-refractory ovarian cancer, small cell lung cancer, and cervical cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

The `original_moa` field in this dataset is marked as a data gap, and detailed DrugBank mechanism-of-action data has not yet been retrieved. Based on the evidence collected for this prediction, Topotecan's pharmacology is nonetheless well characterized: it is a semisynthetic camptothecin derivative that inhibits topoisomerase I by stabilizing the topo I–DNA cleavable complex, generating DNA double-strand breaks during replication that trigger apoptosis in rapidly dividing cells (PMID 10472342). This mechanism underlies broad-spectrum activity across solid tumors, including in vivo activity against breast carcinoma xenografts.

Breast carcinoma shares the high-proliferation, chemosensitive biology of Topotecan's approved indications, which is why the drug has been repeatedly tested in advanced/metastatic breast cancer since the 1990s — including a CALGB Phase 2 monotherapy trial (PMID 10362325), infusional-dosing studies (PMID 9413954), and combination regimens with paclitaxel (PMID 9626200) or as part of the TIME regimen (Topotecan/Ifosfamide/Etoposide, NCT00006032) prior to autologous stem cell rescue.

Despite this history, the mechanistic case has not translated into guideline adoption: across three decades of trials, Topotecan showed moderate but not superior activity relative to anthracycline/taxane-based standards, with dose-limiting myelosuppression consistently reported. More recent mechanistic work suggests renewed interest specifically in triple-negative breast cancer (TNBC), where TFDP1 has been proposed as a Topotecan-relevant therapeutic target through suppression of cellular senescence (PMID 40300683), and where BCRP/P-glycoprotein-mediated resistance pathways have been characterized in detail (PMID 10930538, PMID 25236865) — pointing to potential combination strategies (e.g., with BCRP inhibitors) that could revive this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's-choice chemotherapy in gBRCA1/2-mutated platinum-sensitive relapsed ovarian cancer; Topotecan's specific role in this regimen could not be confirmed from the trial title alone and requires further verification |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib vs. standard chemotherapy in platinum-resistant recurrent ovarian/peritoneal/fallopian tube cancer; whether Topotecan serves as the chemotherapy backbone is unconfirmed |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (Topotecan + Ifosfamide/Mesna + Etoposide) followed by autologous stem cell rescue, designed specifically for metastatic breast cancer; trial was terminated |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A (organoid screen) | Unknown | 35 | Patient-derived organoid drug-screening study (SCORE) for refractory solid tumors; provides in vitro drug-sensitivity data only, not a therapeutic intervention trial |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemotherapy/immunotherapy regimens in advanced malignancies; Topotecan's specific relevance to the breast cancer arm is unclear |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | RCT/Phase 2 | American Journal of Clinical Oncology | CALGB Phase 2 trial of Topotecan monotherapy in 53 previously treated advanced breast cancer patients (47 eligible, 40 evaluable) |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase 2 | British Journal of Cancer | Two open Phase 2 studies of continuous infusional Topotecan in chemo-naive advanced breast cancer and NSCLC; no evidence of increased efficacy over standard dosing |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort/Pilot | Onkologie | Pilot study of Topotecan as primary chemotherapy for symptomatic brain metastases in metastatic breast cancer |
| [39013199](https://pubmed.ncbi.nlm.nih.gov/39013199/) | 2024 | Review/Expert Consensus | Revista Colombiana de Obstetricia y Ginecología | Expert consensus on profiling and management of advanced/metastatic epithelial ovarian cancer; contextual reference, not breast-cancer specific |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical | Anticancer Research | Human breast, colon, and lung carcinoma xenografts tested against doxorubicin, cisplatin, irinotecan, and Topotecan; Topotecan showed measurable in vivo activity against breast cancer cell lines |
| [27444351](https://pubmed.ncbi.nlm.nih.gov/27444351/) | 2016 | Preclinical/Mechanistic | Phytomedicine | MHP-1 (a Cordyceps-derived compound) restores Topotecan sensitivity and inhibits metastasis via EMT/TGF-β regulation in breast cancer cells |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical/Mechanistic | International Journal of Biological Macromolecules | TFDP1 identified as a driver of triple-negative breast cancer via senescence suppression and proposed as a therapeutic target for Topotecan |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase 2 | Journal of Clinical Oncology | Phase 2 trial of paclitaxel + Topotecan with G-CSF support in pretreated Stage IV breast cancer; pharmacokinetics correlated with toxicity |
| [21514634](https://pubmed.ncbi.nlm.nih.gov/21514634/) | 2011 | Phase 2 | Gynecologic Oncology | Phase 2 trial of lapatinib + Topotecan (LapTop) in platinum-refractory/resistant ovarian and peritoneal carcinoma, targeting BCRP/P-gp-mediated Topotecan resistance |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical/Mechanistic | Pharmacological Research | Daidzein enhances Topotecan's anticancer effect and reverses BCRP-mediated drug resistance in breast cancer models |

---

## EU Market Information

Topotecan currently has **no recorded marketing authorization** in this EU regulatory dataset (market status: **Not marketed**, 0 authorizations on file). No license-level detail (product name, dosage form, or approved indication text) is available for extraction.

---

## Cytotoxicity

Topotecan is a conventional cytotoxic chemotherapy agent (camptothecin-class topoisomerase I inhibitor), meeting the antineoplastic classification criteria.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High — directly documented in the evidence base: in a Phase 2 trial of Topotecan in cisplatin-refractory germ cell tumors, myelosuppression was the dose-limiting toxicity, with median nadir leukocyte count 1.75 ×10⁹/L, neutrophil count 1.55 ×10⁹/L, hemoglobin 8.75 g/dL, and platelet count 20,500/mm³ (PMID 8617580) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential (neutrophils, platelets), given documented severe myelosuppression; renal function (Topotecan undergoes renal clearance) |
| Handling Protection | Must follow standard cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack — notably, the absence of TFDA label warnings/contraindications is flagged as a **blocking data gap** (DG001), which prevents this candidate from entering the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Mechanistic plausibility and a long track record of Phase 2 exploration in breast cancer exist, but no trial has established Topotecan as competitive with anthracycline/taxane-based standards, and the most directly relevant breast-cancer-specific trial (TIME regimen, NCT00006032) was terminated. Combined with a blocking gap in safety labeling data (DG001), the evidence supports further targeted research rather than a Go/Hold decision at this time.

**To proceed, the following is needed:**
- TFDA/EMA-approved label warnings and contraindications (DG001, blocking — required before S1 safety pre-screening)
- Structured DrugBank mechanism-of-action data (DG002)
- Confirmation of Topotecan's actual regimen role in NCT02282020 and NCT04739800, both of which appear ovarian-cancer-focused based on trial titles
- Updated clinical evidence on Topotecan combination strategies (e.g., with BCRP/P-gp inhibitors) specifically in HER2-negative or triple-negative breast cancer populations, building on the TFDP1 mechanistic rationale (PMID 40300683)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

