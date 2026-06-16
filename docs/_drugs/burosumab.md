---
layout: default
title: Burosumab
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Burosumab
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

# Burosumab: From X-linked Hypophosphatemia to Renal Osteodystrophy

## One-Sentence Summary

Burosumab (Crysvita®) is a fully human anti-FGF23 monoclonal antibody approved globally for X-linked Hypophosphatemia (XLH), a rare genetic disorder causing chronic hypophosphatemia and progressive bone disease — though it currently holds no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Renal Osteodystrophy** (top-ranked prediction, score: 96.9%), supported by **1 publication** addressing related FGF23 pathophysiology.
Notably, the model also flags **Bone Remodeling Disease** (rank #4) with **2 completed Phase 3 RCTs** — evidence that largely coincides with burosumab's existing XLH approval pathway and warrants careful overlap assessment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | X-linked Hypophosphatemia (XLH) — globally approved (FDA 2018 / EMA), not yet marketed in Taiwan |
| Predicted New Indication | Renal Osteodystrophy |
| TxGNN Prediction Score | 96.9% |
| Evidence Level | L4 (renal osteodystrophy); Bone Remodeling Disease reaches L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, Burosumab is a fully human IgG1 monoclonal antibody that selectively binds to and neutralizes fibroblast growth factor 23 (FGF23). By blocking FGF23 signaling, burosumab restores renal tubular phosphate reabsorption and stimulates renal synthesis of 1,25-dihydroxyvitamin D, correcting the hypophosphatemia and impaired skeletal mineralization (osteomalacia/rickets) characteristic of XLH.

Renal osteodystrophy (ROD) is a spectrum of bone disorders arising in chronic kidney disease (CKD) as part of CKD-mineral and bone disorder (CKD-MBD). In CKD, FGF23 rises steeply as a compensatory response to phosphate retention — engaging precisely the same FGF23 axis that burosumab targets. Elevated FGF23 in CKD is associated with impaired bone mineralization, cardiovascular toxicity, and immune dysfunction. This shared FGF23 biology provides the theoretical basis for TxGNN's prediction.

However, the mechanistic direction in CKD is double-edged and clinically uncertain. Blocking FGF23 in CKD patients may relieve FGF23-mediated extraskeletal toxicity but simultaneously worsen the underlying hyperphosphatemia — potentially aggravating rather than improving renal osteodystrophy. A 2024 case report (PMID 38195892) documented successful burosumab use in an adult XLH patient who had developed CKD Stage 3b, suggesting cautious feasibility in carefully selected patients, but no formal clinical evidence for ROD as a de novo indication currently exists.

---

## Clinical Trial Evidence

Currently no related clinical trials for renal osteodystrophy with burosumab are registered.

> **Context — Adjacent Indication (Bone Remodeling Disease, Rank #4):** The strongest trial evidence in this evidence pack comes from the bone remodeling disease category, where the two pivotal Phase 3 trials underpinning burosumab's global XLH approval were identified. These are listed below for completeness but should not be counted as novel repurposing evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02526160](https://clinicaltrials.gov/study/NCT02526160) | Phase 3 | Completed | 134 | Randomized, double-blind, placebo-controlled RCT with open-label extension; burosumab significantly increased serum phosphorus and improved fracture healing vs. placebo in adults with XLH — one of the pivotal FDA/EMA approval trials |
| [NCT02537431](https://clinicaltrials.gov/study/NCT02537431) | Phase 3 | Completed | 14 | Open-label single-arm study; burosumab treatment reduced osteoid volume (OV/BV) in adults with XLH-associated osteomalacia — histological bone mineralization improvement as primary endpoint |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | Observational diagnostic study measuring mitochondrial ATP by ³¹P-MRS in phosphate diabetes (including XLH); does not evaluate burosumab as a treatment intervention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38195892](https://pubmed.ncbi.nlm.nih.gov/38195892/) | 2024 | Case Report | Calcified Tissue International | Successful burosumab treatment in an adult XLH patient with concurrent CKD Stage 3b; phosphate levels normalized and bone pain improved — most directly relevant to the renal osteodystrophy prediction |
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Current Pediatric Reviews | Diagnostic and therapeutic approaches to hypophosphatasia and XLH in children; burosumab discussed as targeted therapy for FGF23-driven metabolic bone disease |
| [32701599](https://pubmed.ncbi.nlm.nih.gov/32701599/) | 2020 | Perspective | Current Opinion in Nephrology & Hypertension | Reviews burosumab's mechanism and XLH approval; explicitly discusses the theoretical implications of FGF23 blockade for CKD-MBD — directly addresses the renal osteodystrophy hypothesis |
| [37180412](https://pubmed.ncbi.nlm.nih.gov/37180412/) | 2022 | Review | Therapeutic Advances in Rare Disease | Comprehensive review of burosumab vs. conventional therapy in adult XLH; efficacy, safety, quality-of-life data — reference for mechanism and safety profile |
| [36382755](https://pubmed.ncbi.nlm.nih.gov/36382755/) | 2022 | Review | Archives of Endocrinology & Metabolism | Novel treatments for hypophosphatemic rickets/osteomalacia; FGF23 regulation of phosphate in gut, skeleton, and kidney; burosumab mechanism contextualized |
| [37843399](https://pubmed.ncbi.nlm.nih.gov/37843399/) | 2024 | Cohort | J Clinical Endocrinology & Metabolism | Cardiovascular risk assessment in adult XLH patients; contextualizes FGF23 cardiovascular effects relevant to CKD-MBD safety concerns |
| [35103802](https://pubmed.ncbi.nlm.nih.gov/35103802/) | 2022 | Case Series | Zeitschrift für Rheumatologie | Tumor-induced osteomalacia (TIO) — paraneoplastic FGF23 overproduction causing renal phosphate wasting; mechanistic analog to XLH with burosumab potential |
| [31905439](https://pubmed.ncbi.nlm.nih.gov/31905439/) | 2019 | Review | Annals of Pediatric Endocrinology & Metabolism | Skeletal mineralization mechanisms; matrix vesicle biology, phosphate insufficiency, and FGF23's role in rickets/osteomalacia — foundational mechanistic context |
| [35235937](https://pubmed.ncbi.nlm.nih.gov/35235937/) | 2023 | Review | Hormone Research in Paediatrics | Novel treatment options in childhood bone diseases including XLH (burosumab), pediatric osteoporosis, and achondroplasia |

---

## Taiwan Market Information

Burosumab currently has **no marketing authorization in Taiwan** (0 approved licenses on record). The drug is commercially known as Crysvita® and holds regulatory approval in the United States (FDA, 2018), European Union (EMA), and other jurisdictions for X-linked Hypophosphatemia in pediatric and adult patients.

---

## Safety Considerations

No drug interaction data was identified for burosumab in this evidence pack, and Taiwan FDA prescribing information (TFDA SmPC) is not yet available. Two data gaps were flagged as requiring resolution before safety evaluation can proceed:

- **DG001 (Blocking):** TFDA prescribing information (warnings/contraindications) — must be obtained from TFDA official website before entering S1 safety review
- **DG002 (High):** Mechanism of action data — required for mechanistic linkage analysis; can be retrieved via DrugBank API

Please refer to the EMA SmPC (Crysvita®) for current safety information pending TFDA data availability.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FGF23–phosphate axis provides a biologically plausible but mechanistically ambiguous bridge between burosumab's known pharmacology and renal osteodystrophy: while FGF23 is elevated in CKD and contributes to bone and cardiovascular pathology, blocking FGF23 in the CKD context risks worsening hyperphosphatemia, and no dedicated clinical trials or controlled studies for ROD have been conducted. The two blocking data gaps (TFDA safety information and MOA data) also prevent progression to formal safety evaluation.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain and parse TFDA prescribing information PDF to extract contraindications, warnings, and special population precautions
- **Resolve DG002 (High):** Retrieve complete MOA data from DrugBank to enable mechanistic linkage scoring
- **Clarify repurposing novelty:** Confirm whether the intended indication (renal osteodystrophy / CKD-MBD) is genuinely distinct from the existing XLH approval — the Rank #4 bone remodeling evidence is largely the XLH pivotal trial data, not novel repurposing evidence
- **Renal safety assessment:** Obtain pharmacokinetic and dose-adjustment data for burosumab in patients with reduced renal function (GFR <30 mL/min), as CKD Stage 3b+ use is outside current approved labeling
- **Prospective clinical evidence:** Commission or identify registry data, investigator-initiated trials, or expanded access programs specifically enrolling CKD-MBD patients to assess the safety of FGF23 blockade in the context of existing hyperphosphatemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

