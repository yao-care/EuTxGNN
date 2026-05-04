---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab is a PCSK9 inhibitor monoclonal antibody used globally for hypercholesterolemia and atherosclerotic cardiovascular disease risk reduction, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Cholesterol Catabolic Process Disease** (encompassing familial hypercholesterolemia and related LDL clearance disorders),
with **1 completed Phase 3 clinical trial** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally indicated for hypercholesterolemia / atherosclerotic cardiovascular risk reduction |
| Predicted New Indication | Cholesterol Catabolic Process Disease |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alirocumab is a fully human monoclonal antibody that targets PCSK9 (proprotein convertase subtilisin/kexin type 9). Detailed MOA data is not available in the current Evidence Pack; however, alirocumab's mechanism is well-established in the literature: by binding and neutralising circulating PCSK9, it prevents PCSK9 from docking onto LDL receptors on hepatocyte surfaces and driving their lysosomal degradation. The result is a sustained increase in LDL receptor density, accelerating LDL-cholesterol (LDL-C) clearance from plasma — a direct intervention in the cholesterol catabolic pathway.

Cholesterol catabolic process disease encompasses conditions where the cellular or systemic machinery for cholesterol degradation and clearance is impaired. The most prominent example is familial hypercholesterolemia (FH), where loss-of-function mutations in the LDL receptor reduce hepatic LDL-C uptake. Alirocumab compensates for this deficit by preserving whatever residual LDL receptor expression remains, making the mechanistic alignment between drug and disease category exceptionally direct. The HIV-associated dyslipidemia subgroup studied in NCT03207945 represents a metabolically distinct but clinically relevant example of cholesterol catabolic dysfunction driven by antiretroviral therapy and systemic inflammation.

Multiple tier-1 systematic reviews and the large ODYSSEY OUTCOMES safety dataset (>47,000 patient-years) converge to confirm alirocumab's role across the spectrum of LDL-C disorders. The breadth and quality of published evidence, combined with a completed Phase 3 trial, place this prediction at the highest achievable evidence tier (L1) among all 10 indications assessed in this Evidence Pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | PCSK9 inhibition in HIV-infected patients at increased cardiovascular risk; evaluated impact on vascular inflammation, endothelial function, and non-calcified plaque burden using specialised non-invasive imaging |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Clinical Analysis | European Heart Journal: Cardiovascular Pharmacotherapy | ODYSSEY OUTCOMES trial: alirocumab over 47,296 patient-years significantly reduced recurrent ischaemic cardiovascular events and all-cause mortality, with a well-characterised safety profile |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review (Tier 1) | Signal Transduction and Targeted Therapy | Comprehensive review of PCSK9 across lipid metabolism, cardiovascular disease, liver disease, infectious disease, and cancer; establishes PCSK9 as a multi-system therapeutic target |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Mechanistic Review | Pharmacology & Therapeutics | Compares extracellular PCSK9 inhibition (alirocumab, evolocumab) vs. hepatic siRNA knockdown (inclisiran); clarifies mechanism of action differences with clinical implications |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review (Tier 1) | Current Opinion in Lipidology | Update on PCSK9-directed therapies; summarises two landmark cardiovascular outcomes trials demonstrating marked LDL-C reduction and cardiovascular risk reduction |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review (Tier 1) | Current Atherosclerosis Reports | Novel pharmacological approaches for homozygous familial hypercholesterolemia, a prototypical cholesterol catabolic process disease |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review (Tier 1) | Kardiologia Polska | Evidence review of PCSK9 inhibitors on lipid parameters and cardiovascular risk; biochemical and genomic validation of PCSK9's role in LDL metabolism |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Review | Pharmacotherapy | State-of-the-art review of PCSK9-directed therapies as add-on to statins; addresses statin intolerance and suboptimal LDL-C lowering |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review (Tier 2) | International Journal of Molecular Sciences | Overview of dyslipidemia treatments including PCSK9 inhibitors; addresses LDL-C, TG, and quality-of-life outcomes |
| [36411665](https://pubmed.ncbi.nlm.nih.gov/36411665/) | 2022 | Review (Tier 2) | Biomedicine & Pharmacotherapy | Safety review of PCSK9 inhibitors; only 43% of statin-treated patients in Europe achieve LDL-C targets, supporting add-on PCSK9 inhibition |
| [38191052](https://pubmed.ncbi.nlm.nih.gov/38191052/) | 2024 | Research | Metabolism: Clinical and Experimental | PCSK9 inhibition prevents and alleviates cholesterol gallstones via PPARα-mediated CYP7A1 activation; extends the drug's relevance to hepatic cholesterol catabolism beyond cardiovascular disease |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alirocumab's PCSK9 inhibition mechanism directly and specifically targets the LDL receptor pathway — the core defect in cholesterol catabolic process disease — making this one of the most mechanistically coherent repurposing predictions in this Evidence Pack. A completed Phase 3 trial plus 19 publications including multiple tier-1 reviews and the ODYSSEY OUTCOMES dataset justify an L1 evidence classification.

**To proceed, the following is needed:**
- Taiwan regulatory strategy: alirocumab is not currently registered in Taiwan; a TFDA market authorisation application or compassionate use pathway should be evaluated
- Retrieve TFDA SmPC equivalent (or Praluent EU/US label) to document key warnings, contraindications, and monitoring requirements before clinical deployment
- Retrieve complete MOA data from DrugBank (DB09302) to finalise the mechanistic justification section
- Define the specific target subpopulation within "cholesterol catabolic process disease" — e.g., heterozygous FH, homozygous FH, HIV-associated dyslipidemia, or statin-intolerant hypercholesterolemia — as each may require a separate regulatory pathway
- Assess reimbursement and cost-effectiveness data, as PCSK9 inhibitors are high-cost biologics with payer coverage variability across markets
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

