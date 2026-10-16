---
layout: default
title: Ixekizumab
parent: AI Predictions (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ixekizumab: predicted new indication Rheumatoid vasculitis (evidence level L5). Approved use: Moderate to severe plaque psoriasis in adults who are candidates for…"
monitor_inn: "Ixekizumab"
predicted_indications: ["rheumatoid vasculitis", "acute lymphoblastic/lymphocytic leukemia", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease", "polyarticular juvenile rheumatoid arthritis", "vertebral disease", "fibromatosis, gingival"]
---

# Ixekizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ixekizumab: From Plaque Psoriasis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab (brand name Taltz) is an IL-17A–blocking antibody, originally used to treat plaque psoriasis, psoriatic arthritis, axial spondyloarthritis and juvenile arthritis subtypes.
The TxGNN model's top-ranked prediction is **rheumatoid vasculitis**, but this prediction has **no direct supporting studies**: the one linked trial is about perioperative immunosuppressant management, and no literature was retrieved.
The clinical evidence in the compiled data (**18 trials** and **20 publications** under the sixth-ranked prediction, inflammatory spondylopathy) mostly confirms existing approved uses rather than a new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe plaque psoriasis in adults who are candidates for systemic therapy (the label also covers paediatric psoriasis, psoriatic arthritis, axial spondyloarthritis and juvenile idiopathic arthritis subtypes) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Cancelled only (no currently valid authorization in the data compiled) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ixekizumab is a monoclonal antibody that neutralizes IL-17A, a cytokine that drives inflammation in psoriasis, psoriatic arthritis and spondyloarthritis.

IL-17A is also implicated in systemic vasculitis and other autoimmune inflammation, so blocking it is biologically plausible for rheumatoid vasculitis. However, this is a computational prediction only. No clinical or literature evidence supports ixekizumab in this condition.

The other predictions in the list are weaker:
- Several (acute lymphoblastic leukaemia, the CLL/SLL entries, hypermobility of the coccyx, Kummell disease, gingival fibromatosis) have no clear mechanistic link and no evidence.
- Polyarticular juvenile rheumatoid arthritis has indirect support, because ixekizumab is already used in two JIA subtypes (juvenile psoriatic arthritis and enthesitis-related arthritis).
- "Inflammatory spondylopathy" and "vertebral disease" overlap with axial spondyloarthritis, which is already an approved use. This is closer to confirming an existing label than to true repurposing.

## Clinical Trial Evidence

**Rheumatoid vasculitis (top prediction)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty. It does not test ixekizumab for rheumatoid vasculitis, so it is not efficacy evidence. |

**Inflammatory spondylopathy (the best-supported prediction; overlaps with approved uses)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04285229](https://clinicaltrials.gov/study/NCT04285229) | Phase 3 | Completed | 147 | Randomized, placebo-controlled study in Chinese patients with radiographic axial spondyloarthritis |
| [NCT02696798](https://clinicaltrials.gov/study/NCT02696798) | Phase 3 | Completed | 316 | Randomized, placebo-controlled study in TNF inhibitor–experienced radiographic axSpA |
| [NCT02757352](https://clinicaltrials.gov/study/NCT02757352) | Phase 3 | Completed | 303 | 52-week randomized, placebo-controlled study in non-radiographic axSpA |
| [NCT02696785](https://clinicaltrials.gov/study/NCT02696785) | Phase 3 | Completed | 341 | Active- and placebo-controlled study in biologic-naive radiographic axSpA |
| [NCT03129100](https://clinicaltrials.gov/study/NCT03129100) | Phase 3 | Completed | 773 | 104-week extension with randomized withdrawal and retreatment in axSpA |
| [NCT02349295](https://clinicaltrials.gov/study/NCT02349295) | Phase 3 | Completed | 363 | Placebo-controlled study in biologic-experienced psoriatic arthritis |
| [NCT01695239](https://clinicaltrials.gov/study/NCT01695239) | Phase 3 | Completed | 417 | Active- and placebo-controlled study in biologic-naive psoriatic arthritis |
| [NCT02584855](https://clinicaltrials.gov/study/NCT02584855) | Phase 3 | Completed | 394 | Open-label lead-in followed by randomized withdrawal in psoriatic arthritis |
| [NCT03151551](https://clinicaltrials.gov/study/NCT03151551) | Phase 4 | Completed | 566 | Open-label comparison of ixekizumab versus adalimumab in psoriatic arthritis |
| [NCT06588296](https://clinicaltrials.gov/study/NCT06588296) | Phase 3 | Completed | 279 | Ixekizumab alone versus with tirzepatide in psoriatic arthritis with obesity or overweight |

Further trials were retrieved for this prediction. They include a paediatric study (NCT04527380), a tapering study (NCT04610476), an Indian safety study (NCT05855967), and several registry or vaccine-response studies. They are omitted here because they are less relevant.

## Literature Evidence

No literature was found for rheumatoid vasculitis. The following publications were retrieved for the spondyloarthritis-related predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31813637](https://pubmed.ncbi.nlm.nih.gov/31813637/) | 2020 | RCT (COAST-X) | Lancet | Ixekizumab in non-radiographic axial spondyloarthritis |
| [30343531](https://pubmed.ncbi.nlm.nih.gov/30343531/) | 2019 | RCT | Arthritis Rheumatol | 16-week results in radiographic axSpA after TNF inhibitor failure |
| [27553214](https://pubmed.ncbi.nlm.nih.gov/27553214/) | 2017 | RCT (SPIRIT-P1) | Ann Rheum Dis | Ixekizumab in biologic-naive psoriatic arthritis, with adalimumab as active control |
| [31563894](https://pubmed.ncbi.nlm.nih.gov/31563894/) | 2020 | RCT | Ann Rheum Dis | Head-to-head ixekizumab versus adalimumab in psoriatic arthritis (24 weeks) |
| [41903163](https://pubmed.ncbi.nlm.nih.gov/41903163/) | 2026 | RCT | Arthritis Rheumatol | Ixekizumab plus tirzepatide gave greater disease control than ixekizumab alone in psoriatic arthritis with overweight or obesity |
| [38503473](https://pubmed.ncbi.nlm.nih.gov/38503473/) | 2024 | Systematic review | Ann Rheum Dis | Evidence informing the 2023 EULAR psoriatic arthritis recommendations |
| [36270657](https://pubmed.ncbi.nlm.nih.gov/36270657/) | 2023 | Systematic review | Ann Rheum Dis | Biologic DMARD evidence informing the 2022 ASAS-EULAR axSpA recommendations |
| [41050680](https://pubmed.ncbi.nlm.nih.gov/41050680/) | 2025 | Network meta-analysis | Front Immunol | Efficacy and safety of IL-17, IL-12/23 and IL-23 inhibitors in psoriatic arthritis |
| [32719044](https://pubmed.ncbi.nlm.nih.gov/32719044/) | 2020 | Review | Ann Rheum Dis | Paradoxical gastrointestinal effects of IL-17 blockers, including disease exacerbation in Crohn's disease and ulcerative colitis |
| [40701624](https://pubmed.ncbi.nlm.nih.gov/40701624/) | 2025 | Cohort study | RMD Open | Real-world effectiveness in 709 Danish patients with axSpA and PsA |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003943 (cancelled) | Taltz | Not specified | Plaque psoriasis in adults; paediatric plaque psoriasis; psoriatic arthritis; ankylosing spondylitis and non-radiographic axial spondyloarthritis; juvenile psoriatic arthritis... |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries; the 20 listed in the data compiled include one **major** interaction and several moderate ones.
  - **Major**: adalimumab (combining two immunomodulatory biologics).
  - **Moderate** (examples): warfarin, apixaban, rivaroxaban, dicoumarol, simvastatin, tacrolimus, theophylline, aminophylline, roflumilast, nifedipine, fentanyl, lidocaine, hydrocodone, and tetanus toxoid vaccine.
  - **Minor**: zinc salts.
- **Class-related monitoring points** (from the literature and mechanistic review): paradoxical inflammatory bowel disease or gastrointestinal effects of IL-17 blockers, infections including candidiasis, and vaccination planning.

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, rheumatoid vasculitis, has a high model score (97.53%) and a plausible IL-17A rationale. It has no direct trial or literature support, so it remains at evidence level L5.
- The strong Phase 3 evidence applies to spondyloarthritis and psoriatic arthritis, which are already approved uses (that prediction would be L1, Proceed with Guardrails, but it is confirmation of an existing label rather than new repurposing).

**To proceed, the following is needed:**
- Mechanism of action data and a detailed mechanistic analysis for vasculitis
- Case reports, case series or preclinical studies of IL-17A blockade in rheumatoid vasculitis
- Label warnings and contraindications from the SmPC (currently missing)
- Clarification of the cancelled EU authorization status, since no valid marketing authorization appears in the data compiled
- If pursuing the spondyloarthritis-related predictions, narrowing them to specific inflammatory entities rather than broad categories like "vertebral disease"
- A safety plan covering inflammatory bowel disease, infection and vaccination, and a review of the major adalimumab interaction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

