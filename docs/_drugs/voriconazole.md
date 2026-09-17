---
layout: default
title: Voriconazole
parent: AI Predictions (L5)
nav_order: 653
evidence_level: L5
indication_count: 10
---

# Voriconazole
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

# Voriconazole: From Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a triazole antifungal agent used to treat invasive fungal infections (e.g., aspergillosis, candidiasis) by inhibiting fungal CYP450-dependent 14α-demethylase and blocking ergosterol synthesis. The TxGNN model's top-ranked prediction is **Multidrug-Resistant Tuberculosis (MDR-TB)**, but this pairing is currently supported by **0 clinical trials** and only **3 tangentially related publications**, none of which describe voriconazole as a treatment for tuberculosis itself. The evidence pack's own mechanistic analysis flags this prediction as a likely **false positive** driven by knowledge-graph co-occurrence noise rather than genuine pharmacological relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available regulatory data; drug class identified as triazole antifungal (invasive fungal infections) |
| Predicted New Indication | Multidrug-Resistant Tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed MOA data in the standard field is a data gap, but the evidence pack's rationale text identifies voriconazole as a **triazole antifungal** whose mechanism is inhibition of fungal 14α-demethylase and blockade of ergosterol synthesis. This mechanism has **no known antimycobacterial activity** — it does not act on any target relevant to *Mycobacterium tuberculosis*.

The literature retrieved for this pairing consistently describes patients with MDR-TB who **also** develop a fungal co-infection (aspergilloma, invasive aspergillosis) in TB-damaged lung cavities. In these cases, voriconazole is used to treat the **fungal co-infection**, not the tuberculosis itself. The TxGNN model appears to have picked up this frequent clinical co-occurrence in the literature as a spurious drug–disease association, rather than a genuine treatment relationship.

Consequently, this prediction should be interpreted as a **likely false positive**: the pharmacological mechanism does not support efficacy against MDR-TB, and no clinical trial or direct treatment evidence exists. A more mechanistically defensible reframing — supported by a lower-ranked signal in this same evidence pack (rank 8, "inactive tuberculosis," L4, decision stage S1, "Research Question") — is that voriconazole may have a legitimate secondary role in treating **chronic pulmonary aspergillosis arising in post-TB lung cavities**, which is a distinct clinical entity from tuberculosis itself and would require re-scoping the indication target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case Report | Cases Journal | MDR-TB coexisting with aspergilloma/invasive aspergillosis in a diabetic patient; voriconazole was used to treat the fungal co-infection, not the tuberculosis itself |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | Case Report/In-vitro | Braz J Microbiol | In-vitro study of photodynamic inactivation against multidrug-resistant *Fonsecaea nubica* (chromoblastomycosis); does not involve voriconazole or tuberculosis |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Basic Research | Virulence | Genetic diversity study of fluconazole-resistant *Candida krusei*; unrelated to *M. tuberculosis* or voriconazole treatment |

None of these publications provide direct evidence that voriconazole treats tuberculosis; all relate to fungal pathogens co-occurring with TB or unrelated to TB entirely.

---

## EU Market Information

This product currently holds no EU marketing authorization on record (market status: not marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between voriconazole (antifungal, ergosterol-synthesis inhibitor) and multidrug-resistant tuberculosis (a mycobacterial infection) is absent. All retrieved literature describes fungal co-infections occurring alongside TB rather than voriconazole treating TB directly, and no clinical trials exist for this pairing. This is assessed as a likely knowledge-graph false positive (evidence level L5).

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank
- If pursuing a related, more plausible signal: re-scope the candidate indication to "chronic pulmonary aspergillosis in post-TB cavitary lung disease" (supported by rank 8 evidence, L4) rather than tuberculosis itself, and gather targeted clinical evidence for that reframed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

