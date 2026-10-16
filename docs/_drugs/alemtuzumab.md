---
layout: default
title: Alemtuzumab
parent: AI Predictions (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alemtuzumab: predicted new indication Syndrome with combined immunodeficiency (evidence level L5). Approved use: Adult patients with relapsing-remitting multiple sclerosis (RRMS) wit…"
---

# Alemtuzumab
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

# Alemtuzumab: From Relapsing-Remitting Multiple Sclerosis to Syndrome with Combined Immunodeficiency

## One-Sentence Summary

Alemtuzumab (Lemtrada) was originally authorized in the EU for adults with active relapsing-remitting multiple sclerosis (RRMS).
The TxGNN model predicts it may be useful for **syndrome with combined immunodeficiency**, the highest-ranked prediction with real supporting evidence, with **7 clinical trials** and **8 publications** supporting this direction.
The evidence is mostly small, early-phase studies in which alemtuzumab is one part of a transplant conditioning regimen.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adult patients with relapsing-remitting multiple sclerosis (RRMS) with active disease defined by clinical or imaging features |
| Predicted New Indication | Syndrome with combined immunodeficiency |
| TxGNN Prediction Score | 93.73% |
| Evidence Level | L2 (see note below) |
| EU Market Status | Cancelled only (marketing authorization cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

*Note on the evidence level: the only trial with a Phase 3 component is NCT01019876 (Phase 2/3, completed), and it is uncertain how much of it is alemtuzumab-specific. L2 is therefore the most generous reading of the data.*

*Note on the other predictions: the top-ranked prediction, hepatic infarction (score 94.44%), has no clinical trials or literature and no plausible mechanism (Level L5). It was not chosen for this report for that reason. The other predictions, mostly urothelial carcinomas and peliosis hepatis, are also model-only, and hepatic veno-occlusive disease is a transplant toxicity rather than a treatment target.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, alemtuzumab is a monoclonal antibody that depletes CD52-positive lymphocytes. This property underlies its use in RRMS, where it reduces the immune cells driving disease activity.

In combined immunodeficiency, including severe combined immunodeficiency (SCID), alemtuzumab is not a treatment for the underlying defect. It is used as a lymphodepleting and serotherapy agent in reduced-intensity conditioning before allogeneic hematopoietic stem cell transplantation (HSCT). It depletes host T cells to help the donor graft take hold and to reduce graft-versus-host disease, while avoiding the toxicity of conventional chemotherapy conditioning.

The link to the original indication is therefore the shared immune-cell-depleting effect, not a shared disease. Because most regimens combine alemtuzumab with other agents (fludarabine, melphalan, busulfan, treosulfan), its independent contribution is hard to separate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01019876](https://clinicaltrials.gov/study/NCT01019876) | Phase 2/3 | Completed | 38 | Risk-adapted reduced-intensity allogeneic HSCT for mixed donor chimerism in non-malignant diseases, including immunodeficiencies |
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Phase 1/2 | Terminated | 3 | CD45 antibody plus alemtuzumab conditioning for allogeneic transplant in SCID and other primary immunodeficiencies (directly tests alemtuzumab, but very small) |
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Phase 2 | Terminated | 7 | Alemtuzumab with plerixafor-based mobilization for HSCT in children with SCID, avoiding chemotherapy conditioning |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Allogeneic HSCT for chronic granulomatous disease with an alemtuzumab, busulfan and TBI-based regimen plus cytokine antagonists |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | Reduced-intensity conditioning in pediatric and young adult non-malignant disorders (alemtuzumab likely part of the regimen) |
| [NCT01652092](https://clinicaltrials.gov/study/NCT01652092) | NA | Active, not recruiting | 57 | Standard-of-care allogeneic HSCT guideline for primary immune deficiencies (role of alemtuzumab unclear) |
| [NCT00152100](https://clinicaltrials.gov/study/NCT00152100) | Phase 1 | Completed | 4 | Haploidentical CD133+ HSCT in children with SCID (focus on graft manipulation; alemtuzumab relevance indirect) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alemtuzumab/fludarabine/melphalan reduced-intensity conditioning (4 patients) compared with myeloablative busulfan/cyclophosphamide/ATG (14 patients) in chronic granulomatous disease |
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Cohort | Biol Blood Marrow Transplant | UK experience of treosulfan and fludarabine conditioning in 160 children with primary immunodeficiency |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Cohort | Blood | Treosulfan-based conditioning with alemtuzumab in 70 children with primary immunodeficiency |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | Cohort | Blood | International survey of HCT for XIAP deficiency; poor outcomes, with reduced-intensity regimens mostly alemtuzumab-based |
| [26073206](https://pubmed.ncbi.nlm.nih.gov/26073206/) | 2015 | Cohort | Pediatr Transplant | Single-center HSCT experience in 5 patients with hyper-IgM syndrome due to CD40L defects |
| [19471859](https://pubmed.ncbi.nlm.nih.gov/19471859/) | 2009 | Cohort | Immunol Res | FOXP3 expression after reduced-intensity bone marrow transplantation in an infant with IPEX syndrome |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Review | Haematologica | Infectious toxicity associated with alemtuzumab |
| [18502831](https://pubmed.ncbi.nlm.nih.gov/18502831/) | 2008 | Case report | Blood | EBV-positive immunodeficiency lymphoma after alemtuzumab-CHOP in peripheral T-cell lymphoma (a safety signal) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003718 | Lemtrada | Not specified | Adult patients with relapsing-remitting multiple sclerosis (RRMS) with active disease defined by clinical or imaging features. (status: cancelled) |

---

## Cytotoxicity

Alemtuzumab is an immunosuppressive monoclonal antibody, and its original indication here (RRMS) is not an oncology indication. It is not classed as an antineoplastic in the data compiled for this report, so a cytotoxicity profile is not provided.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. The ones listed are mostly of Moderate severity, including:
  - Corticosteroids: hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone
  - Acetylsalicylic acid
  - Anticoagulants: heparin, argatroban, lepirudin
  - Radiopharmaceuticals and related agents: ibritumomab tiuxetan, iobenguane (I-131), tositumomab, strontium chloride Sr-89, palifermin
  - **Major** severity: deferiprone and samarium (153Sm) lexidronam
- **Literature safety signals**: infectious toxicity with alemtuzumab (PMID 15590388) and an EBV-positive lymphoproliferative disorder after alemtuzumab-CHOP (PMID 18502831).

Warnings and contraindications from the product information are not available in the data compiled for this report. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Alemtuzumab appears only as one component of conditioning regimens before HSCT in combined immunodeficiency. It does not treat the immune defect, and the trials are small, early-phase and often terminated. Its EU authorization is cancelled, and warnings and contraindications could not be retrieved.
- This is better treated as a research question about its role in conditioning than as a repurposing candidate for development.

**To proceed, the following is needed:**
- Safety information from the EMA product information (warnings and contraindications), which blocks safety screening
- Mechanism of action data (for example, from DrugBank)
- Comparative data separating alemtuzumab's contribution from other conditioning agents, and results from the ongoing trials (NCT05463133, NCT01962415)
- A safety assessment of infection and EBV-related lymphoproliferation risk in already immunodeficient patients
- Clarification of the cancelled EU authorization status and of the available formulations and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

