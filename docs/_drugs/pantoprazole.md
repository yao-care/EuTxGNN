---
layout: default
title: Pantoprazole
parent: High Evidence (L1-L2)
nav_order: 465
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Pantoprazole: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Short-term treatment of reflux symptoms (e.g. heartburn…"
monitor_inn: "Pantoprazole"
predicted_indications: ["duodenal obstruction", "acne (disease)", "Smouldering systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pantoprazole: From Reflux Symptoms to Active Peptic Ulcer Disease
{: .text-alpha }

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor originally authorized in the EU for short-term treatment of reflux symptoms (heartburn, acid regurgitation) in adults.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, with **1 clinical trial** and **20 publications** currently supporting this direction.
This is effectively an on-label class use of the drug rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Short-term treatment of reflux symptoms (e.g. heartburn, acid regurgitation) in adults |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (all licences cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pantoprazole irreversibly inhibits the gastric H+/K+ ATPase (the proton pump) in parietal cells. This suppresses acid secretion, which allows ulcers to heal. Detailed mechanism of action data was not available in the structured drug record, but this mechanism is well described in the literature compiled for this report.

Reflux symptoms and peptic ulcer are both driven by excess gastric acid exposure. The original indication (reflux symptoms) and the predicted indication (active peptic ulcer disease) therefore share the same therapeutic target. Reducing acid load is the common mechanism, so the prediction extends the drug's existing acid-related use rather than introducing a new biological concept.

Other top-ranked predictions such as duodenal ulcer and gastric ulcer follow the same logic and are also well supported. Predictions such as acne, duodenal obstruction and the mastocytosis entities have no plausible mechanistic link and look like model artifacts (see Conclusion).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial of ilaprazole vs pantoprazole triple therapy (7 days) for H. pylori eradication in gastric/duodenal ulcer patients. The comparator and endpoint details should be verified. |

The related disease entities duodenal ulcer and gastric ulcer have additional pantoprazole trials (for example NCT00843063, a Phase 4 trial of famotidine vs pantoprazole in preventing recurrent aspirin-induced ulcer, n=161), which add indirect support.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review / network meta-analysis | Am J Gastroenterol | P-CAB vs PPI for healing grade C/D esophagitis (indirect to ulcer) |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | Multicenter RCT (tegoprazan, not pantoprazole) | Gut Liver | Tegoprazan for endoscopic resection-induced artificial ulcers (indirect) |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole binds irreversibly to the proton pump; no drug interactions identified in numerous studies |
| [10450061](https://pubmed.ncbi.nlm.nih.gov/10450061/) | 1999 | Review | Pharmacology | Relative efficacy of PPIs; similar dose-response relationships at equal milligram doses |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Review | Int J Clin Pharmacol Ther | Impact of CYP2C19 polymorphism on PPI action |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Comparative study | Am J Gastroenterol | Pantoprazole vs ranitidine in duodenal ulcer, Brazilian multicenter study |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative study | Hepatogastroenterology | Lansoprazole vs pantoprazole in active duodenal ulcer and H. pylori eradication |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Pharmacology review | Eur J Gastroenterol Hepatol | Pantoprazole is acid-activated in the parietal cell and has a predictable activity profile |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (rat) | Inflammopharmacology | Pantoprazole plus mesenchymal stem cells in experimental gastric ulcer |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Review | Expert Opin Investig Drugs | Update on gastric and duodenal ulcer therapy (H. pylori and NSAIDs as main causes) |

Most retrieved publications are reviews or comparisons among PPIs. Direct randomized evidence for pantoprazole in ulcer healing is stronger under the duodenal ulcer entity (for example PMID 7569755 and 7614102, both RCTs from 1995).

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001098 | Somac Control | Not specified | Short-term treatment of reflux symptoms (e.g. heartburn, acid regurgitation) in adults. (Cancelled) |
| EMEA/H/C/001097 | Controloc Control | Not specified | Short-term treatment of reflux symptoms (e.g. heartburn, acid regurgitation) in adults. (Cancelled) |
| EMEA/H/C/001013 | Pantozol Control | Not specified | Short-term treatment of reflux symptoms (e.g. heartburn, acid regurgitation) in adults. (Cancelled) |

All three centrally authorized products are cancelled, and none are currently valid.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not from label text): osteoporosis, postmenopausal osteoporosis, bone fracture, and pernicious anemia. These are consistent with known concerns about long-term acid suppression (reduced calcium and vitamin B12 absorption) and should be verified against the SmPC.
- **Drug interactions**: 100 interactions were identified in the DDInter database. Examples include:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: atorvastatin, bosutinib, alpelisib, apalutamide, fenofibrate, hydrochlorothiazide, amphotericin B, amikacin, amphetamine, armodafinil, bumetanide
  - **Minor**: acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin

Label-based warnings and contraindications were not available; please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Active peptic ulcer disease is a core acid-related indication. A completed Phase 3 randomized trial and a substantial body of ulcer-related literature (including randomized duodenal ulcer trials) support it, so the evidence level is L1. The guardrails reflect that all three EU centrally authorized products are cancelled, that the Phase 3 trial is a comparison of PPI-based H. pylori triple therapy rather than a pantoprazole-versus-placebo ulcer-healing study, and that safety label data are missing.

Other predictions in the ranking vary widely:
- **Duodenal ulcer and gastric ulcer**: L1, Proceed with Guardrails.
- **Peptic ulcer perforation and duodenogastric reflux**: L3, Research Question (adjunct or physiological evidence only).
- **Gastrojejunal ulcer**: L4, Research Question.
- **Duodenal obstruction, acne, and the two mastocytosis entities**: L5, Hold (no credible mechanistic link or no evidence; likely model artifacts).

**To proceed, the following is needed:**
- Warnings and contraindications from the current SmPC, since this information was not available for this report
- Confirmation of the comparator and endpoints of NCT02084420
- Clarification of the regulatory route, since the EU centrally authorized licences are all cancelled (national authorizations should be checked)
- Review of long-term safety concerns (bone health, vitamin B12 status) and the major drug interactions listed above
- Detailed mechanism of action data from DrugBank to complete the mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

