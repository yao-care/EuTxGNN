---
layout: default
title: Carbidopa
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Carbidopa
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

# Carbidopa: From Parkinson's Disease Adjunct to Lewy Body Dementia

## One-Sentence Summary

Carbidopa is a peripheral DOPA decarboxylase inhibitor used exclusively in combination with levodopa as the standard of care for Parkinson's disease motor symptoms; it carries no standalone EU marketing authorization in the database reviewed here.
The TxGNN model generated **10 novel predicted indications** across rare neurological and metabolic disorders; the strongest clinical evidence supports **Lewy Body Dementia (LBD)**, with **1 clinical trial** and **18 publications** identified — primarily reviews, retrospective cohorts, and case reports.
TxGNN's top-ranked prediction (Rasmussen subacute encephalitis, score 98.43%) currently has **zero supporting clinical evidence** and remains a **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (peripheral decarboxylase inhibitor, adjunct to levodopa) |
| Best-Evidenced Predicted Indication | Lewy Body Dementia |
| TxGNN Score — Top Prediction | 98.43% (Rasmussen subacute encephalitis, Rank 1) |
| TxGNN Score — Best Evidence | 95.99% (Lewy Body Dementia, Rank 6) |
| Evidence Level | L3 (Lewy Body Dementia) |
| EU Market Status | Not authorized as standalone product |
| Number of EU Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (Lewy Body Dementia) |

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Rasmussen subacute encephalitis | 98.43% | L5 | Hold |
| 2 | PLA2G6-associated neurodegeneration (PLAN) | 97.60% | L4 | Research Question |
| 3 | Transaldolase deficiency | 97.40% | L5 | Hold |
| 4 | Myelitis | 97.40% | L5 | Hold |
| 5 | Fructose-1,6-bisphosphatase deficiency | 97.09% | L5 | Hold |
| **6** | **Lewy body dementia** | **95.99%** | **L3** | **Proceed with Guardrails** |
| 7 | Paralysis agitans, juvenile, of Hunt | 95.60% | L5 | Research Question |
| 8 | PSP-corticobasal syndrome | 95.36% | L4 | Hold |
| 9 | X-linked intellectual disability-ataxia-apraxia (MCT8 deficiency) | 94.87% | L4 | Research Question |
| 10 | X-linked intellectual disability-cerebellar hypoplasia | 93.72% | L4 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for carbidopa in this evidence pack. Based on established pharmacology, carbidopa is a peripheral aromatic L-amino acid decarboxylase inhibitor that does not cross the blood-brain barrier. Co-administered with levodopa, it prevents peripheral conversion of levodopa to dopamine — increasing the fraction of levodopa that reaches the central nervous system while markedly reducing systemic dopaminergic side effects such as nausea and orthostatic hypotension.

Lewy Body Dementia (LBD) and Parkinson's disease share a core pathological substrate: α-synuclein accumulation (Lewy bodies) with progressive loss of dopaminergic neurons in the substantia nigra. Patients with LBD develop prominent parkinsonism as a defining clinical feature, making the pharmacological rationale for carbidopa/levodopa mechanistically identical to that in classical PD. Multiple clinical consensus documents — including the 2017 DLB Consortium Fourth Report — acknowledge levodopa/carbidopa as the preferred option for managing motor symptoms when treatment is clinically indicated in LBD.

The critical complication is that LBD patients carry significantly elevated risk of levodopa-induced hallucinations and are exquisitely sensitive to dopaminergic dose escalation. This is not a contraindication but a guardrail: dose titration in LBD must be far more conservative than in PD, and concurrent cholinergic therapy (rivastigmine) is typically prioritized for cognitive and neuropsychiatric symptoms. The TxGNN model's high score for LBD likely reflects the shared knowledge-graph features between PD and LBD dopaminergic pathology — in this case, the mechanistic connection is real and well-supported by clinical consensus.

---

## Focused Analysis: Lewy Body Dementia

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging in α-synucleinopathies (PD, MSA, DLB). Carbidopa is used as a **peripheral pretreatment to enhance imaging quality** by blocking peripheral decarboxylation of the radiotracer — this is a **diagnostic study**, not a therapeutic trial for LBD. |

> **Note:** No dedicated therapeutic clinical trials of carbidopa/levodopa specifically targeting LBD motor or cognitive endpoints were identified in the current evidence base.

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36402160](https://pubmed.ncbi.nlm.nih.gov/36402160/) | 2022 | Phase 3 RCT | The Lancet Neurology | Foslevodopa-foscarbidopa 24-h subcutaneous infusion vs. oral levodopa in **advanced PD**: significantly reduced "off" time. Provides the strongest available efficacy evidence for the carbidopa/levodopa mechanism — applicable by analogy to LBD parkinsonism. |
| [11581527](https://pubmed.ncbi.nlm.nih.gov/11581527/) | 2001 | Review | Current Treatment Options in Neurology | Comprehensive DLB treatment review: explicitly recommends levodopa/carbidopa to improve parkinsonism in DLB. Identifies it as standard of care for motor symptoms alongside cholinesterase inhibitors for cognition. |
| [14594099](https://pubmed.ncbi.nlm.nih.gov/14594099/) | 2003 | Review | Canadian Family Physician | DLB pharmacological management guide for family physicians: acknowledges levodopa benefit with explicit caveat on hallucination risk and the critical importance of avoiding conventional antipsychotics. |
| [37016564](https://pubmed.ncbi.nlm.nih.gov/37016564/) | 2023 | Review | American Journal of Case Reports | Emphasizes dopamine transporter (DAT-SPECT) evaluation as a biomarker supporting dopaminergic therapy decision-making in DLB; reinforces physiological basis for levodopa use. |
| [40585751](https://pubmed.ncbi.nlm.nih.gov/40585751/) | 2025 | Case Report | Cureus | Sublingual levodopa/carbidopa as a novel administration route in an LBD patient with dysphagia: demonstrates real-world route adaptation and ongoing clinical use of carbidopa in LBD. |
| [15040654](https://pubmed.ncbi.nlm.nih.gov/15040654/) | 2004 | Case Report | Pharmacotherapy | Dose-dependent resolution of apraxia of lid opening in a confirmed LBD+PD patient with carbidopa-levodopa: directly documents dose-response relationship in an LBD patient. |
| [11808350](https://pubmed.ncbi.nlm.nih.gov/11808350/) | 2001 | Case Report | Clinical Neurology | Probable DLB patient developed hallucinations within 2 days of levodopa/carbidopa 100 mg/day initiation, then improved on donepezil: illustrates both the therapeutic need and the hallucination risk unique to LBD. |
| [11790237](https://pubmed.ncbi.nlm.nih.gov/11790237/) | 2002 | Retrospective Cohort | Archives of Neurology | Neuropathological study of dementia in PD: documents waning levodopa response as concurrent Lewy body pathology spreads — directly informs expectations for LBD treatment durability. |
| [9748031](https://pubmed.ncbi.nlm.nih.gov/9748031/) | 1998 | Retrospective Cohort | Neurology | Early-onset dopaminergic hallucinations in PD patients: early hallucinations associated with underlying DLB pathology, reinforcing the need for lower starting doses and slower titration in patients with Lewy pathology. |
| [41031701](https://pubmed.ncbi.nlm.nih.gov/41031701/) | 2025 | Prospective Cohort | Pharmacotherapy | Pharmacodynamic characterization of levodopa's acute hypotensive effects in PD: clinically relevant to LBD management given LBD patients' pronounced autonomic dysfunction and orthostatic instability. |

---

## Notable Secondary Predictions

### PLA2G6-Associated Neurodegeneration (PLAN) — L4 · Research Question

PLAN is an NBIA subtype caused by PLA2G6 mutations; adult-onset disease presents with rapidly progressive dopaminergic parkinsonism, dystonia, and cognitive impairment. PMID 41769496 (2026, *Cureus*) directly describes a young adult male with PLA2G6-related parkinsonism — the parkinsonian phenotype logically supports carbidopa/levodopa as symptomatic therapy, by analogy to levodopa use in other genetic parkinsonisms (Parkin, DJ-1). No clinical trials exist. Three case-level publications. **Recommend formal case series and proof-of-concept documentation.**

### X-Linked Intellectual Disability-Ataxia-Apraxia Syndrome (MCT8 Deficiency / AHDS) — L4 · Research Question

This TxGNN prediction maps onto Allan-Herndon-Dudley Syndrome (AHDS), caused by SLC16A2 mutations impairing thyroid hormone entry into neurons. Insufficient intraneuronal T3 disrupts dopaminergic circuit development and function. PMID 41144879 (2026, *Movement Disorders*) directly reports altered dopamine metabolism and levodopa/carbidopa treatment response in MCT8-deficient patients; PMID 40088079 (2025, *Movement Disorders*) documents parkinsonism features in childhood AHDS responding to levodopa/carbidopa. **This is an emerging, mechanistically grounded area with active 2025-2026 research momentum — strongest secondary candidate.**

### PSP-Corticobasal Syndrome — L4 · Hold

PSP-CBS is a tauopathy with modest nigral dopaminergic involvement. Critically, simultaneous postsynaptic dopamine receptor degeneration means levodopa response rates are poor (<30% of patients achieve lasting benefit). NCT02994719 is an observational gait study, not a therapeutic trial. 2017 PSP diagnostic standards note levodopa trials are permissible but expectations should be managed as responses are typically transient. **Not recommended for active development without a validated patient selection biomarker.**

---

## EU Market Information

Carbidopa does not appear as a standalone authorized product in the EU regulatory database reviewed. In clinical practice, carbidopa is exclusively available as fixed-dose combinations with levodopa (co-careldopa), marketed under trade names such as Sinemet and generic equivalents. Standalone carbidopa is occasionally used in specific clinical settings (e.g., as a 5-hydroxy-tryptophan adjunct in research contexts), but no EU standalone authorization was identified for this review.

---

## Safety Considerations

Safety data specific to carbidopa alone is not available in this evidence pack. The following class-level considerations are directly relevant to the repurposing context:

- **Hallucination risk in LBD**: LBD patients are substantially more susceptible to levodopa/carbidopa-induced visual hallucinations than classical PD patients due to coexisting cholinergic deficit. Initiate at the lowest feasible dose and titrate slowly.
- **Antipsychotic contraindication**: Conventional antipsychotics (haloperidol, risperidone) are potentially fatal in DLB due to neuroleptic hypersensitivity. If hallucinations emerge, dose reduction or quetiapine (not haloperidol) is the appropriate response.
- **Orthostatic hypotension**: LBD-associated autonomic dysfunction amplifies carbidopa/levodopa-related blood pressure drops — monitor standing BP at each dose escalation.

For complete prescribing information, refer to the SmPC of the relevant carbidopa/levodopa combination product.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Lewy Body Dementia)*

**Rationale:**
Carbidopa/levodopa is already embedded in published DLB management guidelines for motor symptom control, supported by expert consensus, retrospective data, and directly relevant case reports. The mechanistic connection is strong (shared nigral dopaminergic pathology with PD). The L3 evidence level reflects the absence of a dedicated LBD-specific RCT — the current critical evidence gap — rather than any mechanistic uncertainty.

**To proceed, the following is needed:**

- Carbidopa standalone MOA documentation (DrugBank API retrieval — currently Data Gap)
- Safety review from the relevant carbidopa/levodopa SmPC (TFDA/EMA — currently Data Gap)
- Dedicated Phase 2 RCT in LBD: primary endpoints should include UPDRS-III motor score, hallucination rating (NPI hallucination subscale), and caregiver-reported quality of life
- Standardized hallucination monitoring and management protocol as a trial safeguard
- Subgroup analysis protocol to identify LBD patients most likely to benefit (e.g., by DAT-SPECT uptake level, baseline hallucination burden)
- Pharmacokinetic characterization of carbidopa/levodopa in elderly patients with concurrent cognitive impairment and autonomic dysfunction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

