---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Autoinflammatory Disorders to Extracutaneous Mastocytoma

## One-Sentence Summary

Anakinra is a recombinant human interleukin-1 receptor antagonist (IL-1Ra), internationally approved for rheumatoid arthritis and autoinflammatory conditions, but currently not registered in Taiwan.
The TxGNN model ranks **extracutaneous mastocytoma** as the top predicted new indication (score 99.93%), though this carries only AI-prediction-level evidence (L5) with no supporting clinical data.
Across all 10 predicted indications in this multi-indication pack, the strongest clinical evidence lies in **autosomal recessive familial Mediterranean fever** (20 publications, L3) and **pyogenic autoinflammatory syndrome** (19 publications, L3), both of which share a direct IL-1β overactivation pathomechanism that Anakinra is mechanistically designed to block.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally used for rheumatoid arthritis and autoinflammatory conditions |
| Top TxGNN Prediction | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level (Top Prediction) | L5 |
| Taiwan Market Status | Not marketed |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision (Top Prediction) | Hold |

---

## All Predicted Indications Overview

| Rank | Disease | TxGNN Score | Evidence Level | Clinical Trials | Publications | Recommendation |
|------|---------|-------------|----------------|-----------------|--------------|----------------|
| 1 | Extracutaneous mastocytoma | 99.93% | L5 | 0 | 0 | Hold |
| 2 | Hepatic infarction | 99.89% | L5 | 0 | 0 | Hold |
| 3 | Autosomal recessive familial Mediterranean fever | 99.89% | **L3** | 0 | **20** | Research Question |
| 4 | Aggressive systemic mastocytosis | 99.88% | L4 | 0 | 2 | Research Question |
| 5 | Hepatic veno-occlusive disease | 99.88% | L5 | 0 | 0 | Hold |
| 6 | Peliosis hepatis | 99.85% | L5 | 0 | 0 | Hold |
| 7 | Oligoarticular JIA with ANA | 99.85% | L4 | 0 | 1 | Research Question |
| 8 | Oligoarticular JIA without ANA | 99.85% | L4 | 0 | 1 | Research Question |
| 9 | Pyogenic autoinflammatory syndrome | 99.83% | **L3** | 0 | **19** | **Proceed with Guardrails** |
| 10 | Unclassified autoinflammatory syndrome | 99.81% | **L3** | 0 | **2** | Research Question |

---

## Why is This Prediction Reasonable?

### Top Prediction: Extracutaneous Mastocytoma (Rank 1)

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Anakinra is a recombinant form of the naturally occurring human IL-1 receptor antagonist that competitively inhibits the binding of both IL-1α and IL-1β to the IL-1 type I receptor (IL-1RI), thereby blocking IL-1-driven inflammatory signalling.

For extracutaneous mastocytoma specifically, the TxGNN rationale notes that IL-1 signalling may participate in mast cell activation. Mast cells are known to produce IL-1β, and systemic mast cell diseases can be accompanied by inflammatory cytokine release. However, extracutaneous mastocytoma is an extremely rare neoplastic disease, and no direct or indirect clinical evidence currently supports the efficacy of IL-1 blockade in this condition.

The high TxGNN score (99.93%) most likely reflects the global network connectivity of mast cell disease nodes in the knowledge graph rather than disease-specific mechanistic evidence. Until preclinical or clinical data emerge, this prediction should be treated as hypothesis-generating only.

---

### Best-Evidenced Predictions

#### Autosomal Recessive Familial Mediterranean Fever (Rank 3, L3)

FMF is caused by mutations in the *MEFV* gene encoding pyrin (marenostrin). Mutant pyrin undergoes abnormal hypophosphorylation in response to RhoA GTPase signalling, leading to constitutive activation of the pyrin inflammasome, excessive caspase-1 cleavage, and uncontrolled IL-1β and IL-18 secretion. This IL-1β overproduction is the central driver of recurrent febrile serositis attacks and, over time, systemic AA amyloidosis.

Anakinra, as a direct IL-1 receptor antagonist, is mechanistically the most rational intervention in this pathway. Multiple published case series report successful use of Anakinra in colchicine-resistant or colchicine-intolerant FMF patients, including suppression of attacks and partial reversal of amyloid-related proteinuria. Genetic association data (PMID 26861613) further demonstrate that IL-1Ra polymorphisms influence FMF susceptibility, directly linking the drug target to disease biology.

#### Pyogenic Autoinflammatory Syndrome (Rank 9, L3)

Pyogenic autoinflammatory syndromes — including PAPA (pyogenic arthritis, pyoderma gangrenosum, acne), PAPASH, and PASH — are caused by gain-of-function mutations in *PSTPIP1*, which encodes a scaffolding protein regulating NLRP3 inflammasome assembly. Hyperphosphorylated PSTPIP1 binds pyrin, dysregulates caspase-1 activation, and drives massive IL-1β overproduction. This makes IL-1Ra the most direct targeted therapy.

A 2023 systematic scoping review (PMID 38259483) and a 2024 case report (PMID 39006661) directly document Anakinra's efficacy and safety in PSTPIP1-associated inflammatory diseases, supporting an evidence-backed rationale for further investigation.

---

## Clinical Trial Evidence (Top Prediction: Extracutaneous Mastocytoma)

Currently no related clinical trials registered.

---

## Literature Evidence: Autosomal Recessive Familial Mediterranean Fever (Rank 3, L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case Series | Nephrol Dial Transplant | Anakinra successfully treated colchicine-resistant FMF with AA amyloidosis; stable graft function maintained post-renal transplant |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Case Report | Rheumatol Int | Anakinra effective in a 52-year-old colchicine-resistant FMF patient with secondary amyloidosis and end-stage renal disease |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case Series | Nephrol Dial Transplant | IL-1 inhibitor (including Anakinra) showed dramatic benefit in FMF patients complicated with amyloidosis and renal failure |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case Report | Joint Bone Spine | FMF-associated myositis and spondyloarthritis successfully treated with Anakinra after colchicine failure |
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case Series + Review | Semin Arthritis Rheum | Multi-patient series demonstrating IL-1 targeting (Anakinra/canakinumab) as a rational new approach for FMF; mechanistic link via pyrin-IL-1 axis |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | IL-1β biological treatment of FMF; summarises evidence base for Anakinra and canakinumab in colchicine-resistant disease |
| [26861613](https://pubmed.ncbi.nlm.nih.gov/26861613/) | 2016 | Genetic Association | Gene | IL-1Ra (rs2234663) polymorphisms associated with FMF susceptibility in Turkish population, directly linking drug target to disease biology |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohort | Rheumatol Int | Real-world data: canakinumab effective in FMF patients resistant/intolerant to colchicine **and/or Anakinra**, confirming Anakinra as prior standard of care |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Review | Curr Med Chem | Comprehensive review of colchicine and biologics (including Anakinra) for FMF; positions IL-1 blockade as second-line for non-responders |
| [31205631](https://pubmed.ncbi.nlm.nih.gov/31205631/) | 2019 | Review | Mediterr J Hematol Infect Dis | FMF treatment planning review; RhoA/pyrin axis described as mechanistic basis for IL-1β overactivation and IL-1Ra relevance |

---

## Literature Evidence: Pyogenic Autoinflammatory Syndrome (Rank 9, L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Systematic Review / Case Series | Front Immunol | Comprehensive scoping review of Anakinra and canakinumab efficacy/safety in PSTPIP1-associated inflammatory diseases (PAPA, PAMI spectrum) |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Case Report | Cureus | Anakinra successfully used in PAPASH spectrum disorder; case report with literature review confirming IL-1 pathway as the therapeutic target |
| [27448064](https://pubmed.ncbi.nlm.nih.gov/27448064/) | 2016 | Review | Hautarzt | Anakinra used in PASH and PAPASH autoinflammatory diseases based on IL-1β involvement |
| [24275598](https://pubmed.ncbi.nlm.nih.gov/24275598/) | 2013 | Review | Semin Immunol | Landmark review on IL-1 blocking therapies; documents expanding list of diseases responsive to IL-1Ra, including pyogenic syndromes |
| [22161697](https://pubmed.ncbi.nlm.nih.gov/22161697/) | 2012 | Case Series | Arthritis Rheum | Genotype-phenotype correlation in 5 PAPA syndrome patients; IL-1β overproduction identified as molecular hallmark |
| [21532836](https://pubmed.ncbi.nlm.nih.gov/21532836/) | 2010 | Review | Curr Genomics | PAPA syndrome: PSTPIP1 mutations cause hyper-phosphorylated protein, dysregulated inflammasome, and IL-1β overproduction — rationale for IL-1Ra |
| [28251506](https://pubmed.ncbi.nlm.nih.gov/28251506/) | 2017 | Case Report + Review | Infection | PAPA syndrome diagnosis and clinical management challenges; includes discussion of IL-1 targeting |
| [21745697](https://pubmed.ncbi.nlm.nih.gov/21745697/) | 2012 | Case Report | J Am Acad Dermatol | PASH syndrome described as distinct from PAPA; PSTPIP1 promoter involvement and IL-1 pathway dysregulation documented |
| [29742056](https://pubmed.ncbi.nlm.nih.gov/29742056/) | 2018 | Review | Clin Exp Rheumatol | Dermatologic perspective on autoinflammatory diseases; IL-1 blockade positioned as key therapeutic strategy in PSTPIP1-related syndromes |
| [27464597](https://pubmed.ncbi.nlm.nih.gov/27464597/) | 2016 | Review | Curr Opin Rheumatol | Expanding spectrum of PSTPIP1 autoinflammatory diseases and pathogenesis insights; supports mechanistic rationale for Anakinra |

---

## Literature Evidence: Unclassified Autoinflammatory Syndrome (Rank 10, L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36589607](https://pubmed.ncbi.nlm.nih.gov/36589607/) | 2022 | Retrospective Cohort | Arch Rheumatol | Single-centre experience of Anakinra in paediatric rheumatic diseases including unclassified autoinflammatory conditions; documents real-world efficacy |
| [37747561](https://pubmed.ncbi.nlm.nih.gov/37747561/) | 2024 | Multicentre Cohort | Rheumatol Int | German GARROD registry: 152 patients with autoinflammatory diseases receiving anti-IL-1 therapy (including Anakinra); includes FMF, CAPS, TRAPS, and unclassified AIDs |

---

## Literature Evidence: Aggressive Systemic Mastocytosis (Rank 4, L4)

> **Note**: Retrieved literature relates to Schnitzler syndrome (an IL-1-driven urticarial disorder with mast cell overlap), not aggressive systemic mastocytosis directly. This constitutes indirect mechanistic evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40718535](https://pubmed.ncbi.nlm.nih.gov/40718535/) | 2025 | Case Report | Oxford Med Case Reports | Anakinra effective in Schnitzler syndrome (IL-1-driven chronic urticaria with mast cell involvement); 14 months of good tolerance without steroids |
| [25840575](https://pubmed.ncbi.nlm.nih.gov/25840575/) | 2015 | Case Report | Hellenic J Nucl Med | Schnitzler syndrome with bone remodelling abnormalities responds well to IL-1 inhibitor Anakinra; bone imaging characterised |

---

## Taiwan Market Information

Anakinra is **not registered in Taiwan** (market status: 未上市). No marketing authorizations are on file with the Taiwan FDA. Prescribers wishing to use Anakinra in Taiwan would need to apply for special import approval on a compassionate use or named-patient basis.

> For reference: Anakinra (Kineret®, Swedish Orphan Biovitrum) holds EMA marketing authorization in the EU for rheumatoid arthritis and selected autoinflammatory conditions including NOMID/CINCA syndrome. No Taiwan-specific regulatory data is available in this Evidence Pack.

---

## Safety Considerations

No Taiwan FDA prescribing information, key warnings, or contraindication data were available for this analysis. Drug-drug interaction data query returned no results.

Please refer to the current Kineret® Summary of Product Characteristics (SmPC) for full safety information, including:
- Risk of serious infections (immunosuppression)
- Contraindication in patients with active infection
- Neutropenia monitoring requirements
- Injection site reactions (most common adverse effect)
- Use in renal impairment (dose adjustment required for eGFR < 30 mL/min)

---

## Conclusion and Next Steps

### For the Top TxGNN Prediction (Extracutaneous Mastocytoma)

**Decision: Hold**

**Rationale:**
Extracutaneous mastocytoma is an extremely rare neoplastic disease with no clinical or preclinical evidence supporting IL-1 blockade. The high TxGNN score likely reflects non-specific knowledge graph topology rather than disease-specific biology.

**To proceed, the following is needed:**
- Preclinical data (in vitro or murine model) demonstrating IL-1β involvement in extracutaneous mastocytoma pathogenesis
- Case reports or registry data from international mastocytosis centres

---

### For Autosomal Recessive Familial Mediterranean Fever (Rank 3)

**Decision: Research Question — Proceed to Investigator-Initiated Study**

**Rationale:**
Multiple published case series and reviews document Anakinra efficacy in colchicine-resistant FMF with a direct IL-1Ra mechanistic rationale. Evidence is L3 (observational); formal prospective data is lacking but biological plausibility is high.

**To proceed, the following is needed:**
- Systematic review or meta-analysis of existing case series
- Prospective registry study in colchicine-resistant FMF patients
- Taiwan-specific assessment: identify FMF patient population via rheumatology centres (rare in Taiwan but cases reported in Japanese/Korean populations)
- Obtain Anakinra SmPC and establish named-patient import pathway

---

### For Pyogenic Autoinflammatory Syndrome (Rank 9)

**Decision: Proceed with Guardrails**

**Rationale:**
A 2023 systematic scoping review and 2024 case report directly document Anakinra efficacy in PSTPIP1-associated inflammatory diseases. The mechanistic link (IL-1β overproduction via mutant PSTPIP1 → inflammasome dysregulation) is well-established, and Anakinra is a rational first-line biologic for patients refractory to conventional therapy.

**To proceed, the following is needed:**
- Genetic testing capability for *PSTPIP1* mutation confirmation in target patients
- Establish compassionate use / special import approval pathway for Anakinra in Taiwan
- Define monitoring protocol: CBC, CRP/SAA, injection site assessment, infection surveillance
- Prospective documentation of cases to build local evidence registry
- Full MOA data retrieval from DrugBank and TFDA SmPC equivalent to complete safety assessment (current DG001 and DG002 data gaps must be resolved before clinical implementation)

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

