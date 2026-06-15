---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Buprenorphine: From Opioid Use Disorder to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist and κ-opioid receptor antagonist used globally for treating opioid use disorder and moderate-to-severe pain, though it is not currently registered in Taiwan.
The TxGNN model predicts it may have relevance for **Acute Intermittent Porphyria (AIP)** as the top-ranked new indication (score: 99.41%),
with **0 clinical trials** and **1 case report** currently supporting this direction — the connection reflects a safety-profile association rather than a disease-modifying therapeutic claim.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid Use Disorder / Pain Management (globally established; not registered in Taiwan) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack (Data Gap: DG002). Based on well-established global pharmacology, Buprenorphine is a partial agonist at the μ-opioid receptor (MOR), an antagonist at the κ-opioid receptor (KOR) and δ-opioid receptor, and a partial agonist at the nociceptin/orphanin FQ peptide receptor (NOP/ORL1). This unique receptor profile underpins its dual therapeutic role in opioid dependence management and analgesia.

The mechanistic rationale for the AIP prediction is safety-based rather than therapeutic. Buprenorphine exhibits low CYP1A2 and CYP2C9 induction activity, meaning it theoretically does not promote the accumulation of δ-aminolevulinic acid (δ-ALA) or other porphyrin precursors responsible for triggering acute porphyric crises. This places Buprenorphine among the preferred opioid analgesics for pain management in AIP patients who require perioperative or chronic pain control — a "porphyria-safe" classification recognized in anesthetic and metabolic disease guidelines.

It is important to distinguish this safety association from a disease-modifying treatment claim. The sole supporting publication (PMID 8301837, 1993) describes anesthetic management of an AIP patient using Buprenorphine during oncological surgery — it documents safe use in an AIP patient, not the use of Buprenorphine to treat AIP itself. The TxGNN knowledge graph appears to have captured this safety-adjacency relationship, but direct therapeutic repurposing of Buprenorphine for AIP as a primary indication has no current clinical or mechanistic basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui (Japanese Journal of Anesthesiology) | Perioperative anesthetic management of a 40-year-old female AIP patient undergoing ovarian tumor surgery; Buprenorphine was selected for its low porphyrinogenic risk. Describes safe use in an AIP patient, not treatment of AIP. |

---

## Taiwan Market Authorization

No Taiwan (TFDA) regulatory licenses on record. Buprenorphine is not currently registered in Taiwan (market_status: 未上市).

---

## Safety Considerations

Please refer to the relevant SmPC or prescribing information for safety data.

> **Important note:** Taiwan-specific package insert (仿單) warnings and contraindications were not retrievable during this review (Data Gap: DG001 — severity: Blocking). This gap prevents formal S1 safety screening. Any clinical evaluation must be preceded by retrieval and review of the TFDA 仿單 or applicable regulatory safety documents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Acute Intermittent Porphyria appears to capture Buprenorphine's known *porphyria-safe* profile — its low CYP induction activity makes it a preferred opioid option for AIP patients requiring analgesia — rather than identifying a genuine disease-modifying therapeutic opportunity. With zero clinical trials and only a single 1993 case report documenting perioperative safety rather than AIP treatment, the evidence base cannot support progression to clinical investigation for this indication.

**To proceed, the following is needed:**

- **Hypothesis clarification first:** Define the research question — is the goal to evaluate Buprenorphine as a *safe analgesic within AIP* (already reasonable and supported by existing safety literature), or as a *disease-modifying agent targeting heme biosynthesis or porphyrin pathway*?
  - If the former: A structured safety-in-AIP literature review would suffice; no new trials are indicated
  - If the latter: Mechanistic studies establishing how opioid receptor modulation interacts with the heme biosynthesis pathway are needed before any clinical work — this hypothesis currently has no published basis
- **DG001 remediation:** Retrieve and review the TFDA 仿單 PDF for warnings, contraindications, and drug interactions (currently a blocking data gap)
- **DG002 remediation:** Query DrugBank API to confirm full MOA, receptor binding profile, and CYP interaction data

---

> **Reviewer note — Highest-evidence repurposing candidate in this pack:**
> Among all 10 TxGNN-predicted indications evaluated, **Schizophrenia (rank 8, L2)** carries the strongest evidence base: 4 clinical trials including an actively recruiting Phase 2 RCT ([NCT05778591](https://clinicaltrials.gov/study/NCT05778591), n=40, 2024–2026) directly testing low-dose Buprenorphine for schizophrenia negative symptoms (social motivation), plus 20 publications including a 1987 open-label clinical trial (PMID [3310672](https://pubmed.ncbi.nlm.nih.gov/3310672/)) and a 2020 meta-analysis of opioid antagonists in schizophrenia (PMID [32516800](https://pubmed.ncbi.nlm.nih.gov/32516800/)). If the objective is to identify the most actionable repurposing opportunity from this Evidence Pack, Schizophrenia should be elevated for priority review with a recommended decision of **Research Question / Proceed with Guardrails**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

