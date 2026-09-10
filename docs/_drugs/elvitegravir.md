---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Elvitegravir
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

# Elvitegravir: From HIV-1 Infection to Congenital Human Immunodeficiency Virus

## One-Sentence Summary

Elvitegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), established as part of combination antiretroviral regimens for HIV-1 infection treatment. Among the ten TxGNN-predicted indications, several top-ranked outputs (simian/feline immunodeficiency virus, an unrelated rare neurodevelopmental disorder) are non-human or mechanistically implausible artifacts with no supporting evidence; the most clinically credible signal is **Congenital Human Immunodeficiency Virus** (rank 4, within the same disease family as the approved use), supported by **12 clinical trials** and **8 publications**, most focused on INSTI safety/efficacy in pregnancy and pediatric populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (integrase strand transfer inhibitor class) — not confirmable from EU license text as the drug is not currently marketed in the EU dataset; inferred from pharmacological class per literature evidence |
| Predicted New Indication | Congenital Human Immunodeficiency Virus |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on known information from the supporting literature, elvitegravir is an HIV-1 integrase inhibitor that blocks strand transfer during proviral DNA integration, and its efficacy against HIV-1 has been established as part of fixed-dose combination regimens (e.g., with cobicistat/emtricitabine/tenofovir).

Congenital HIV infection (perinatal/vertical mother-to-child transmission) is not a distinct pathogen or mechanism — it is the same HIV-1 disease process in a specific transmission context. Because elvitegravir's approved mechanism directly targets HIV-1 replication, applicability to prevention/treatment of congenital HIV is mechanistically sound rather than a cross-mechanism extrapolation.

It is worth noting that TxGNN's top-scored outputs for this drug (ranks 1–3: simian immunodeficiency virus infection, feline acquired immunodeficiency syndrome, and an unrelated rare neurodevelopmental disorder) are not viable human indications — they reflect either animal-model research contexts or embedding-similarity noise, and none carry supporting clinical evidence. Rank 4 (congenital HIV) is the highest-ranked prediction with an actual evidence base and a "Proceed with Guardrails" scoring outcome, making it the most defensible candidate to evaluate further. A caveat: the clinical trials retrieved are largely general adult HIV-1 populations (switch/maintenance studies) rather than trials specifically enrolling perinatally-infected or pregnant/neonatal subjects, so the ontology label and trial population are not fully matched.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01854775](https://clinicaltrials.gov/study/NCT01854775) | Phase 2/3 | Completed | 129 | PK, safety and antiviral activity of E/C/F/TAF single-tablet regimen (contains elvitegravir) in ART-naive adolescents and virologically suppressed children |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A (Phase 4) | Completed | 1578 | IMPAACT P1026s: pharmacokinetics of antiretroviral/TB drugs in pregnant women and infants, relevant to prevention of mother-to-child transmission |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | Switch to dolutegravir + rilpivirine non-inferiority vs. continuing INI/NNRTI/PI regimen in virologically suppressed HIV-1 adults |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | FLAIR study: long-acting IM cabotegravir + rilpivirine for maintaining suppression after switching from an INSTI single-tablet regimen |
| [NCT04442737](https://clinicaltrials.gov/study/NCT04442737) | Phase 4 | Completed | 103 | Safety/tolerability of switching to D/C/F/TAF vs. continuing INI+TAF/FTC in patients with rapid weight gain |
| [NCT01568892](https://clinicaltrials.gov/study/NCT01568892) | Phase 3 | Completed | 30 | Antiviral activity of dolutegravir in INSTI-experienced, resistant HIV-1 adults (includes raltegravir/elvitegravir failures) |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Switch to dolutegravir + rilpivirine non-inferiority study (companion trial to NCT02422797) |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3b | Active, not recruiting | 1049 | ATLAS-2M: long-acting cabotegravir + rilpivirine every 8 vs. 4 weeks in virologically suppressed HIV-1 adults |
| [NCT02397096](https://clinicaltrials.gov/study/NCT02397096) | Phase 3 | Completed | 673 | Switch to doravirine/lamivudine/tenofovir (MK-1439A) from a boosted PI + 2 NRTI regimen |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS study: switch to long-acting IM cabotegravir + rilpivirine from current INSTI/NNRTI/PI regimen |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37307279](https://pubmed.ncbi.nlm.nih.gov/37307279/) | 2023 | Cohort | PLoS One | Compared congenital malformation and preeclampsia incidence in pregnancies exposed to INSTI vs. non-INSTI antiretroviral therapy |
| [30531300](https://pubmed.ncbi.nlm.nih.gov/30531300/) | 2019 | Cohort/Surveillance | J Acquir Immune Defic Syndr | UK/Ireland surveillance of congenital anomalies after raltegravir or elvitegravir exposure during pregnancy (2008–2018) |
| [38864586](https://pubmed.ncbi.nlm.nih.gov/38864586/) | 2024 | Cohort | AIDS | Characterized congenital anomaly associations with first-trimester exposure to newer antiretroviral agents in a US cohort of HIV-exposed infants |
| [33048878](https://pubmed.ncbi.nlm.nih.gov/33048878/) | 2021 | Cohort | AIDS | Evaluated birth defect and perinatal outcome risk after INSTI exposure at conception, following the dolutegravir neural tube defect signal |
| [39086081](https://pubmed.ncbi.nlm.nih.gov/39086081/) | 2024 | Pharmacovigilance | Pharmacol Res Perspect | VigiBase disproportionality analysis of INSTI-class drugs and congenital anomaly signals during pregnancy |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | Clin Infect Dis | Analysis of multiple pharmacovigilance databases for dolutegravir/INSTI safety signals in pregnancy |
| [31021990](https://pubmed.ncbi.nlm.nih.gov/31021990/) | 2019 | Review | J Acquir Immune Defic Syndr | Reviews the WHO safety signal on neural tube defects and evidence gaps for other INSTIs, including elvitegravir, in pregnancy |
| [35809963](https://pubmed.ncbi.nlm.nih.gov/35809963/) | 2022 | Case Report | Chest | Case of a 28-year-old man with congenital HIV presenting with diffuse bilateral pulmonary nodules |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are not available in this Evidence Pack — TFDA/EMA labelling review is required before any S1 safety assessment, per data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism (HIV-1 integrase inhibition) is directly aligned with the predicted indication, and multiple cohort studies specifically evaluate INSTI-class safety in pregnancy/perinatal contexts, giving genuine (if indirect) evidentiary support (L2). However, none of the retrieved Phase 3 trials specifically enroll congenitally/perinatally-infected patients, and core safety/MOA data are missing, so guardrails are needed before advancing.

**To proceed, the following is needed:**
- TFDA/EMA SmPC warnings, contraindications, and DDI data (blocking gap, DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Clarification of EU marketing authorization status, since current data shows elvitegravir as not marketed in the EU
- Trial-level review to confirm whether any of the listed Phase 3 studies actually enrolled pregnant women or perinatally-infected pediatric patients, rather than general suppressed adults
- Pregnancy/pediatric-specific pharmacokinetic and safety data to support use in the congenital/vertical-transmission context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

