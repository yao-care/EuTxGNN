---
layout: default
title: Pantoprazole
parent: High Evidence (L1-L2)
nav_order: 450
evidence_level: L1
indication_count: 10
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Pantoprazole: From Acid-Related GI Disorders to Active Peptic Ulcer Disease

## One-Sentence Summary

> Pantoprazole is a proton pump inhibitor (PPI) widely used to suppress gastric acid secretion in acid-related gastrointestinal disorders.
> The TxGNN model's top-ranked prediction is **Active Peptic Ulcer Disease**, with **3 clinical trials** and **19 publications** currently supporting this direction.
> **Important caveat**: the evidence pack's own rationale flags that this "new" indication substantially overlaps with pantoprazole's already-established, textbook use as a PPI — the empty `original_indications` field appears to be a data gap rather than evidence that this is a genuinely novel repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no EU authorization record on file (see EU Market Information below) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (per this evidence pack) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) field is not available for this drug. Based on the literature evidence collected in this pack, pantoprazole is a substituted benzimidazole that irreversibly and selectively inhibits the gastric parietal cell H⁺/K⁺-ATPase (the "proton pump"), the final common step of gastric acid secretion. It accumulates preferentially in the acidic canalicular space of the parietal cell and must be acid-activated before binding covalently to the pump (PMID 8930575, 9017763).

This mechanism is directly and classically applicable to active peptic ulcer disease: acid suppression is the cornerstone of ulcer healing, both as monotherapy and combined with *H. pylori* eradication regimens (amoxicillin/clarithromycin-based triple therapy). Multiple completed Phase 3 RCTs in this evidence pack (e.g., NCT02084420) directly test pantoprazole-based triple therapy for gastric/duodenal ulcer with *H. pylori* infection.

**Caveat on novelty**: the evidence pack's own repurposing rationale for this candidate states that active peptic ulcer disease "belongs to PPI's core original indication rather than a novel repurposing," and that the empty `original_indications` field should be treated as a data gap, not as evidence of a new discovery. The same pattern applies to several lower-ranked candidates in this pack (duodenal ulcer, gastric ulcer, peptic ulcer perforation) — these are all established PPI use cases. Genuinely exploratory candidates in this pack (e.g., duodenogastric reflux, duodenal obstruction, mastocytosis-related indications) carry much weaker evidence (L3–L5) and are flagged "Hold" or "Research Question."

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | RCT comparing Ilaprazole vs. pantoprazole triple therapy for 7-day *H. pylori* eradication in gastric/duodenal ulcer patients |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated PPI effect on clopidogrel antiplatelet activity in PCI patients (ulcer-history population); indirect relevance |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor healing/rebleeding in peptic ulcer hemorrhage after high-dose PPI infusion |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective RCT: intermittent vs. continuous pantoprazole infusion in peptic ulcer bleeding |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazole + amoxicillin + azithromycin/clarithromycin for *H. pylori* eradication in duodenal ulcer |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Comparison of three pantoprazole-based triple therapies for *H. pylori* eradication and gastric ulcer healing |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | Randomized trial: amoxicillin/clarithromycin plus sucralfate or pantoprazole for *H. pylori* eradication in duodenal ulcer |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review | Am J Gastroenterol | Network meta-analysis: P-CAB vs. PPI efficacy/safety for Grade C/D esophagitis |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole pharmacology; no identified drug-drug interactions in numerous interaction studies |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Mechanism Study | Eur J Gastroenterol Hepatol | Describes pantoprazole's acid-activation and precise H⁺/K⁺-ATPase inhibition profile |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative Study | Hepato-gastroenterology | Compares lansoprazole vs. pantoprazole in active duodenal ulcer treatment and *H. pylori* eradication |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Clinical Study | Medical Archives | Efficacy of PPI after endoscopic hemostasis in bleeding peptic ulcer, role of *H. pylori* |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | Reviews PPI mechanism and superiority over H2RAs in controlling acid secretion for acid-related disease |

---

## EU Market Information

No EU marketing authorization data is available in this evidence pack — `taiwan_regulatory.licenses` is empty and `market_status` is recorded as "Not Marketed" with 0 total authorizations. This should be verified directly against the EMA/national registries before any decision is finalized, as pantoprazole is a long-established PPI internationally.

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, supported by multiple completed RCTs (including Phase 3) directly testing pantoprazole in peptic ulcer disease. However, this predicted "new" indication is very likely an established PPI use rather than a true repurposing discovery — the drug's `original_indications` field is empty, which is flagged in the evidence pack itself as a probable data gap. This significantly limits confidence in framing this as a novel repurposing opportunity, and blocks a full safety assessment.

**To proceed, the following is needed:**
- Confirm pantoprazole's actual approved indications (DG001/DG002 remediation: retrieve TFDA/EMA label and DrugBank MOA data) to determine whether "active peptic ulcer disease" is already an on-label use
- Resolve safety data gaps: SmPC-derived key warnings, contraindications, and full DDI profile
- Verify true EU marketing/authorization status, since the current record (0 licenses, "Not Marketed") appears inconsistent with pantoprazole's known global availability and should be re-checked against source data
- If confirmed as an already-approved indication, reclassify this candidate outside the repurposing pipeline; if genuinely novel (e.g., a specific ulcer subtype or population not currently labeled), define that population precisely before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

