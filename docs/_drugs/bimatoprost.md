---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma to Alopecia

## One-Sentence Summary

Bimatoprost is a synthetic prostamide F2α analog, internationally marketed as Lumigan® (intraocular pressure reduction in glaucoma) and Latisse® (FDA-approved for eyelash hypotrichosis), though it currently has no Taiwan regulatory authorization.
The TxGNN model predicts it may be effective for **Alopecia** (including androgenetic alopecia and alopecia areata),
with **11 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular hypertension (Lumigan®); Eyelash hypotrichosis (Latisse®, FDA-approved 2008) |
| Predicted New Indication | Alopecia (androgenetic alopecia and alopecia areata) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bimatoprost is a synthetic analog of prostaglandin F2α (prostamide class), primarily used in ophthalmology to lower intraocular pressure. Detailed MOA documentation for the Taiwan regulatory dossier is currently unavailable (DG002), but the mechanism underlying the alopecia prediction is well-characterized in the literature: bimatoprost binds FP receptors (prostaglandin F2α receptors) expressed in hair follicle dermal papilla cells, prolongs the anagen (active growth) phase of the hair cycle, and stimulates follicular cell proliferation. The biological plausibility of this application was first established when clinicians observed hypertrichosis as a side effect of topical prostaglandin analogs in glaucoma patients — an observation that directly led to FDA approval of Latisse®.

The bridge from eyelash hypotrichosis to scalp alopecia is mechanistically direct: the same FP receptor system present in eyelid follicles is expressed in scalp hair follicles. A landmark FASEB Journal study (PMID 23104985) demonstrated that prostamide-mediated signaling is functionally active in human scalp follicles and proposed bimatoprost as a candidate for scalp alopecias. Both androgenetic alopecia and alopecia areata are characterized by premature truncation of the anagen phase, making them logical targets for anagen-prolonging therapy.

Among the 10 TxGNN-predicted indications in this Evidence Pack, "alopecia" stands out as the sole indication with L2-grade clinical evidence. The remaining nine predictions — including rare malformation syndromes and genetic hair shaft disorders — are either biologically implausible links or have zero supporting clinical data (all rated L5/Hold). The high TxGNN scores for those conditions likely reflect non-specific prostaglandin–inflammation graph connections in the knowledge graph rather than genuine therapeutic opportunities.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Double-blind dose-comparison of bimatoprost vs. vehicle vs. open-label minoxidil 5% in male AGA — largest scalp AGA RCT for this drug |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Double-blind dose-comparison of bimatoprost vs. vehicle vs. open-label minoxidil 2% in female pattern hair loss |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in male AGA — independent Phase 2 confirmatory study |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | CO₂ fractional laser combined with bimatoprost 0.03% in alopecia areata — evaluates synergistic combination approach |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Mechanistic study of bimatoprost effect on androgen-dependent hair follicles — validates FP receptor pathway in scalp |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% for eyelash hypotrichosis in children — provides pediatric safety profile |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Scalp pharmacokinetics and tolerability following 14-day topical application in male AGA patients |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety and PK of novel bimatoprost formulations for topical alopecia use — two formulation comparisons |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose-escalation safety/tolerability/PK in male AGA — early termination limits data interpretation |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Latanoprost vs. bimatoprost ophthalmic solution for eyelash regrowth in alopecia areata — small exploratory study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | RCT | Archives of Dermatological Research | CO₂ fractional laser + bimatoprost significantly enhances hair regrowth in alopecia areata versus laser alone; confirms adjunctive efficacy |
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Systematic Review | Journal of Dermatological Treatment | Network meta-analysis of non-surgical AGA treatments in men and women; bimatoprost included as an emerging comparator |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Prospective Study | Dermatologic Therapy | Topical bimatoprost for eyelash loss in alopecia totalis/universalis: 16 of 19 patients showed measurable response over ~30 weeks |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Prospective Non-Randomized | Indian Dermatology Online Journal | Head-to-head comparison of bimatoprost vs. clobetasol propionate in scalp alopecia areata; bimatoprost shows comparable outcomes |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opinion on Investigational Drugs | Comprehensive synthesis of bimatoprost evidence across eyelash, eyebrow, and scalp alopecia — key reference for repurposing rationale |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Clinical Guideline | Journal of Dermatology | Japanese 2017 guidelines for male and female pattern hair loss — positions bimatoprost in the treatment landscape |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Review | Indian Dermatology Online Journal | Overview of bimatoprost in dermatology: mechanism, alopecia subtypes, and pigmentation applications |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Experimental | Drug Delivery | Novel topical formulation achieves 4.6× higher skin flux and 529% greater dermal deposition vs. standard preparation — formulation optimization data |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Current Oncology | Chemotherapy-induced alopecia prevention and treatment overview — bimatoprost discussed as topical hair growth promoter |
| [32642317](https://pubmed.ncbi.nlm.nih.gov/32642317/) | 2020 | Review | Dermatology Practical & Conceptual | CIA prevention and treatment review — provides context for bimatoprost's potential in chemotherapy-related hair loss |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: TFDA package insert data (warnings, contraindications) and DDI profile are currently unavailable (DG001, DG002). These data gaps are rated Blocking and High severity respectively and must be resolved before entering formal safety evaluation.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 RCTs (n = 244–307 per trial) demonstrate bimatoprost's safety and biological activity in androgenetic alopecia, and Phase 1/2 data in alopecia areata is encouraging; FDA approval of Latisse® for eyelash hypotrichosis provides a regulatory precedent and safety baseline that substantially de-risks topical development.

**To proceed, the following is needed:**
- Resolve DG001: Obtain and parse TFDA package insert PDF to identify key warnings and contraindications
- Resolve DG002: Retrieve full MOA documentation from DrugBank API (DB00905)
- Conduct DDI profiling (currently zero interactions on record — unknown whether truly absent or data gap)
- Assess Taiwan TFDA regulatory pathway: reference to FDA Latisse® NDA and Phase 2 AGA RCT packages
- Design or identify a Phase 3 trial for scalp AGA — existing Phase 2 data does not confirm superiority over minoxidil, which is the primary barrier to commercialization
- Establish scalp-specific safety monitoring protocol, including ocular adverse event surveillance (iris pigmentation, periocular changes) for topical scalp application
- Clarify route compatibility for Taiwan development (topical solution formulation optimization data available — PMID 35040730)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

