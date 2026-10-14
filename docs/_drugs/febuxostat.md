---
layout: default
title: Febuxostat
parent: Medium Evidence (L3-L4)
nav_order: 254
evidence_level: L4
indication_count: 10
---

# Febuxostat
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

# Febuxostat: From Chronic Hyperuricaemia to Renal Hypouricaemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat chronic hyperuricaemia in patients with gout, and to prevent and treat hyperuricaemia in adults receiving chemotherapy for haematologic malignancies at risk of tumour lysis syndrome.
The TxGNN model predicts it may be effective for **renal hypouricaemia**, but only **1 clinical trial** (weakly relevant) and **2 publications** (reviews/case-level) are linked to this prediction.
The mechanistic rationale is weak and the prediction is more likely a knowledge-graph artefact than a real therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of chronic hyperuricaemia where urate deposition has already occurred (including a history of, or presence of, tophus and/or gouty arthritis) |
| Predicted New Indication | Hypouricaemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Febuxostat is known to be a non-purine selective xanthine oxidase inhibitor that lowers serum urate, and its efficacy in chronic hyperuricaemia and gout is established.

Renal hypouricaemia is the opposite problem. Serum urate is already low because of defective renal urate reabsorption (for example, loss of function of URAT1 or GLUT9). A urate-lowering drug has no obvious therapeutic rationale here and could worsen the condition. The high TxGNN score most likely reflects a graph association with urate metabolism rather than a true therapeutic opportunity.

The only plausible link is indirect and speculative. A 2023 case report describes a 16-year-old football player with familial renal hypouricaemia and recurrent exercise-induced acute kidney injury, in whom a non-purine selective xanthine oxidoreductase inhibitor was explored as prophylaxis when hydration alone failed. This is a single-patient observation, not evidence of efficacy.

Other predictions in the list (HPRT partial deficiency and Lesch-Nyhan syndrome) are mechanistically more coherent, since they involve urate overproduction. They largely overlap with the existing hyperuricaemia indication, and none addresses the neurological features of those diseases.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of the effect of uric acid control on stone recurrence and renal function in patients with calculi and hyperuricaemia. This is likely a hyperuricaemia study matched on drug name and is not direct evidence for renal hypouricaemia (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (classified as Review) | Internal Medicine | A 16-year-old footballer with familial renal hypouricaemia (URAT1 compound heterozygous mutations) had recurrent exercise-induced acute kidney injury. Hydration did not prevent it, and a non-purine xanthine oxidoreductase inhibitor (febuxostat) was considered as prophylaxis. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricaemia (serum urate < 2 mg/dL), covering causes and what practicing rheumatologists should know. It does not support urate-lowering therapy in this condition. |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000777 | Adenuric | Not specified | 80 mg: chronic hyperuricaemia with urate deposition (including tophus and/or gouty arthritis). 120 mg: the same, plus prevention and treatment of hyperuricaemia in adults undergoing chemotherapy for haematologic malignancies at intermediate to high ris... |
| EMEA/H/C/004374 | Febuxostat Viatris (previously Febuxostat Mylan) | Not specified | Chronic hyperuricaemia with urate deposition (including tophus and/or gouty arthritis); prevention and treatment of hyperuricaemia in adults undergoing chemotherapy for haematologic malignan... |
| EMEA/H/C/004773 | Febuxostat Krka | Not specified | Treatment of chronic hyperuricaemia in conditions where urate deposition has already occurred (including a history, or presence of, tophus and/or gouty arthritis). Indicated in adults. |

All three authorizations are cancelled.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): stroke disorder, cerebrovascular disorder, cerebral infarction, myocardial infarction, coronary thrombosis, and hemoglobinopathy.
- **Drug Interactions**: 22 interactions were identified in total. The **major** interactions are:
  - Mercaptopurine
  - Azathioprine
  - Leflunomide
  - Teriflunomide

  **Moderate** interactions include theophylline and related xanthines (dyphylline, aminophylline, oxtriphylline), methotrexate, tioguanine, clofarabine, asparaginase and pegaspargase, brentuximab vedotin, trabectedin, epirubicin, naltrexone, and interferon beta products.
- **Other considerations**: Reducing urate production in conditions with purine overproduction may raise xanthine/hypoxanthine excretion, with a risk of xanthine nephropathy or stones. Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Renal hypouricaemia is a state of already low urate, so lowering urate further has no clear therapeutic logic. The supporting evidence is one weakly relevant trial and two literature items, including a single-patient case report. The high TxGNN score appears to reflect graph association rather than real therapeutic potential. No EU authorizations are currently valid.

**To proceed, the following is needed:**
- Detailed mechanism of action data and the SmPC safety information (warnings and contraindications)
- Mechanistic and clinical justification for urate-lowering in renal hypouricaemia, ideally with controlled data on exercise-induced acute kidney injury prevention
- Confirmation of what NCT04398251 actually studied
- If a related direction is pursued, consider the mechanistically more coherent HPRT deficiency indications, with attention to xanthine stone risk and cardiovascular safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

