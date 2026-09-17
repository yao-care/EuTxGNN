---
layout: default
title: Vibegron
parent: AI Predictions (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
---

# Vibegron
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

# Vibegron: From Overactive Bladder to Polycystic Kidney Disease 3

## One-Sentence Summary

Vibegron is a beta-3 adrenergic receptor agonist originally developed for overactive bladder (OAB), acting by relaxing the detrusor muscle.
The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)**,
but this candidate currently has **no clinical trials** and **20 literature hits, none of which are drug-specific** — and the underlying pharmacology appears to point in the opposite therapeutic direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive Bladder (OAB) — inferred from known pharmacology; not confirmed via EU regulatory data, as the drug is not currently authorized in the EU |
| Predicted New Indication | Polycystic Kidney Disease 3 with or without Polycystic Liver Disease |
| TxGNN Prediction Score | 94.50% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vibegron is a beta-3 adrenergic receptor agonist. It couples to the Gs protein and increases intracellular cAMP, which relaxes detrusor smooth muscle — the basis for its use in OAB.

Autosomal dominant polycystic kidney disease (ADPKD, the disease family that includes PKD3) is driven mechanistically by *excessive* cAMP signaling in renal tubular epithelial cells, which promotes epithelial proliferation and fluid secretion into cysts. This is precisely why vasopressin V2-receptor antagonists such as tolvaptan — which *lower* intracellular cAMP — are the established disease-modifying treatment for ADPKD.

Because vibegron raises cAMP rather than lowering it, its mechanism of action points in the **opposite direction** from what is therapeutically needed in polycystic kidney/liver disease, and there is no positive mechanistic rationale supporting repurposing. The high TxGNN score most likely reflects topological proximity between vibegron and kidney/bladder-related nodes in the knowledge graph, rather than a genuine pharmacological relationship. None of the 20 retrieved publications mention vibegron or beta-3 agonists — they are background clinical/pathophysiology reviews of ADPKD and polycystic liver disease, indicating that the literature co-occurrence is disease-context noise rather than drug-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All retrieved publications concern the pathophysiology, genetics, and clinical management of polycystic kidney/liver disease; **none reference vibegron or beta-3 adrenergic agonists directly**. They are listed below for background context only and do not constitute drug-specific evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Review | Am J Gastroenterol | ACG clinical guideline on focal liver lesions, including polycystic liver disease management |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of ADPKD as a systemic disorder with renal and extrarenal manifestations |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Discusses tolvaptan (V2 antagonist, lowers cAMP) as ADPKD treatment; no mention of beta-3 agonists |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap between ADPKD and autosomal dominant polycystic liver disease |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of PKD1/PKD2 mutations and resulting phenotypes |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL clinical practice guidelines on cystic liver disease management |
| [34034501](https://pubmed.ncbi.nlm.nih.gov/34034501/) | 2022 | Review | Rev Esp Enferm Dig | Diagnosis and management of hepatic hydatid cyst (unrelated etiology) |
| [37208103](https://pubmed.ncbi.nlm.nih.gov/37208103/) | 2023 | Review | J Hepatol | Multi-organ (liver-kidney) transplantation considerations in polycystic disease |
| [40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/) | 2025 | Review | Biochem Pharmacol | Extracellular matrix dynamics as a therapeutic target in PKD/PLD |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Rev Med Suisse | General overview of polycystic liver disease subtypes |

---

## EU Market Information

Vibegron currently holds **no marketing authorization in the European Union** (0 licenses on record; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information. No verified warnings, contraindications, or drug–drug interaction data were available for this evaluation (TFDA label data and DrugBank MOA data are flagged as blocking/high-severity data gaps in the source Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (PKD3/polycystic liver disease) has no supporting clinical trials and no drug-specific literature. More importantly, the drug's known mechanism — increasing intracellular cAMP via beta-3 agonism — runs counter to the established disease biology, where *reducing* cAMP (e.g., via tolvaptan) is the therapeutic strategy. The high TxGNN score is best interpreted as a graph-topology artifact rather than a genuine repurposing signal, and the same caveat applies to the other nine ranked candidates in this Evidence Pack, all of which are L5 with zero clinical or drug-specific literature support.

**To proceed, the following is needed:**
- Confirmed DrugBank/SmPC mechanism-of-action data for vibegron (currently a data gap)
- TFDA/EMA label warnings and contraindications (currently a blocking data gap)
- In-vitro or preclinical data on vibegron's effect on cAMP signaling and cyst growth in renal tubular epithelium, to formally test (and likely refute) the mechanistic hypothesis before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

