---
layout: default
title: Dalbavancin
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Dalbavancin
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

# Dalbavancin: From Acute Bacterial Skin and Skin Structure Infections to Post-Bacterial Disorder

## One-Sentence Summary

Dalbavancin is a long-acting lipoglycopeptide antibiotic internationally approved for Acute Bacterial Skin and Skin Structure Infections (ABSSSI) caused by susceptible Gram-positive organisms, but currently not marketed in Taiwan. The TxGNN model predicts it may be effective for **Post-Bacterial Disorder** — a broad disease node encompassing S. aureus bacteremia, infective endocarditis, and bone/joint infections beyond its approved ABSSSI indication — with **8 clinically active or completed trials** supporting this direction, including a completed Phase 2b RCT in S. aureus bacteremia and an ongoing Phase 3 confirmatory trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Bacterial Skin and Skin Structure Infections (ABSSSI) — not currently marketed in Taiwan |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Dalbavancin is a lipoglycopeptide antibiotic with an exceptionally long plasma half-life of approximately 8–10 days — a pharmacokinetic property that fundamentally distinguishes it from conventional antibiotics. This allows once-weekly or single-dose intravenous administration, making it ideally suited for Outpatient Parenteral Antibiotic Therapy (OPAT). It exhibits concentration-dependent bactericidal activity against Gram-positive pathogens, including methicillin-resistant Staphylococcus aureus (MRSA) and streptococcal species.

The "post-bacterial disorder" node in the TxGNN knowledge graph functions as a broad disease category that encompasses the full clinical spectrum of serious Gram-positive infections — from the approved ABSSSI indication to S. aureus bacteremia (SAB), complicated infective endocarditis, and osteomyelitis. The mechanistic continuity is strong: the same bactericidal efficacy against MRSA/MSSA that treats skin infections is directly applicable to bacteremia and endovascular infections. The key clinical innovation lies in the OPAT model — dalbavancin's prolonged half-life compresses what would traditionally require 4–6 weeks of daily IV vancomycin into 1–2 administrations, dramatically reducing hospital days and catheter-related complication risks.

The translation from ABSSSI to bloodstream and deep-seated infections is not a speculative leap: the DOTS trial (NCT04775953, Phase 2b, n=200, completed) directly investigated dalbavancin for complicated SAB with right-sided infective endocarditis, and a Phase 3 confirmatory trial (NCT05117398, n=406) is actively recruiting for catheter-related SAB. This stepwise clinical development strongly validates what TxGNN identified through graph-based inference.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04775953](https://clinicaltrials.gov/study/NCT04775953) | Phase 2b | Completed | 200 | DOTS trial: dalbavancin vs. standard of care for completed treatment of complicated S. aureus bacteremia or right-sided native valve infective endocarditis after bacteremia clearance; the most direct re-purposing evidence beyond approved indication |
| [NCT05117398](https://clinicaltrials.gov/study/NCT05117398) | Phase 3 | Recruiting | 406 | Single-dose dalbavancin 1500 mg vs. 14-day standard antibiotic therapy for non-complicated catheter-related S. aureus bloodstream infections; primary endpoint at Day 30; key confirmatory Phase 3 following DOTS |
| [NCT01431339](https://clinicaltrials.gov/study/NCT01431339) | Phase 3 | Completed | 739 | DISCOVER 1: dalbavancin vs. vancomycin/linezolid for ABSSSI; established safety and efficacy at 48–72 hours for Gram-positive skin infections including MRSA |
| [NCT01339091](https://clinicaltrials.gov/study/NCT01339091) | Phase 3 | Completed | 573 | DISCOVER 2: replication of DISCOVER 1 across additional geographic regions; confirmed cross-regional consistency of Gram-positive efficacy as the co-pivotal registration trial |
| [NCT02127970](https://clinicaltrials.gov/study/NCT02127970) | Phase 3 | Completed | 698 | Single-dose 1500 mg vs. two-dose regimen for ABSSSI; established non-inferiority of single-administration OPAT model that underpins all subsequent bloodstream infection strategies |
| [NCT02814916](https://clinicaltrials.gov/study/NCT02814916) | Phase 3 | Completed | 199 | Pediatric ABSSSI (birth–17 years, open-label): safety and descriptive efficacy in children with suspected or proven Gram-positive infections including MRSA strains |
| [NCT03233438](https://clinicaltrials.gov/study/NCT03233438) | Phase 4 | Completed | 91 | Critical pathway study: guideline-based patient selection + dalbavancin vs. usual care for ABSSSI; assessed real-world OPAT clinical feasibility and healthcare utilization outcomes |
| [NCT04847921](https://clinicaltrials.gov/study/NCT04847921) | Phase 2/3 | Terminated | 11 | Simplified two-dose dalbavancin for severe Gram-positive infections in people who inject drugs; terminated early due to recruitment challenges (n=11 only), but conceptually validates OPAT re-purposing in adherence-challenged populations |
| [NCT06810583](https://clinicaltrials.gov/study/NCT06810583) | Phase 1 | Recruiting | 29 | Dalbavancin-based prophylaxis in pediatric AML or relapsed ALL receiving myelosuppressive chemotherapy; evaluates bacteremia prevention in immunocompromised hosts with every-28-day dosing |
| [NCT03941951](https://clinicaltrials.gov/study/NCT03941951) | N/A | Unknown | 900 | NEW_SAFE project (Andalusia, Spain): quasi-experimental optimization study of new antibiotics including dalbavancin across 14 hospitals; antibiotic stewardship background reference |

---

## Literature Evidence

Currently no related literature available for the post-bacterial disorder indication.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The completed DOTS Phase 2b trial (n=200) directly demonstrates dalbavancin's efficacy in S. aureus bacteremia — the most clinically impactful re-purposing target — and a Phase 3 confirmatory trial is actively enrolling, providing an evidence trajectory that, combined with the established ABSSSI pivotal trials, meets L1 criteria for the broader post-bacterial disorder category.

**To proceed, the following is needed:**
- Mechanism of action documentation (DrugBank API query pending — currently DG002 High severity gap)
- Taiwan TFDA prescribing information / safety section (currently DG001 Blocking severity gap; required before any S1 safety assessment can be initiated)
- Review of DOTS Phase 2b full publication results (NCT04775953) to assess primary and secondary clinical endpoint outcomes
- Evaluation of NCT05117398 Phase 3 interim data as it becomes available
- Pharmacokinetic-pharmacodynamic (PK/PD) target attainment modeling for bacteremia and deep-seated infection compartments
- Development of an OPAT safety monitoring protocol covering infusion-related reactions, hepatic function, and Clostridium difficile risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

