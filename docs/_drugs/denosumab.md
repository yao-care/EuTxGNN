---
layout: default
title: Denosumab
parent: AI Predictions (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Denosumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Treatment of osteoporosis in postmenopausal women and in men at incre…"
monitor_inn: "Denosumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dermatitis", "diabetic cataract", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "amyopathic dermatomyositis"]
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a monoclonal antibody against RANKL, originally used to treat osteoporosis and bone loss, and to prevent skeletal complications in patients with advanced cancers involving bone.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this specific prediction.
The next-ranked prediction, dermatitis, has somewhat more supporting material (1 Phase 1 trial and several case reports), so it is also discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of osteoporosis in postmenopausal women and in men at increased risk of fractures; treatment of bone loss associated with hormone ablation in men with prostate cancer |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 20 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, denosumab is a human monoclonal antibody that inhibits RANKL (receptor activator of nuclear factor κB ligand), a cytokine that drives osteoclast-mediated bone resorption. Its efficacy in osteoporosis and bone loss is established, and mechanistically it might be applicable to other conditions in which RANKL signaling plays a role.

For severe nonproliferative diabetic retinopathy, the link is speculative. One possible route is RANKL/OPG signaling in vascular calcification and inflammation in diabetic microvascular disease, but no data compiled for this report support it. The very high TxGNN score (0.996) therefore reflects a model-derived association, not demonstrated biology or clinical benefit.

The other top-ranked predictions have a similar profile. Diabetic retinopathy (99.23%) is supported only by indirect papers on denosumab in type 2 diabetes, which do not address retinal outcomes. Dermatitis (97.25%) has a plausible rationale, because RANKL is involved in UV-induced immunosuppression in skin, and it is the only prediction with a registered trial. However, most dermatitis-related literature consists of case reports of denosumab-induced skin reactions, which are safety signals rather than evidence of benefit.

## Clinical Trial Evidence

No clinical trials are registered for severe nonproliferative diabetic retinopathy. The only trial linked to the top-ranked predictions concerns the dermatitis prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01978483](https://clinicaltrials.gov/study/NCT01978483) | Phase 1 | Completed | 31 | Effect of RANKL inhibition on UV-induced immunosuppression; a mechanistic skin-immunology study that did not test efficacy in dermatitis patients |

## Literature Evidence

No publications are available for severe nonproliferative diabetic retinopathy. The closest related papers, for diabetic retinopathy and dermatitis, are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Review/observational | Diabetes Obes Metab | Denosumab vs bisphosphonates in osteoporosis: lower incidence of type 2 diabetes, lower foot ulceration risk and lower all-cause mortality; retinal outcomes not specifically established (diabetic retinopathy prediction) |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observational | Cureus | FRAX fracture risk tool in adults with type 2 diabetes; not related to retinopathy (diabetic retinopathy prediction) |
| [22108301](https://pubmed.ncbi.nlm.nih.gov/22108301/) | 2011 | Review | Clin Ther | Review of denosumab for bone loss in postmenopausal osteoporosis (dermatitis prediction; background on the drug) |
| [39175449](https://pubmed.ncbi.nlm.nih.gov/39175449/) | 2024 | Case report | Acta Derm Venereol | Denosumab-induced acute generalized exanthematous pustulosis (adverse event) |
| [31890758](https://pubmed.ncbi.nlm.nih.gov/31890758/) | 2020 | Case report | Bone Rep | First documented DRESS syndrome in response to denosumab (adverse event) |
| [32656848](https://pubmed.ncbi.nlm.nih.gov/32656848/) | 2021 | Case report | Clin Exp Dermatol | Two cases of lichen planus associated with denosumab (adverse event) |
| [29076163](https://pubmed.ncbi.nlm.nih.gov/29076163/) | 2018 | Case report | J Cutan Pathol | Denosumab-induced cutaneous lichenoid hypersensitivity reaction with a new lymphohistiocytic pattern (adverse event) |

## EU Market Information

All 20 EU authorizations for denosumab products are listed as cancelled. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001120 | Prolia | Not specified | Treatment of osteoporosis in postmenopausal women and in men at increased risk of fractures. In postmenopausal women Prolia significantly reduces... |
| EMEA/H/C/002173 | Xgeva | Not specified | Prevention of skeletal related events (pathological fracture, radiation to bone, spinal cord compression or surgery to bone) in adults with... |
| EMEA/H/C/006378 | Wyost | Not specified | Prevention of skeletal related events (SREs) (pathological fracture, radiation to bone, spinal cord compression or surgery to bone) in adults... |
| EMEA/H/C/006507 | Rolcya | Not specified | Treatment of osteoporosis in postmenopausal women and in men at increased risk of fractures. In postmenopausal women denosumab significantly... |
| EMEA/H/C/006157 | Osenvelt | Not specified | Prevention of skeletal related events (pathological fracture, radiation to bone, spinal cord compression or surgery to bone) in adults with... |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screen; those displayed are all rated Moderate. They include systemic corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, methylprednisolone, betamethasone, triamcinolone, budesonide), immunosuppressants (tacrolimus, mercaptopurine), dupilumab, and radiopharmaceuticals or related agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab).
- **Skin reactions**: The literature compiled for the dermatitis prediction contains multiple case reports of denosumab-associated cutaneous adverse events (AGEP, DRESS, lichen planus, hypersensitivity reactions, erythema nodosum, c-ANCA vasculitis). These argue for caution in any dermatologic repurposing.
- **Paediatric use**: Several lower-ranked predictions involve children or neonates, where denosumab is not established and safety concerns (such as hypocalcaemia and effects on bone growth) apply.

Please refer to the SmPC for the full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, severe nonproliferative diabetic retinopathy, rests only on a high model score, with no trials, no literature, and no supported mechanism (Evidence Level L5). The only prediction with a registered trial, dermatitis, is supported by a Phase 1 mechanistic study and is outweighed by reports of denosumab-induced skin reactions. It could be treated as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Mechanism of action data for denosumab, to allow a proper mechanistic cross-check
- Preclinical or mechanistic studies linking RANKL/OPG signaling to diabetic retinal microvascular disease
- Retinal outcome data from existing diabetic cohorts treated with denosumab
- Full SmPC warnings and contraindications for safety screening
- Clarification of the cancelled status of all 20 EU authorizations
- For dermatitis: results from NCT01978483 and a risk-benefit review given the reported cutaneous adverse events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

