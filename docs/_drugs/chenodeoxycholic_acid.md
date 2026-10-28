---
layout: default
title: Chenodeoxycholic Acid
parent: AI Predictions (L5)
nav_order: 145
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Chenodeoxycholic Acid: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Inborn errors of primary bile acid synthesis due to sterol 27-hydroxy…"
monitor_inn: "Chenodeoxycholic acid"
predicted_indications: ["homozygous familial hypercholesterolemia", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "obsolete familial combined hyperlipidemia", "obsolete hyperuricemia (disease)"]
---

# Chenodeoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Chenodeoxycholic Acid: From Cerebrotendinous Xanthomatosis to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Chenodeoxycholic acid (CDCA) is a bile acid originally authorised in the EU to treat inborn errors of primary bile acid synthesis caused by sterol 27-hydroxylase deficiency (cerebrotendinous xanthomatosis, CTX).
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but there are **no registered clinical trials** and only **1 publication** (a CTX review, not a study in this disease) linked to this prediction.
The prediction rests mainly on model-based network proximity and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inborn errors of primary bile acid synthesis due to sterol 27-hydroxylase deficiency (CTX), ages 1 month to 18 years and adults |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, CDCA is an endogenous bile acid and a potent agonist of the farnesoid X receptor (FXR). Through FXR it suppresses hepatic bile acid and cholesterol synthesis by negative feedback on enzymes such as CYP7A1 and CYP8B1. In CTX, this reduces the accumulation of cholestanol and other cholesterol-derived metabolites.

CTX and homozygous familial hypercholesterolemia are both inherited disorders of lipid/sterol metabolism, which gives a conceptual link. However, the link is indirect. CDCA is not an established lipid-lowering therapy, and it can raise LDL cholesterol in some settings, such as gallstone dissolution. The only linked publication is a CTX review, not a study in familial hypercholesterolemia.

The high model score is likely driven by shared lipid/sterol metabolism network proximity rather than direct evidence. The prediction should be regarded as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Review | Orphanet J Rare Dis | Comprehensive review of CTX: a CYP27A1 (sterol 27-hydroxylase) mutation reduces bile acid synthesis and causes cholestanol accumulation in tissues. It addresses CTX, not familial hypercholesterolemia. |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004061 (cancelled) | Chenodeoxycholic acid Leadiant (previously Chenodeoxycholic acid sigma-tau) | Not specified | Inborn errors of primary bile acid synthesis due to sterol 27 hydroxylase deficiency (presenting as cerebrotendinous xanthomatosis (CTX)) in infants, ch... |

---

## Safety Considerations

- **Disease associations of concern (knowledge graph, not label text)**: The drug-disease contraindication links in the TxGNN knowledge graph include liver disease, gallbladder disease, diarrheal disease, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, sclerosing cholangitis, primary biliary cholangitis and Reynolds syndrome. These come from the knowledge graph rather than a product label and need confirmation against the SmPC.
- **Drug Interactions**: 56 interactions were identified, and all 20 listed in the data compiled for this report are rated Moderate. Main ones:
  - Bile acid sequestrants: cholestyramine, colestipol, colesevelam
  - Aluminium hydroxide
  - Estrogens: ethinylestradiol, estradiol, conjugated estrogens
  - Lipid-lowering agents: gemfibrozil, fenofibrate, clofibrate, ezetimibe
  - Asparaginase products (*E. coli*, *Erwinia chrysanthemi*, calaspargase pegol)
  - Others: brentuximab vedotin, cannabidiol, anisindione, bedaquiline, clofarabine
- Higher doses of CDCA carry a hepatotoxicity risk, and CDCA may raise LDL cholesterol. Both are relevant to a lipid-disorder indication.

Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no disease-specific literature. The mechanistic link is only indirect, and CDCA can raise LDL cholesterol, which runs against the proposed use. The only EU authorisation has been cancelled.

**To proceed, the following is needed:**
- Mechanistic data (MOA) and an analysis of how FXR-mediated effects would affect LDL-C in familial hypercholesterolemia
- Preclinical or early clinical studies of CDCA in lipid disorders
- Current EU label warnings and contraindications (the cancelled SmPC) for a full safety assessment
- A hepatotoxicity risk assessment and a plan for managing the interactions with lipid-lowering drugs and bile acid sequestrants

---

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 4 | Familial combined hyperlipidemia (obsolete term) | 0.9934 | L5 | Plausible but unsupported; the disease term is obsolete. |
| 2, 3, 5, 6, 8, 9, 10 | COL4A1-related disorders, hyperuricemia (obsolete term) | 0.9927–0.9943 | L5 | No identified mechanistic link; the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

