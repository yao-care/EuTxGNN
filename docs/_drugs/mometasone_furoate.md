---
layout: default
title: Mometasone Furoate
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Mometasone Furoate
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

# Mometasone Furoate: From Topical Corticosteroid Therapy to Sinonasal Polyp-Related Conditions

## One-Sentence Summary

Mometasone furoate is a topical corticosteroid; however, this evidence pack shows the drug is **not currently marketed in Taiwan or the EU**, and both the original approved indication and mechanism of action (MOA) are missing from the source data. TxGNN screened **10 candidate new indications** (all polyp/growth-related conditions), of which **8 have zero supporting evidence** (pure AI prediction) and only **2 — polyp of frontal sinus and polyp of middle ear — are backed by clinical trials and literature**, though one of these two appears to involve an ontology-mapping discrepancy that needs clarification before it can be treated as genuine repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available registrational data (no licenses on file; Mometasone furoate is a known topical corticosteroid class drug, but this specific approved indication is not confirmed in this evidence pack) |
| Predicted New Indications | 10 candidates evaluated; top TxGNN score: **2-hydroxyethyl methacrylate sensitization** (98.62%); highest-evidence candidate: **Polyp of frontal sinus** (97.56%) |
| TxGNN Prediction Score Range | 97.51% – 98.62% |
| Evidence Level | L2 (2 of 10 candidates) / L5 (8 of 10 candidates) |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacological class information, mometasone furoate is a synthetic **topical/intranasal glucocorticoid**, generally understood to suppress Th2-driven inflammation (IL-4/IL-5/IL-13 axis), reduce eosinophilic infiltration, and decrease mucosal edema — mechanisms well established for allergic rhinitis and chronic rhinosinusitis with nasal polyps (CRSwNP).

Among the 10 TxGNN-predicted indications, **8 are structurally or pathologically unrelated to corticosteroid anti-inflammatory action** (e.g., fibroepithelial polyp, neoplastic polyp, epulis, ureteral polyp) — these are largely mechanical, neoplastic, or reactive proliferative lesions rather than Th2-inflammation-driven conditions, and none have any clinical trial or literature support (L5, model prediction only).

The two candidates with actual evidence are both **anatomical subtypes/variants connected to chronic rhinosinusitis with nasal polyps**, a condition where mometasone's mechanism is already well validated:
- **Polyp of frontal sinus** has genuine device-specific evidence: mometasone-eluting bioabsorbable implants (PROPEL/Sinuva-class devices) placed directly in the frontal sinus ostium, which is a real drug-device repurposing pathway rather than simple mechanistic extrapolation.
- **Polyp of middle ear**, however, shows a likely **ontology mapping discrepancy** — the linked trials and literature substantively describe standard sinonasal CRSwNP (an already-approved indication for mometasone nasal spray), not the middle ear. This candidate should be treated as an artifact requiring MONDO/disease-mapping review before being counted as a true "new" indication.

---

## Clinical Trial Evidence

*(Combining evidence linked to "Polyp of frontal sinus" and "Polyp of middle ear" — the two candidates with any trial data; other 8 candidates have no registered trials)*

| Trial Number | Phase | Status | Enrollment | Indication (as mapped) | Key Findings |
|---------|------|------|------|------|---------|
| [NCT03607175](https://clinicaltrials.gov/study/NCT03607175) | Phase 2/3 | Unknown | 30 | Frontal sinus polyp | Steroid-eluting implant vs. triamcinolone-CMC foam for post-FESS nasal polyposis care |
| [NCT01616160](https://clinicaltrials.gov/study/NCT01616160) | Phase 4 | Terminated | 11 | Middle ear polyp (mapped)* | Steroid sensitivity of mometasone furoate nasal spray in nasal polyp tissue |
| [NCT04915456](https://clinicaltrials.gov/study/NCT04915456) | Phase 4 | Completed | 106 | Middle ear polyp (mapped)* | Postoperative topical steroid spray ± systemic steroid in CRSwNP |
| [NCT03280550](https://clinicaltrials.gov/study/NCT03280550) | Phase 3 | Completed | 138 | Middle ear polyp (mapped)* | Omalizumab (not mometasone) in CRSwNP — disease-relevant only |
| [NCT02898454](https://clinicaltrials.gov/study/NCT02898454) | Phase 3 | Completed | 448 | Frontal sinus polyp | Dupilumab add-on to mometasone furoate nasal spray background therapy in bilateral nasal polyps |
| [NCT02912468](https://clinicaltrials.gov/study/NCT02912468) | Phase 3 | Completed | 276 | Frontal sinus polyp | Dupilumab + mometasone background therapy, 24-week nasal polyposis study |
| [NCT03401229](https://clinicaltrials.gov/study/NCT03401229) | Phase 3 | Completed | 413 | Frontal sinus polyp | Benralizumab (not mometasone) in severe nasal polyposis — disease-relevant only |
| [NCT04851964](https://clinicaltrials.gov/study/NCT04851964) | Phase 3 | Completed | 416 | Frontal sinus polyp | Tezepelumab (not mometasone) in severe CRSwNP — disease-relevant only |
| [NCT05545072](https://clinicaltrials.gov/study/NCT05545072) | Phase 3 | Terminated | 5 | Frontal sinus polyp | Dupilumab + intranasal corticosteroid post-ESS in allergic fungal rhinosinusitis |
| [NCT04596189](https://clinicaltrials.gov/study/NCT04596189) | Phase 4 | Completed | 30 | Frontal sinus polyp | Dupilumab peri-operative use for CRSwNP recurrence prevention |

*\* Note: trials mapped to "polyp of middle ear" substantively describe nasal/sinus polyposis, not middle ear disease — likely an ontology mapping error (see rationale above).*

The remaining 8 predicted indications (HEMA sensitization, vocal cord polyp, external auditory canal polyp, fibroepithelial polyp, vulvar polyp, ureteral polyp, epulis, neoplastic polyp) currently have **no related clinical trials registered**.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29350840](https://pubmed.ncbi.nlm.nih.gov/29350840/) | 2018 | RCT (Phase 3) | Int Forum Allergy Rhinol | Mometasone furoate sinus implant significantly improves outcomes in recurrent nasal polyposis after sinus surgery |
| [27302143](https://pubmed.ncbi.nlm.nih.gov/27302143/) | 2016 | RCT | Am J Rhinol Allergy | Sodium hyaluronate added to topical corticosteroids improves CRSwNP outcomes |
| [33465455](https://pubmed.ncbi.nlm.nih.gov/33465455/) | 2021 | RCT | Ann Allergy Asthma Immunol | Dupilumab improves airway control in CRSwNP with comorbid asthma (mometasone as background therapy) |
| [27141307](https://pubmed.ncbi.nlm.nih.gov/27141307/) | 2016 | Review | Multidiscip Respir Med | Systematic review: intranasal mometasone furoate for rhinosinusitis, nasal polyposis, and middle-ear involvement of adenoidal hypertrophy |
| [30843454](https://pubmed.ncbi.nlm.nih.gov/30843454/) | 2019 | Review | J Manag Care Spec Pharm | Budget impact of mometasone-eluting steroid implant vs. sinus surgery for CRSwNP |
| [19289710](https://pubmed.ncbi.nlm.nih.gov/19289710/) | 2009 | Cohort | Arch Otolaryngol Head Neck Surg | Mometasone furoate prevents nasal polyp relapse after endoscopic sinus surgery |
| [31117809](https://pubmed.ncbi.nlm.nih.gov/31117809/) | 2019 | Cohort | Am J Rhinol Allergy | Pooled analysis: in-office mometasone sinus implants for recurrent nasal polyps |
| [35362251](https://pubmed.ncbi.nlm.nih.gov/35362251/) | 2022 | Cohort | Int Forum Allergy Rhinol | Intraoperative frontal sinus mometasone-eluting stents reduce IL-5/IL-13 in CRSwNP |
| [27758142](https://pubmed.ncbi.nlm.nih.gov/27758142/) | 2016 | Cohort | Expert Opin Drug Deliv | PROPEL mometasone-eluting mini sinus implant for frontal sinus disease |
| [30431709](https://pubmed.ncbi.nlm.nih.gov/30431709/) | 2019 | Cohort | Int Forum Allergy Rhinol | Pooled RCT analysis: bioabsorbable mometasone-releasing implants in frontal sinus ostia |

The remaining 8 predicted indications currently have **no related literature available**.

---

## EU Market Information

This drug bundle shows **0 EU/Taiwan marketing authorizations** on file — Mometasone furoate is not currently marketed under this evidence pack's regulatory dataset, so no license table can be produced.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> ⚠️ **Blocking data gap**: TFDA label warnings/contraindications (DG001) could not be retrieved, which prevents completion of the S1 safety screening stage for any of the 10 candidates. No drug-drug interaction data is currently available (query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This drug is not marketed in Taiwan or the EU, its original indication and mechanism of action are undocumented in this evidence pack, and a **Blocking-severity safety data gap** (missing TFDA label) prevents even a preliminary safety screen (S1). Of the 10 TxGNN-predicted indications, 8 have no clinical or literature support at all (L5, decision stage S0), and the 2 with evidence (L2, S2, "Research Question") require further verification — one due to a likely disease-ontology mapping error, and both because the identified evidence largely concerns a different, already-approved indication (CRSwNP) or a different drug (biologics used alongside mometasone as background therapy) rather than mometasone-specific efficacy in a genuinely new indication.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA SmPC for warnings, contraindications, and DDI data (resolves DG001, currently Blocking)
- Retrieve confirmed MOA and original approved indication from DrugBank (resolves DG002)
- Clarify MONDO/ontology mapping for "polyp of middle ear" — current evidence suggests this may actually represent nasal polyposis (an existing indication), not a new indication
- If pursuing "polyp of frontal sinus," evaluate feasibility of the implant/device-based delivery route (Propel/Sinuva-class), since mometasone-specific evidence here is device-mediated rather than via standard nasal spray or systemic administration
- Deprioritize (Hold) the remaining 8 candidates until independent clinical or preclinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

