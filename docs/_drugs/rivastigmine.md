---
layout: default
title: Rivastigmine
parent: Medium Evidence (L3-L4)
nav_order: 515
evidence_level: L4
indication_count: 10
---

# Rivastigmine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Rivastigmine: From Alzheimer's Disease to Glaucoma

## One-Sentence Summary

Rivastigmine is a selective acetylcholinesterase (AChE) inhibitor established for Alzheimer's disease dementia.
The TxGNN model predicts it may be effective for **Glaucoma**,
with **0 clinical trials** and **3 publications** currently supporting this direction — all preclinical/mechanistic in nature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease dementia (inferred from literature evidence in this pack; no EU/TFDA license record exists) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently a data gap. Based on the literature evidence collected in this pack, Rivastigmine is a selective carbamate-type acetylcholinesterase (AChE) inhibitor, with established efficacy in Alzheimer's disease dementia by increasing central acetylcholine levels to compensate for cholinergic deficit.

The link to glaucoma comes from a separate branch of AChE pharmacology: non-selective AChE inhibitors have long been known as ocular hypotensive agents, and cholinergic signaling via muscarinic receptors (M3R) in the trabecular meshwork directly regulates intraocular pressure (IOP) (PMID 39130374). A direct animal study (PMID 10673128) tested **topical rivastigmine** in rabbits and found it lowered IOP over an 8-hour observation period, despite rivastigmine's selectivity for a CNS-predominant AChE isoform.

Mechanistically, this suggests that even a CNS-selective AChE inhibitor can produce a local IOP-lowering effect when applied topically, without necessarily triggering the systemic cholinergic side effects associated with non-selective agents (PMID 27967267). This is a plausible but early-stage mechanistic hypothesis rather than a clinically validated pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical (animal study) | J Ocul Pharmacol Ther | Topical rivastigmine lowered intraocular pressure in normotensive rabbits, monitored hourly over 8 hours |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review | Front Mol Biosci | Reviews cholinergic/muscarinic (M3R) regulation of IOP via the trabecular meshwork; notes systemic cholinergic side effects limit current M3R agonists |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review (patent literature) | Expert Opin Ther Pat | Notes mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis, **and glaucoma** |

---

## EU Market Information

Rivastigmine currently has no EU marketing authorization record in this evidence pack (market status: **Not marketed / Not marketed**, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA warnings/contraindications and full DrugBank DDI data are currently unavailable — see Next Steps below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the glaucoma indication is limited to one 2000-era animal study and two narrative reviews (Evidence Level L4) — no clinical trials or RCTs exist. Combined with the drug's current non-marketed status in the EU and a **blocking** data gap on TFDA safety labeling, the candidate is not yet ready to advance to safety screening (S1).

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — **blocking gap (DG001)**; remediation: download PDF from TFDA official site and parse
- Confirmed MOA data — **high-priority gap (DG002)**; remediation: query DrugBank API
- Identification of any registered/planned clinical trials evaluating rivastigmine (topical or systemic) for IOP reduction or glaucoma
- Confirmation of current global marketing/regulatory status for rivastigmine formulations suitable for ocular use
- Preclinical-to-clinical translation data (topical dose, ocular tolerability, route feasibility)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

