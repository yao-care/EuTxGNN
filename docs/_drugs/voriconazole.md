---
layout: default
title: Voriconazole
parent: AI Predictions (L5)
nav_order: 677
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

# Voriconazole: From Invasive Fungal Infections to Multidrug-Resistant Tuberculosis

## One-Sentence Summary

Voriconazole is a broad-spectrum triazole antifungal, originally used to treat invasive aspergillosis and serious Candida, Scedosporium and Fusarium infections.
The TxGNN model predicts it may be effective for **multidrug-resistant tuberculosis**, but there are **0 clinical trials** and only **3 publications** (a case report and two unrelated microbiology studies), none showing that voriconazole treats tuberculosis itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive aspergillosis; candidaemia in non-neutropenic patients; fluconazole-resistant serious invasive Candida infections (including C. krusei); serious Scedosporium and Fusarium infections |
| Predicted New Indication | Multidrug-resistant tuberculosis |
| TxGNN Prediction Score | 98.67% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Voriconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks synthesis of ergosterol, an essential component of the fungal cell membrane.

*Mycobacterium tuberculosis* has several cytochrome P450 enzymes (CYP121, CYP125 and CYP51-like enzymes), and azoles bind some of them in vitro. This is the only conceivable mechanistic bridge to tuberculosis. It has not translated into clinically meaningful anti-mycobacterial activity, so no direct mechanistic link is established.

The high TxGNN score (98.67%) is a model prediction only. The retrieved literature describes aspergillosis occurring alongside MDR-TB. This reflects antifungal treatment of a comorbid fungal infection, not treatment of tuberculosis. The other top-ranked predictions are mostly unsupported: other tuberculosis variants (bovine, avian, inactive, ascites), cysticercosis, and rare congenital malformation or hair disorders. They look like knowledge-graph artifacts rather than real signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18992166](https://pubmed.ncbi.nlm.nih.gov/18992166/) | 2008 | Case report | Cases Journal | A diabetic woman with MDR-TB co-existing with aspergilloma and invasive aspergillosis; the antifungal relates to the fungal infection, not TB |
| [37145297](https://pubmed.ncbi.nlm.nih.gov/37145297/) | 2023 | In vitro study | Brazilian Journal of Microbiology | Photodynamic inactivation of multidrug-resistant *Fonsecaea nubica* (chromoblastomycosis); unrelated to tuberculosis |
| [39359062](https://pubmed.ncbi.nlm.nih.gov/39359062/) | 2024 | Microbiological study | Virulence | Biology and genetic diversity of *Candida krusei* isolates from fermented vegetables and clinical samples in China; unrelated to tuberculosis |

---

## EU Market Information

All three authorizations are cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002669 | Voriconazole Accord | Not specified | Invasive aspergillosis; candidaemia in non-neutropenic patients; fluconazole-resistant serious invasive Candida infecti... |
| EMEA/H/C/000387 | Vfend | Not specified | Invasive aspergillosis; candidaemia in non-neutropenic patients; fluconazole-resistant serious invasive Candida infecti... |
| EMEA/H/C/003737 | Voriconazole Hikma (previously Voriconazole Hospira) | Not specified | Invasive aspergillosis; candidaemia in non-neutropenic patients; fluconazole-resistant serious invasive Candida infecti... |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Examples of **Major** interactions: loperamide, triamcinolone, budesonide, chlorpropamide. Examples of **Moderate** interactions: famotidine, rabeprazole, omeprazole, hydrocortisone, dexamethasone, betamethasone, pioglitazone, alosetron, aprepitant, clarithromycin, bisacodyl. Minor interactions include amphotericin B and cimetidine.
- **Knowledge-graph contraindication signals** (from a drug-disease graph, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, impaired renal function, vision disorder, blindness, cardiomyopathy (including hypertrophic), endomyocardial fibrosis and myocardial disorder.

Official warnings and contraindications from the product information were not available for this report. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no literature showing activity against tuberculosis, and no plausible established mechanism. Voriconazole also has no currently valid EU authorization, and the graph flags several cardiac, hepatic and renal safety concerns.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and in vitro evidence of voriconazole activity against *M. tuberculosis*, including MDR strains
- Preclinical efficacy data (in vitro and animal models) before any clinical consideration
- Official safety information (warnings and contraindications) from the SmPC, with particular attention to QT prolongation, liver function and the drug interaction burden
- A review of whether any current EU marketing authorization or supply route exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

