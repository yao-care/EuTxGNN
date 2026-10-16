---
layout: default
title: Esomeprazole
parent: High Evidence (L1-L2)
nav_order: 243
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Esomeprazole: predicted new indication Duodenal ulcer (evidence level L1). Approved use: Short-term treatment of reflux symptoms (e.g. heartburn and acid regu…"
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)", "active peptic ulcer disease", "abnormality of glucagon secretion", "gastrojejunal ulcer", "peptic ulcer perforation", "Smouldering systemic mastocytosis", "multiple endocrine neoplasia", "acne (disease)"]
---

# Esomeprazole
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

# Esomeprazole: From Reflux Symptoms to Duodenal Ulcer

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor, originally authorised in the EU (as Nexium Control) for short-term treatment of reflux symptoms such as heartburn and acid regurgitation in adults.
The TxGNN model predicts it may be effective for **duodenal ulcer**, with **30 clinical trials** and **20 publications** currently supporting this direction.
Note that this is an established acid-related use rather than a truly novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Short-term treatment of reflux symptoms (e.g. heartburn and acid regurgitation) in adults |
| Predicted New Indication | Duodenal ulcer (the top-ranked TxGNN prediction is duodenogastric reflux; duodenal ulcer, rank 3, is the best-supported candidate and is the one evaluated below) |
| TxGNN Prediction Score | 99.39% (duodenal ulcer); 99.53% (duodenogastric reflux, rank 1) |
| Evidence Level | L1 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, esomeprazole is the S-isomer of omeprazole and a proton pump inhibitor. It blocks the gastric H+/K+ ATPase, producing profound and sustained acid suppression.

Reflux symptoms and duodenal ulcer are both acid-related disorders. Sustained acid suppression promotes ulcer healing. Esomeprazole is also a core component of *H. pylori* eradication regimens (triple and bismuth quadruple therapy), which address the main cause of duodenal ulcer.

The model's top-ranked prediction, duodenogastric reflux, is mainly an alkaline or bile-driven process. Acid suppression is therefore only indirectly relevant, and the evidence for it is weak (L4, one review). Several other high-scoring predictions, including duodenal obstruction, abnormality of glucagon secretion, peptic ulcer perforation, smouldering systemic mastocytosis and acne, have no clinical or literature support and should be treated as model output only.

---

## Clinical Trial Evidence

Thirty trials were retrieved for duodenal ulcer. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00633932](https://clinicaltrials.gov/study/NCT00633932) | Phase 3 | Completed | 602 | Esomeprazole 20/40 mg vs omeprazole 20 mg for healing of reflux esophagitis at 8 weeks |
| [NCT00633672](https://clinicaltrials.gov/study/NCT00633672) | Phase 3 | Completed | 400 | Esomeprazole 40/20 mg vs ranitidine for healing NSAID-associated gastric ulcers |
| [NCT00542789](https://clinicaltrials.gov/study/NCT00542789) | Phase 3 | Completed | 343 | Esomeprazole 20 mg vs placebo for preventing gastric/duodenal ulcers with daily NSAID use |
| [NCT00629928](https://clinicaltrials.gov/study/NCT00629928) | Phase 3 | Completed | 800 | Esomeprazole 40/20 mg vs placebo for preventing gastric and duodenal ulcers with NSAID use |
| [NCT01069939](https://clinicaltrials.gov/study/NCT01069939) | Phase 3 | Completed | 427 | Esomeprazole 20 mg vs placebo for preventing ulcers with low-dose aspirin |
| [NCT01142245](https://clinicaltrials.gov/study/NCT01142245) | Phase 3 | Completed | 263 | IV and oral esomeprazole for preventing recurrent peptic ulcer bleeding after endoscopic therapy |
| [NCT02296021](https://clinicaltrials.gov/study/NCT02296021) | Phase 4 | Completed | 612 | Berberine-based vs bismuth-based quadruple therapy including esomeprazole for *H. pylori* eradication |
| [NCT04678492](https://clinicaltrials.gov/study/NCT04678492) | Phase 4 | Completed | 658 | High-dose esomeprazole plus amoxicillin vs bismuth quadruple therapy for *H. pylori* rescue |
| [NCT06850480](https://clinicaltrials.gov/study/NCT06850480) | Phase 3 | Recruiting | 356 | Zastaprazan vs Nexium in reflux esophagitis (no results yet) |
| [NCT07312370](https://clinicaltrials.gov/study/NCT07312370) | Phase 4 | Not yet recruiting | 120 | IV esomeprazole plus sucralfate for ulcer healing after gastric ESD |

Most of the ulcer trials are in gastric or NSAID-associated ulcer settings or *H. pylori* eradication regimens. They are closely related to, but not specific to, duodenal ulcer treatment.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11742194](https://pubmed.ncbi.nlm.nih.gov/11742194/) | 2001 | RCT | Eur J Gastroenterol Hepatol | One week of esomeprazole-based triple therapy eradicates *H. pylori* and heals duodenal ulcer |
| [11121908](https://pubmed.ncbi.nlm.nih.gov/11121908/) | 2000 | RCT | Aliment Pharmacol Ther | One-week esomeprazole triple therapy gives effective *H. pylori* eradication in duodenal ulcer disease |
| [19221370](https://pubmed.ncbi.nlm.nih.gov/19221370/) | 2009 | Randomized trial | Ann Intern Med | IV esomeprazole for prevention of recurrent peptic ulcer bleeding |
| [12093317](https://pubmed.ncbi.nlm.nih.gov/12093317/) | 2002 | Review | Drugs | Esomeprazole in acid-related disorders; better acid control than racemic PPIs |
| [18627213](https://pubmed.ncbi.nlm.nih.gov/18627213/) | 2008 | Review | Drugs | Esomeprazole in gastric acid-related diseases, including *H. pylori*-associated duodenal ulcer |
| [10983736](https://pubmed.ncbi.nlm.nih.gov/10983736/) | 2000 | Review | Drugs | Esomeprazole gives better intragastric pH control than omeprazole, lansoprazole and pantoprazole |
| [22372726](https://pubmed.ncbi.nlm.nih.gov/22372726/) | 2012 | Review | Drugs Aging | Fixed-dose aspirin/esomeprazole reduces gastric and duodenal ulcer risk |
| [16335855](https://pubmed.ncbi.nlm.nih.gov/16335855/) | 2005 | Review | Drugs | PPIs are recommended for *H. pylori* eradication, ulcer healing and NSAID-induced lesions |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Review | Expert Opin Investig Drugs | Update on gastric and duodenal ulcer therapy; *H. pylori* and NSAIDs are the two principal causes |
| [39319279](https://pubmed.ncbi.nlm.nih.gov/39319279/) | 2024 | Clinical study | Pediatr Gastroenterol Hepatol Nutr | Long-term esomeprazole in Japanese paediatric patients for reflux esophagitis maintenance and NSAID/aspirin ulcer prevention |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002618 (cancelled) | Nexium Control | Not specified | Nexium Control is indicated for the short-term treatment of reflux symptoms (e.g. heartburn and acid regurgitation) in adults. |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not label text): liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture, chronic atrophic gastritis.
- **Drug Interactions**: 100 interactions were identified, of which 20 are shown in the compiled data. Major interactions include **acalabrutinib** and **atazanavir**. Moderate interactions include hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib and bumetanide. Minor interactions include acetylsalicylic acid, axitinib, bortezomib, brivaracetam and cyanocobalamin. The trial data also flag clarithromycin and clopidogrel as relevant to ulcer regimens.

Please refer to the SmPC for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 randomised trials and Phase 4 *H. pylori* eradication trials support esomeprazole in ulcer-related settings, which meets the L1 criterion. The indication is already well established for acid-related disease, so it is arguably not a novel repurposing. The only EU authorisation is a cancelled OTC reflux product.

**To proceed, the following is needed:**
- Confirm the regional label scope, since the only EU licence is cancelled and covers reflux symptoms only
- Review the SmPC warnings and contraindications (label data are currently missing)
- Obtain detailed mechanism of action data
- Confirm duodenal-ulcer-specific trial data, since most retrieved Phase 3 trials are in gastric or NSAID-associated settings
- Check local *H. pylori* resistance patterns
- Prepare a DDI management plan covering clarithromycin, clopidogrel, atazanavir and acalabrutinib
- Consider bone health and hepatic function monitoring, given the knowledge-graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

