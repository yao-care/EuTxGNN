---
layout: default
title: Ticagrelor
parent: AI Predictions (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Prevention of atherothrombotic events in adults with ACS or a history…"
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome Prevention to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is a P2Y12 platelet inhibitor, originally used together with aspirin to prevent atherothrombotic events in patients with acute coronary syndromes (ACS) or a prior myocardial infarction (MI).
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**, with **2 clinical trials** and **2 publications** currently supporting this direction.
The evidence is still early: the main Phase 3 trial is ongoing and has no results yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of atherothrombotic events in adults with ACS or a history of MI and a high risk of atherothrombotic events (co-administered with aspirin) |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (capped, because the key Phase 3 trial is ongoing and ticagrelor is only one of several tested agents) |
| EU Market Status | Cancelled only (the single Brilique authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ticagrelor is a P2Y12 receptor antagonist. It reduces platelet aggregation and thrombus formation, which underlies its approved use in ACS and prior MI.

Intracranial arteriosclerosis is also an atherothrombotic disease. Platelet-driven clot formation on plaques in brain arteries can cause stroke, so the same mechanism may apply. Ticagrelor has also been used in dual antiplatelet regimens for neurointerventional procedures such as intracranial stenting. It may offer an advantage over clopidogrel in patients carrying CYP2C19 loss-of-function variants, who respond poorly to clopidogrel.

Other predictions for this drug, such as ischemic disease, are broader and largely overlap with the approved indication. Intracranial arteriosclerosis is therefore the most distinct and clinically actionable new direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1683 | CAPTIVA: tests whether rivaroxaban, ticagrelor, or both are superior to clopidogrel in lowering 1-year ischemic stroke, intracerebral hemorrhage, or vascular death in intracranial atherosclerotic stenosis. No results yet. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Not applicable | Recruiting | 100 | Pilot study of genotype-guided P2Y12 inhibitor selection (including ticagrelor) versus clopidogrel in symptomatic intracranial atherosclerotic disease. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of NeuroInterventional Surgery | Experience with ticagrelor 60 mg twice daily plus aspirin 81 mg compared with standard aspirin plus clopidogrel for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design/protocol | International Journal of Stroke | Design and early progress of CAPTIVA, which compares other dual antithrombotic combinations against clopidogrel plus aspirin for symptomatic intracranial stenosis. |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001241 (cancelled) | Brilique | Not specified | Brilique, co administered with acetylsalicylic acid (ASA), is indicated for the prevention of atherothrombotic events in adult patients with  acute coronary syndromes (ACS) or a history of... |

---

## Safety Considerations

- **Possible disease-related contraindications** (from drug-disease relationships in a knowledge graph, not from label text): liver failure, liver disease, gallbladder disease, intracranial hemorrhage. The intracranial hemorrhage signal is especially important for any use in cerebrovascular disease, and the CAPTIVA primary endpoint includes intracerebral hemorrhage.
- **Drug Interactions**: 100 interactions were identified. The one rated Major is **clarithromycin**. Moderate interactions include acetylsalicylic acid (aspirin), morphine, simvastatin, dexamethasone, aprepitant, miconazole and saxagliptin. Minor interactions include naloxegol and prucalopride.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The biological rationale is sound, and a large Phase 3 trial (CAPTIVA, n=1683) that includes a ticagrelor arm is under way. However, there are no efficacy results yet, ticagrelor is not the only agent tested, and bleeding risk, particularly intracranial hemorrhage, is a real concern.

**To proceed, the following is needed:**
- CAPTIVA results (expected after the January 2027 completion date), including the ticagrelor arm outcomes and intracerebral hemorrhage rates
- Results of the genotype-guided pilot study (NCT06714526)
- Confirmation of the current EU regulatory status, since the only listed authorization is cancelled, and the full SmPC warnings and contraindications
- Detailed mechanism of action data
- A bleeding-risk management plan, including review of interacting drugs such as clarithromycin and aspirin co-administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

