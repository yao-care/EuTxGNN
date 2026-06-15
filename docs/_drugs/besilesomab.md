---
layout: default
title: Besilesomab
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Besilesomab
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

# Besilesomab: From Granulocyte Scintigraphy to Diabetic Cataract

## One-Sentence Summary

Besilesomab (Scintimun) is a murine IgG1 monoclonal antibody targeting NCA-95 on granulocytes, originally developed as a diagnostic radiolabeled imaging agent for scintigraphic detection of bone and joint infections, including osteomyelitis and diabetic foot infections.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, ranking this as the highest-scored novel indication in the analysis.
However, **0 clinical trials** and **0 publications** currently support this predicted direction, placing the evidence entirely at the AI model prediction stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Granulocyte scintigraphy — diagnostic imaging of bone and joint infections |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Besilesomab is a murine IgG1 monoclonal antibody directed against NCA-95 (non-specific cross-reacting antigen 95, also called CD66b), a glycoprotein expressed on the surface of granulocytes — particularly neutrophils. Its clinical application is as a diagnostic imaging agent: when radiolabeled with technetium-99m and injected intravenously, it homes to sites of granulocyte accumulation, enabling scintigraphic localization of infectious or inflammatory foci. It has no established therapeutic mechanism; it does not block, deplete, or modulate granulocyte function.

The predicted indication of diabetic cataract shares the "diabetic" disease context with the drug's existing use in diabetic foot infection imaging, but differs fundamentally in pathomechanism. Diabetic cataract arises from the polyol pathway (aldose reductase converts glucose to sorbitol, causing osmotic stress in the lens), non-enzymatic glycation producing advanced glycation end-products (AGEs), and chronic oxidative stress — none of which directly involve granulocyte-mediated inflammation. The TxGNN prediction most likely reflects a knowledge-graph clustering effect: diabetic complications (retinopathy, cataract, neuropathy, foot infection) cluster tightly as neighboring disease nodes around diabetes-related drug nodes, generating co-occurrence signals rather than true mechanistic links.

Among all 10 predicted indications, **diabetic retinopathy** (rank 10) is the most biologically plausible. There is published evidence that neutrophils contribute to leukostasis — physical plugging of retinal capillaries — in the diabetic retina, which could in principle be a target for an anti-granulocyte agent. However, Besilesomab remains a diagnostic agent, not a therapeutic antibody, and no preclinical or clinical data support its use as a treatment for any of the predicted indications. For all cataract subtypes (ranks 1–9), there is no known biological pathway connecting granulocyte activity to lens opacification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Besilesomab in any of the 10 predicted indications (diabetic cataract, mature cataract, craniostenosis cataract, tetanic cataract, immature cataract, type 2 diabetes-associated cataract, nuclear senile cataract, cortical cataract, senile cataract, or diabetic retinopathy).

---

## Literature Evidence

Currently no related literature available for Besilesomab in any of the 10 predicted indications.

---

## Taiwan Market Information

Besilesomab is not currently authorized for marketing in Taiwan (0 registered licenses). No dosage form, approved indication, or authorization number is on record in the Taiwan regulatory database.

> Note: Besilesomab is authorized in the European Union by EMA (Scintimun, EU/1/10/644) for granulocyte scintigraphy in the diagnosis of suspected bone and joint infections. This EMA authorization does not extend to Taiwan.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Safety data for Besilesomab (key warnings, contraindications, and drug-drug interactions) are not available in this Evidence Pack. DG001 (TFDA SmPC / prescribing information) is flagged as a **Blocking** data gap. Given that Besilesomab contains a murine protein backbone, hypersensitivity and human anti-mouse antibody (HAMA) reactions are a class-level concern for murine monoclonal antibodies that should be reviewed before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are rated L5 — purely AI model-generated with no supporting clinical trials or published literature — and the mechanistic link between Besilesomab's NCA-95 granulocyte-targeting mechanism and cataract pathophysiology lacks any established biological basis. Furthermore, Besilesomab is a diagnostic imaging agent rather than a therapeutic drug, raising a fundamental question of whether drug repurposing as a treatment is conceptually applicable without substantial molecular re-engineering.

**To proceed, the following is needed:**

- **Clarify therapeutic vs. diagnostic classification**: Confirm whether Besilesomab can exert any therapeutic effect (e.g., antibody-dependent cellular cytotoxicity against granulocytes) beyond its imaging role, as current evidence supports only diagnostic use
- **Obtain full MOA data** (DG002): Query DrugBank API for complete pharmacology, targets, and known off-target effects
- **Obtain Taiwan SmPC / prescribing information** (DG001, Blocking): Required before any safety evaluation can proceed
- **For the most biologically plausible indication (diabetic retinopathy)**: Conduct preclinical studies in leukostasis models (in vitro human retinal endothelial cell adhesion assays, streptozotocin-induced diabetic mouse retina) to establish whether NCA-95-directed neutralization reduces granulocyte adhesion before any clinical consideration
- **For cataract indications**: Independent mechanistic evidence linking granulocyte activity to lens opacification pathology would be required — currently absent in the literature — before these indications can be considered viable repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

