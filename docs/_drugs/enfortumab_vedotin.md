---
layout: default
title: Enfortumab Vedotin
parent: High Evidence (L1-L2)
nav_order: 218
evidence_level: L2
indication_count: 10
---

# Enfortumab Vedotin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Enfortumab Vedotin: From Urothelial Carcinoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Enfortumab vedotin is an anti-Nectin-4 antibody-drug conjugate (ADC) carrying the cytotoxic payload MMAE, established for advanced urothelial (bladder) cancer. TxGNN scored ten candidate indications; nine of them (including leprosy, the top-ranked hit) have no clinical or literature support and are treated as model noise. The only candidate with corroborating real-world evidence is **HER2-positive breast carcinoma**, backed by **4 clinical trials** (mostly indirect basket-type studies) and **4 publications**, reaching evidence level **L2**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided as structured data in this pack (`original_indications` is empty); trial/literature context (e.g., bladder-cancer FAERS study, EV-202 solid-tumor trial) points to advanced urothelial (bladder) carcinoma as the approved indication |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.99% (rank 9,579 of model output) |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Other TxGNN Predictions Screened (Not Pursued)

Nine other high-score candidates were screened and excluded for lack of any supporting evidence:

| Disease | TxGNN Score | Why Not Pursued |
|---------|------------|------------------|
| Leprosy (rank 1) | 99.53% | No mechanistic link, no trials/literature |
| Multiple endocrine neoplasia | 99.43% | No known mechanistic link |
| Cytomegalovirus infection | 99.36% | No mechanistic basis |
| Candidiasis | 99.30% | Sole literature hit is a FAERS pharmacovigilance study showing candidiasis as a likely **adverse event** from MMAE-related immunosuppression — a safety signal, not a treatment opportunity |
| Cerebral infarction | 99.23% | Mechanistically unrelated; ADCs carry thrombotic risk, opposite direction |
| HIV infectious disease | 99.19% | Immunosuppressive profile works against this indication |
| Homozygous familial hypercholesterolemia | 99.18% | No mechanistic link (genetic lipid disorder) |
| Infectious bovine rhinotracheitis | 99.13% | Veterinary/cattle disease — likely knowledge-graph noise |
| Malignant catarrh | 99.13% | Veterinary/wildlife herpesvirus disease — likely knowledge-graph noise |

---

## Why is This Prediction Reasonable?

The structured MOA field for this drug is marked as a data gap (DG002) in this pack. However, the evidence pack's own rationale annotations consistently describe enfortumab vedotin as an **anti-Nectin-4 antibody-drug conjugate** delivering the microtubule-disrupting payload **MMAE (monomethyl auristatin E)**. Nectin-4 is well characterized as highly expressed in urothelial carcinoma, the drug's original target population.

The rationale for the breast-cancer candidate notes that Nectin-4 overexpression has also been reported in breast cancer tissue, including the HER2-positive subtype, giving a plausible biological basis for extending an anti-Nectin-4 ADC beyond urothelial cancer. This is consistent with the broader trend in oncology of ADC platforms (same or related targets/payloads) being tested across multiple HER2-driven and Nectin-4-expressing solid tumors via basket and multi-cohort designs — exactly the trial pattern seen in the evidence below.

That said, none of the identified trials or publications directly confirm efficacy of enfortumab vedotin specifically in a HER2-positive breast cancer cohort; the signal is inferred from adjacent basket trials and general ADC-class literature rather than a dedicated study.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | Active, not recruiting | 329 | EV-202: multicohort study of enfortumab vedotin in locally advanced/metastatic solid tumors; drug is confirmed as EV itself, but the abstract does not confirm a dedicated HER2+ breast cohort — indirect support only |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated (enrollment 11) | 11 | StrataPATH basket trial testing approved drugs in biomarker-guided populations; terminated early, EV's specific role unconfirmed — weak evidence |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1b/2 | Recruiting | 428 | Studies ASP2998 (a different TROP2-targeted agent) combined with several regimens including enfortumab vedotin in solid tumors; EV is a combination partner, not the study drug — low direct relevance |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | Recruiting | 90 | Studies trastuzumab rezetecan (a different HER2-targeted ADC) in HER2+ solid tumors; co-occurs with EV only by ADC/solid-tumor search overlap, not a shared drug — low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Real-world evidence review | Critical Reviews in Oncology/Hematology | Narrative synthesis of real-world evidence for 10 recently approved oncology drugs (class-level context, not EV/breast-cancer specific) |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Review/mechanism | Cancer Letters | Describes polyploid giant cancer cells mediating resistance to HER2-targeting ADCs (trastuzumab emtansine, trastuzumab deruxtecan, XMT-1522, disitamab vedotin) in HER2+ breast/gastric cancer models — relevant to ADC-class resistance mechanisms, but not about enfortumab vedotin itself |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | Molecular pathology of bladder cancer — background on the drug's original tumor type, not breast cancer |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | General review of ADC targets and payloads across cancer types — background class knowledge only |

---

## Cytotoxicity

Enfortumab vedotin is an antineoplastic ADC (MMAE payload), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Nectin-4-directed ADC) delivering a conventional cytotoxic payload (MMAE, microtubule inhibitor) |
| Myelosuppression Risk | Not formally quantified in this pack; the evidence pack's own FAERS signal analysis (candidiasis candidate, rank 4) flags MMAE-related myelosuppression/immunosuppression as a plausible driver of opportunistic infection — please refer to the SmPC for definitive grading |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The drug is not marketed in this jurisdiction (0 authorizations), and TFDA/SmPC labeling data (warnings, contraindications) is a **blocking data gap** (DG001) — safety cannot be evaluated yet.
- The only candidate indication with any supporting evidence, HER2-positive breast carcinoma, is backed solely by indirect basket-trial and class-level review evidence (L2), not a dedicated study confirming efficacy in this population.
- The nine other high-scoring TxGNN predictions have zero clinical or literature support, and two are veterinary conditions — indicating this batch of predictions needs quality filtering before further action.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, contraindications, and DDI data (DG001 remediation)
- Structured mechanism-of-action data from DrugBank (DG002 remediation)
- A dedicated clinical or preclinical study confirming Nectin-4 expression and enfortumab vedotin activity specifically in HER2-positive breast cancer, rather than relying on basket-trial inference
- Re-screening or filtering of the TxGNN output to exclude non-human/veterinary disease terms and confirm the biological plausibility of remaining high-score, zero-evidence candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

