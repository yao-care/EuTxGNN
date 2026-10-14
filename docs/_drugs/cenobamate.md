---
layout: default
title: Cenobamate
parent: AI Predictions (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Cenobamate
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

# Cenobamate: From Focal-Onset Seizures to Guanidinoacetate Methyltransferase Deficiency

## One-Sentence Summary

Cenobamate is an antiseizure medication originally used as add-on treatment for focal-onset seizures in adults with epilepsy who are not controlled by other drugs.
The TxGNN model's top-ranked prediction is **guanidinoacetate methyltransferase (GAMT) deficiency**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** retrieved for it.
The best-supported direction among the predictions is **status epilepticus** (rank 2), with **1 early-phase clinical trial** and several case series and a systematic review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunctive treatment of focal-onset seizures with or without secondary generalisation in adult patients with epilepsy not adequately controlled despite at least 2 antiepileptic medicinal products |
| Predicted New Indication | Guanidinoacetate methyltransferase deficiency (rank 1); status epilepticus (rank 2) is the best-supported alternative |
| TxGNN Prediction Score | 97.83% (rank 1); 97.48% (status epilepticus) |
| Evidence Level | L5 (rank 1); L4 (status epilepticus) |
| EU Market Status | Cancelled only (the EU authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold (rank 1); status epilepticus is better framed as a research question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The published literature in the retrieved set describes cenobamate as having a dual action: enhancing the inactivated state of voltage-gated sodium channels (blocking the persistent sodium current) and positively modulating GABA-A receptors at a non-benzodiazepine site.

For the top prediction, GAMT deficiency is a creatine synthesis disorder in which epilepsy is a major feature. Seizure control is therefore plausibly relevant, but no direct mechanistic or clinical support for cenobamate was found. This is a model prediction only.

For status epilepticus, the dual mechanism is plausibly relevant to terminating prolonged seizures. Clinical evidence is limited to case series, a systematic review of those reports, and an early-phase trial that has not started recruiting. Safety in acute, high-dose ICU settings is still being characterised.

Other predictions (visual epilepsy, startle epilepsy, eating seizures, orgasm-induced seizures, micturition-induced seizures) are focal or reflex seizure types, so the rationale is indirect and class-level. Beta-ketothiolase deficiency has no evident mechanistic link.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (GAMT deficiency). For status epilepticus, the only trial is:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06352723](https://clinicaltrials.gov/study/NCT06352723) | Early Phase 1 | Not yet recruiting | 10 | Cenobamate in ICU patients with acute frequent seizures and status epilepticus (multi-center, planned start 2026-06). No results yet. |

## Literature Evidence

No literature was retrieved for GAMT deficiency. The most relevant publications for status epilepticus (rank 2) are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42438398](https://pubmed.ncbi.nlm.nih.gov/42438398/) | 2026 | Systematic Review | Can J Neurol Sci | Systematic review of cenobamate in status epilepticus |
| [42400400](https://pubmed.ncbi.nlm.nih.gov/42400400/) | 2026 | Case Series | Epileptic Disord | Three cases of super-refractory status epilepticus; evidence described as limited |
| [37064924](https://pubmed.ncbi.nlm.nih.gov/37064924/) | 2023 | Case Series | Neurohospitalist | Two super-refractory status epilepticus cases where cenobamate was added safely with slow up-titration to reduce hypersensitivity risk |
| [39060539](https://pubmed.ncbi.nlm.nih.gov/39060539/) | 2025 | Review/Commentary | Neurol Sci | Early considerations on the safety of cenobamate in status epilepticus |
| [40292823](https://pubmed.ncbi.nlm.nih.gov/40292823/) | 2025 | Retrospective cohort | Epilepsia | No effectiveness and seizure worsening in six children with Dravet syndrome (negative result, a different condition) |
| [39388362](https://pubmed.ncbi.nlm.nih.gov/39388362/) | 2024 | Case series | Epilepsia Open | Add-on cenobamate in refractory epilepsy due to Rasmussen's encephalitis |

For general focal epilepsy (indirect support for visual epilepsy and other focal or reflex seizure types), the key RCTs are [31734103](https://pubmed.ncbi.nlm.nih.gov/31734103/) (Lancet Neurol, 2020, dose-response RCT) and [32409485](https://pubmed.ncbi.nlm.nih.gov/32409485/) (Neurology, 2020, randomized Phase 2), plus the Cochrane review [39087564](https://pubmed.ncbi.nlm.nih.gov/39087564/) (2024). None of these studied the predicted rare conditions specifically.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005377 | Ontozry | Not specified | Adjunctive treatment of focal-onset seizures with or without secondary generalisation in adult patients with epilepsy who have not been adequately controlled despite a history of treatment with at least 2 anti-epileptic medicinal products. (status: cancelled) |

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 interactions in total. The entries listed, all rated Moderate, include hydrocortisone, bupropion, aprepitant, triamcinolone, morphine, omeprazole, dexamethasone, chlorpropamide, cisapride, clarithromycin, dronabinol, eliglustat, esomeprazole, granisetron, linagliptin and metoclopramide.

Literature notes that cenobamate inhibits CYP2C19, which affects concomitant phenytoin and phenobarbital and requires dose adjustment of other antiseizure medications. Drug reaction with eosinophilia and systemic symptoms (DRESS) occurred during development, so slow up-titration is used. These points come from published articles, not from the label.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked indication, GAMT deficiency)

**Rationale:**
- GAMT deficiency has a high model score but no trials or literature, so it is an L5 prediction only.
- Status epilepticus (L4) is the most credible direction, but evidence is limited to case series, a systematic review of them, and an unstarted 10-patient early-phase trial. It is best treated as a research question rather than a Go.
- The EU authorization is cancelled, which complicates any near-term regulatory path.

**To proceed, the following is needed:**
- The mechanism of action data and the SmPC warnings and contraindications (currently missing).
- Results from NCT06352723 or similar prospective data in status epilepticus, including acute-setting safety.
- For GAMT deficiency, preclinical or case-level evidence of benefit in creatine synthesis disorders.
- Clarification of the cancelled EU authorization status and available routes of administration for acute use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

