---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Fluticasone Furoate
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

# Fluticasone Furoate: From Unspecified Indication to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate's original approved indication is not documented in the current dataset (no EU marketing authorization on file), and its mechanism of action is also unrecorded here. The TxGNN model predicts it may be effective for **Atopic Eczema**, with **11 clinical trials** and **2 publications** currently identified as supporting evidence for this candidate pair.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in dataset (0 EU authorizations on file) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fluticasone furoate is not available in this dataset. Elsewhere in the same evidence pack, the drug is characterized as a third-generation, high-potency synthetic glucocorticoid that binds the glucocorticoid receptor (GR) to suppress IL-4/5/13-driven inflammatory pathways — the pharmacological basis for its established respiratory combination products (e.g., fluticasone furoate/vilanterol, fluticasone furoate/umeclidinium/vilanterol).

Because no original indication is documented here, the relationship between a prior use and atopic eczema cannot be drawn directly from this dataset. Instead, the rationale rests on drug-class mechanism: topical and systemic glucocorticoids suppress the keratinocyte and T-cell inflammatory cascade via GR, which is the standard pharmacological basis for corticosteroid use in atopic dermatitis/eczema.

However, it is important to note that the direct clinical evidence identified for this indication is drawn almost entirely from **fluticasone propionate** (marketed as Cutivate/Flixotide) rather than the furoate ester evaluated here. Fluticasone furoate has substantially higher GR-binding affinity and a different formulation history (primarily developed for intranasal and inhaled use), so its applicability to topical eczema treatment currently relies on extrapolation from the propionate ester rather than furoate-specific trial data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone propionate) 0.05% lotion and its effect on the HPA axis in pediatric atopic dermatitis |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Randomized study of intermittent fluticasone propionate 0.05% cream (twice weekly) plus daily moisturizer to reduce relapse risk in stabilized pediatric AD |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Double-blind, vehicle-controlled paired study of combined pimecrolimus (Elidel) + fluticasone (Cutivate) cream in severe AD lesions |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Randomized double-blind comparison of tacrolimus 0.03% vs. fluticasone 0.005% ointment in children ≥2 years with moderate-to-severe AD |
| [NCT03594565](https://clinicaltrials.gov/study/NCT03594565) | Early Phase 1 | Completed | 13 | Case series on topical nasal steroids for skin reactions to continuous glucose monitors in children/youth with type 1 diabetes |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Randomized double-blind comparison of tacrolimus 0.1% vs. fluticasone 0.005% ointment in adults with facial ("red face") AD lesions |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Pilot RCT comparing EpiCeram device vs. mid-strength fluticasone propionate 0.05% steroid cream in pediatric AD |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | N/A | Completed | 98 | RCT of oral probiotic supplementation in children with AD, using SCORAD index outcome |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | RCT of proactive skin-barrier care (EpiCeram) plus proactive fluticasone propionate cream vs. reactive therapy to prevent AD/food allergy in infants |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | RCT of twice-weekly fluticasone propionate 0.05% cream maintenance therapy to reduce AD relapse risk in children |

*(One additional low-relevance trial, NCT00426283 — swallowed fluticasone propionate for eosinophilic esophagitis — was excluded as a disease mismatch.)*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian Journal of Otolaryngology and Head and Neck Surgery | Case study on allergen immunotherapy in a patient with autoimmune terrain; notes recent applications of immune-modulating approaches to atopic dermatitis |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review (safety) | Neuroimmunomodulation | Review of intranasal corticosteroids and HPA-axis adrenal suppression risk, relevant to corticosteroid safety monitoring in allergic/atopic conditions |

## EU Market Information

No EU marketing authorizations for fluticasone furoate were found in the reviewed dataset (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this dataset (DDI query returned no results).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking**-severity data gap exists on TFDA/EMA label warnings and contraindications, which prevents even an initial (S1) safety assessment for this drug.
- The atopic eczema evidence base is L2 and largely extrapolated from fluticasone **propionate** trials rather than furoate-specific data, and no EU marketing authorization for furoate is on file in this dataset.

**To proceed, the following is needed:**
- TFDA/EMA product label (warnings, contraindications) — blocking gap, must be resolved before any safety review
- Furoate-specific mechanism of action / receptor-binding data (currently a High-severity gap)
- Confirmation of EU marketing authorization status for fluticasone furoate products
- Furoate-specific (not propionate-ester) clinical evidence in atopic dermatitis/eczema
- Consider a separate evaluation of **obstructive lung disease** (rank 9 in this same evidence pack): it carries L1 evidence with multiple completed Phase 3 RCTs (e.g., IMPACT, FULFIL, SUMMIT) already supporting fluticasone furoate combination therapy, and may be a stronger candidate for guardrailed progression than atopic eczema.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

