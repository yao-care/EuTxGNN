---
layout: default
title: Bazedoxifene
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Bazedoxifene
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

# Bazedoxifene: From Postmenopausal Osteoporosis to Amenorrhea

## One-Sentence Summary

Bazedoxifene is a third-generation selective estrogen receptor modulator (SERM), approved in Europe for postmenopausal osteoporosis prevention and used as part of the conjugated estrogens/bazedoxifene (CE/BZA) tissue selective estrogen complex (TSEC) for menopausal symptom management; it is not currently marketed in Taiwan.
The TxGNN model predicts it may be applied to **Amenorrhea**, with **1 Phase 3 clinical trial** (n = 1,886) and **4 publications** currently supporting this direction.
This prediction aligns with bazedoxifene's well-characterized endometrial antagonism within the TSEC framework — making it one of the more mechanistically grounded predictions in this pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postmenopausal osteoporosis (EU: Conbriza); menopausal symptoms as CE/BZA TSEC (EU: Duavive) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, bazedoxifene acts as a tissue-selective estrogen receptor modulator: it behaves as an agonist in bone — reducing osteoclast-mediated bone resorption — while functioning as an antagonist in endometrial and breast tissue. This selectivity underpins its utility in postmenopausal women who still have an intact uterus.

The mechanistic rationale for amenorrhea centres on bazedoxifene's role in the CE/BZA TSEC combination. Conjugated estrogens (CE) relieve vasomotor symptoms and protect bone, but also stimulate the endometrium, historically requiring a progestin to prevent hyperplasia. Bazedoxifene substitutes for the progestin: its endometrial antagonism blocks CE's proliferative effect on the uterine lining, suppresses withdrawal bleeding, and induces amenorrhea — all without the adverse effects associated with progestogens.

It is critical to frame this finding correctly: the "amenorrhea" predicted here is a pharmacologically intended, clinically favourable outcome of the TSEC approach — not a treatment for pathological amenorrhea (e.g., hypothalamic, pituitary, or primary ovarian insufficiency). Multiple Phase 3 SMART trials have confirmed CE/BZA's ability to maintain high amenorrhea rates while simultaneously relieving menopausal symptoms and preserving bone mineral density. The TxGNN prediction therefore reflects an already-documented mechanism rather than a speculative leap, lending it high face validity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1,886 | Double-blind, randomised, placebo- and active-controlled RCT of CE/BZA combinations in postmenopausal women; evaluated endometrial hyperplasia prevention (primary endpoint) and osteoporosis prevention; amenorrhea (absence of uterine bleeding) was a key safety and secondary efficacy endpoint, ~14.5-month follow-up |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22853444](https://pubmed.ncbi.nlm.nih.gov/22853444/) | 2012 | Review | *Climacteric* | Comprehensive review of CE/BZA TSEC efficacy for vasomotor and vaginal symptoms; discusses amenorrhea rates as a marker of endometrial safety and compares benefit/risk profile with traditional HRT |
| [24929044](https://pubmed.ncbi.nlm.nih.gov/24929044/) | 2014 | Review | *Steroids* | Describes the development rationale for CE/BZA; explains bazedoxifene's endometrial antagonism mechanism enabling progestin-free amenorrhea induction while preserving estrogen's benefits on bone and vasomotor symptoms |
| [29790381](https://pubmed.ncbi.nlm.nih.gov/29790381/) | 2018 | Review | *Gynecological Endocrinology* | Reviews CE 0.45 mg/BZA 20 mg as a progestogen-free HRT option for non-hysterectomized women; summarises clinical data on amenorrhea outcomes and endometrial protection across the SMART trial programme |
| [30895900](https://pubmed.ncbi.nlm.nih.gov/30895900/) | 2019 | Review | *Climacteric* | Advances in TSECs and SERMs; comparative tissue-selective profile of bazedoxifene, with amenorrhea induction discussed as a primary uterine safety endpoint distinguishing TSECs from progestin-based HRT |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note for reviewers:** The repurposing analysis flagged that bazedoxifene, as a SERM, carries a class-wide risk of venous thromboembolism (VTE). Several other TxGNN predictions in this pack (thrombophilia, antithrombin deficiency, factor V excess) were rated "Hold" precisely because SERM-mediated promotion of coagulation factors directly contradicts the therapeutic goal. TFDA package insert data is currently unavailable (Data Gap DG001); full SmPC review is required before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CE/BZA-induced amenorrhea application is underpinned by a completed Phase 3 RCT enrolling nearly 1,900 subjects and four review publications spanning 2012–2019, giving it the strongest evidence level (L1) in this prediction pack. The mechanism is well-characterised and reproducible across the SMART trial programme. However, the indication must be precisely framed — this is CE/BZA TSEC-induced amenorrhea as a uterine protection strategy within postmenopausal HRT, not a treatment for pathological amenorrhea — and the combination is not yet registered in Taiwan.

**To proceed, the following is needed:**

- **Safety data gap closure:** Download and parse the TFDA package insert (DG001) to confirm local warnings, contraindications, and VTE-related precautions
- **MOA documentation:** Retrieve full mechanism of action data from DrugBank (DG002) to support regulatory submissions
- **Indication scoping:** Formally define the clinical indication boundary — CE/BZA TSEC for menopausal symptom management with uterine protection — and explicitly exclude pathological amenorrhea treatment
- **Taiwan regulatory pathway:** Bazedoxifene/CE combination (Duavive) holds EU approval; assess TFDA filing feasibility and required bridging studies for the Taiwanese population
- **VTE risk management plan:** Establish screening criteria and monitoring protocols for thromboembolism risk, consistent with known SERM class effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

