---
layout: default
title: Ribociclib
parent: Medium Evidence (L3-L4)
nav_order: 503
evidence_level: L4
indication_count: 10
---

# Ribociclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ribociclib: From HR+/HER2- Advanced Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

> Ribociclib is a selective CDK4/6 inhibitor originally developed and approved for HR+/HER2-negative advanced breast cancer.
> The TxGNN model's top-ranked new-indication signal is **Myeloid Leukemia** (score **99.35%**),
> but this is currently supported only by **0 clinical trials** and **2 relevant publications** (1 preclinical, 1 case report), with the case report pointing toward drug-related AML risk rather than therapeutic benefit — the evidence direction is ambiguous.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2-negative Advanced Breast Cancer *(not present in `taiwan_regulatory.licenses`, which is empty; identified from context within the evidence pack — rank #7 entry explicitly flags this as ribociclib's already-approved indication, supported by the MONALEESA-2/-3/-7 registrational Phase 3 RCTs)* |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (Not Marketed) — as recorded in this evidence pack; see caveat under "EU Market Information" |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is marked as a Data Gap in this evidence pack. However, across the collected trial and literature evidence, ribociclib is consistently described as a selective **CDK4/6 (cyclin-dependent kinase 4/6) inhibitor** that blocks the G1→S cell-cycle transition by preventing retinoblastoma (Rb) protein phosphorylation. Its original and only well-established indication, confirmed by the MONALEESA-2/-3/-7 Phase 3 trials found elsewhere in this evidence pack, is HR+/HER2-negative advanced/early breast cancer, in combination with endocrine therapy.

The mechanistic rationale for extending CDK4/6 inhibition to acute myeloid leukemia (AML) is that AML cells also depend on cell-cycle progression, and one in vitro study (PMID 32560251) explored combining CDK4/6 inhibitors with anthracyclines to overcome ABCB1/ABCG2-mediated drug resistance in AML cell lines — a plausible but purely preclinical rationale.

However, the evidence is directionally conflicted: the second relevant publication (PMID 30575100) is a case report describing AML that **developed after** CDK4/6 inhibitor treatment, attributed to underlying clonal hematopoiesis of indeterminate potential (CHIP) — i.e., a possible treatment-related adverse event/secondary malignancy signal, not a therapeutic effect. No clinical trial has tested ribociclib as AML treatment. This prediction should be treated as a mechanistic hypothesis requiring preclinical validation, not a repurposing candidate ready for clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/Mechanistic | Cancers | In vitro study combining CDK4/6 inhibitors with anthracyclines to overcome ABCB1/ABCG2-mediated pharmacokinetic drug resistance in AML cells; supports a mechanistic rationale but provides no in vivo or clinical efficacy data |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case Report (adverse event) | American Journal of Hematology | AML with eosinophilia emerged **after** CDK4/6 inhibitor treatment, attributed to underlying clonal hematopoiesis (CHIP) — signals a possible treatment-related AML risk rather than therapeutic benefit |

*Note: One additional literature hit returned by the automated search (PMID 41641105, a case report on vulvar/breast adenocarcinoma) was excluded as clearly unrelated to AML, per its own classification tag in the evidence pack ("不相關病例").*

---

## EU Market Information

No marketing authorization records are present in `taiwan_regulatory.licenses` (0 entries). The evidence pack records `market_status = Not marketed (Not Marketed)`.

**Data quality caveat:** Ribociclib (Kisqali®) is a well-known EMA-approved medicine for HR+/HER2- advanced breast cancer; a "Not Marketed / 0 licenses" status is inconsistent with this and likely reflects incomplete regulatory data extraction in this pack rather than an actual lack of EU authorization. This should be corrected before the report is used for regulatory or market-status decisions.

---

## Cytotoxicity

Ribociclib is an antineoplastic agent (approved for breast cancer; drug class confirmed as CDK4/6 inhibitor throughout the collected trial/literature evidence), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective CDK4/6 inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | High — literature within this evidence pack (e.g., meta-analyses/pharmacovigilance studies on CDK4/6 inhibitors) consistently reports neutropenia and thrombocytopenia as common, dose-limiting toxicities |
| Emetogenicity Classification | Not directly reported in this evidence pack — please refer to the SmPC |
| Monitoring Items | CBC with differential (neutropenia/thrombocytopenia); liver function tests (transaminase elevation reported); ECG/QTc monitoring (QT prolongation and cardiac arrhythmia signals reported in the collected literature) |
| Handling Protection | Not specified in this evidence pack (see Data Gap DG001); follow institutional hazardous/antineoplastic drug handling protocols pending confirmation from the TFDA/SmPC label |

---

## Safety Considerations

Please refer to the SmPC for safety information. (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all marked as Data Gap / not found in this evidence pack — this is flagged as a **Blocking** gap, DG001, preventing entry into the S1 safety initial-evaluation stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Myeloid Leukemia) has no clinical trial support and only 2 relevant publications, one of which suggests CDK4/6 inhibitor treatment may **cause** rather than treat AML — the evidence direction is unresolved (Evidence Level L4).
- Mandatory safety data (TFDA/SmPC warnings and contraindications, DG001) is missing and blocks progression to the S1 safety review stage regardless of indication.

**To proceed, the following is needed:**
- Resolve the Blocking data gap (DG001): obtain the SmPC/label warnings and contraindications
- Resolve the MOA data gap (DG002) via DrugBank API to formally document the CDK4/6 mechanism
- Preclinical (in vivo) validation of CDK4/6 inhibition in AML models to clarify whether the mechanistic signal is therapeutic or represents a treatment-related AML risk signal
- Correct the EU market-status discrepancy in the regulatory dataset (0 licenses appears inconsistent with ribociclib's known EMA approval)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

