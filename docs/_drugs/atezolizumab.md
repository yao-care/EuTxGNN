---
layout: default
title: Atezolizumab
parent: AI Predictions (L5)
nav_order: 67
evidence_level: L5
indication_count: 6
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-12
description: "Atezolizumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Locally advanced or metastatic urothelial carcinoma (after prior plat…"
---

# Atezolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Atezolizumab: From Urothelial Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Atezolizumab (Tecentriq) is an antibody-based cancer immunotherapy, originally approved in the EU for urothelial carcinoma and several lung, breast and liver cancers.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**,
but currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma (after prior platinum-containing chemotherapy, or cisplatin-ineligible, PD-L1 ≥ 5%); the label also covers NSCLC, small cell lung cancer, triple-negative breast cancer and hepatocellular carcinoma |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for atezolizumab: "PD L1 may be expressed on tumor cells and/or tumor infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD L1 to the PD 1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation and cytokine production. […] Atezolizumab is a monoclonal antibody that binds to PD L1 and blocks its interactions with both PD 1 and B7.1 receptors." ([DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee), label version 2026-10-13; accessed 2026-11-19.) Atezolizumab is generally known to be an antibody that blocks PD-L1, which restores T-cell activity against tumours. It has proven efficacy in several PD-L1-expressing cancers, so it may be mechanistically applicable to other tumours with immune infiltration.

The predicted disease is an adenocarcinoma of the female genital tract. PD-L1 blockade could plausibly act on such tumours, but this is speculative for this specific entity. The prediction comes from the model only. No study in the compiled data tests atezolizumab in uterine ligament adenocarcinoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004143 | Tecentriq | atezolizumab | Valid |

<!-- licenses:end -->

The authorisation covers single-agent use of Tecentriq in several cancers (urothelial carcinoma, early-stage and advanced NSCLC, ES-SCLC, TNBC, HCC). The uterine ligament adenocarcinoma prediction is not part of any of these approved indications.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 75 entries. The main ones in the data are:
  - **Major**: adalimumab, baricitinib, live BCG vaccine (Tice strain).
  - **Moderate**: systemic corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, methylprednisolone, betamethasone, budesonide, triamcinolone, deflazacort), azathioprine, alemtuzumab, anakinra, alefacept, roflumilast, and several vaccines (tetanus toxoid, anthrax, adenovirus type 4).

  Many of these are immunosuppressants or live vaccines, which can interfere with or be affected by immune-activating therapy.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies atezolizumab in uterine ligament adenocarcinoma, so the 0.9993 TxGNN score is an unsupported model prediction (Evidence Level L5). Another prediction in the same output, endocervical carcinoma, does have small early-phase atezolizumab trials registered. It would be a better candidate for a separate evaluation.

**To proceed, the following is needed:**
- Retrieve and review the EMA SmPC for warnings and contraindications, which is currently a blocking gap for safety screening
- Obtain mechanism of action data from DrugBank to support the mechanistic-link analysis
- Review the literature and trial registries for PD-L1 expression and immunotherapy outcomes in uterine ligament adenocarcinoma or closely related gynaecological adenocarcinomas
- Confirm the clinical need and disease definition, since this is a rare entity

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tecentriq (atezolizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

