---
layout: default
title: Imiquimod
parent: High Evidence (L1-L2)
nav_order: 305
evidence_level: L1
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From No Taiwan-Registered Indication to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod (DrugBank DB00724) is a topical Toll-like receptor 7 (TLR7) agonist that is **not currently marketed in Taiwan** (0 TFDA licenses on file), so no original approved indication is available in this evidence pack. The TxGNN model predicts it may be effective for **Pre-malignant Neoplasm**, and this direction is supported by **19 clinical trials** and **9 publications** collected in this pack — though only a subset (mainly actinic keratosis, VIN, and CIN studies) directly evaluate imiquimod in this disease category; most other trials use imiquimod as a vaccine adjuvant and are not directly relevant.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Imiquimod is not currently marketed in Taiwan (0 TFDA licenses on file) |
| Predicted New Indication | Pre-malignant Neoplasm |
| TxGNN Prediction Score | 99.92% (rank 1240 among all predictions) |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for Imiquimod is currently a data gap in this evidence pack (DrugBank MOA field not populated — see DG002). Based on the trial and literature evidence collected, however, Imiquimod is known to act as a **TLR7 agonist**: it activates local innate immunity (inducing IFN-α and other cytokines), which promotes apoptosis of dysplastic keratinocytes.

This mechanism is already an established treatment pathway for several epidermal and mucosal pre-malignant conditions — actinic keratosis, vulvar intraepithelial neoplasia (VIN), and cervical intraepithelial neoplasia (CIN) — all of which fall under the broader "pre-malignant neoplasm" category being predicted here. Because the mechanism is local immune activation rather than tumor-type-specific cytotoxicity, it plausibly generalizes across different pre-malignant epithelial lesions, which is consistent with why multiple Phase 2/3 trials already exist for related conditions even though "pre-malignant neoplasm" as a formal indication has not been evaluated as a single entity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Evaluated duration of effect of imiquimod 5% cream (3x/week, 1–2 cycles) for actinic keratoses on the head |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT of topical imiquimod for high-grade cervical intraepithelial lesions (CIN) from persistent HPV 16/18 infection |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod vs. LLETZ surgery for high-grade CIN (CIN 2-3); terminated early, small sample |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | Compared 5%, 0.05%, and nanoencapsulated 0.05% imiquimod gel for actinic cheilitis (premalignant lip lesion); terminated |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT of surgery+imiquimod vs. excision alone for nodular basal cell carcinoma (malignant, borderline relevance) |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Assessed imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explored immune escape mechanisms and efficacy of imiquimod for vulvar intraepithelial neoplasia (VIN 2/3) and anogenital warts |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Neoadjuvant imiquimod to reduce excision size/risk of incomplete excision in lentigo maligna (intraepidermal melanoma) of the face |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot trial of neoadjuvant topical imiquimod (Aldara) immunotherapy in early-stage oral squamous cell carcinoma |

*Note: 10 additional registered trials use imiquimod solely as a vaccine adjuvant in advanced/malignant cancers (prostate, melanoma, lung, glioma) and are not direct evidence for pre-malignant neoplasm; they are omitted from this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review | Cochrane Database Syst Rev | Systematic review of interventions (including imiquimod) for anal intraepithelial neoplasia (AIN), an HPV-related pre-malignant condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review | Cochrane Database Syst Rev | Systematic review of medical interventions, including imiquimod, for high-grade vulval intraepithelial neoplasia (VIN) |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Reviews combined photodynamic therapy approaches for non-melanoma skin cancer and precursor lesions |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Reviews topical treatment strategies (incl. imiquimod) for non-melanoma skin cancer and precursor lesions |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Reviews current management of actinic keratosis, including topical field therapies |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Cohort | Urol Oncol | Rat model PK/PD of TLR7 agonists related to imiquimod for (pre)malignant urothelial lesions |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Der Hautarzt | Case of disseminated superficial actinic porokeratosis with coexisting actinic keratoses resistant to topical treatment |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | High-grade VIN successfully treated with topical imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis successfully treated with topical imiquimod 5% cream |

---

## Taiwan Market Information

Imiquimod is **not currently marketed in Taiwan** — 0 TFDA licenses are on file in this evidence pack, so no authorization number, product name, dosage form, or approved indication text is available.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — resolving this is a **blocking** data gap, see DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2/3 trials (including two completed Phase 3 studies) directly support imiquimod's efficacy in related pre-malignant epithelial lesions (actinic keratosis, VIN, CIN), giving this prediction L1 evidence strength. However, imiquimod is not currently marketed in Taiwan, and drug-level safety labeling and MOA data are still missing, so the recommendation cannot advance to unconditional "Go."

**To proceed, the following is needed:**
- TFDA-equivalent safety labeling (key warnings/contraindications) — currently a blocking gap (DG001)
- Confirmed DrugBank/MOA record for formal mechanism-of-action analysis (DG002)
- A regulatory pathway assessment, since Imiquimod holds no existing Taiwan market authorization
- Route/formulation compatibility confirmation (topical route availability against required route for pre-malignant neoplasm indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

