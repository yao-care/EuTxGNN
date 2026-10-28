---
layout: default
title: Pregabalin
parent: AI Predictions (L5)
nav_order: 498
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: predicted new indication Tendinitis (evidence level L5). Approved use: Neuropathic painPregabalin Viatris Pharma is indicated for the treatm…"
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Pregabalin: Tendinitis
{: .text-alpha }

## One-Sentence Summary

Pregabalin was originally authorised in the EU for peripheral and central neuropathic pain, adjunctive treatment of partial seizures, and generalised anxiety disorder.
The TxGNN model predicts it may be effective for **tendinitis**, but there are **no registered clinical trials** and only **6 loosely related publications**, none of which tests pregabalin as a treatment for tendinitis.
Of the other top-ranked predictions, **osteoarthritis** (L1), **headache disorder** (L1) and **migraine disorder** (L2) have the strongest supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuropathic painPregabalin Viatris Pharma is indicated for the treatment of peripheral and central neuropathic pain in adults. Epilepsy&nbsp;Pregabalin Viatris Pharma is indicated as adjunctive therapy in adults with partial seizures with or without secondary generalisation. Generalised Anxiety Diso |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 (tendinitis); the higher-evidence alternatives are osteoarthritis and headache disorder (L1) |
| EU Market Status | Marketed (valid licences: 6 of 6) |
| Number of Authorizations | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pregabalin binds the alpha-2-delta subunit of voltage-gated calcium channels. This reduces central sensitisation and neuropathic pain signalling. Detailed mechanism of action data was not available in the data compiled for this report, so this description comes from the mechanistic rationale prepared for the predictions.

Tendinitis is mainly a local inflammatory or degenerative condition, so the link to pregabalin is indirect. Any benefit would apply only to a neuropathic pain component, not to the underlying tendon pathology. The retrieved literature does not change this: it covers peri-operative analgesia after rotator cuff repair, a nerve impingement case report, a fluoroquinolone-associated disability case, and an animal neuropathy study. None of it evaluates pregabalin as a treatment for tendinitis.

The TxGNN score is high, but the supporting evidence is weak. Predictions with better clinical support are summarised below.

### Other Top-Ranked Predictions

| Predicted Indication | TxGNN Score | Evidence Level | Summary |
|------|------|------|------|
| Migraine disorder | 0.9947 | L2 | Small paediatric RCTs against propranolol and valproate. The only Phase 3 trial was withdrawn. |
| Migraine with brainstem aura | 0.9943 | L5 | Preclinical evidence of inhibition of cortical spreading depression. |
| Inclusion body myositis | 0.9952 | L5 | Only an unrelated case report was retrieved. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for tendinitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin gave postoperative pain scores equivalent to interscalene block after arthroscopic rotator cuff repair (peri-operative pain, not tendinitis treatment) |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Analgesic and opioid-sparing effect of pregabalin after rotator cuff repair, with conflicting results in the literature |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Fluoroquinolone-associated disability after ciprofloxacin, including tendinopathy as a side effect (not a pregabalin study) |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement after a marathon, with hamstring tendonitis |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Commentary on piriformis syndrome diagnosis and treatment by sciatic neurolysis |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | A plant extract attenuated vincristine-induced neuropathy in rats (not related to pregabalin treatment of tendinitis) |

---

## EU Market Information

All six authorisations are valid; the drug is marketed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000546 | Lyrica | Not specified | Neuropathic pain, epilepsy (adjunctive, partial seizures), generalised anxiety disorder |
| EMEA/H/C/003880 | Pregabalin Viatris Pharma (previously Pregabalin Pfizer) | Not specified | Neuropathic pain, epilepsy (adjunctive), generalised anxiety disorder |
| EMEA/H/C/004024 | Pregabalin Accord | Not specified | Epilepsy (adjunctive, partial seizures), generalised anxiety disorder |
| EMEA/H/C/003900 | Pregabalin Zentiva | Not specified | Neuropathic pain, epilepsy (adjunctive), generalised anxiety disorder |
| EMEA/H/C/004010 | Pregabalin Sandoz | Not specified | Neuropathic pain, epilepsy (adjunctive), generalised anxiety disorder |

A sixth authorisation (EMEA/H/C/004078, Pregabalin Viatris, previously Pregabalin Mylan) is also cancelled, with the same three indications as above.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are drug-disease edges from the TxGNN knowledge graph, not label text, and need confirmation against the SmPC): anxiety disorder, neurotic disorder, dysthymic disorder, thrombocytopenia, angioedema (including hereditary and acquired forms), myopathy and other skeletal muscle diseases, rhabdomyolysis, familial periodic paralysis, nodular fasciitis, impaired renal function, and atrioventricular block.

**Drug Interactions** (100 interactions recorded; selected examples):
- **Major:** morphine, liposomal morphine (additive central nervous system and respiratory depression)
- **Moderate:** opioid-type and antidiarrhoeal agents (difenoxin, diphenoxylate, opium), cannabinoids (dronabinol, nabilone), metoclopramide, sibutramine, and thiazolidinediones (pioglitazone, rosiglitazone, troglitazone)

**Other signals from the literature:** sedation, sexual dysfunction, and potential for abuse and dependence.

Please refer to the SmPC for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The tendinitis prediction relies on a high model score with no clinical trials, and the mechanistic link is indirect and limited to a possible neuropathic pain component. The literature retrieved does not address tendinitis treatment.
- All six authorisations are valid, and the drug is marketed.

**To proceed, the following is needed:**
- Clinical studies of pregabalin specifically in tendinitis or tendinopathy pain, ideally in patients with a neuropathic or centrally sensitised component
- Confirmation of current EU marketing status, since the data show only cancelled authorisations
- Official SmPC warnings and contraindications, and detailed mechanism of action data
- A safety plan covering sedation, abuse potential, opioid co-prescription, and renal impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

