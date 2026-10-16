---
layout: default
title: Vardenafil
parent: AI Predictions (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vardenafil: predicted new indication Amenorrhea (evidence level L5). Approved use: Treatment of erectile dysfunction in adult men"
monitor_inn: "Vardenafil"
predicted_indications: ["amenorrhea (disease)", "hypoalphalipoproteinemia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypertrichosis (disease)", "malignant catarrh", "infectious bovine rhinotracheitis", "duodenogastric reflux"]
---

# Vardenafil
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

# Vardenafil: From Erectile Dysfunction to Amenorrhea

## One-Sentence Summary

Vardenafil is a PDE5 inhibitor, originally authorized in the EU (as Levitra) for treating erectile dysfunction in adult men.
The TxGNN model predicts it may be effective for **amenorrhea**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of erectile dysfunction in adult men |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 98.37% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Vardenafil is a PDE5 inhibitor. PDE5 inhibition raises cGMP levels and promotes smooth muscle relaxation and vasodilation, which is how it supports erections. Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on the drug's known drug class rather than source data.

A link between erectile dysfunction and amenorrhea is not obvious. The only plausible bridge is increased blood flow to the uterus or ovaries, and this is speculative. No trials or publications support it. The high TxGNN score (0.98) reflects a computational prediction from a knowledge graph and should not be read as evidence of efficacy. Because the mechanism data is missing, the rationale cannot be checked against source data.

Other top predictions (such as hypoalphalipoproteinemia, hypertrichosis, and several congenital malformation syndromes) also lack supporting evidence. Two of them, malignant catarrh and infectious bovine rhinotracheitis, are veterinary diseases and are most likely knowledge-graph artifacts.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (derived from drug-disease links in the TxGNN knowledge graph, not from official label text):
- Cardiovascular: familial long QT syndrome, aortic stenosis (including valve disease and supravalvular forms), hypotensive disorder, acute coronary syndrome, myocardial infarction, coronary thrombosis, hypertrophic cardiomyopathy (including familial form)
- Cerebrovascular: stroke disorder, cerebrovascular disorder, cerebral infarction
- Blood disorders: blood coagulation disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, hemoglobinopathy, plasma cell myeloma, leukemia
- Genitourinary: priapism, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans
- Other: liver failure, hearing loss disorder, X-linked mixed deafness with perilymphatic gusher, anterior ischemic optic neuropathy

**Drug Interactions** (100 interactions found in total; examples of the 20 retrieved):
- **Major**: Clarithromycin, Dolasetron, Cisapride
- **Moderate**: Famotidine, Loperamide, Aprepitant, Lorcaserin, Bisacodyl, Metronidazole, Canagliflozin, Cimetidine, Dapagliflozin, Empagliflozin, Palonosetron, Clotrimazole, among others

Please refer to the SmPC for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, the mechanistic link to amenorrhea is speculative, and the only EU authorization has been cancelled. The knowledge-graph contraindication signals (mainly cardiovascular) would also need careful consideration in any new population.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) from DrugBank
- Official warnings and contraindications from the EMA product information
- Preclinical or literature evidence linking PDE5 inhibition to the pathophysiology of amenorrhea
- Review of whether the predicted indication is clinically meaningful, and a decision on whether to prioritize other candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

