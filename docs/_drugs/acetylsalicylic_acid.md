---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Acetylsalicylic Acid
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

# Acetylsalicylic Acid (Aspirin): From Pain and Cardiovascular Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (Aspirin, DB00945) is a widely used analgesic, antipyretic, anti-inflammatory, and antiplatelet agent with established roles in cardiovascular event prevention, though no formal indication records were retrieved in the current dataset.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a high-risk migraine subtype associated with elevated cerebrovascular risk —
with **0 registered clinical trials** but **19 publications** currently supporting this direction, including a 2025 systematic review and a retrospective cohort study directly evaluating ASA in migraine-with-aura prophylaxis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal indication data in current dataset |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed MOA data is not available in the current dataset. Based on established pharmacology, Aspirin irreversibly inhibits COX-1 (and to a lesser extent COX-2) in platelets, permanently blocking synthesis of thromboxane A2 (TXA2) — a potent platelet activator and vasoconstrictor — for the entire 7–10 day platelet lifespan. At low doses, this antiplatelet effect is achieved while largely preserving prostacyclin (PGI2) production in the vascular endothelium, theoretically maintaining a vasodilatory counterbalance.

Migraine with brainstem aura (MBA), formerly known as "basilar-type migraine," is a rare subtype characterized by fully reversible brainstem symptoms (vertigo, dysarthria, diplopia, ataxia) followed by headache. The leading pathophysiological mechanism is cortical spreading depression (CSD) originating in posterior cortex or brainstem, with emerging evidence that microembolism and platelet activation may trigger CSD episodes. MBA carries significantly elevated stroke risk, which provides a mechanistic rationale for antiplatelet intervention: by suppressing TXA2-mediated platelet aggregation, Aspirin may reduce the frequency of microembolic events that seed CSD initiation, while its anti-inflammatory effect on prostaglandin pathways may further dampen neuroinflammation during the aura phase.

Supporting this rationale, a 2025 systematic review (*Headache*, PMID 39989443) specifically investigated antithrombotic drugs — including Aspirin — as migraine preventive agents. A 2014 retrospective cohort study (*Current Health Sciences Journal*, PMID 25729594) evaluated low-dose Aspirin in 95 patients with migraine with aura at a university headache centre, comparing it against standard prophylactic therapies over at least 4 months. The antiplatelet hypothesis is further reinforced by a 2005 report showing that clopidogrel (another antiplatelet agent) reduced migraine with aura episodes after cardiac shunt closure (PMID 16103551), suggesting a shared antiplatelet mechanism may be genuinely protective in this patient group.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registering acetylsalicylic acid as an intervention for migraine with brainstem aura have been identified in ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Explored available evidence on antithrombotic drugs (including ASA) as migraine preventive medication; most direct and recent synthesis of evidence |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | Current Health Sciences Journal | 95 migraine-with-aura patients treated with low-dose ASA vs other prophylactics for ≥4 months; evaluated efficacy and tolerability |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Guideline / Evidence Review | Headache | AHS updated evidence assessment of acute migraine pharmacotherapies; ASA included as evidence-based option |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | Double-blind multicenter RCT (n=278): IV lysine ASA (1 g) vs sumatriptan 6 mg sc vs placebo in acute migraine with or without aura |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Comprehensive overview of migraine with aura: CSD as core mechanism, ICHD-III diagnostic criteria, epidemiology |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Compares pathophysiology, epidemiology, and clinical management implications between migraine with and without aura |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Clinical Guideline | FP Essentials | AHA/ASA stroke primary prevention guidelines; recommends ASA in high-risk groups, including migraine-with-aura patients given their elevated stroke risk |
| [15891416](https://pubmed.ncbi.nlm.nih.gov/15891416/) | 2005 | Review | Current Opinion in Neurology | Explores the mechanistic triangle of patent foramen ovale, cryptogenic stroke, and migraine with aura — supports antiplatelet intervention rationale |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Case Series | Heart (BCS) | Clopidogrel reduced migraine with aura after transcatheter shunt closure; supports the hypothesis that antiplatelet agents benefit this migraine subtype |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Treatment landscape of acute migraine; confirms ASA and caffeine-containing analgesics as first-line options for mild-to-moderate attacks |

---

## Safety Considerations

Please refer to the TFDA SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aspirin's antiplatelet and anti-inflammatory mechanism is biologically plausible for migraine with brainstem aura — a high-stroke-risk subtype where platelet-mediated microembolism may trigger cortical spreading depression — and is supported by a 2025 systematic review and a retrospective cohort study directly examining this approach. However, no prospective controlled trial has been registered for this specific indication, and the TFDA safety data profile is currently unverified, warranting a structured research pathway rather than immediate broad adoption.

**To proceed, the following is needed:**

- Design and registration of a prospective controlled trial specifically in migraine with brainstem aura (prophylaxis endpoint), distinguishing from acute treatment
- Retrieval and review of the TFDA SmPC (or equivalent regulatory document) for formal contraindications and warnings — currently a blocking data gap
- Formal MOA documentation from DrugBank API to complete the mechanistic rationale section
- Dose regimen definition: low-dose prophylaxis (75–100 mg/day) versus acute IV formulation requires separate trial arms
- Stroke risk stratification protocol for the MBA population, given the elevated cerebrovascular risk profile of this subtype
- Review of the 2025 systematic review (PMID 39989443) findings in full to assess whether any formal recommendations were made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

