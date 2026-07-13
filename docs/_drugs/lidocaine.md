---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Conjunctival Disorder

## One-Sentence Summary

Lidocaine is a classic sodium channel blocker universally established as a local anesthetic and Class Ib antiarrhythmic agent.
The TxGNN model predicts applications across a spectrum of ophthalmic conditions; **Conjunctival Disorder** carries the strongest evidence base among the top 10 predictions, supported by **17 clinical trials** and **20 publications**, earning Evidence Level L2 and a "Proceed with Guardrails" recommendation.
Note: The highest-ranked TxGNN prediction (punctate epithelial keratoconjunctivitis, 99.99%) has zero supporting trials or literature (L5), making conjunctival disorder the operationally actionable focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (no market authorization data) |
| Predicted New Indication | Conjunctival Disorder (Best-evidence prediction; TxGNN Rank #6) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Lidocaine is a voltage-gated Na⁺ channel blocker that reversibly prevents action potential initiation and propagation in neuronal membranes. This mechanism underpins both its local anesthetic effect at peripheral nerve endings and its membrane-stabilizing antiarrhythmic effect — and both pathways are relevant to conjunctival disorders.

Two mechanistically distinct rationales support this prediction. First, **topical surface anesthesia**: lidocaine gel and drop formulations already have extensive clinical use anesthetizing the conjunctival surface before ocular surgery (pterygium excision, intravitreal injections, cataract surgery). This establishes both tolerability and bioavailability at the target tissue. Second, **neurogenic conjunctival inflammation**: intravenous lidocaine has been explored for SUNCT/SUNA syndrome — Short-lasting Unilateral Neuralgiform Headache attacks with Conjunctival injection and Tearing — where membrane stabilization suppresses trigeminal nerve depolarization responsible for the characteristic conjunctival injection and lacrimation.

The TxGNN knowledge graph likely captures this dual mechanistic overlap. The procedural anesthesia pathway is backed by Phase 4 trial evidence, while the SUNCT/SUNA pathway adds a genuine therapeutic repurposing angle with prospective clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine Ophtesic Gel vs. subconjunctival xylocaine injection for pterygium excision — direct head-to-head of two lidocaine-based formulations for conjunctival surgery |
| [NCT02324166](https://clinicaltrials.gov/study/NCT02324166) | Phase 4 | Unknown | 54 | Cefazolin-Lidocaine solution reduces pain from subconjunctival antibiotic injection in vitreoretinal surgery — direct conjunctival lidocaine application |
| [NCT01087489](https://clinicaltrials.gov/study/NCT01087489) | N/A | Completed | 53 | 4% lidocaine drops vs. 3.5% lidocaine HCl ophthalmic gel for intravitreal injection comfort — comparing two topical conjunctival formulations |
| [NCT02150460](https://clinicaltrials.gov/study/NCT02150460) | Phase 4 | Completed | 100 | Single vs. double-injection peribulbar anaesthesia (lidocaine) for cataract surgery — double-blind RCT validating lidocaine in ocular regional anesthesia |
| [NCT03397069](https://clinicaltrials.gov/study/NCT03397069) | N/A | Completed | 90 | Midazolam adjunct to lidocaine peribulbar block — RCT evaluating block duration and safety for ophthalmic procedures |
| [NCT03189329](https://clinicaltrials.gov/study/NCT03189329) | Phase 4 | Completed | 66 | Retrobulbar block with lidocaine vs. levobupivacaine in vitreoretinal surgery — cerebral oxygen saturation and early postoperative cognitive safety |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye (London) | Lidocaine 2% gel vs. tetracaine 1% drops as sole topical anesthetic for primary pterygium surgery — RCT showing comparable efficacy |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical Study | Acta Ophthalmol Scand | Lidocaine 2% gel effective as sole topical anesthetic for pterygium surgery — conjunctival surface application validated |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical Study | Ophthalmologica | Viscous lidocaine 2% gel provides effective post-pterygium surgical pain relief — direct topical conjunctival application |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective + Meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT/SUNA (headache with conjunctival injection) — open-label study with single-arm meta-analysis; IV lidocaine among evaluated therapies |
| [10696746](https://pubmed.ncbi.nlm.nih.gov/10696746/) | 2000 | Clinical Study | Retina | Topical lidocaine evaluated as alternative to peribulbar/retrobulbar anesthesia for posterior vitrectomy |
| [23330822](https://pubmed.ncbi.nlm.nih.gov/23330822/) | 2013 | Case Series / Clinical Study | Curr Eye Res | Anesthetic options including lidocaine for pain management during intravitreal injections — efficacy and tolerability comparison |
| [34003160](https://pubmed.ncbi.nlm.nih.gov/34003160/) | 2021 | Review | Neurology India | SUNCT and SUNA update — summarizes IV lidocaine as acute rescue therapy; conjunctival injection is a defining diagnostic feature |
| [12828881](https://pubmed.ncbi.nlm.nih.gov/12828881/) | 2003 | Review | Curr Pain Headache Rep | SUNCT syndrome clinical review in 50 patients — conjunctival injection as hallmark symptom; lidocaine among treatment strategies discussed |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Basic Science | JCI Insight | Nerve-goblet cell association promotes allergic conjunctivitis via rapid antigen passage — identifies neurogenic pathway potentially amenable to Na⁺ channel blockade |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review (Safety) | Cephalalgia | Neuropsychiatric and cardiac side-effects of IV lidocaine in 20 patients — key safety reference for systemic repurposing scenarios |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 4 trials confirm that lidocaine gel, drops, and peribulbar/retrobulbar injectable formulations are safe and effective for conjunctival surface applications in ophthalmology. The SUNCT/SUNA literature adds a genuine therapeutic repurposing angle — IV lidocaine has prospective open-label data for a condition defined by conjunctival injection and tearing. The L2 evidence classification reflects this combined support, though the majority of current evidence is for procedural anesthesia rather than disease-modifying treatment of conjunctival pathology.

**To proceed, the following is needed:**
- Identify the specific target indication within "conjunctival disorder" (procedural analgesia vs. SUNCT/SUNA vs. neurogenic/allergic conjunctivitis) — each requires a different formulation strategy and evidence pathway
- Obtain Taiwan TFDA safety data (SmPC / package insert) — currently a blocking data gap that prevents S1 safety screening
- Query DrugBank API to formally document the mechanism of action
- Assess risk of corneal epithelial toxicity with prolonged topical use — long-term local anesthetic application is a known concern
- Design a protocol that clearly distinguishes the proposed therapeutic use from already-established procedural anesthesia use to justify a new repurposing claim
- Determine the administration route based on target indication: topical gel for surface conditions, IV infusion for SUNCT/SUNA, or subconjunctival injection for localized disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

