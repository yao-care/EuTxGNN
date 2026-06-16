---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Cardiovascular Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is an irreversible P2Y12 receptor antagonist originally used for preventing thrombotic events in acute coronary syndrome, percutaneous coronary intervention, and ischemic stroke.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (score 99.44%), with no dedicated clinical trials for this specific subtype but **16 publications** addressing the clopidogrel–aura migraine connection; when broadened to migraine disorder, **8 clinical trials** and **20 publications** substantially reinforce the mechanistic and clinical plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardiovascular thromboembolic prevention (ACS, PCI, ischemic stroke) — EU authorization data not captured in this dataset |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (observational studies + systematic review; no dedicated RCT for this subtype) |
| EU Market Status | Not in dataset (data gap — Clopidogrel / Plavix is known to hold EU authorizations) |
| Number of Authorizations | 0 (data gap) |
| Recommended Decision | Research Question → Proceed with Guardrails for PFO-positive subgroup |

---

## Why is This Prediction Reasonable?

Clopidogrel irreversibly inhibits the P2Y12 receptor on platelets, blocking ADP-mediated activation and aggregation. Critically, the P2Y12 receptor is not confined to platelets — it is also constitutively expressed on microglia in the central nervous system. This dual peripheral and central expression is the cornerstone of the repurposing hypothesis.

The mechanistic connection to migraine with brainstem aura operates through two complementary pathways. First, the **vascular-embolic pathway**: patients with patent foramen ovale (PFO) or atrial septal defect (ASD) have a cardiac right-to-left shunt. Activated platelets, microemboli, and vasoactive platelet-derived substances (serotonin, thromboxane A₂) bypass the pulmonary capillary filter and enter the cerebral circulation, where they are believed to trigger cortical spreading depression (CSD) — the electrophysiological event underlying migraine aura. Brainstem aura, once termed "basilar migraine," arises when CSD propagates into or originates from the posterior fossa, a region particularly vulnerable to embolic compromise of the posterior circulation. Clopidogrel, by suppressing platelet aggregation, reduces this embolic load. Second, the **neuroinflammatory pathway**: a 2019 animal study (PMID 31722730) demonstrated that P2Y12 receptors mediate microglial activation in the trigeminal nucleus caudalis (TNC) via the RhoA/ROCK signalling cascade. The TNC is the primary central relay for brainstem-mediated migraine pain; P2Y12 blockade in this structure may attenuate central sensitisation independent of the vascular mechanism.

The clinical signal already exists for the broader migraine-with-aura population. The CANOA Phase 4 RCT (NCT00799045, n=220) showed that adding clopidogrel to aspirin significantly reduced new-onset migraine attacks after transcatheter ASD closure (published in *JAMA* 2015 and *JAMA Cardiology* 2021). Because migraine with brainstem aura is a subtype of migraine with aura — sharing the same PFO-CSD mechanistic axis — extrapolation to this subtype is biologically coherent. The gap is the absence of a subtype-specific trial, which represents the key next step.

---

## Clinical Trial Evidence

*No clinical trials were found specifically for "migraine with brainstem aura." The trials below address migraine disorder broadly (rank 2 indication), and are directly mechanistically relevant to the brainstem aura subtype.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA trial: clopidogrel + aspirin vs aspirin alone after transcatheter ASD closure — significantly fewer new-onset migraine episodes in the combination arm (PMID 26551304, 32965476) |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | COMPETE trial: three-arm comparison of anticoagulation vs antiplatelet vs standard migraine therapy in PFO-positive migraineurs — results will define practice guidelines |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING trial: PFO closure vs pharmacotherapy (including antiplatelet agents) in migraine — clopidogrel is a core drug in the medical arm |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial directly testing clopidogrel for migraine with right-to-left shunt — primary outcome is migraine frequency reduction |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | High-risk PFO closure vs medical therapy (including clopidogrel) for migraine — multicentre prospective RCT |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelet therapy for secondary stroke prevention — migraine was a secondary outcome |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | GORE CARDIOFORM septal occluder for migraine relief — terminated due to insufficient enrolment; clopidogrel used as adjunct |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Comprehensive review of antithrombotic drugs (including clopidogrel) in migraine prevention — most current synthesis of the field |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA trial: clopidogrel + aspirin reduced new-onset migraine after ASD closure vs aspirin alone — strongest direct RCT evidence |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT (1-year follow-up) | JAMA Cardiology | CANOA 12-month results: migraine benefit sustained during clopidogrel treatment; effect partially reversed after discontinuation at 3 months |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Pilot randomised trial of clopidogrel as prophylactic treatment for migraine (without PFO restriction) — feasibility confirmed, trend toward benefit |
| [31722730](https://pubmed.ncbi.nlm.nih.gov/31722730/) | 2019 | Basic Science | J Neuroinflammation | P2Y12 receptor mediates microglial activation via RhoA/ROCK in the trigeminal nucleus caudalis in a chronic migraine mouse model — key mechanistic evidence for brainstem aura relevance |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort/Case Series | J Investigative Medicine | Clopidogrel 75 mg/day as add-on prophylaxis in drug-refractory migraine with PFO — significant reduction in attack frequency at 3 and 6 months |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational | Heart | Clopidogrel reduced migraine with aura following transcatheter closure of PFO and ASD — early clinical observation triggering the research hypothesis |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | Neurology | TRACTOR study: ticagrelor (another P2Y12 inhibitor) reduced migraine in PFO patients, supporting the class-level P2Y12 mechanism rather than clopidogrel-specific effects |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective | Neurology | Retrospective review of thienopyridine therapy (clopidogrel/prasugrel) in migraineurs with PFO — 65% of patients showed ≥50% reduction in attack frequency |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective | Cephalalgia | Clopidogrel as primary therapy for migraineurs with right-to-left shunt — mechanistic framing: platelet activation + paradoxical embolisation model |

---

## Safety Considerations

Please refer to the SmPC for safety information. Based on the Evidence Pack, formal warning, contraindication, and drug interaction data were not captured for this dataset.

> **Practical note for reviewers**: Clopidogrel carries well-established class-level risks including bleeding (including intracranial haemorrhage), thrombotic thrombocytopenic purpura (TTP), and CYP2C19 pharmacogenomic variability affecting antiplatelet efficacy. Any migraine repurposing protocol must include bleeding risk stratification and CYP2C19 genotyping guidance. One case report (PMID 38107217) also documented clopidogrel-associated inflammatory arthritis, warranting monitoring in longer-term use scenarios.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (PFO-positive migraine with aura subgroup) / Research Question (brainstem aura–specific subtype)**

**Rationale:**
The mechanistic hypothesis is well-grounded — P2Y12 blockade reduces platelet-driven CSD triggers via the PFO/right-to-left shunt pathway and independently attenuates neuroinflammation in the trigeminal nucleus caudalis. One completed Phase 4 RCT (CANOA, n=220, published in *JAMA*) already demonstrates that clopidogrel + aspirin prevents new-onset migraine after ASD closure, and two active Phase 3/4 trials (SPRING, COMPETE) will provide additional prospective data. The specific "brainstem aura" subtype lacks dedicated trial data, but given its shared pathophysiology with PFO-associated migraine with aura, the evidence base is directionally supportive and the gap is addressable.

**To proceed, the following is needed:**

- **MOA data completion**: Retrieve full DrugBank mechanism-of-action profile to formally document P2Y12 antagonism and off-target effects relevant to neuroinflammation
- **EU SmPC review**: Confirm current EU-authorised indications, contraindications, and warnings (Plavix/Iscover SmPC) — current dataset shows a data gap for EU regulatory status
- **PFO subgroup enrichment strategy**: Any prospective study should pre-specify PFO/ASD screening (contrast-enhanced TCD or TEE) to identify the enriched responder population
- **Brainstem aura–specific trial design**: Design a dedicated proof-of-concept RCT in migraine with brainstem aura + confirmed PFO, using clopidogrel 75 mg/day for 3–6 months, with ICHD-3 brainstem aura criteria as the primary eligibility criterion
- **CYP2C19 pharmacogenomic protocol**: Include genotyping to address the well-known variability in clopidogrel bioactivation, which may explain heterogeneity in prior observational studies
- **Await COMPETE trial results** (NCT05546320, n=1,000, expected completion June 2025): these data will directly compare antiplatelet vs anticoagulant vs standard migraine therapy and should inform the positioning of clopidogrel in the treatment algorithm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

