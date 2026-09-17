---
layout: default
title: Pertuzumab
parent: Medium Evidence (L3-L4)
nav_order: 468
evidence_level: L4
indication_count: 10
---

# Pertuzumab
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

Using no additional skill — this is a direct content-generation task with an already fully specified template; I'll follow it exactly against the supplied Evidence Pack.

A few data-fidelity notes before the report: `predicted_indications[0]` is **"normal breast-like subtype of breast carcinoma"**, which per the pack's own `repurposing_rationale` is flagged as a likely TxGNN over-generalization artifact (L4/Hold), not the strongest candidate in the pack (ranks 2–3 have L1/Proceed-with-Guardrails evidence, but those are PR-status stratifications of Pertuzumab's *existing* approved indication, not a new indication). I've followed the instruction to build the report around `predicted_indications[0]` as specified, and flagged this context where relevant so the report isn't misleading.

---

# Pertuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

> Pertuzumab is a HER2-targeted monoclonal antibody whose approved use is referenced throughout the evidence pack as HER2-positive breast cancer (structured indication/MOA fields are a data gap in this pack).
> The TxGNN model's top-ranked prediction is **normal breast-like (PAM50 "normal-like") subtype of breast carcinoma**,
> but **0 of the 6 identified clinical trials specifically enrolled this subtype**, and **no supporting literature** was found — the biological rationale is weak and possibly contradictory to the drug's mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (inferred from evidence annotations; structured license/indication data is a data gap) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this pack). Based on the available context, Pertuzumab is a HER2-targeted monoclonal antibody used in HER2-positive breast cancer, where it blocks HER2 domain II-mediated heterodimerization (notably with HER3), complementing trastuzumab's mechanism.

The predicted indication, however, raises a biological concern: PAM50 "normal-like" breast carcinoma is a subtype typically characterized as **low-proliferation and HER2-negative leaning**, which sits awkwardly against an anti-HER2 mechanism of action. This mismatch is explicitly noted in the pack's own scoring rationale.

Consistent with this concern, all six identified clinical trials are general HER2-positive neoadjuvant treatment studies (T-DXd trials, vaccine combinations, precision-medicine platforms) — none specifically enrolled or stratified for the "normal-like" molecular subtype. The most plausible explanation is that TxGNN's knowledge-graph embedding over-generalized "breast cancer" trial evidence across molecular subtypes that are not mechanistically interchangeable. This prediction should be treated as **hypothesis-generating only**, not as an actionable repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | Trastuzumab deruxtecan (T-DXd) vs. standard preoperative treatment in HER2+ breast cancer; biology-driven neoadjuvant selection (ARIADNE) — general HER2+ trial, no normal-like subtype stratification |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as preoperative therapy for inflammatory breast cancer; small sample, general HER2+ population |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine combined with neoadjuvant chemotherapy and HER2-targeted therapy; non-subtype-specific |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | Precision neoadjuvant treatment platform for operable breast cancer; no evidence of subtype-specific stratification |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Drug-screening (patient-derived tumor-like cell clusters)-guided neoadjuvant therapy for HER2+ early breast cancer |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Optimal neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2+ breast cancer |

**Note:** All six trials were graded "C" relevance (indirect) — none specifically enrolled or reported outcomes for the PAM50 normal-like subtype.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Pertuzumab is currently **not marketed** under this evidence pack (0 authorizations on record; no license entries available).

## Cytotoxicity

Pertuzumab is a monoclonal antibody targeted therapy used in an oncology context (HER2-positive breast cancer), so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-targeted monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (normal breast-like subtype) has weak, indirect evidence — no trial or publication specifically supports Pertuzumab's use in this subtype, and the mechanistic link is biologically questionable given the subtype's typical HER2-negative leaning. This is best treated as a data-quality/over-generalization artifact of the TxGNN model rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed HER2 amplification/overexpression status specifically within PAM50 "normal-like" tumors, to establish a valid biological rationale
- Core drug-level data gaps must be closed first: original indication/MOA (DG002) and TFDA/EMA label warnings and contraindications (DG001, Blocking)
- If a repurposing signal is still desired, ranks 2–3 in this pack ("progesterone-receptor positive/negative breast cancer") have substantially stronger evidence (L1, multiple completed Phase 3 RCTs) — but note these represent PR-status stratification within Pertuzumab's **existing** HER2-positive breast cancer indication, not a novel indication, and should be labeled accordingly rather than presented as new repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

