---
layout: default
title: Toripalimab
parent: AI Predictions (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: From Advanced Solid Tumors to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Toripalimab is an anti-PD-1 immune checkpoint inhibitor monoclonal antibody; the supporting literature in this Evidence Pack shows it used exclusively across various advanced solid tumors (nasopharyngeal carcinoma, esophageal cancer, hepatocellular carcinoma, renal cell carcinoma, melanoma, bladder and breast cancer). The TxGNN model predicts it may be effective for **Mixed-Type Autoimmune Hemolytic Anemia**, but this is a **pure AI prediction with no supporting clinical trials or literature (L5)**, and the underlying mechanistic rationale is flagged as **contradictory** — PD-1 inhibitors are a documented cause of autoimmune hemolytic anemia as an immune-related adverse event (irAE), not a treatment for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this Evidence Pack (regulatory data unavailable); literature indicates use across multiple advanced solid tumors as anti-PD-1 immunotherapy |
| Predicted New Indication | Mixed-Type Autoimmune Hemolytic Anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in this Evidence Pack. Based on the literature retrieved for this drug, toripalimab is an anti-PD-1 (programmed cell death protein-1) monoclonal antibody that blocks the PD-1/PD-L1 checkpoint, thereby releasing brakes on T-cell mediated immune activity — a mechanism used to enhance anti-tumor immunity in oncology.

This is precisely why the model's prediction for mixed-type autoimmune hemolytic anemia should be treated with caution rather than as a genuine repurposing opportunity. Autoimmune hemolytic anemia is itself an immune-mediated destructive process, and PD-1 inhibitors are pharmacologically known to *increase* immune activation — they are documented in the clinical literature as a **cause** of drug-induced autoimmune hemolytic anemia (irAE), not a treatment. The repurposing_rationale attached to this candidate explicitly notes this contradiction: "no clinical evidence; mechanistically contradictory — PD-1 inhibitors are known to induce AIHA as an irAE rather than treat it; the predicted direction may be reversed."

This pattern is not isolated to the top-ranked candidate. Several other high-ranking predictions from this same model run (dermatitis, proteinuria) are supported only by oncology trial/literature evidence in which the "predicted indication" actually appears as an **adverse effect** of toripalimab (e.g., SJS/TEN, lichenoid drug eruption, proteinuria during HCC/RCC treatment), not as a therapeutic endpoint. Taken together, this strongly suggests the model may be picking up an irAE co-occurrence signal rather than a true efficacy signal, and reinforces that this candidate should not proceed without independent mechanistic and clinical validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Toripalimab currently has no EU marketing authorization (market status: Not marketed; total authorizations: 0). No product, dosage form, or approved indication information is available in this Evidence Pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor monoclonal antibody) |
| Myelosuppression Risk | Low (checkpoint inhibitors are not conventional myelosuppressive cytotoxic agents) |
| Emetogenicity Classification | Low |
| Monitoring Items | Immune-related adverse event (irAE) monitoring — thyroid function, liver function (ALT/AST/bilirubin), renal function/urinalysis (proteinuria), skin examination, and complete blood count with differential (given hematologic irAE signals identified below) |
| Handling Protection | Standard biologic/monoclonal antibody infusion precautions; not subject to conventional cytotoxic drug handling regulations |

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available in this Evidence Pack — please refer to the SmPC for formal safety information. Notably, a **blocking data gap** exists for TFDA label warnings/contraindications, which prevents this candidate from entering the S1 safety pre-screening stage.

**Immune-related adverse events identified in supporting literature (not formal label data, but relevant safety signals surfaced during this evaluation):**
- Severe cutaneous adverse reactions, including Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis (SJS/TEN), reported in case series associated with PD-1/PD-L1 inhibitor use.
- Lichenoid drug eruption reported as a case report following toripalimab treatment.
- Proteinuria observed as an adverse finding during toripalimab combination oncology trials (HCC, RCC), not as a treatment response.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for mixed-type autoimmune hemolytic anemia has no supporting clinical trials or literature (L5, AI prediction only), and the proposed mechanistic link is directionally contradictory — PD-1 inhibition is a documented cause of autoimmune hemolytic anemia rather than a treatment for it. Combined with a blocking data gap on TFDA label warnings/contraindications, this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA/EMA product label (warnings, contraindications) to complete S1 safety pre-screening (currently blocking)
- Confirmed mechanism of action data from DrugBank or the manufacturer
- Independent pharmacovigilance review to determine whether this TxGNN signal reflects a genuine repurposing hypothesis or a reversed-direction artifact (i.e., an irAE co-occurrence being misread as efficacy)
- If pursued further, preclinical or case-level evidence specifically supporting an immune-suppressive (rather than immune-activating) benefit of toripalimab in autoimmune hemolytic anemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

