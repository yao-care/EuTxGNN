---
layout: default
title: Trifluridine
parent: AI Predictions (L5)
nav_order: 620
evidence_level: L5
indication_count: 10
---

# Trifluridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Trifluridine: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

*Note: The Evidence Pack contains no structured `original_indications` or EU license data for this substance (market status: not marketed). The original indication below is inferred from the drug's known pharmacology as referenced throughout the repurposing rationale text (trifluridine + tipiracil / TAS-102 / Lonsurf), not from the `taiwan_regulatory.licenses` field.*

## One-Sentence Summary

> Trifluridine, in combination with tipiracil (TAS-102/Lonsurf), is a clinically established cytotoxic antimetabolite for metastatic colorectal cancer.
> The TxGNN model predicts it may be effective for **cecum villous adenoma**, a benign colonic polyp,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale text flags it as a probable false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (as trifluridine/tipiracil combination); no structured EU license record available in this Evidence Pack |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form for this candidate. Based on known pharmacology, trifluridine is a thymidine analog/antimetabolite that, in combination with tipiracil, is clinically established (TAS-102/Lonsurf) for metastatic colorectal cancer. Its cytotoxicity depends on incorporation into DNA of rapidly proliferating malignant cells, inhibiting further tumor growth.

Cecum villous adenoma, however, is a **benign** glandular polyp. While it carries a recognized risk of malignant transformation, it is not itself a malignant proliferative lesion, and standard care is endoscopic or surgical resection — not cytotoxic chemotherapy. The Evidence Pack's own mechanistic assessment explicitly flags this pairing as a likely false positive, attributing the high TxGNN score to anatomical proximity between "colon/cecum" nodes in the knowledge graph rather than a genuine pharmacological relationship.

Because there is no clinical precedent for using a DNA-incorporating cytotoxic antimetabolite in a benign, low-proliferation lesion, and no trial or literature evidence links trifluridine to this indication, the mechanistic rationale for repurposing is weak. This assessment is consistent across the broader candidate list for this drug: nearly all top-10 predictions are benign colonic/cecal lesions (lipoma, lymphangioma, leiomyoma, cavernous hemangioma) or non-specific terms, none supported by direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No EU marketing authorization records are available for this substance in the Evidence Pack (market status: not marketed; total licenses: 0).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (thymidine-based nucleoside analog/antimetabolite; combined with tipiracil to inhibit thymidine phosphorylase and increase systemic exposure) |
| Myelosuppression Risk | High — neutropenia and leukopenia are documented adverse effects of trifluridine/tipiracil in the associated literature evidence for this drug (e.g., leukopenia, neutropenia, fatigue, diarrhea, vomiting reported with TAS-102 treatment) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (especially neutrophil count), liver and renal function, monitoring for cutaneous reactions (leukocytoclastic vasculitis has been reported) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the SmPC for safety information. *(Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this Evidence Pack — notably DG001, a Blocking-severity gap on TFDA label warnings/contraindications.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an AI model score (L5) with zero clinical trials and zero publications, and the pack's own mechanistic analysis identifies it as a likely knowledge-graph false positive driven by anatomical proximity rather than genuine pharmacology. In addition, a Blocking-severity data gap (DG001: TFDA label warnings/contraindications) prevents this candidate from even entering the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (resolve Blocking gap DG001)
- Confirmed mechanism of action data via DrugBank (resolve High-severity gap DG002)
- Direct preclinical or clinical evidence connecting trifluridine to cecum villous adenoma (or any benign colonic lesion) before advancing beyond S0
- Clarification of the EU regulatory status of the trifluridine/tipiracil combination product, since this dataset records "not marketed" despite the combination's established clinical use for mCRC
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

