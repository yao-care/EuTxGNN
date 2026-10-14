---
layout: default
title: Eravacycline
parent: AI Predictions (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Eravacycline
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

# Eravacycline: From Complicated Intra-abdominal Infections to Bronchitis

## One-Sentence Summary

Eravacycline is an intravenous fluorocycline (tetracycline-class) antibiotic, originally used to treat complicated intra-abdominal infections (cIAI).
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on model output and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated intra-abdominal infections (cIAI) in adults and adolescents aged 12 years or older weighing at least 50 kg |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 96.85% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general knowledge of the class, eravacycline is a broad-spectrum tetracycline-class antibiotic that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit. It is active against many Gram-positive and Gram-negative bacteria, including some multidrug-resistant strains. This could plausibly cover bacterial pathogens involved in bronchitis.

The link between the original and new indication is therefore only indirect. Both are bacterial-infection settings in which an antibacterial could act. However, acute bronchitis is mostly viral, and guidelines advise against antibiotics for it. The only plausible target would be bacterial exacerbations of chronic bronchitis, a use already covered by existing tetracyclines and other agents. The high TxGNN score probably reflects the antibacterial class association rather than eravacycline-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004237 (cancelled) | Xerava | Not specified | Xerava is indicated in adolescents from the age of 12 years weighing at least 50 kg, and in adults, for the treatment of complicated intra-abdominal infections (cIAI). Consideration should be given to official guidance on the ap... |

## Safety Considerations

- **Drug Interactions**: 24 interactions were recorded in total (20 are in the compiled detail list). The main ones by severity:
  - **Major**: Vitamin A, Lumacaftor, Isotretinoin, Acitretin, Tretinoin, Apalutamide, Bexarotene, Mitotane
  - **Moderate**: Picosulfuric acid, Warfarin, Dicoumarol, Methoxsalen, Ethinylestradiol, Mycophenolic acid, topical aminolevulinic acid, topical methyl aminolevulinate
  - **Minor**: Clarithromycin, Cobicistat, Ketoconazole, Ceritinib

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score and class-level reasoning. There are no trials or publications, acute bronchitis is mostly viral and not an antibiotic target, existing agents already cover bacterial exacerbations, and the EU authorization is cancelled.

**To proceed, the following is needed:**
- Eravacycline-specific preclinical or clinical data in respiratory infections, for example lung penetration and activity against respiratory pathogens
- Mechanism of action data from DrugBank
- Warnings and contraindications from the SmPC, for safety screening
- Clarification of why the EU authorization was cancelled and of the current regulatory status
- A defined target population, such as bacterial exacerbations of chronic bronchitis with resistant pathogens, and a comparison against existing therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

