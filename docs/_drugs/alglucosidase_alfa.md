---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: From Pompe Disease (GSD II) to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa (Myozyme/Lumizyme) is a recombinant human acid alpha-glucosidase (GAA) used as enzyme replacement therapy (ERT) for Pompe disease (Glycogen Storage Disease Type II), where GAA deficiency leads to progressive lysosomal glycogen accumulation in muscle and nervous tissue.
The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease (APBD)**, a rare neurodegenerative disorder driven by partial GBE1 deficiency causing polyglucosan body accumulation in neurons — sharing the same glycogen metabolism pathway as Pompe disease.
Currently, **no clinical trials** and **no published literature** directly support this repurposing direction, placing this candidate at evidence level **L5** (AI model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pompe disease (Glycogen Storage Disease Type II / GSD II) |
| Predicted New Indication | Adult Polyglucosan Body Disease (APBD) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 — AI prediction only, no clinical or preclinical studies found |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alglucosidase alfa is a recombinant form of human acid alpha-glucosidase (GAA), the enzyme that degrades lysosomal glycogen by cleaving α-1,4 glycosidic bonds. In Pompe disease (GSD II), complete or near-complete GAA deficiency causes glycogen to accumulate progressively in skeletal muscle, cardiac muscle, and motor neurons, ultimately leading to respiratory failure and cardiomyopathy. As an enzyme replacement therapy, alglucosidase alfa is taken up by cells via mannose-6-phosphate receptors and delivered to the lysosome, where it restores the missing catalytic activity.

Adult Polyglucosan Body Disease (APBD) is caused by *partial* deficiency of glycogen branching enzyme (GBE1), resulting in the accumulation of abnormally structured polyglucosan bodies — poorly branched, amylose-like glycogen polymers rich in linear α-1,4 glucose chains — in neurons, astrocytes, and peripheral nerves. Because these polyglucosan bodies contain the same α-1,4 linkages that alglucosidase alfa cleaves, there is a theoretical substrate-level rationale for partial degradation. Both disorders belong to the glycogen storage pathway, making APBD the mechanistically strongest repurposing candidate among all top TxGNN predictions for this drug.

Nonetheless, the mechanistic link is indirect. APBD arises from GBE1 deficiency, not GAA deficiency, so alglucosidase alfa does not correct the primary enzymatic lesion. Polyglucosan bodies also contain α-1,6 branch points that GAA cannot cleave, limiting clearance efficiency. Whether intravenously administered GAA can reach affected neurons in sufficient concentrations — and whether partial polyglucosan clearance translates into clinical benefit — remains entirely unvalidated. The prediction is biologically plausible but requires laboratory and preclinical confirmation before any clinical translation is considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Taiwan regulatory data (TFDA SmPC warnings and contraindications) were not available at the time of this analysis. Known class effects for alglucosidase alfa include risk of infusion-associated reactions, anaphylaxis, and immune-mediated reactions — these should be reviewed from the EMA or FDA prescribing information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This repurposing prediction is supported solely by the TxGNN model score (99.47%) and a theoretically plausible but indirect mechanistic link between GAA activity and the linear glycan component of polyglucosan bodies in APBD. With no clinical trials, no supporting literature, and a primary enzymatic defect (GBE1) distinct from the drug's established target (GAA), there is insufficient evidence to advance beyond a research question at this stage.

**To proceed, the following is needed:**

- **Preclinical substrate studies**: Confirm in vitro that alglucosidase alfa can degrade GBE1-deficient polyglucosan bodies, and determine the extent of degradation given the presence of α-1,6 branch points
- **Animal model validation**: Test ERT efficacy and CNS delivery in GBE1-knockout or APBD mouse models, assessing both polyglucosan clearance and neurological outcomes
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank API and published pharmacology literature (data gap DG002)
- **Regulatory safety review**: Download and parse the TFDA SmPC PDF to extract warnings and contraindications (data gap DG001); also cross-reference with EMA and FDA product labels for infusion reaction and immunogenicity risk management
- **Research question formulation**: Define a formal hypothesis, patient population, endpoints, and IND-enabling study plan if preclinical results are encouraging
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

