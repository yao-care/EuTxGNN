---
layout: default
title: Nitisinone
parent: AI Predictions (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitisinone: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Hereditary tyrosinemia type 1 (HT-1)…"
monitor_inn: "Nitisinone"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone was originally used to treat hereditary tyrosinemia type 1 (HT-1) and alkaptonuria (AKU).
The TxGNN model predicts it may be effective for **renal tubular acidosis**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary tyrosinemia type 1 (HT-1), in combination with dietary restriction of tyrosine and phenylalanine; alkaptonuria (AKU) in adults |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), an enzyme in the tyrosine breakdown pathway. Blocking it prevents the build-up of toxic downstream metabolites in HT-1. Detailed mechanism of action data is not available in the data compiled for this report, so this description relies on the drug's known pharmacology.

The link to renal tubular acidosis is indirect. Renal tubular dysfunction (Fanconi-type) is a recognized manifestation of HT-1, so treating HT-1 may relieve some kidney tubule problems. However, no direct evidence supports an effect in primary renal tubular acidosis. The very high TxGNN score is a computational prediction only and should not be read as proof of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for renal tubular acidosis.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000555 (cancelled) | Orfadin | Not specified | Hereditary tyrosinemia type 1 (HT 1) in adult and paediatric patients, in combination with dietary restriction of tyrosine and phenylalanine. Alkaptonuria (AKU) in adults... |
| EMEA/H/C/004582 (cancelled) | Nityr | Not specified | Adult and paediatric patients with confirmed hereditary tyrosinemia type 1 (HT-1), in combination with dietary restriction of tyrosine and phenylalanine. |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, thrombocytopenia, leukopenia, hypophosphatemia, tyrosinemia. These come from drug-disease contraindication edges in the TxGNN knowledge graph and need confirmation against the official product information. Kidney disease is directly relevant to the predicted indication.
- **Drug Interactions:** 100 interactions were found, and the 20 listed in the data are mostly Moderate (one is Minor). Examples include abiraterone, amiodarone, amlodipine, nifedipine, ibuprofen, pioglitazone, dexamethasone, atazanavir, aprepitant, apalutamide, baricitinib, bexarotene, bicalutamide, isotretinoin, aldesleukin, avatrombopag, amobarbital, abametapir (topical) and ginger. Armodafinil is the Minor one.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or literature, and the mechanistic link is only indirect, through the kidney tubule problems seen in HT-1. There are also no valid EU authorizations, and the label safety data could not be retrieved.

**To proceed, the following is needed:**
- Official product information (warnings and contraindications) from the EMA, which is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- A literature search specific to renal tubular acidosis or Fanconi-type tubulopathy, to see whether any supportive data exist
- Clarification of why both EU authorizations are cancelled (for example commercial withdrawal versus a safety reason)
- Review of the knowledge-graph flags for kidney disease, hypophosphatemia and blood cell counts (thrombocytopenia, leukopenia) before any study in a kidney population

**Other predictions in this analysis:** The remaining top-ranked predictions are galactosemia, serpinopathy with toxic serpin polymerization, C1 inhibitor deficiency, glycogen storage disease, adult polyglucosan body disease, glycogen storage disease due to glucose-6-phosphatase deficiency, Griscelli syndrome, X-linked chronic granulomatous disease and ermine phenotype. All were judged Hold. They have no trials, and the only supporting literature is general reviews of pediatric liver disease, with no mechanistic rationale linking HPPD inhibition to these conditions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

