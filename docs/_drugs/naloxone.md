---
layout: default
title: Naloxone
parent: AI Predictions (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Naloxone: predicted new indication Continuous spikes and waves during sleep (evidence level L5). Approved use: Emergency therapy for known or suspected opioid overdose with respira…"
monitor_inn: "Naloxone"
predicted_indications: ["continuous spikes and waves during sleep", "lissencephaly with cerebellar hypoplasia", "progressive encephalopathy with leukodystrophy due to DECR deficiency", "schizophreniform disorder", "nasal cavity disease", "psychotic disorder", "hypoglycemia", "acute pulmonary heart disease", "drug-induced dyskinesia", "acute laryngopharyngitis"]
---

# Naloxone
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

# Naloxone: From Opioid Overdose to Continuous Spikes and Waves During Sleep

## One-Sentence Summary

Naloxone is an opioid antagonist, originally used as emergency therapy for opioid overdose and, in combination products, for opioid dependence.
The TxGNN model predicts it may be effective for **continuous spikes and waves during sleep**, but **no clinical trials and no publications** currently support this specific prediction.
A more evidence-backed alternative among the model's predictions is **hypoglycemia (specifically hypoglycemia-associated autonomic failure)**, with **3 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Emergency therapy for known or suspected opioid overdose with respiratory and/or central nervous system depression (Nyxoid) |
| Predicted New Indication | Continuous spikes and waves during sleep |
| TxGNN Prediction Score | 88.17% |
| Evidence Level | L5 |
| EU Market Status | ✗ Cancelled only (all authorizations cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, naloxone is a competitive opioid receptor antagonist. Its efficacy in reversing opioid-induced respiratory and central nervous system depression is established, and in combination products it is used to deter intravenous misuse in opioid dependence treatment.

For continuous spikes and waves during sleep (an epileptic encephalopathy), no trials or literature were found. Any link through opioid-receptor modulation of cortical excitability is speculative. The score of 0.88 is a model prediction only. Note also that the knowledge graph lists epilepsy among naloxone's contraindicated conditions, which argues for caution.

**Other predictions ranked by the model (for context):**
- **Hypoglycemia (L2, most supported):** Opioid receptor blockade may blunt the counter-regulatory failure seen in hypoglycemia-associated autonomic failure (HAAF). Three small, terminated trials and recent 2025 publications on intranasal naloxone support this line of inquiry. It is better framed as prevention or attenuation of HAAF in diabetes than as treatment of hypoglycemia itself.
- **Drug-induced dyskinesia (L3):** Naloxone reduced levodopa-induced dyskinesia in primate models, but old, small human studies in tardive dyskinesia were inconclusive.
- **Schizophreniform disorder and psychotic disorder (L3):** 1980s studies were small and inconsistent, with largely negative results.
- **Lissencephaly with cerebellar hypoplasia, DECR deficiency encephalopathy, acute laryngopharyngitis (L5):** No evidence and no plausible mechanism.
- **Nasal cavity disease and acute pulmonary heart disease (L4):** The evidence reflects delivery route or rescue use, not therapeutic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for continuous spikes and waves during sleep.

For reference, trials registered for the best-supported alternative prediction (hypoglycemia):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678145](https://clinicaltrials.gov/study/NCT00678145) | Phase 2 | Terminated | 39 | Mechanisms of hypoglycemia-associated autonomic failure in type 1 diabetes |
| [NCT03608163](https://clinicaltrials.gov/study/NCT03608163) | Phase 4 | Terminated | 4 | Naloxone and diazoxide to prevent HAAF in healthy subjects |
| [NCT02700048](https://clinicaltrials.gov/study/NCT02700048) | Phase 1/2 | Terminated | 11 | Intranasal naloxone vs saline for impaired awareness of hypoglycemia |

---

## Literature Evidence

Currently no related literature available for continuous spikes and waves during sleep.

For reference, key publications for the alternative prediction (hypoglycemia):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39026458](https://pubmed.ncbi.nlm.nih.gov/39026458/) | 2025 | Clinical study | J Clin Endocrinol Metab | Intranasal naloxone effects on HAAF in susceptible individuals |
| [39331519](https://pubmed.ncbi.nlm.nih.gov/39331519/) | 2025 | Commentary/Review | J Clin Endocrinol Metab | Discusses whether intranasal naloxone can prevent HAAF |
| [20811039](https://pubmed.ncbi.nlm.nih.gov/20811039/) | 2011 | Preclinical | Diabetes | Naloxone preserved responses to hypoglycemia after antecedent hypoglycemia |
| [37106491](https://pubmed.ncbi.nlm.nih.gov/37106491/) | 2023 | Case report | Adv Emerg Nurs J | Possible opioid-induced hypoglycemia and a potential role for naloxone |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004325 | Nyxoid | Not specified | Emergency therapy for known or suspected opioid overdose manifested by respiratory and/or CNS depression... |
| EMEA/H/C/004407 | Zubsolv | Not specified | Substitution treatment for opioid drug dependence, within a framework of medical, social and psychological treatment... |
| EMEA/H/C/000697 | Suboxone | Not specified | Substitution treatment for opioid-drug dependence, within a framework of medical, social and psychological treatment... |

All three authorizations are currently cancelled.

---

## Safety Considerations

- **Contraindication signals (knowledge-graph based, not label text):** The TxGNN knowledge graph links naloxone to a number of conditions, including epilepsy, long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, chronic obstructive pulmonary disease, respiratory failure, kidney disease, liver disease (including chronic hepatitis B and C), adrenal insufficiency, hypothyroidism, inflammatory bowel disease and benign prostatic hyperplasia. These are model-derived associations and need verification against the label.
- **Drug Interactions:** 88 interactions were identified. The only **Major** interaction among those listed is **droperidol**. Many **Moderate** interactions involve other opioids (fentanyl, morphine, oxycodone, methadone, codeine, tramadol, hydrocodone, remifentanil, sufentanil, butorphanol) and peripherally acting opioid antagonists (methylnaltrexone, naldemedine, naloxegol), as well as binimetinib. Hydrocortisone is a Minor interaction.

Please also refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, continuous spikes and waves during sleep, rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. All EU authorizations are cancelled, and epilepsy appears among the knowledge-graph contraindication signals.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic rationale linking opioid antagonism to this epileptic encephalopathy
- Preclinical or clinical evidence specific to the predicted indication
- EU label warnings and contraindications (the package insert data are currently missing, a blocking gap for safety screening)
- Consideration of redirecting evaluation to the better-supported **HAAF / impaired awareness of hypoglycemia** indication (intranasal naloxone), where the three small trials were terminated and larger, adequately powered studies would be needed
- Clarification of the route and formulation, and of how the cancelled EU market status affects development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

