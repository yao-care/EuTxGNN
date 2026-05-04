---
layout: default
title: Alemtuzumab
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Alemtuzumab
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

# Alemtuzumab: From B-Cell Malignancy / Multiple Sclerosis to Syndrome with Combined Immunodeficiency

## One-Sentence Summary

Alemtuzumab is a humanized anti-CD52 monoclonal antibody with established global approvals for B-cell chronic lymphocytic leukaemia (B-CLL) and relapsing-remitting multiple sclerosis; it carries no regulatory registration in Taiwan.
The TxGNN model's highest-evidence prediction points to **Syndrome with Combined Immunodeficiency**, where alemtuzumab functions as a cornerstone reduced-intensity conditioning (RIC) agent prior to haematopoietic stem cell transplantation (HSCT),
supported by **13 clinical trials** and **12 publications** at an evidence level of **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan (globally: B-CLL, relapsing-remitting multiple sclerosis) |
| Predicted New Indication | Syndrome with Combined Immunodeficiency |
| TxGNN Prediction Score | 93.73% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, alemtuzumab (Campath-1H / Lemtrada) is a humanized IgG1κ monoclonal antibody that targets CD52, a glycoprotein expressed at high density on the surface of mature T lymphocytes, B lymphocytes, monocytes, and natural killer cells. Binding of alemtuzumab to CD52 triggers rapid and profound lymphodepletion through antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct apoptotic signalling. This mechanism is the basis of its efficacy in lymphocytic malignancies and its immune-modulating effect in multiple sclerosis.

In the context of syndrome with combined immunodeficiency — encompassing SCID and related primary immunodeficiency disorders — allogeneic HSCT is the only curative treatment. The fundamental challenge is preventing graft rejection without inflicting the severe organ toxicity of conventional myeloablative chemotherapy on patients who are already fragile, chronically infected, and often very young. By eliminating host CD52⁺ T and B cells before transplant, alemtuzumab creates the immunological "space" required for donor stem cell engraftment, while simultaneously reducing the risk of graft-versus-host disease (GvHD). This positions alemtuzumab as the immunological bridge that makes safer HSCT feasible in these vulnerable patients — a rationale that is direct, mechanistically coherent, and well-documented in transplant literature.

The repurposing signal is therefore not a novel off-target effect but a deliberate extension of alemtuzumab's established lymphodepleting biology into the RIC-HSCT conditioning setting. Multiple published cohorts from major transplant centres document alemtuzumab-fludarabine-based RIC as a standard clinical approach for SCID and related PIDs, lending strong biological plausibility to the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01019876](https://clinicaltrials.gov/study/NCT01019876) | Phase 2/3 | Completed | 38 | Risk-adapted allogeneic SCT with RIC (including alemtuzumab) for mixed donor chimerism in non-malignant diseases including immunodeficiencies; highest-quality completed trial in this dataset |
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Phase 1/2 | Terminated | 3 | CD45 + alemtuzumab monoclonal antibody conditioning for allogeneic SCT in SCID and other PIDs using HLA-mismatched donors; terminated early — accrual reasons to be confirmed |
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Phase 2 | Terminated | 7 | Novel alemtuzumab + plerixafor/filgrastim HSCT protocol for children with SCID designed to avoid toxic chemotherapy conditioning; terminated — reason (safety vs. accrual) requires clarification |
| [NCT01652092](https://clinicaltrials.gov/study/NCT01652092) | N/A | Active, Not Recruiting | 57 | Standard-of-care HSCT treatment guideline for a broad range of primary immune deficiencies; largest accrual in this dataset despite lack of formal phase designation |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | RIC with UCBT/BMT/PBSCT for paediatric patients and young adults ≤55 years with non-malignant disorders; alemtuzumab is one of the conditioning backbone options |
| [NCT07284641](https://clinicaltrials.gov/study/NCT07284641) | Phase 2 | Recruiting | 25 | RIC HSCT with TBI for CVID and other primary immune regulatory disorders; directly addresses the combined immunodeficiency spectrum |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Alemtuzumab + busulfan + TBI conditioning for HSCT in chronic granulomatous disease; combined immunodeficiency-adjacent indication with cytokine antagonists co-intervention |
| [NCT02512679](https://clinicaltrials.gov/study/NCT02512679) | Phase 2 | Terminated | 20 | Related-donor HSCT protocol covering genetic lymphohematological diseases including combined immune deficiency and Wiskott-Aldrich syndrome; terminated with limited follow-up data |
| [NCT01821781](https://clinicaltrials.gov/study/NCT01821781) | Phase 2 | Active, Not Recruiting | 20 | RIC preparative regimen for immune function disorders maximising host immunosuppression to optimise donor engraftment |
| [NCT04528355](https://clinicaltrials.gov/study/NCT04528355) | N/A | Recruiting | 50 | Prospective outcomes study examining simplified alemtuzumab dosing strata in RIC-HSCT across paediatric and adult non-malignant disorders |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Prospective Cohort | Biol Blood Marrow Transplant | Treosulfan + fludarabine + alemtuzumab conditioning in 160 UK children with PID; improved T-cell chimerism and lower toxicity versus treosulfan-cyclophosphamide arm |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Retrospective Cohort | Blood | Treosulfan conditioning in 70 PID children; alemtuzumab included; fludarabine arm demonstrated lower VOD incidence and better T-cell immune reconstitution |
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Retrospective Cohort | Biol Blood Marrow Transplant | Alemtuzumab (1 mg/kg) + fludarabine + melphalan RIC vs myeloablative busulfan/cyclophosphamide/ATG for CGD; RIC showed reduced toxicity with comparable engraftment |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | International Survey | Blood | Allogeneic HCT for XIAP deficiency (n=19); alemtuzumab-predominant RIC used in 11 patients; overall poor outcomes highlight continued need for optimised conditioning protocols |
| [26073206](https://pubmed.ncbi.nlm.nih.gov/26073206/) | 2015 | Retrospective Cohort | Pediatr Transplant | HSCT for hyper-IgM syndrome due to CD40L defects (n=5); demonstrates curative potential of HSCT across the combined immunodeficiency spectrum |
| [18940685](https://pubmed.ncbi.nlm.nih.gov/18940685/) | 2008 | Retrospective Cohort | Biol Blood Marrow Transplant | Campath-1H (alemtuzumab) + fludarabine sub-myeloablative regimen rescued SCT graft failure in 12 children including 4 with SCID; all achieved successful engraftment |
| [19471859](https://pubmed.ncbi.nlm.nih.gov/19471859/) | 2009 | Case Report | Immunol Res | FOXP3⁺ regulatory T-cell reconstitution following alemtuzumab-conditioned BMT for IPEX syndrome; demonstrates durable immune reconstitution as a functional endpoint |
| [11841458](https://pubmed.ncbi.nlm.nih.gov/11841458/) | 2002 | Case Report | Br J Haematol | Non-myeloablative alemtuzumab-based BMT in a 26-year-old adult with Wiskott-Aldrich syndrome; partial engraftment and immune restoration achieved — early feasibility signal in adult PID |
| [35065305](https://pubmed.ncbi.nlm.nih.gov/35065305/) | 2022 | Case Report | Clin Immunol | Diagnostic workup of bare lymphocyte syndrome type II (novel RFXANK mutation, MHC class II deficiency) presenting as SCID-like phenotype; contextualises the diagnostic breadth of combined immunodeficiency |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Safety Report | Haematologica | Infectious toxicity profile of alemtuzumab; essential safety reference for its use in immunocompromised HSCT candidates |

---

## Taiwan Market Information

Alemtuzumab is not registered in Taiwan. No marketing authorizations are on record with the TFDA, and no approved indication text is available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — humanized anti-CD52 monoclonal antibody (IgG1κ); profound lymphodepletion is the intended therapeutic mechanism, not non-selective DNA damage |
| Myelosuppression Risk | High — sustained, severe lymphopenia is the desired pharmacological effect; pancytopenia and markedly increased susceptibility to opportunistic infections (CMV, EBV, fungal) are expected sequelae |
| Emetogenicity Classification | Low — monoclonal antibodies carry minimal direct emetogenic potential; infusion-related reactions (rigors, fever, hypotension) are the more common acute adverse events |
| Monitoring Items | CBC with differential and lymphocyte subsets (CD4, CD8, NK), CMV and EBV viral loads (PCR), liver function tests, renal function, galactomannan / β-D-glucan (fungal surveillance), and donor chimerism post-HSCT |
| Handling Protection | Follow institutional protocols for biological agents and cytotoxic drugs; standard PPE required; consult pharmacy for preparation and administration guidelines |

---

## Safety Considerations

TFDA product insert (仿單) warnings, contraindications, and Taiwan-specific drug interaction data are not available for this evidence pack. Please refer to the current EMA Summary of Product Characteristics (SmPC) for Alemtuzumab (Lemtrada / MabCampath) for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alemtuzumab-based RIC conditioning for HSCT in combined immunodeficiency is backed by one completed Phase 2/3 trial (NCT01019876, n=38), multiple Phase 2 studies, and several retrospective multi-centre cohorts documenting its use as a standard lymphodepleting backbone — placing the overall evidence at L2. The mechanistic rationale (CD52-targeted lymphodepletion enabling donor stem cell engraftment with reduced GvHD risk) is direct, biologically sound, and clinically well-established at leading transplant centres worldwide.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA product insert (仿單) to establish Taiwan-specific warnings, contraindications, and precautions
- Confirm mechanism of action data via DrugBank API query (DB00087) to complete the mechanistic dossier
- Clarify the termination rationale for NCT00579137 (n=3) and NCT01182675 (n=7) — determine whether termination was due to safety signals or poor accrual
- Conduct a structured comparison of alemtuzumab-based RIC versus ATG-based or thiotepa-based alternatives to define the optimal conditioning backbone by SCID sub-type
- Establish route-of-administration compatibility and pharmacy infrastructure for IV alemtuzumab in the HSCT conditioning setting in Taiwan
- Define patient eligibility boundaries (age, donor match grade, specific PID genotype) based on sub-group outcomes from existing cohort data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

