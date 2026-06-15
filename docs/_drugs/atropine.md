---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Atropine
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

# Atropine: From Bradycardia Treatment to Migraine Disorder

## One-Sentence Summary

Atropine is a classic muscarinic receptor antagonist used clinically for bradycardia, organophosphate poisoning, and pre-operative antisialagogue preparation; it is currently not registered in Taiwan with no available domestic regulatory data.
The TxGNN model predicts it may be effective for **Migraine Disorder** (prediction score 99.56%), supported by **0 registered clinical trials** and **13 publications** — predominantly animal models and mechanistic studies.
A critically important secondary finding: the related indication **Headache Disorder** (rank #8, specifically **post-dural puncture headache**) is backed by a **completed Phase 3 RCT** and two additional RCTs, elevating that pathway to **Evidence Level L2** with a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (not registered in Taiwan; known for bradycardia, organophosphate poisoning, pre-operative use) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (Migraine Disorder) / L2 (Headache Disorder — PDPH) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine is a competitive, non-selective antagonist of muscarinic acetylcholine receptors (M1–M5), with pronounced effects at M2 (cardiac SA node → tachycardia), M3 (glands, smooth muscle, pupil → reduced secretions, relaxation, mydriasis), and M1 (CNS and ganglia). Detailed mechanism-of-action data is not available in the current evidence pack. Based on established pharmacology, atropine blocks parasympathetic neurotransmission broadly, and this property forms the core rationale for its potential role in headache disorders.

The parasympathetic nervous system plays an increasingly recognized role in migraine pathophysiology. A 2024 animal study (PMID 36485173) demonstrated that muscarinic receptor activation promotes meningeal mast cell degranulation, triggering CGRP and histamine release that drives dural vasodilation — a central event in migraine pathogenesis. Atropine's M1/M3 blockade could theoretically suppress this parasympathetically-driven neuroinflammatory cascade. Complementary evidence shows that stimulation of the intracranial parasympathetic pathway (sphenopalatine ganglion) directly induces plasma protein extravasation in rat dura mater (PMID 9344563), further implicating cholinergic drive as a trigger of neurogenic dural inflammation. The anti-migraine drug sumatriptan has also been shown to exert antinociception partly via atropine-reversible cholinergic pathways in rodents (PMID 8930196), suggesting that central muscarinic tone modulates descending pain signaling in headache states.

Despite this biologically plausible framework, all supporting data for primary migraine remains preclinical. No human clinical trial has directly tested atropine for migraine disorder. However, a mechanistically related secondary headache — post-dural puncture headache (PDPH) — provides important clinical proof of concept: neostigmine+atropine combinations have been evaluated in completed Phase 3 RCTs with positive outcomes, demonstrating that cholinergic modulation can effectively reduce headache in a neuraxial inflammation context. Whether this PDPH mechanism (cholinergic amplification of CSF acetylcholine via neostigmine, attenuated by atropine's antisecretory effects) translates to primary migraine pathophysiology remains an open scientific question.

---

## Clinical Trial Evidence

Currently **no clinical trials** testing atropine specifically for migraine disorder are registered on ClinicalTrials.gov or ICTRP.

For the related indication **Headache Disorder (Post-Dural Puncture Headache)** — which provides the strongest clinical evidence across all 10 predictions in this report — the following directly relevant trials were identified:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Double-blind RCT comparing nebulized dexmedetomidine vs nebulized neostigmine/atropine vs saline placebo for PDPH after cesarean section — currently the highest-level direct evidence for atropine in any headache indication |
| [NCT03997006](https://clinicaltrials.gov/study/NCT03997006) | Phase 4 | Completed | 60 | Prospective RCT: IV aminophylline vs IV neostigmine/atropine for treatment of established PDPH; directly evaluates comparative efficacy of the combination |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Prophylactic IV neostigmine+atropine vs ketorolac for prevention of PDPH in infraumbilical surgery; largest planned trial in this indication |
| [NCT06824025](https://clinicaltrials.gov/study/NCT06824025) | Early Phase 1 | Not yet recruiting | 111 | Nebulized neostigmine/atropine vs nebulized lignocaine for acute PDPH after subarachnoid block in parturients — evaluates inhaled delivery route |
| [NCT03587441](https://clinicaltrials.gov/study/NCT03587441) | Phase 4 | Completed | 240 | Intrathecal neostigmine adjuvant to bupivacaine to reduce PDPH incidence and severity after cesarean section |

---

## Literature Evidence

The following publications are most relevant to the **migraine disorder** indication (rank #1):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Mechanistic | Eur J Neurosci | Cholinergic activation promotes meningeal mast cell degranulation and CGRP/histamine release in a nitroglycerin migraine model; muscarinic antagonism suppresses this cascade — strongest direct mechanistic support |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Animal Study | Exp Neurol | Parasympathetic sphenopalatine ganglion stimulation causes dural plasma protein extravasation; establishes intracranial cholinergic drive as a trigger of neurogenic dural inflammation |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Animal Study | J Pharmacol Exp Ther | Sumatriptan antinociception is partly mediated by the central cholinergic system; atropine pretreatment reverses this effect, identifying M-receptor involvement in migraine pain modulation |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Case Series | Cephalalgia | Systemic atropine markedly reduced autonomic symptoms (sweating, tearing, nasal secretion) during chronic paroxysmal hemicrania attacks — direct clinical observation of atropine's antisympathetic effects in a headache context |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Mechanistic | Neurosci Lett | CGRP release from trigeminal afferents drives cranial blood flow changes in a migraine model; nicotinic-cholinergic interaction characterised as a potential upstream trigger |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacological review of anisodamine (atropine derivative with less CNS toxicity); establishes class-level anti-inflammatory and anticholinergic properties potentially applicable to neurological indications |

For **Headache Disorder (PDPH)**, the most clinically actionable literature:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [30169405](https://pubmed.ncbi.nlm.nih.gov/30169405/) | 2018 | RCT | Anesth Analg | First prospective RCT showing neostigmine+atropine added to conventional PDPH management significantly reduces headache severity — cornerstone clinical evidence for this combination |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiol | Nebulized neostigmine/atropine vs nebulized dexmedetomidine for PDPH after cesarean section; comparable efficacy, establishes inhaled route as viable delivery method |
| [37802666](https://pubmed.ncbi.nlm.nih.gov/37802666/) | 2023 | Case Report | Br J Anaesth | Reversible cerebral vasoconstriction syndrome (RCVS) following neostigmine+atropine administration for PDPH — critical safety signal that must inform any clinical development plan |

---

## Taiwan Market Information

Atropine is **not currently registered** in Taiwan. No product licensing data is available (0 authorizations). Please refer to international SmPC references (e.g., EMA or FDA labeling) for regulatory context.

---

## Safety Considerations

No Taiwan SmPC-based warnings or contraindications data is available in the current dataset.

The following safety signals were identified directly from the evidence collection:

- **RCVS Risk (Serious)**: A 2023 case report (PMID 37802666, *Br J Anaesth*) documents reversible cerebral vasoconstriction syndrome following IV neostigmine/atropine administration for PDPH — a serious cerebrovascular adverse event that must be addressed in any headache indication development plan
- **IOP Elevation**: Atropine-induced mydriasis (M3 blockade) can raise intraocular pressure in susceptible patients; studies in open-angle glaucoma confirm IOP elevation with atropine use (PMID 5640848, 39027062), making this a contraindication in those patients
- **Systemic Anticholinergic Toxicity**: Dose-dependent risk of tachycardia, dry mouth, urinary retention, blurred vision, and cognitive impairment — particularly significant in elderly patients or at doses exceeding the therapeutic window for neurological applications

Please refer to the SmPC for comprehensive contraindications, warnings, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For migraine disorder specifically, evidence is limited to animal models and in vitro mechanistic studies (L4); no human data exists. The biological rationale for parasympathetic blockade in migraine neuroinflammation is credible but unvalidated in humans. The RCVS safety signal from the PDPH context and the known IOP-raising risk add further caution. The post-dural puncture headache pathway (rank #8) is substantially more advanced — a completed Phase 3 RCT provides L2 evidence — but PDPH represents a mechanistically distinct secondary headache that cannot be assumed to share primary migraine biology.

**To proceed, the following is needed:**

- **PDPH indication (actionable now):** The completed Phase 3 RCT (NCT04910477) and two supporting RCTs provide sufficient basis to discuss a formal PDPH regulatory filing; this pathway should be separated from the migraine pathway and advanced independently with a safety monitoring protocol for RCVS
- **Primary migraine pathway (earlier stage):**
  - Obtain full drug SmPC (TFDA or EMA) to define contraindications relevant to neurological applications
  - Commission a human pharmacodynamic study measuring atropine's effect on plasma CGRP levels and cranial blood flow during experimental trigeminovascular activation
  - Systematically evaluate atropine derivatives (anisodamine, scopolamine) with better CNS safety profiles as candidate molecules for migraine
- **Safety monitoring requirements:** Any clinical protocol must include: (1) baseline and on-study IOP monitoring excluding patients with glaucoma risk; (2) neurovascular surveillance (TCD or MR angiography) for RCVS detection; (3) dose-finding study to define the anticholinergic-to-headache-therapeutic window
- **Route and formulation decision:** Define whether IV (for acute PDPH), inhaled/nebulized, or intranasal delivery is most appropriate for the target headache subtype, as systemic atropine exposure at neurologically active doses carries significant peripheral anticholinergic burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

