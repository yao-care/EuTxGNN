---
layout: default
title: Roflumilast
parent: Medium Evidence (L3-L4)
nav_order: 534
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Roflumilast: predicted new indication Pulmonary hypertension (evidence level L4). Approved use: Maintenance treatment of severe COPD (post-bronchodilator FEV1 below…"
monitor_inn: "Roflumilast"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "headache disorder", "female breast carcinoma", "trigeminal autonomic cephalalgia", "obsolete patella aplasia, coxa vara, and tarsal synostosis", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "pulmonary hypertension, primary, autosomal recessive"]
---

# Roflumilast
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Roflumilast: From Severe COPD to Pulmonary Hypertension

## One-Sentence Summary

Roflumilast is an oral PDE4 inhibitor, originally used as add-on maintenance treatment for severe chronic obstructive pulmonary disease (COPD) with chronic bronchitis.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are currently **no registered clinical trials** and only **preclinical and review literature** (10 publications) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maintenance treatment of severe COPD (post-bronchodilator FEV1 below 50% predicted) associated with chronic bronchitis in adults with frequent exacerbations, as add-on to bronchodilator treatment |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, roflumilast is a selective PDE4 inhibitor. By blocking PDE4 it raises intracellular cAMP, which gives anti-inflammatory, anti-emphysema and other effects in COPD.

The link to pulmonary hypertension is plausible. Pulmonary hypertension is a frequent complication of advanced COPD. PDE4 is expressed in human pulmonary artery smooth muscle cells, and PDE4 inhibition has anti-proliferative effects there. In rats, roflumilast attenuated hypoxia- and monocrotaline-induced pulmonary hypertension. It also reduced lung injury caused by pulmonary air embolism in an animal model. These findings suggest vasodilatory, anti-remodelling and anti-inflammatory effects.

These data are preclinical only, and there is no human efficacy evidence. The high TxGNN score is consistent with the mechanism but is a computational prediction, not clinical evidence. One cited paper concerns ensifentrine, a different PDE3/4 inhibitor, so it offers only indirect class-level support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19386793](https://pubmed.ncbi.nlm.nih.gov/19386793/) | 2009 | Preclinical (animal) | J Pharmacol Exp Ther | Roflumilast attenuated hypoxia- and monocrotaline-induced pulmonary hypertension in rats |
| [31004869](https://pubmed.ncbi.nlm.nih.gov/31004869/) | 2019 | Preclinical (animal) | J Surg Res | Roflumilast attenuated lung injury induced by pulmonary air emboli |
| [16423283](https://pubmed.ncbi.nlm.nih.gov/16423283/) | 2006 | Preclinical (in vitro) | Respir Res | PDE4 is expressed in human pulmonary artery smooth muscle cells, and its inhibition has anti-proliferative effects |
| [37524492](https://pubmed.ncbi.nlm.nih.gov/37524492/) | 2023 | Review | Adv Pharmacol | PDE inhibitors as targets in lung diseases, including COPD, asthma, cystic fibrosis and pulmonary hypertension |
| [21316552](https://pubmed.ncbi.nlm.nih.gov/21316552/) | 2010 | Review | Arch Bronconeumol | Pharmacological profile of roflumilast: PDE4 inhibition, raised cAMP, anti-inflammatory effects |
| [20381629](https://pubmed.ncbi.nlm.nih.gov/20381629/) | 2010 | Review | Pulm Pharmacol Ther | Preclinical pharmacology of roflumilast, a selective oral PDE4 inhibitor |
| [16458289](https://pubmed.ncbi.nlm.nih.gov/16458289/) | 2006 | Review | Eur J Pharmacol | PDE inhibitors in airways disease: cAMP elevation, airway smooth muscle relaxation, reduced inflammation |
| [42582753](https://pubmed.ncbi.nlm.nih.gov/42582753/) | 2026 | Commentary / early data | Open Respir Med J | Early data on ensifentrine (a different PDE3/4 inhibitor) in COPD-associated pulmonary hypertension; indirect support only |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001179 (cancelled) | Daxas | Not specified | Maintenance treatment of severe chronic obstructive pulmonary disease (COPD) (FEV1 post-bronchodilator less than 5... |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total, and the 20 listed in the data are all of Moderate severity. The main groups are:
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Cimetidine
  - Obeticholic acid
  - Deferasirox
  - Radiopharmaceuticals/antibodies: iobenguane (I-131), ibritumomab tiuxetan, tositumomab
  - Others: fostamatinib, ticlopidine, levamisole, thiabendazole, trimetrexate
- **Knowledge-graph contraindication signals** (from a computational graph, not label text): liver failure, anxiety disorder, neurotic disorder, dysthymic disorder.

For full warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to animal and in vitro studies plus reviews (L4), with no human efficacy data and no registered trials. The only EU authorization is cancelled, and the label safety information has not been reviewed.

**To proceed, the following is needed:**
- Review of the SmPC warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Human evidence, such as a pilot or Phase 2 study in pulmonary hypertension, ideally in COPD-associated disease
- Dose and tolerability assessment in pulmonary hypertension patients, including the graph-flagged liver and psychiatric considerations
- Clarification of the regulatory and market situation, given that the EU authorization has been cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

