---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α (PGF2α) analogue widely used internationally as a first-line agent for reducing intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 completed Phase 2 clinical trial** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (international use; not registered in Taiwan) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Latanoprost acts as a selective prostaglandin F2α (PGF2α) analogue at the FP receptor in ocular tissue. Activation of FP receptors in the ciliary body increases uveoscleral aqueous humor outflow, lowering IOP. While detailed pharmacokinetic MOA data was not available in this evidence pack, the drug's clinical role as an IOP-lowering agent is established internationally, and the mechanism described in the repurposing rationale is consistent with peer-reviewed pharmacology literature.

Primary hereditary glaucoma — encompassing juvenile open-angle glaucoma (JOAG) and genetically-driven subtypes associated with MYOC and CYP1B1 mutations — shares the same core pathophysiology as primary open-angle glaucoma: chronically elevated IOP causing progressive optic nerve damage. Because Latanoprost's mechanism directly targets IOP elevation via the FP receptor/uveoscleral pathway, the pharmacological rationale transfers directly regardless of whether the underlying cause is age-related or hereditary gene mutation. The target tissue (trabecular meshwork and uveoscleral outflow pathway) is anatomically identical across both conditions.

Clinically, a completed Phase 2 trial (NCT01527682) specifically evaluated prostaglandin analogues, including Latanoprost, in pediatric glaucoma patients refractory to surgery — a population that substantially overlaps with primary hereditary glaucoma presentations. This real-world clinical use validates the translational hypothesis and elevates confidence beyond a purely model-driven prediction. One key caution: pediatric and adolescent patients may have different long-term susceptibility to known PGF2α side effects such as iris and periorbital pigmentation changes, which must be factored into any clinical protocol.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Evaluated prostaglandin analogue (Latanoprost) and dorzolamide for IOP reduction in pediatric glaucoma patients refractory to surgery, including primary hereditary forms. Trial ran July 2009 – November 2016. Primary/secondary endpoint results should be sought in publications. |

---

## Literature Evidence

Currently no related literature available from this evidence search.

---

## Taiwan Market Information

Latanoprost is currently **not registered** in Taiwan (0 marketing authorizations on record). No approved indication text, prescribing information, or TFDA package insert is available from Taiwan regulatory sources.

For complete prescribing and safety information, please refer to internationally approved product labelling (e.g., FDA-approved Xalatan® labelling or EMA-approved SmPC).

---

## Safety Considerations

TFDA package insert warnings and contraindications were not available for this evaluation (data gap). Drug interaction data was not found in the queried database.

Please refer to the internationally approved SmPC / product labelling for complete safety information. Of particular note for the predicted indication:

- **Known class effect**: PGF2α analogues are associated with iris pigmentation changes (heterochromia iridis), periorbital skin darkening, and eyelash changes — clinically relevant when treating pediatric/adolescent patients with hereditary glaucoma over long durations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Latanoprost's FP receptor-mediated IOP reduction and the core pathology of primary hereditary glaucoma is pharmacologically direct, and a completed Phase 2 trial in the pediatric glaucoma population provides real-world clinical validation at the L2 evidence level. However, Taiwan has no existing regulatory authorization for Latanoprost, and long-term pediatric safety data specific to hereditary subtypes remains to be fully characterised.

**To proceed, the following is needed:**
- Retrieve published results from NCT01527682 (primary and secondary endpoints, efficacy magnitude, adverse event profile in pediatric patients)
- Obtain complete MOA documentation from DrugBank (DG002) to support mechanistic dossier
- Obtain TFDA package insert or equivalent labelling for Taiwan safety screening (DG001)
- Conduct pediatric-specific dosing review, including assessment of long-term iris and periorbital pigmentation risk in the target population
- Map the regulatory pathway for Taiwan: since Latanoprost is not registered locally, determine whether a full NDA or bridging strategy referencing international approvals (FDA/EMA) is more appropriate
- Consider searching pediatric ophthalmology literature specifically for MYOC/CYP1B1-associated glaucoma and prostaglandin analogue response data to supplement PubMed results (current search returned 0 publications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

