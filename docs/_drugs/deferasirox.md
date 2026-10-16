---
layout: default
title: Deferasirox
parent: Medium Evidence (L3-L4)
nav_order: 179
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Deferasirox: predicted new indication HIV infectious disease (evidence level L4). Approved use: Chronic iron overload due to frequent blood transfusions in beta thal…"
monitor_inn: "Deferasirox"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "beta-thalassemia with other manifestations", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Deferasirox
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

# Deferasirox: From Transfusional Iron Overload to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator, originally used to treat chronic iron overload caused by blood transfusions in beta thalassaemia and other anaemias.
The TxGNN model predicts it may be effective for **HIV infectious disease**,
but there are currently **0 clinical trials** and only **2 publications** (one preclinical study and one general drug overview), so this remains a research hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic iron overload due to frequent blood transfusions in beta thalassaemia major (aged 6 years and older), and in other settings where deferoxamine is contraindicated or inadequate (other anaemias, non-transfusion-dependent thalassaemia syndromes) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, deferasirox is an iron chelator: it binds excess iron and helps remove it from the body. Its efficacy in iron overload is established, and its use there is the basis of its marketing authorizations.

The link to HIV is indirect and rests on iron homeostasis. Iron availability is known to influence HIV-1 replication. A 2021 preclinical study (PMID 34550543) reported that iron in endolysosomes restricts Tat-mediated HIV-1 LTR transactivation. This suggests that iron status affects the virus, but it does not show that deferasirox treats HIV. The study also points to iron *restricting* Tat activity, so the direction of any therapeutic effect is not clear. No clinical trials exist, and the other cited paper is a general new-drug overview that provides no HIV evidence.

### Other Predictions (Context Only)

The other top-ranked predictions have even less support:

- **Chronic hepatitis C infection** (99.39%): Iron overload is common in chronic hepatitis C and may worsen liver injury, so chelation is conceptually plausible. The only cited paper is a methodological study of ferritin and hemosiderin iron, with no data on deferasirox. Evidence level L5.
- **Beta-thalassaemia with other manifestations, hereditary pyropoikilocytosis and pyruvate kinase deficiency** (98.5–98.6%): These are anaemias with iron overload that largely overlap with the existing label. They are not true repurposing candidates. No specific data were provided, so these are classed as L4 (mechanism-based only).
- **Neurodevelopmental disorder, obsolete familial combined hyperlipidemia, dermatofibrosarcoma protuberans, simian immunodeficiency virus infection and feline AIDS**: These are model predictions only, with no mechanistic rationale or evidence provided. The last two are animal diseases and are not relevant to human repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclinical/In vitro | Journal of Neurovirology | Endolysosomal iron restricts Tat-mediated HIV-1 LTR transactivation by increasing Tat oligomerization and β-catenin expression; relevant to HIV-associated neurocognitive disorder |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Review | Journal of the American Pharmacists Association | General overview of new drugs, including deferasirox; not specific evidence for HIV |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005014 | Deferasirox Mylan | Not stated | Deferasirox Mylan is indicated for the treatment of chronic iron overload due to frequent blood transfusions (≥7 ml/kg/month of packed... |
| EMEA/H/C/005156 | Deferasirox Accord | Not stated | Deferasirox Accord is indicated for the treatment of chronic iron overload due to frequent blood transfusions (≥7 ml/kg/month of packed... |
| EMEA/H/C/000670 | Exjade | Not stated | Exjade is indicated for the treatment of chronic iron overload due to frequent blood transfusions (≥7 ml/kg/month of packed red blood... |

All three authorizations are listed as cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. Major-level examples include hydrocortisone, dexamethasone, betamethasone, triamcinolone, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide and acetylsalicylic acid. Moderate-level examples include rabeprazole, pioglitazone, clarithromycin, aluminum hydroxide, aprepitant, saxagliptin, alosetron, cisapride and dexfenfluramine.
- **Knowledge-graph contraindication signals** (from a drug-disease knowledge graph, not from label text): liver failure, liver disease, cirrhosis, kidney disease, impaired renal function, thrombocytopenia, neutropenia, agranulocytosis, anaemia, hyperbilirubinemia, Gilbert syndrome, gallbladder disease, active peptic ulcer disease, ocular hypertension, multiple organ dysfunction syndrome and cancer. These should be verified against the official label.

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but no clinical trials, and its only supporting study is an in vitro paper with an indirect iron-homeostasis link. All EU authorizations are currently cancelled, and label-level safety data are missing. The evidence supports a research question, not a development decision.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Label warnings and contraindications from the SmPC (for safety screening)
- Direct preclinical data on deferasirox in HIV models, to establish the direction and size of any effect
- A safety assessment for people living with HIV, given the knowledge-graph signals for liver, kidney and blood-cell disorders and the major interactions listed above
- Clarification of why the EU authorizations were cancelled and whether this affects feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

