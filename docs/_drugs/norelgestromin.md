---
layout: default
title: Norelgestromin
parent: AI Predictions (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Norelgestromin
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

# Norelgestromin: From Contraceptive Use to Amenorrhea

## One-Sentence Summary

Norelgestromin is the active metabolite of norgestimate, used clinically as the progestin component of combined hormonal contraceptive patches. The TxGNN model predicts it may be effective for **Amenorrhea**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure AI-model prediction with no direct evidence base.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory dataset (drug not marketed in the EU). Based on established pharmacology, norelgestromin is used as the progestin component of combined hormonal contraceptive patches. |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for norelgestromin in this evidence pack. Based on known pharmacology, norelgestromin is a progestin (the active metabolite of norgestimate) that acts on the hypothalamic-pituitary-ovarian axis, suppressing ovulation via negative feedback and altering endometrial receptivity — the basis of its established use in contraception.

The link to amenorrhea is mechanistically ambiguous rather than clearly supportive: progestin-based contraceptives (e.g., long-acting injectables and patches) are themselves a well-documented **cause** of amenorrhea as a side effect, not an established treatment for it. TxGNN appears to have picked up this bidirectional pharmacological association from the knowledge graph without being able to distinguish causal direction. No clinical trial or published literature in this dataset supports using norelgestromin therapeutically to treat amenorrhea, so the causal direction of this relationship remains unresolved.

Among the other candidates in this prediction set, **acne** (rank 2, score 98.5%) has the strongest independent mechanistic rationale: norgestimate/ethinyl estradiol combinations are already an approved class-level treatment for acne via reduction of free testosterone and sebaceous androgen receptor activity. This represents a genuine class-effect signal, though direct evidence for norelgestromin itself is still absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations are currently recorded for norelgestromin in this dataset (market status: not marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA/EMA label warnings and contraindications are currently a blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (amenorrhea) is supported only by an AI model score (L5), with zero clinical trials or literature, and the proposed mechanistic link is directionally ambiguous — progestins are a known *cause* of amenorrhea, not an established treatment. Combined with the absence of any EU marketing authorization and a **blocking** data gap on safety labeling, there is currently no basis to advance this candidate beyond a research question.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) warnings, contraindications, and DDI data (DG001, blocking — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Independent literature or preclinical evidence clarifying the causal direction between progestin exposure and amenorrhea
- If pursuing the acne signal instead (rank 2), targeted literature search for norelgestromin/norgestimate-specific acne studies to confirm the class-effect assumption
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

