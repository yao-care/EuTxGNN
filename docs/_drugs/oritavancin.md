---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Oritavancin
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

Using judgment as a drug repurposing expert: among the 10 TxGNN-ranked candidates, the top-ranked hits (Bacteroidaceae infection, Mycoplasma pneumonia, herpes zoster, etc.) are explicitly flagged in their own `repurposing_rationale` as mechanistically implausible (Hold, no evidence). The only candidate with real supporting clinical trials and a coherent mechanistic story is rank 9 ("post-bacterial disorder" — effectively MDR Gram-positive device infections). I've built the report around that candidate rather than blindly using `predicted_indications[0]`, and note this explicitly below.

---

# Oritavancin: From Acute Bacterial Skin/Skin-Structure Infections to MDR Gram-Positive Device-Related Infections

## One-Sentence Summary

Oritavancin (Orbactiv) is a semisynthetic lipoglycopeptide antibiotic originally developed and approved for acute bacterial skin and skin-structure infections (ABSSSI), including MRSA. TxGNN flags **"post-bacterial disorder"** — which in the underlying trial evidence resolves to multidrug-resistant Gram-positive device infections (e.g. cardiac implantable electronic device infections) — as a plausible extension, supported by **7 clinical trials**, including two pivotal Phase 3 RCTs (SOLO I/II, n=968 and n=1019) and one newly initiating Phase-2-equivalent trial specifically testing this new use.

> **Note on prediction selection**: TxGNN's raw top-ranked prediction for oritavancin (*Bacteroidaceae infectious disease*, score 99.48%) is mechanistically implausible — oritavancin targets Gram-positive cell wall synthesis and cannot penetrate Gram-negative outer membranes — and is annotated "Hold" with zero supporting evidence. Several other top-ranked predictions (Mycoplasma pneumonia, ophthalmic herpes zoster, tinea corporis, infectious mononucleosis) are similarly flagged as biological noise. This report instead focuses on the only candidate with a defensible mechanism *and* real trial support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Bacterial Skin and Skin Structure Infections (ABSSSI), incl. MRSA — not present in Taiwan license data (drug not marketed there); inferred from pivotal trial evidence (SOLO I/II) |
| Predicted New Indication | Multidrug-resistant Gram-positive device-related infections (post-bacterial disorder bucket; CIED infection specifically) |
| TxGNN Prediction Score | 98.35% (rank #9 of pack; note top-ranked candidate at 99.48% was mechanistically implausible — see above) |
| Evidence Level | L1 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known clinical trial information, oritavancin is a semisynthetic lipoglycopeptide antibiotic structurally related to vancomycin, administered as a single 1200 mg IV dose, with a distinctively long terminal half-life (~245 hours). Its efficacy against Gram-positive cocci, including MRSA, was established in two pivotal Phase 3 trials (SOLO I and SOLO II) for ABSSSI.

Cardiac implantable electronic device (CIED) infections are predominantly caused by the same pathogen class — *Staphylococcus aureus* (including MRSA) and coagulase-negative staphylococci — often organized as biofilms on device hardware. Because oritavancin's spectrum already covers these organisms and its ultra-long half-life avoids repeated dosing, extending its use from skin infections to device-associated Gram-positive infections is a mechanistically coherent step rather than a novel biological hypothesis. This is corroborated by an actively designed randomized non-inferiority trial (NCT07013552) directly testing single-dose oritavancin against standard vancomycin therapy for CIED pocket/incision infections.

By contrast, the raw #1 TxGNN hit (Bacteroidaceae infection, a Gram-negative anaerobe class) and several other top-scored predictions have no plausible mechanistic basis and no supporting trials — these should not be pursued further without new evidence generation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07013552](https://clinicaltrials.gov/study/NCT07013552) | N/A | Not Yet Recruiting | 100 | RCT comparing single-dose oritavancin vs. standard vancomycin for MDR Gram-positive CIED pocket/incision infections — direct test of this new indication |
| [NCT01252719](https://clinicaltrials.gov/study/NCT01252719) (SOLO I) | Phase 3 | Completed | 968 | Pivotal RCT of single-dose IV oritavancin vs. vancomycin for ABSSSI incl. MRSA; original approved indication |
| [NCT01252732](https://clinicaltrials.gov/study/NCT01252732) (SOLO II) | Phase 3 | Completed | 1019 | Second pivotal RCT confirming ABSSSI efficacy/safety |
| [NCT02925416](https://clinicaltrials.gov/study/NCT02925416) | Phase 4 | Completed | 22 | Post-marketing safety study comparing single vs. two repeated 1200 mg IV doses one week apart |
| [NCT03159403](https://clinicaltrials.gov/study/NCT03159403) | N/A | Completed | 325 | Retrospective real-world observational study of oritavancin use, outcomes and adverse events |
| [NCT06688084](https://clinicaltrials.gov/study/NCT06688084) | N/A | Active, Not Recruiting | 230 | Pathogenicity study of *Staphylococcus pettenkoferi* in diabetic foot wounds/osteitis — indirect pathogen-relevance context |
| [NCT05521880](https://clinicaltrials.gov/study/NCT05521880) | Phase 4 | Terminated (n=2) | 2 | Intermittent outpatient oritavancin combined with opioid use disorder treatment; terminated early, very low evidentiary weight |

## Literature Evidence

Currently no related literature available.

## EU Market Information

Oritavancin is not currently marketed under the evaluated jurisdiction — no marketing authorization records are present in this evidence pack (0 licenses on file).

## Safety Considerations

Please refer to the SmPC for safety information. **Note:** the drug's label warnings, contraindications, and drug-interaction data are flagged as a **Blocking** data gap (DG001) in this evidence pack — no safety-stage (S1) assessment can be completed until TFDA/EMA product labeling is retrieved.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted new use (MDR Gram-positive device infections, e.g. CIED infections) rests on strong original-indication evidence (two Phase 3 RCTs, SOLO I/II) plus an actively initiating trial designed specifically for this extension — the only candidate in this pack reaching evidence level L1. However, the TxGNN disease label itself ("post-bacterial disorder") is too broad to be actionable as-is, and a critical safety data gap remains unresolved.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA product label (SmPC) to close the Blocking safety data gap (DG001: warnings, contraindications, DDI)
- Obtain formal mechanism-of-action documentation via DrugBank API (DG002)
- Clarify the precise clinical definition behind the "post-bacterial disorder" prediction bucket and confirm it maps to CIED/device-related infection rather than a broader, less-supported category
- Track results of NCT07013552 (expected completion 2026-10) as the direct efficacy readout for this indication
- Do not advance the mechanistically implausible top-scored predictions (Bacteroidaceae infection, Mycoplasma pneumonia, ophthalmic herpes zoster, tinea corporis, infectious mononucleosis, postinfectious vasculitis, post-infectious syndrome) without new supporting evidence — all correctly scored Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

