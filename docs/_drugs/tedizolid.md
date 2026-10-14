---
layout: default
title: Tedizolid
parent: AI Predictions (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
---

# Tedizolid
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

# Tedizolid: From Acute Bacterial Skin Infections to Orofacial Clefting Syndrome

## One-Sentence Summary

Tedizolid is an oxazolidinone antibacterial originally used to treat acute bacterial skin and skin structure infections (ABSSSI).
The TxGNN model predicts it may be effective for **orofacial clefting syndrome**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute bacterial skin and skin structure infections (ABSSSI) in adults, adolescents and children weighing at least 35 kg (tablets); ABSSSI from birth (infusion) |
| Predicted New Indication | Orofacial clefting syndrome |
| TxGNN Prediction Score | 93.94% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tedizolid is an oxazolidinone antibacterial. This class inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in ABSSSI caused by Gram-positive bacteria is established.

Orofacial clefting is a developmental, largely genetic malformation, not an infection. An antibiotic that acts on bacterial ribosomes has no known role in its development or treatment. The high TxGNN score appears to be an artifact of graph-based similarity to related malformation nodes, not a biologically supported link. **The prediction is not considered mechanistically credible.**

Other predicted indications for this drug were also reviewed. Most are congenital or genetic conditions, including interventricular septum aneurysm, Jeune syndrome with situs inversus, Pierre Robin syndrome variants, Laubry-Pezzi syndrome, and chromosomal deletion syndromes. They share the same problem of having no plausible mechanism. Bronchitis is the only prediction with indirect plausibility, since bacterial lower respiratory infection could in theory respond to an anti-Gram-positive agent. Even there, no trials or literature were found, most bronchitis is viral or self-limiting, and established agents already cover the relevant pathogens.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for orofacial clefting syndrome.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002846 (cancelled) | Sivextro | Tablets; powder for concentrate for infusion solution | Acute bacterial skin and skin structure infections (ABSSSI) in adults, adolescents and children weighing at least 35 kg (tablets); ABSSSI from birth (infusion)... |

## Safety Considerations

- **Drug Interactions**: 28 interactions were identified in total. The 20 listed in the data compiled for this report are all rated Moderate. They include picosulfuric acid, empagliflozin, rosuvastatin, sulfasalazine, eltrombopag, lusutrombopag, rivaroxaban, selexipag, artesunate, lumacaftor, afatinib, ethinylestradiol, alpelisib, binimetinib, cladribine, methotrexate, imatinib, lapatinib, mycophenolic acid and niraparib.

For warnings and contraindications, please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no credible mechanistic link. Tedizolid is an antibacterial, and orofacial clefting is a congenital malformation. The high TxGNN score is likely a graph-based artifact. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, and a biological rationale linking tedizolid to orofacial clefting
- Warnings and contraindications from the SmPC, which are required for safety screening
- Any preclinical or clinical evidence for this indication; none is currently available
- Reconsideration of the prediction priority, since a more plausible use of this drug is within its existing antibacterial scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

