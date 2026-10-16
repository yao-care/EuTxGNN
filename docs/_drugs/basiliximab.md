---
layout: default
title: Basiliximab
parent: AI Predictions (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Basiliximab: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Prophylaxis of acute organ rejection in de-novo allogeneic renal tran…"
---

# Basiliximab
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

# Basiliximab: From Prevention of Kidney Transplant Rejection to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab is an anti-CD25 (IL-2 receptor) antibody, originally used to prevent acute organ rejection in kidney transplant recipients.
The TxGNN model predicts it may be useful for **plasma cell myeloma**,
with **3 clinical trials** and **4 publications** currently supporting this direction. These studies are small and use basiliximab in a supportive or immunomodulatory role, not as a direct anti-myeloma treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of acute organ rejection in de-novo allogeneic renal transplantation in adult and paediatric patients (1-17 years) |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L2 (as assigned in the compiled data; see the note under Clinical Trial Evidence) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Basiliximab blocks the alpha chain of the IL-2 receptor (CD25). This receptor is found on activated T cells and on regulatory T cells (Tregs). In kidney transplantation, blocking it dampens the T-cell response that drives rejection. Detailed mechanism-of-action data are not available in the data compiled for this report. The description here is based on the drug's known class.

The link to myeloma is indirect. The myeloma-related studies use basiliximab in two ways:
1. **Preventing graft-versus-host disease (GVHD)** after non-myeloablative allogeneic stem cell transplantation, by depleting activated T cells.
2. **Depleting Tregs** around autologous stem cell transplantation, to try to strengthen the immune response against myeloma cells.

Both are supportive or immunomodulatory uses. There is no evidence that basiliximab acts directly against myeloma cells. The original indication (kidney transplant rejection) and the new one (myeloma) share only an immune-modulation theme and a transplant setting.

Other predictions on the list, such as bronchitis, gastric carcinoma and several rare genetic disorders, have no plausible mechanistic basis and are not recommended for further work. The hemoglobinopathy prediction (thalassemia) is supported only by GVHD prevention data, not by disease modification.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab plus cyclosporine to prevent GVHD after non-myeloablative allotransplant. Single-arm, and the endpoint is GVHD, not myeloma control |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | Not applicable | Terminated | 10 | Basiliximab plus cyclosporine vs cyclosporine alone for GVHD prevention. Stopped early and too small to draw conclusions |
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot of Treg depletion during autologous stem cell transplant in myeloma. The most mechanistically relevant trial, but early-phase |

**Note:** The L2 level comes from the compiled data. By the stated rules, L2 requires a completed Phase 2/3 RCT. The only completed Phase 2 trial here is small and single-arm, so the true strength is closer to L3-L4, and the evidence should be read cautiously.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Cohort (pilot) | J Immunother Cancer | Treg depletion around autologous stem cell transplant in myeloma, aiming to reduce immune suppression after transplant |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Cohort | Bone Marrow Transplant | Basiliximab was well tolerated and effective in 17 patients with steroid-refractory acute GVHD after allogeneic transplant (one patient had myeloma) |
| [42379467](https://pubmed.ncbi.nlm.nih.gov/42379467/) | 2026 | Case report/Review | Am J Kidney Dis | Kidney transplantation after CAR T-cell therapy in myeloma; relevant to transplant feasibility, not to basiliximab efficacy |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case report | Am J Kidney Dis | Four myeloma patients with kidney failure who received kidney transplants after achieving disease control |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000207 (cancelled) | Simulect | Not specified | Simulect is indicated for the prophylaxis of acute organ rejection in de-novo allogeneic renal transplantation in adult and paediatric patients (1-17 years). It is to be used concomitantly with... |

## Safety Considerations

- **Drug Interactions**: 69 interactions were identified. Those listed in the compiled data include:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, and live BCG vaccine (Tice strain). The pattern is additive immunosuppression and infection risk.
  - **Moderate**: azathioprine, alemtuzumab, anakinra, canakinumab, alefacept, roflumilast, and several vaccines (tetanus toxoid, anthrax, adenovirus type 4, cholera live). Live vaccines are a particular concern in immunosuppressed patients.
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride).

Warnings and contraindications from the product label are not available in the compiled data. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myeloma evidence consists of three small, early-phase or terminated trials and a few cohort studies and case reports. Basiliximab is used there to manage transplant complications (GVHD) or to deplete Tregs, not to treat the myeloma itself. In addition, the only EU authorization is cancelled, and label safety data are missing.

**To proceed, the following is needed:**
- Results from NCT01526096 (Treg depletion pilot) showing a myeloma-relevant efficacy signal, and ideally a randomized trial
- Detailed mechanism-of-action data
- EU SmPC warnings and contraindications (the label should be retrieved and reviewed)
- Clarification of the regulatory pathway, given that the Simulect authorization is cancelled
- A safety plan for infection risk and live-vaccine interactions in myeloma patients, who are already immunocompromised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

