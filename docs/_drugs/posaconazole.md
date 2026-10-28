---
layout: default
title: Posaconazole
parent: AI Predictions (L5)
nav_order: 494
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Noxafil gastro-resistant tablets are indicated for use in the treatme…"
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Posaconazole: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Posaconazole is a triazole antifungal, originally used to treat and prevent invasive fungal infections such as invasive aspergillosis, fusariosis and coccidioidomycosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the data compiled for this report contain **no clinical trials of posaconazole** for this condition and only **5 general publications**, none of which tests posaconazole against Pneumocystis. The prediction is therefore not supported by evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Noxafil gastro-resistant tablets are indicated for use in the treatment of the following fungal infections in adults (see sections 4.2 and 5.1): Invasive aspergillosis Noxafil gastro-resistant tablets are indicated for use in the treatment of the following fungal infections in paediatric patients fr |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Posaconazole is a triazole antifungal. Triazoles inhibit fungal CYP51 (lanosterol 14-alpha-demethylase) and thereby ergosterol synthesis. Its efficacy in invasive fungal infections is established.

The link to pneumocystosis is weak. *Pneumocystis jirovecii* lacks ergosterol and uses cholesterol-type sterols, so the azole mechanism is not expected to work. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Posaconazole penetrates lung epithelial lining fluid well, but that does not establish anti-Pneumocystis activity.

Other predictions in the top 10 are similarly weak:
- **Vulvovaginal candidiasis** is mechanistically plausible, since Candida species are sensitive to CYP51 inhibition. Evidence is limited to in vitro susceptibility studies, isolate surveys and guidelines, with no posaconazole clinical trials. Oropharyngeal candidiasis is already a labeled use.
- They look like TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin versus standard antimicrobial regimen for prevention of invasive fungal disease after allogeneic blood and marrow transplantation. It tests rezafungin (an echinocandin), not posaconazole, so it offers no direct evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Review | The Lancet Infectious Diseases | British Society for Medical Mycology recommendations for diagnosing serious fungal diseases |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review (guideline) | Zhonghua Jie He He Hu Xi Za Zhi | Chinese guideline on diagnosis and management of invasive pulmonary fungal diseases |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia. Notes that mould-active posaconazole prophylaxis reduced invasive fungal infections in high-risk haemato-oncology patients. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of anti-infective agents into pulmonary epithelial lining fluid |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Infectious complications of acute graft-versus-host disease after liver transplantation |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000610 | Noxafil | Not specified | Treatment of invasive aspergillosis, fusariosis, chromoblastomycosis and mycetoma, and coccidioidomycosis; prophylaxis of invasive fungal infections (tablets, infusion, oral suspension, powder for suspension)... |
| EMEA/H/C/005028 | Posaconazole AHCL | Not specified | Oral suspension for invasive aspergillosis, fusariosis, chromoblastomycosis and mycetoma, coccidioidomycosis, oropharyngeal candidiasis, and prophylaxis... |
| EMEA/H/C/005005 | Posaconazole Accord | Not specified | Invasive aspergillosis, fusariosis, chromoblastomycosis and mycetoma, coccidioidomycosis, and prophylaxis of invasive fungal infections... |

All three authorizations are valid, so posaconazole is currently marketed with valid authorization in the data compiled for this report.

## Safety Considerations

**Drug Interactions** (100 interactions recorded; examples of the main ones):
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, clarithromycin, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes)

Acid-suppressing drugs and corticosteroids appear frequently and should be reviewed in any development plan.

For warnings and contraindications, please refer to the SmPC. The prediction analysis also notes that azoles carry a teratogenic risk, which matters for any developmental or paediatric context.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pneumocystosis prediction has a high model score but no direct clinical evidence and no sound mechanistic basis, because Pneumocystis lacks ergosterol. The only trial found tests a different drug. Posaconazole is marketed, with 3 of 3 licences valid.

**To proceed, the following is needed:**
- Mechanism of action data to confirm or refute any anti-Pneumocystis activity
- In vitro or animal evidence of posaconazole activity against *Pneumocystis jirovecii*
- Review of the existing standard of care for Pneumocystis infection and a justification for any role for posaconazole
- Clarification of the current EU regulatory status and the reasons for the cancellations
- SmPC warnings and contraindications for a full safety assessment
- If a repurposing lead is wanted, consider vulvovaginal candidiasis in azole-refractory disease, which is mechanistically more plausible but needs clinical studies. It remains a research question only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

