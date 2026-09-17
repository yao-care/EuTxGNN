---
layout: default
title: Posaconazole
parent: Medium Evidence (L3-L4)
nav_order: 478
evidence_level: L3
indication_count: 10
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

Using the report template requirements below, here is the evaluation report generated directly from the Evidence Pack.

---

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

> Posaconazole is a triazole antifungal already used for prophylaxis of invasive Aspergillus and Candida infections in high-risk immunocompromised patients (e.g., allogeneic stem-cell transplant / GVHD populations).
> The TxGNN model predicts it may also be effective against **Pneumocystosis (Pneumocystis jirovecii pneumonia)**,
> currently supported by **2 clinical trials (both indirect)** and **5 publications (mostly guidelines/reviews)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of invasive fungal infections (invasive aspergillosis/candidiasis) in high-risk immunocompromised patients — no formal license text available in this evidence pack |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia, PCP) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Posaconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol synthesis essential for fungal cell membrane integrity. Although its established use centers on invasive Aspergillus and Candida infections, it also has theoretical activity against *Pneumocystis jirovecii*, an atypical fungus that shares this same enzymatic target.

In clinical practice, posaconazole is already used off-label/adjacently as prophylaxis against invasive fungal disease — including Pneumocystis pneumonia — in high-risk populations such as allogeneic hematopoietic stem cell transplant recipients and patients with graft-versus-host disease (GVHD). This makes the TxGNN prediction mechanistically plausible: it is less a "novel" repurposing and more a formal recognition of an indication class the drug already touches.

However, posaconazole is **not** considered standard therapy for active PCP treatment — trimethoprim-sulfamethoxazole (TMP-SMX) remains first-line. The clinical trial and literature evidence currently available reflects this: it largely concerns prophylaxis in transplant/GVHD populations rather than a direct treatment trial of posaconazole against PCP.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Evaluates IV rezafungin (not posaconazole) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic transplant recipients. **Relevance: Grade C** — different drug, same disease area only. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD-prophylaxis drug combinations in mismatched unrelated donor transplant recipients — a population where posaconazole is a standard antifungal prophylactic agent. **Relevance: Grade B** — indirect; posaconazole not the primary study intervention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | Lancet Infect Dis | British Society for Medical Mycology 2025 update on diagnosis of serious fungal disease. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review/Guideline | Chin J Tuberc Respir Dis | 2025 Chinese clinical guideline on diagnosis/management of invasive pulmonary fungal disease. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and PCP; notes posaconazole prophylaxis reduces invasive candidiasis in high-risk hemato-oncology patients. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | Retrospective review of infectious complications (including fungal) in acute GVHD after liver transplantation. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK) | Clin Pharmacokinet | Reviews pulmonary epithelial lining fluid penetration of antifungal agents, including posaconazole. |

---

## EU Market Information

No marketing authorizations are recorded in this evidence pack (`total_licenses = 0`, market status: Not Marketed). Formal indication text cannot be extracted from local regulatory sources.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Key warnings, contraindications, and DDI data are all marked as missing in this evidence pack — this is flagged as a **Blocking** data gap (DG001), meaning a formal safety pre-screen (S1) cannot currently be completed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L3, but both cited trials are indirect (Grade B/C relevance — neither studies posaconazole as the primary intervention for pneumocystosis), and there is no formal SmPC/warning data available (Blocking gap DG001). The drug also has zero current marketing authorizations in the target jurisdiction. Combined, this is insufficient to move past the research-question stage.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, contraindications, and DDI data (DG001 — Blocking; source: official label PDF)
- Formal MOA and original indication text via DrugBank API (DG002)
- Direct clinical evidence evaluating posaconazole itself (not surrogate agents like rezafungin) for PCP prophylaxis or treatment efficacy
- Confirmation of regulatory pathway, given the drug is not currently marketed in this jurisdiction

*Note: Ranks 3–10 in this prediction set (leprosy, hypertrichosis, Dandy-Walker syndrome, periodontal malformation syndromes, etc.) are flagged by the evidence pack itself as mechanistically implausible (antifungal drug vs. non-fungal/genetic conditions) with no supporting trials or literature — these are model-noise and are already correctly scored L5/Hold and excluded from further consideration.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

