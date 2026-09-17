---
layout: default
title: Fesoterodine
parent: AI Predictions (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Fesoterodine
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

# Fesoterodine: From Overactive Bladder to Polycystic Kidney Disease 3 with or without Polycystic Liver Disease

## One-Sentence Summary

Fesoterodine is a peripherally-selective M3 muscarinic receptor antagonist used for overactive bladder (OAB) and neurogenic detrusor overactivity. The TxGNN model predicts a possible link to **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease**, but this is currently supported by **0 drug-specific clinical trials** and **20 general disease-review publications**, none of which mention fesoterodine or antimuscarinic therapy — a pattern the underlying analysis itself flags as a likely TxGNN false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (OAB) / neurogenic detrusor overactivity (based on known drug classification; no formal EU/TW license text available — drug is not currently marketed in this dataset) |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 91.13% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fesoterodine is not available in this dataset. Based on known pharmacology, fesoterodine is a prodrug that is hydrolyzed to its active metabolite (5-hydroxymethyl tolterodine), a competitive M3 muscarinic receptor antagonist used to reduce involuntary detrusor contractions in OAB.

The theoretical rationale for a link to polycystic kidney/liver disease rests on the fact that M3 receptor and cAMP signaling pathways are involved in cystic epithelial fluid secretion, which is a recognized driver of cyst growth in ADPKD/PLD. This is a plausible but unproven mechanistic hypothesis.

Critically, none of the 20 retrieved publications discuss fesoterodine, antimuscarinic agents, or M3-receptor-targeted therapy in the context of polycystic kidney or liver disease — they are general clinical guidelines and genetics/pathophysiology reviews of PKD/PLD. Combined with the complete absence of registered clinical trials, this indication should be treated as a high-score, low-evidence TxGNN association rather than a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Review | Am J Gastroenterol | ACG guideline on diagnosis/management of focal liver lesions, including polycystic liver disease; no mention of fesoterodine or antimuscarinics |
| [40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/) | 2025 | Review | Biochem Pharmacol | Extracellular matrix/MMP dynamics as therapeutic targets in PKD/PLD cystogenesis; mechanistic review, no antimuscarinic link discussed |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum and ciliopathy-driven mechanism of PKD/PLD; genetics-focused, no drug data |
| [37208103](https://pubmed.ncbi.nlm.nih.gov/37208103/) | 2023 | Review | J Hepatol | Multi-organ (liver-kidney) transplantation considerations in polycystic liver-kidney disease |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Review | Adv Kidney Dis Health | Extrarenal (hepatic) manifestations and complications of ADPKD |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | ADPKD/PLD clinical course; notes tolvaptan use in ADPKD, no reference to fesoterodine |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Review | J Hepatol | EASL clinical practice guideline on management of cystic liver diseases; treatment guidance does not include fesoterodine |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | General overview of ADPKD pathophysiology and systemic manifestations |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic complexity of ADPKD/ADPLD across 8 causative genes; mechanistic/genetic review only |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Case Series | Ann Transplant | Retrospective outcomes of combined liver-kidney transplantation in 9 PLD/PKD patients |

---

## EU Market Information

No EU marketing authorizations are on file for Fesoterodine in this dataset — the drug is recorded as **not marketed** (Not marketed), with 0 registered licenses.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Polycystic Kidney Disease 3 with/without Polycystic Liver Disease) has no clinical trials and no drug-specific literature — all 20 retrieved publications are general PKD/PLD reviews that never mention fesoterodine or antimuscarinic mechanisms. This matches a known TxGNN failure mode (high similarity score, no corroborating evidence) rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Drug-specific preclinical or mechanistic data linking M3 antagonism to cyst fluid secretion in PKD/PLD before further investment
- Fesoterodine's confirmed mechanism of action (MOA) and formal EU/TW approved-indication text, both currently unavailable
- TFDA/SmPC warnings and contraindications for a baseline safety assessment (currently blocking, per data gap DG001)

**Note:** A lower-ranked prediction in the same evidence pack — *low compliance bladder* (rank 7, score 86.5%, evidence level L3) — is mechanistically coherent (fesoterodine's core M3-antagonist action directly addresses detrusor overactivity/bladder compliance) and is supported by human urodynamic and clinical literature. That candidate merits a separate, dedicated evaluation as it represents a substantially stronger repurposing opportunity than the top-ranked PKD/PLD prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

