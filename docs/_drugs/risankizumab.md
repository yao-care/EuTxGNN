---
layout: default
title: Risankizumab
parent: High Evidence (L1-L2)
nav_order: 509
evidence_level: L2
indication_count: 10
---

# Risankizumab
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

Using the evidence-pack schema and decision rules from the project prompt (not a Superpowers skill scenario — this is a templated report-generation task fully specified by the system instructions), here is the report:

---

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

> Risankizumab (an anti-IL-23 p19 monoclonal antibody) was first globally approved for **psoriasis** (psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, erythrodermic psoriasis).
> The TxGNN model predicts it may also be effective for **Dermatitis** — specifically atopic dermatitis (AD) —
> with **7 clinical trials** and **16 publications** currently identified, but only **1 completed Phase 2 RCT** directly testing this new indication, and the sponsor has not advanced it to Phase 3.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis (psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis, erythrodermic psoriasis) — per literature, first approved 2019 in Japan |
| Predicted New Indication | Dermatitis (atopic dermatitis) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (0 authorizations in this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal DrugBank-classified mechanism-of-action record is currently a data gap (DG002) for Risankizumab. However, the identified literature (McKeage & Duggan, *Drugs*, 2019, PMID 31098898) describes it as a humanized IgG monoclonal antibody that selectively targets the **p19 subunit of IL-23**, thereby blocking the IL-23/Th17 inflammatory axis that drives psoriasis.

Psoriasis and dermatitis are both chronic inflammatory skin diseases, which is the conceptual basis for TxGNN's prediction. However, the pathophysiology diverges at the molecular level: atopic dermatitis is predominantly a **Th2 (IL-4/IL-13)** and Th22-driven disease, with IL-23/Th17 playing only a partial, secondary role. This is reflected in the actual trial outcome — the one completed Phase 2 RCT of risankizumab in moderate-to-severe AD (NCT03706040, PMID 36588137) did not lead to Phase 3 development, and published expert opinion notes that IL-23 inhibitors generally underperform relative to IL-4/13 blockers (e.g., dupilumab) or JAK inhibitors in AD.

Notably, several case reports in the literature describe the **opposite direction of effect**: risankizumab-treated psoriasis patients developing *paradoxical eczematous eruptions/dermatitis* as an adverse reaction (PMID 33185530, 36939506, 41645692), while conversely one report used risankizumab to successfully manage eczema induced by a different biologic (brodalumab; PMID 37014149). This bidirectional relationship between risankizumab and "dermatitis" weakens confidence in a straightforward efficacy narrative and should be treated as a signal requiring careful interpretation, not dismissed as noise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Randomized, placebo-controlled RCT of risankizumab in moderate-to-severe atopic dermatitis (adults/adolescents) — the only trial directly testing "dermatitis" as a genuinely new (non-psoriasis) indication |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Double-blind RCT in moderate-to-severe genital or scalp psoriasis — likely a psoriasis-spectrum extension, not a novel dermatitis indication |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Prospective observational biomarker study profiling six immune-mediated skin diseases including atopic dermatitis and psoriasis; real-world evidence, not interventional |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Head-to-head vs. apremilast in moderate plaque psoriasis — known/approved indication, not new |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Observational cohort of moderate-to-severe chronic plaque psoriasis in Taiwan — known/approved indication |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Pharmacogenetic observational study of biologic drug survival in cutaneous psoriasis — not efficacy evidence for a new indication |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Feasibility study of a microdevice testing already-FDA-approved drugs on atopic dermatitis/psoriasis skin — device feasibility, not efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT (Tier 1) | Dermatology and Therapy | Phase 2 RCT of risankizumab in moderate-to-severe AD; rationale based on IL-23/IL-22 blockade in Th2/Th22/Th17-mixed AD pathogenesis |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules for pediatric AA, psoriasis, AD, and HS |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opin Biol Ther | Review of emerging biologics for pediatric atopic dermatitis |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic Review | Am J Clin Dermatol | Systemic therapy management of erythrodermic psoriasis (psoriasis-spectrum, not new indication) |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Cohort | Experimental Dermatology | Retrospective cohort on risankizumab response in patients with history of erythrodermic psoriasis |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Review of systemic immunomodulators for psoriasis and eczema in military populations |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "Risankizumab: First Global Approval" — background on MOA and original approved indications |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case Series | Int J Dermatol | Combined dupilumab + risankizumab in patients with concomitant AD and psoriasis |
| [41645692](https://pubmed.ncbi.nlm.nih.gov/41645692/) | 2026 | Case Report | Dermatology Reports | Paradoxical eczema induced by IL-23 inhibitors (including risankizumab), managed with upadacitinib — safety signal, opposite direction of effect |
| [33185530](https://pubmed.ncbi.nlm.nih.gov/33185530/) | 2020 | Case Report | Eur J Dermatol | Eczematous eruption occurring in psoriasis patients during risankizumab treatment — safety signal |

---

## EU Market Information

No EU marketing authorization records are currently available in this dataset (market status: **Not Marketed**, 0 authorizations). This should be verified directly against the EMA register, as it is unclear whether this reflects an actual regulatory status or a data-collection gap for this drug entry.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) are not currently available for this drug in the evidence pack — this is flagged as a **Blocking** data gap (DG001) that prevents a S1 safety pre-assessment.

- **Literature-derived signal (not from formal DDI/warning data):** Multiple case reports describe risankizumab **inducing** paradoxical eczematous/dermatitis reactions in psoriasis patients (PMID 33185530, 36939506, 41645692), which directly conflicts with, and should temper enthusiasm for, its repurposing as a *treatment* for dermatitis.

> Please refer to the official SmPC for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 2 RCT (L2 evidence) supports risankizumab in atopic dermatitis, the sponsor has not advanced it to Phase 3, and literature also reports the opposite phenomenon — risankizumab-induced dermatitis as a paradoxical adverse event. Combined with a Blocking gap in formal safety/warning data (DG001) and a High-severity gap in confirmed MOA (DG002), the evidence is insufficient to proceed past a research-question stage.

**To proceed, the following is needed:**
- Official SmPC/EMA warnings, contraindications, and DDI data (resolves DG001, currently blocking)
- Confirmed DrugBank-level MOA record (resolves DG002)
- Verification of actual EU marketing authorization status (dataset currently shows "Not Marketed," which should be cross-checked against EMA's public register)
- Sponsor clarification on why the AD Phase 2 program was not progressed to Phase 3
- A structured pharmacovigilance review of the paradoxical eczema signal before any further indication expansion work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

