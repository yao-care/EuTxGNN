---
layout: default
title: Nivolumab
parent: High Evidence (L1-L2)
nav_order: 420
evidence_level: L2
indication_count: 10
---

# Nivolumab
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

# Nivolumab: From Cutaneous Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

> Nivolumab is an anti-PD-1 immune checkpoint inhibitor with established efficacy in cutaneous melanoma.
> The TxGNN model predicts it may also be effective for **Non-Cutaneous Melanoma** (mucosal, acral, uveal and other rare subtypes),
> with **20 clinical trials** and **0 dedicated publications** currently supporting this specific direction (broader subtype-level evidence exists across the wider prediction set).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous Melanoma (established efficacy, referenced in repurposing rationale; not separately listed in this evidence pack's regulatory data) |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not Marketed (per this evidence pack) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nivolumab is an anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 interaction, restoring T-cell–mediated anti-tumor activity. Because this mechanism acts on the host immune system rather than on tumor-specific histology, the efficacy already demonstrated in cutaneous melanoma can in principle be extrapolated to non-cutaneous subtypes (mucosal, acral, uveal). However, non-cutaneous subtypes typically carry a lower tumor mutational burden (TMB), which may reduce response rates compared with cutaneous disease.

This mechanistic generalizability is supported empirically: a large national prospective non-interventional study (NCT02990611, n=1,087) and a completed Phase 1/2 trial in a previously treated Asian population (NCT02593786, n=58) both provide real-world and controlled evidence for nivolumab's activity across melanoma presentations beyond the classic cutaneous phenotype. Ongoing sequential-therapy trials in BRAF-mutant disease (NCT03235245, n=271) further support the applicability of nivolumab-based regimens in molecularly and phenotypically diverse melanoma populations.

Across the broader set of TxGNN-predicted melanoma subtypes evaluated in this evidence pack (mucosal, acral lentiginous, epithelioid, nodular, lentigo maligna, amelanotic, balloon cell), the mechanistic rationale is consistently framed as an extrapolation from proven cutaneous melanoma efficacy — with subtype-specific clinical validation available for mucosal and acral lentiginous melanoma in particular (see prediction ranks 4 and 8, both scored L2 with dedicated randomized or cohort trials), while several rarer histologic variants remain supported only by case reports or mechanistic reasoning.

---

## Clinical Trial Evidence

*(Non-Cutaneous Melanoma — Rank 1 prediction; trials with assessed relevance grade A–C shown)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02593786](https://clinicaltrials.gov/study/NCT02593786) | Phase 1/2 | Completed | 58 | CheckMate 077: nivolumab monotherapy in Chinese subjects with previously treated advanced/recurrent solid tumors, including melanoma; direct single-agent efficacy evidence (Grade A) |
| [NCT02990611](https://clinicaltrials.gov/study/NCT02990611) | N/A (non-interventional) | Completed | 1,087 | National prospective real-world study of nivolumab monotherapy or with ipilimumab in advanced melanoma, including adjuvant setting; broad real-world evidence (Grade A) |
| [NCT03235245](https://clinicaltrials.gov/study/NCT03235245) | Phase 2 | Active, not recruiting | 271 | EBIN study: sequential targeted therapy (encorafenib+binimetinib) followed by nivolumab+ipilimumab vs. immediate combination immunotherapy in BRAF V600-mutant melanoma; indirect supportive evidence (Grade B) |
| [NCT05200143](https://clinicaltrials.gov/study/NCT05200143) | Phase 2 | Terminated | 4 | Triplet ipilimumab+nivolumab+cabozantinib in anti-PD-1/PD-L1 refractory melanoma; terminated with very small sample, low evidentiary weight (Grade C) |

*Note: Numerous additional trials (e.g., NCT02599402/CheckMate 401 Phase 3, n=533) are registered under this prediction but have not yet completed relevance grading ("pending") and are therefore excluded from this table pending review.*

---

## Literature Evidence

Currently no related literature available for this specific prediction (non-cutaneous melanoma).

*(Note: dedicated literature evidence supporting nivolumab efficacy in specific non-cutaneous subtypes — e.g., mucosal melanoma [PMID 28056206, Grade 1 CheckMate pooled analysis; PMID 39269143] and acral lentiginous melanoma [PMID 30447078, PMID 36093750] — is available under the corresponding subtype-specific predictions in this evidence pack, ranks 4 and 8.)*

---

## EU Market Information

According to this evidence pack, Nivolumab currently has **no recorded marketing authorization** (0 authorizations, market status: Not Marketed). No license-level data (authorization number, product name, dosage form, approved indication text) is available for tabulation.

---

## Cytotoxicity

Nivolumab is an oncology agent (immune checkpoint inhibitor) used across multiple melanoma and solid tumor indications, and is therefore evaluated for cytotoxicity considerations below. Note that no DrugBank toxicity data or official mechanism-of-action record was available in this evidence pack (see Data Gaps DG001, DG002); the assessment below is based on drug class and literature-reported adverse event patterns within this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low — mechanism is immune-mediated (T-cell activation) rather than direct cytotoxic bone marrow suppression; primary toxicities are immune-related adverse events (irAEs) |
| Emetogenicity Classification | Low — checkpoint inhibitors are generally minimally emetogenic |
| Monitoring Items | Cardiac function/troponin (myocarditis reported in literature), liver and renal function, thyroid function, GI symptoms (colitis), pulmonary symptoms (pneumonitis), skin (bullous pemphigoid, cutaneous irAEs) |
| Handling Protection | Not classified as a conventional cytotoxic hazardous drug; standard biologics/monoclonal antibody handling and infusion-reaction monitoring protocols apply — please refer to the SmPC for full handling requirements |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack — this is flagged as a **Blocking** data gap, see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The anti-PD-1 mechanism of nivolumab has direct empirical support for broader melanoma applicability through a large real-world cohort (n=1,087) and a completed Phase 1/2 trial (n=58), yielding an L2 evidence level for the top-ranked prediction (non-cutaneous melanoma). However, this drug is not currently marketed in the covered jurisdiction and lacks essential safety labeling data, so any progression must be gated on resolving the outstanding data gaps before clinical or regulatory action.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (DG001 — **Blocking**; required before any S1 safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002 — High priority)
- Subtype-specific prospective trial data for the rarer non-cutaneous histologies currently supported only by case reports (epithelioid, nodular, lentigo maligna, amelanotic, balloon cell subtypes)
- A structured irAE monitoring plan (cardiac, hepatic, GI, pulmonary, dermatologic) prior to any guardrail-based clinical use
- EU/local market authorization status verification, given the discrepancy between this drug's international approval history and the "not marketed" status recorded in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

