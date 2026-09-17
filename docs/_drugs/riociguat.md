---
layout: default
title: Riociguat
parent: High Evidence (L1-L2)
nav_order: 507
evidence_level: L1
indication_count: 10
---

# Riociguat
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

Using the drug-repurposing report template to produce the evaluation for Riociguat.

Note on indication selection: the evidence pack's own annotations flag the raw top-5 TxGNN hits (Ambras hypertrichosis, odontal malformation syndrome, Dandy-Walker syndrome, hair-shaft abnormality, isolated hypertrichosis) as "embedding-space noise" with no mechanistic link and zero clinical/literature support (all L5/Hold). I selected the highest-quality, evidence-triaged candidate instead — **pulmonary arterial hypertension associated with connective tissue disease (CTD-PAH)**, rank 9, which carries L1 evidence and a "Proceed with Guardrails" recommendation from the pack's own scoring — because reporting the raw #1 hit would be clinically misleading.

---

# Riociguat: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease

## One-Sentence Summary

> Riociguat is a soluble guanylate cyclase (sGC) stimulator originally used for pulmonary arterial hypertension (PAH) and chronic thromboembolic pulmonary hypertension.
> The evidence-triaged TxGNN analysis supports extending its use to **PAH associated with connective tissue disease (CTD-PAH)**, a recognized WHO Group 1 PAH subtype,
> with a dedicated Phase 3 subgroup analysis (PATENT-1/2) and **12 supporting publications** currently backing this direction. No dedicated CTD-PAH interventional trial (with registered NCT number) currently exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the regulatory data provided (0 licenses on file); trial context indicates riociguat is an approved sGC stimulator for pulmonary arterial hypertension |
| Predicted New Indication | Pulmonary arterial hypertension associated with connective tissue disease (CTD-PAH) |
| TxGNN Prediction Score | 91.55% |
| Evidence Level | L1 |
| EU Market Status | Not marketed (per available regulatory data) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data was not available in the regulatory record (flagged as a blocking data gap). However, the supporting evidence in this pack consistently describes riociguat as an sGC stimulator acting on the sGC–cGMP vasodilatory pathway — the same mechanism underlying its established efficacy in idiopathic/heritable PAH, as demonstrated in the pivotal PATENT-1 (Phase 3, randomized, double-blind, placebo-controlled) and PATENT-2 (long-term open-label extension) trials.

CTD-PAH is classified as a WHO Group 1 PAH subtype, sharing the same underlying pulmonary vascular remodeling pathophysiology as idiopathic PAH. Because PATENT-1/2 pre-specified CTD-PAH as a subgroup, dedicated subgroup efficacy and safety data already exist (Humbert et al., *Ann Rheum Dis* 2017), directly supporting mechanistic and clinical plausibility rather than relying on TxGNN embedding similarity alone.

A second candidate identified through the same evidence-triage process — PAH associated with congenital heart disease (CHD-PAH, rank 6) — is also a WHO Group 1 subtype with L1-level PATENT subgroup evidence (Rosenkranz et al., *Heart* 2015), reinforcing that riociguat's mechanism generalizes reasonably across Group 1 PAH etiologies. By contrast, the raw top-5 TxGNN outputs (hypertrichosis syndromes, dental/periodontal malformation syndrome, Dandy-Walker malformation) have no plausible vascular mechanism, no clinical trials, and largely disease-cluster/topic-overlap literature unrelated to riociguat — these were excluded from further consideration despite higher raw model scores.

## Clinical Trial Evidence

Currently no dedicated interventional clinical trials registered specifically for CTD-PAH with riociguat as the primary study drug (all supporting clinical data derive from the pre-specified PATENT-1/2 subgroup analysis, documented as literature below rather than as a distinct registered trial).

*For reference, the mechanistically related CHD-PAH subtype (rank 6) has one ongoing Phase 4 trial:*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07356778](https://clinicaltrials.gov/study/NCT07356778) | Phase 4 | Recruiting | 36 | Sotatercept add-on vs. standard PAH pulmonary vasodilator therapy (riociguat as background/comparator therapy) in adults with PAH from unrepaired congenital shunts, including Eisenmenger syndrome |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27457511](https://pubmed.ncbi.nlm.nih.gov/27457511/) | 2017 | RCT (subgroup analysis) | Ann Rheum Dis | PATENT-1/2 prospective subgroup analysis: efficacy and safety of riociguat specifically in PAH-CTD patients |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review / Meta-analysis | Intern Emerg Med | Meta-analysis of RCTs (incl. riociguat) in CTD-PAH: functional class, survival, 6MWD outcomes |
| [28671485](https://pubmed.ncbi.nlm.nih.gov/28671485/) | 2017 | Cohort (open-label switch) | Pulm Circ | Case series switching PDE-5 inhibitor to riociguat in CTD-PAH (incl. systemic sclerosis) patients |
| [40331647](https://pubmed.ncbi.nlm.nih.gov/40331647/) | 2025 | Cohort (prospective observation) | Kardiologiia | Long-term survival analysis in PAH associated with immune-mediated rheumatic disease, including riociguat-treated patients |
| [33131480](https://pubmed.ncbi.nlm.nih.gov/33131480/) | 2020 | Review | Kardiologiia | Role of riociguat in treatment of PAH associated with systemic connective tissue diseases |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of CTD-associated PAH, including sGC stimulator class |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General diagnosis/treatment review of PAH, contextualizing sGC-stimulator class |
| [27941129](https://pubmed.ncbi.nlm.nih.gov/27941129/) | 2017 | Guideline | Ann Rheum Dis | EULAR recommendations for systemic sclerosis treatment, incl. PAH management |
| [40592721](https://pubmed.ncbi.nlm.nih.gov/40592721/) | 2025 | Review | RMD Open | New horizons in systemic sclerosis treatment, including PAH-directed therapy |
| [39985455](https://pubmed.ncbi.nlm.nih.gov/39985455/) | 2025 | Preclinical | Rheumatology (Oxford) | Characterization of avenciguat, a novel sGC activator (successor class to riociguat) with antifibrotic effects in SSc preclinical models |

## EU Market Information

No marketing authorization records are present in the regulatory data provided (0 licenses; market status: not marketed). Real-world regulatory context indicates riociguat is approved elsewhere as Adempas® for PAH and CTEPH, but this could not be independently confirmed from the supplied evidence pack.

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (flagged as a blocking data gap — DG001).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CTD-PAH is a WHO Group 1 PAH subtype with a pre-specified, Phase 3 pivotal-trial subgroup analysis (PATENT-1/2) directly supporting riociguat's efficacy and safety, giving this prediction L1-level evidence — substantially stronger than the raw TxGNN top-ranked outputs, which lack any mechanistic or clinical support. However, this remains subgroup-level evidence rather than a dedicated primary indication trial, and critical safety/regulatory data gaps remain unresolved.

**To proceed, the following is needed:**
- TFDA/EMA SmPC warnings, contraindications, and DDI data (currently blocking — DG001)
- Formal, structured mechanism-of-action documentation from DrugBank (currently high-severity gap — DG002)
- Consideration of a dedicated CTD-PAH interventional trial (current evidence is a pre-specified subgroup analysis, not a primary-endpoint trial for this indication)
- Regulatory confirmation of riociguat's EU marketing/authorization status, which could not be verified from the supplied data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

