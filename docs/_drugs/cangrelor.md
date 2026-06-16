---
layout: default
title: Cangrelor
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Cangrelor
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

# Cangrelor: From PCI Antiplatelet Support to Myocardial Infarction

## One-Sentence Summary

Cangrelor (DB06441) is an intravenous P2Y12 receptor antagonist used as adjunct antiplatelet therapy during percutaneous coronary intervention (PCI), and is not currently approved or marketed in Taiwan.
The TxGNN model predicts it may be effective for **Myocardial Infarction** — the second-ranked prediction and strongest repurposing signal — with **25+ clinical trials** and **19 publications** supporting this direction, including the pivotal Phase 3 CHAMPION PHOENIX RCT (n=11,145).
The top-ranked TxGNN prediction (hemoglobinopathy) lacks mechanistic support and is assessed as a likely knowledge-graph topology false positive; this report focuses on myocardial infarction as the primary clinically actionable finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | PCI adjunct antiplatelet therapy (inferred from trial evidence; TFDA package insert data not available) |
| Predicted New Indication | Myocardial Infarction |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the DrugBank record is not available (Data Gap DG002). Based on information extracted from clinical trial descriptions and the prediction rationale in this evidence pack, cangrelor is a direct-acting, fully reversible intravenous antagonist of the platelet P2Y12 ADP receptor. Unlike oral P2Y12 inhibitors (clopidogrel, prasugrel, ticagrelor), cangrelor achieves near-complete platelet inhibition within 2 minutes of intravenous infusion and platelet function returns to baseline within 60 minutes of discontinuation — a pharmacokinetic profile uniquely suited for the urgent, time-sensitive procedural environment of acute myocardial infarction.

Myocardial infarction (MI) treatment centers on rapid restoration of coronary perfusion via primary PCI, while simultaneously preventing acute re-occlusion through potent antiplatelet suppression. During PCI, arterial injury, stent deployment, and plaque disruption all trigger ADP-dependent platelet activation — the exact pathway that cangrelor blocks. Critically, oral P2Y12 inhibitors are unreliable in AMI patients with cardiogenic shock, cardiac arrest, or mechanical ventilation because gastrointestinal absorption is impaired or impossible, creating a dangerous window of inadequate platelet inhibition during the highest-risk procedural moments. Cangrelor's intravenous route completely bypasses this limitation.

The mechanistic connection is therefore direct, well-characterized, and clinically validated: cangrelor's P2Y12 blockade is precisely the pharmacological target required to prevent periprocedural platelet-mediated stent thrombosis and major adverse cardiovascular events (MACE) in AMI patients. This is the hypothesis evaluated in the landmark CHAMPION PHOENIX trial (n=11,145), which forms the cornerstone of the drug's regulatory approvals in the US and EU. In Taiwan, where cangrelor is not yet approved, this evidence base supports a formal NDA submission pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01156571](https://clinicaltrials.gov/study/NCT01156571) | Phase 3 | Completed | 11,145 | CHAMPION PHOENIX: cangrelor vs. clopidogrel in patients requiring PCI (including AMI); demonstrated superiority in reducing 48-hour composite of death, MI, ischemia-driven revascularization, and stent thrombosis — the pivotal trial underpinning FDA/EMA approvals |
| [NCT03551964](https://clinicaltrials.gov/study/NCT03551964) | Phase 4 | Completed | 605 | DAPT-SHOCK-AMI: randomized, double-blind trial of IV cangrelor vs. crushed oral ticagrelor in AMI complicated by initial cardiogenic shock undergoing primary PCI; assessed onset rate and depth of platelet inhibition in this hemodynamically unstable population |
| [NCT04611607](https://clinicaltrials.gov/study/NCT04611607) | N/A | Completed | 303 | Registry of cangrelor in very high-risk AMI patients undergoing PCI who are unable to swallow tablets (post-CPR, ventilated, or cardiogenic shock); characterizes real-world efficacy and safety beyond pivotal trial conditions |
| [NCT04076813](https://clinicaltrials.gov/study/NCT04076813) | N/A | Active, not recruiting | 5,050 | CAMEO Registry: large multicenter real-world registry evaluating optimal platelet inhibition strategies in MI patients prior to coronary angiography or CABG; complements RCT data with effectiveness and safety in routine clinical practice |
| [NCT04471870](https://clinicaltrials.gov/study/NCT04471870) | N/A | Completed | 1,005 | Post-authorisation safety study (PASS) in ACS patients undergoing PCI; prospective cohort evaluating safety of cangrelor-to-oral P2Y12 inhibitor (clopidogrel, prasugrel, ticagrelor) transition in real-world practice |
| [NCT04927949](https://clinicaltrials.gov/study/NCT04927949) | Phase 4 | Completed | 128 | Adding cangrelor to ticagrelor in primary PCI patients with high on-ticagrelor platelet reactivity vs. ticagrelor alone; evaluated impact on myocardial reperfusion quality and residual thrombotic burden |
| [NCT02978040](https://clinicaltrials.gov/study/NCT02978040) | Phase 4 | Completed | 122 | FABOLUS FASTER: cangrelor vs. tirofiban vs. chewed/intact prasugrel in STEMI patients undergoing primary PCI; head-to-head comparison of speed and magnitude of platelet inhibition at the time of intervention |
| [NCT03273075](https://clinicaltrials.gov/study/NCT03273075) | Phase 4 | Unknown | 60 | PK/PD study of cangrelor vs. standard DAPT in STEMI patients post-out-of-hospital cardiac arrest on targeted temperature management; therapeutic hypothermia markedly impairs oral drug absorption, making IV cangrelor the pharmacologically logical choice |
| [NCT04251039](https://clinicaltrials.gov/study/NCT04251039) | N/A | Unknown | 550 | RESPONSE Study: prospective observational multicenter registry of cangrelor in stable coronary artery disease (SCAD) patients undergoing complex PCI; evaluates efficacy/safety in elective complex interventions |
| [NCT06792643](https://clinicaltrials.gov/study/NCT06792643) | Phase 2 | Recruiting | 50 | SURVIVE trial: cangrelor on top of bivalirudin anticoagulation in AMI-related cardiogenic shock/cardiac arrest patients requiring VA-ECMO support; dose-adjusted platelet function-guided protocol to balance bleeding and thrombosis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38625596](https://pubmed.ncbi.nlm.nih.gov/38625596/) | 2024 | Systematic Review & Meta-analysis | Egyptian Heart Journal | Pooled analysis of cangrelor vs. ticagrelor in STEMI undergoing PCI; comparative efficacy and safety across multiple RCTs |
| [38742915](https://pubmed.ncbi.nlm.nih.gov/38742915/) | 2024 | RCT | Circulation | PITRI Trial: cangrelor administered at reperfusion in STEMI patients — randomized evaluation of infarct size reduction and prevention of microvascular obstruction vs. oral ticagrelor |
| [40760769](https://pubmed.ncbi.nlm.nih.gov/40760769/) | 2025 | Cohort Study | Catheterization and Cardiovascular Interventions | Safety and efficacy of cangrelor in AMI-related cardiogenic shock with and without cardiac arrest; demonstrates clinical utility specifically where oral P2Y12 inhibitor absorption is compromised |
| [39432252](https://pubmed.ncbi.nlm.nih.gov/39432252/) | 2024 | RCT Protocol | EuroIntervention | DAPT-SHOCK-AMI trial design and rationale; articulates why cangrelor's pharmacokinetic profile makes it the optimal P2Y12 inhibitor for cardiogenic shock AMI |
| [37995040](https://pubmed.ncbi.nlm.nih.gov/37995040/) | 2024 | Network Meta-analysis | American Journal of Cardiovascular Drugs | Cangrelor safety and efficacy in ACS: network meta-analysis comparing cangrelor vs. oral P2Y12 inhibitors, clopidogrel, and placebo across the ACS spectrum |
| [32860058](https://pubmed.ncbi.nlm.nih.gov/32860058/) | 2021 | Clinical Practice Guideline | European Heart Journal | 2020 ESC Guidelines for NSTE-ACS management; includes class recommendations for antiplatelet therapy strategies during PCI, providing regulatory and clinical context for cangrelor use |
| [30933619](https://pubmed.ncbi.nlm.nih.gov/30933619/) | 2019 | Meta-analysis | Circulation | Cangrelor for STEMI: comparative outcomes data synthesis for ST-elevation MI patients, supporting evidence base for this high-risk subgroup |
| [40470562](https://pubmed.ncbi.nlm.nih.gov/40470562/) | 2025 | Review | Eur Heart J Cardiovascular Pharmacotherapy | Current role of cangrelor in acute and high-risk PCI settings; comprehensive review covering STEMI, cardiogenic shock, cardiac arrest, and bridging scenarios |
| [35621210](https://pubmed.ncbi.nlm.nih.gov/35621210/) | 2022 | Real-World Registry | Journal of the American Heart Association | CAMEO Registry initial results: cangrelor use patterns and transition to oral P2Y12 inhibitors in MI patients across US clinical practice sites; characterizes real-world utilization |
| [26320110](https://pubmed.ncbi.nlm.nih.gov/26320110/) | 2016 | Clinical Practice Guideline | European Heart Journal | 2015 ESC Guidelines for NSTE-ACS; established the foundational framework for P2Y12 inhibitor selection in ACS patients that cangrelor subsequently augmented |

---

## Taiwan Market Authorization Status

Cangrelor is **not approved or marketed in Taiwan** (0 regulatory licenses on record). No Taiwan-registered pharmaceutical products exist for this drug.

> Based on the clinical trial data in this evidence pack — multiple trials conducted at European and US centers, and references to EMA post-authorisation studies — cangrelor holds regulatory approvals in Western markets (branded as Kengrexal in the EU; Kengreal in the US) for use as adjunct antiplatelet therapy during PCI. Taiwan market entry would require a full NDA submission to the TFDA, including local pharmacovigilance planning.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Data Gap Alert:** TFDA package insert warnings and contraindications were not available at the time of this assessment (Data Gap DG001 — Blocking severity). A formal safety review against the local SmPC/package insert is required before any clinical or regulatory steps. Based on the drug class, clinicians should expect considerations around **bleeding risk** (as with all antiplatelet agents), management of the **cangrelor-to-oral P2Y12 inhibitor transition window** (incorrect sequencing can lead to platelet receptor competition and inadequate coverage), and use in patients with **active pathological bleeding** or those at high bleeding risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cangrelor has robust, replicated Phase 3/4 RCT evidence for myocardial infarction management during PCI — including the CHAMPION PHOENIX pivotal trial (n=11,145), multiple Phase 4 studies in high-risk subgroups (cardiogenic shock, cardiac arrest, intubated patients), and a large real-world registry (CAMEO, n=5,050). The pharmacological mechanism is direct, well-characterized, and matches the clinical need precisely. The absence of Taiwan approval represents an unmet market need rather than an evidence gap, as regulatory approvals in the US and EU confirm the drug's established safety-efficacy profile.

**To proceed, the following is needed:**

- **TFDA package insert (仿單) review** for Taiwan-specific safety warnings and contraindications (Data Gap DG001 — Blocking; must be resolved before S1 safety evaluation)
- **Formal MOA documentation** from DrugBank API (Data Gap DG002 — High; required for mechanistic dossier)
- **TFDA NDA submission feasibility assessment**: determine if a bridging study is required or if the CHAMPION PHOENIX and Phase 4 evidence package is sufficient for a reference-country-based approval pathway
- **Local market analysis**: Taiwan-specific comparison against currently approved P2Y12 inhibitors (clopidogrel, ticagrelor, prasugrel) and assessment of catheterization laboratory adoption readiness
- **Pharmacoeconomic evaluation**: cost-effectiveness modeling for cangrelor in Taiwanese AMI/PCI patients under NHI reimbursement framework
- **Transition protocol validation**: confirm institutional protocols for cangrelor-to-oral-agent handoff are in place at target catheterization centers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

