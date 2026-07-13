---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I (MPS I) to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase (Aldurazyme) is a recombinant human alpha-L-iduronidase used as enzyme replacement therapy (ERT) for Mucopolysaccharidosis type I (MPS I, including Hurler syndrome) — a rare lysosomal storage disorder caused by the hereditary deficiency of this enzyme.
The TxGNN model predicts it may be effective for **lysosomal storage disease with skeletal involvement**, with **0 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucopolysaccharidosis type I (MPS I / Hurler syndrome) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Laronidase is a recombinant human alpha-L-iduronidase — the enzyme that is deficient in MPS I. When this enzyme is absent, glycosaminoglycans (GAGs), specifically dermatan sulfate and heparan sulfate, progressively accumulate in tissues throughout the body. In the skeletal system, this GAG accumulation in bone matrix and connective tissue leads to the characteristic dysostosis multiplex, short stature, joint contractures, and ligamentous laxity that define the musculoskeletal phenotype of MPS I across its disease spectrum.

The mechanistic link to lysosomal storage disease with skeletal involvement is directly supported by experimental evidence. A key in vitro study (PMID 18758061) demonstrated that laronidase is taken up by both fibroblasts and **osteoblasts** via mannose-6-phosphate (M6P) receptors, is subsequently transported to lysosomes, and there cleaves accumulated substrates. This provides molecular-level proof that laronidase can act within bone-forming cells. Clinically, a 6.5-year observational follow-up of a patient with Scheie syndrome (attenuated MPS I, PMID 23127271) documents detailed skeletal monitoring — joint range of motion, skeletal radiographs — as primary outcome measures, confirming that skeletal manifestations are a core therapeutic target for ERT in MPS I.

This prediction is best understood as a formal classification of the **skeletal manifestation subtype** of MPS I, the drug's already-approved indication, rather than a truly novel repurposing target. The biological overlap is very high. The primary uncertainty lies in disease classification boundaries rather than in mechanism, making this one of the highest-confidence, most clinically plausible predictions in this Evidence Pack.

---

## Clinical Trials

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Case report / observational | *Pediatric Neurology* | 6.5-year ERT follow-up of a boy with Scheie syndrome (attenuated MPS I) initiated at age 2.5; detailed tracking of skeletal radiographs, joint range of motion, cardiac, ophthalmologic, and audiologic outcomes; disease progression observed despite therapy |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro mechanistic study | *Biological & Pharmaceutical Bulletin* | Direct demonstration that laronidase is taken up by MPS I fibroblasts **and osteoblasts** via M6P receptors; enzyme transported to lysosomes and processes accumulated GAG substrates — key mechanistic evidence for skeletal cell activity |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | *Pediatric Endocrinology Reviews* | Comprehensive review of MPS I disease spectrum (Hurler, Hurler/Scheie, Scheie); describes skeletal involvement across phenotypes including dysostosis multiplex; covers diagnostic workup and treatment options |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Drug review | *BioDrugs* | Early development overview of laronidase; reports Phase I trial in MPS I patients; US and EU orphan drug designation; BioMarin-Genzyme joint venture background |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication — lysosomal storage disease with skeletal involvement — represents the skeletal phenotype of MPS I, the drug's established therapeutic target. Direct in vitro evidence confirms that laronidase is active in osteoblasts, and clinical observational data document skeletal outcomes in ERT-treated MPS I patients. However, formal clinical endpoints specifically designed for skeletal disease, and complete safety documentation for Taiwan, are currently absent.

**To proceed, the following is needed:**
- Retrieve TFDA SmPC or EMA SmPC (Aldurazyme) to complete safety evaluation — currently no warnings or contraindications data available in this pack (DG001, Blocking)
- Document the full mechanism of action via DrugBank (DG002) — particularly CNS penetration limitations relevant to Hurler-type severe skeletal disease with concurrent neurological involvement
- Identify or design clinical outcome measures specifically targeting skeletal endpoints (e.g., 6-minute walk test, joint range of motion, radiographic bone age) in MPS I ERT trials — existing Phase 3 data are broad somatic endpoints rather than skeletal-specific
- Assess feasibility of Taiwan patient identification: MPS I is ultra-rare; newborn screening programs and registry data should be surveyed before any local study planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

