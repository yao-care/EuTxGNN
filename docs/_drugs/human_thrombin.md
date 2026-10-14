---
layout: default
title: Human Thrombin
parent: AI Predictions (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Human Thrombin
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

# Human Thrombin: From Surgical Haemostasis to Esophageal Disease

## One-Sentence Summary

Human thrombin is the haemostatic component of fibrin-sealant products (TachoSil, VeraSeal), originally used as a supportive treatment in surgery where standard techniques are insufficient to control bleeding or seal tissue.
The TxGNN model's top-ranked prediction is **primary release disorder of platelets**, but it has no supporting studies. The best-supported prediction is **esophageal disease** (rank 8), which has **no registered clinical trials** and **11 publications**, mostly observational studies of endoscopic thrombin injection for varices.

> Note: The report covers the top-ranked prediction (rank 1) as the headline prediction, and additionally the most evidence-supported candidate (rank 8), because rank 1 has no evidence at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Supportive treatment in surgery for improvement of haemostasis, tissue sealing and suture support in vascular surgery where standard techniques are insufficient; supportive sealing of the dura mater (TachoSil) |
| Predicted New Indication | Primary release disorder of platelets (rank 1); best-supported alternative: esophageal disease (rank 8) |
| TxGNN Prediction Score | 96.95% (rank 1); 86.54% (esophageal disease, rank 8) |
| Evidence Level | L5 (rank 1); L3 (esophageal disease) |
| EU Market Status | Cancelled only (both authorizations cancelled) |
| Number of Authorizations | 2 (0 valid, 2 cancelled) |
| Recommended Decision | Hold (rank 1); esophageal disease is a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, thrombin is a key coagulation enzyme that converts fibrinogen to fibrin and is also a strong platelet agonist. In fibrin-sealant products it supports local clot formation.

**Rank 1 (primary release disorder of platelets):** The link is plausible only in principle, because thrombin activates platelets. Release disorders, however, involve defective platelet granule secretion or signalling, and exogenous thrombin would not be expected to correct an intrinsic platelet defect. It is also a topical or local agent, not a systemic therapy. The other high-scoring platelet and bleeding disorders (Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defects, Scott syndrome) share the same limitation. At most, topical thrombin might provide local fibrin-based support downstream of platelet function, which is speculative.

**Esophageal disease (rank 8):** Here the rationale is stronger. Endoscopic injection of human thrombin into gastric and esophageal varices promotes local clot formation and obliterates the varix. This is conceptually close to the original haemostatic use. Most of the data, however, concern gastric varices rather than esophageal disease, and endoscopic injection is an off-label route that differs from the approved topical surgical use.

Several other predictions (such as non-syndromic esophageal malformation and fetal and neonatal alloimmune thrombocytopenia) have no plausible mechanism and likely reflect graph proximity only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the rank 1 prediction or esophageal disease.

---

## Literature Evidence

**Rank 1 (primary release disorder of platelets):** Currently no related literature available.

**Esophageal disease (rank 8), selected publications:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37983812](https://pubmed.ncbi.nlm.nih.gov/37983812/) | 2024 | Comparative study (glue vs thrombin; design to be confirmed) | J Clin Gastroenterol | Endoscopic glue versus human thrombin injection for bleeding gastric varices |
| [24892515](https://pubmed.ncbi.nlm.nih.gov/24892515/) | 2014 | Cohort | Eur J Gastroenterol Hepatol | Endoscopic human thrombin appears simple and efficacious, with fewer complications than tissue adhesives; data limited |
| [30196518](https://pubmed.ncbi.nlm.nih.gov/30196518/) | 2018 | Review/Cohort | Indian J Gastroenterol | Human thrombin appears to be an effective new option for bleeding gastric varices; data sparse |
| [23139607](https://pubmed.ncbi.nlm.nih.gov/23139607/) | 2012 | Case series/Review | World J Gastroenterol | Efficacy of human thrombin in bleeding gastric and ectopic varices |
| [12094854](https://pubmed.ncbi.nlm.nih.gov/12094854/) | 2002 | Case series | Am J Gastroenterol | Experience with human thrombin in bleeding gastric varices |
| [2765808](https://pubmed.ncbi.nlm.nih.gov/2765808/) | 1989 | Prospective randomized study | Br J Surg | Human thrombin plus 5% ethanolamine oleate for sclerosing oesophageal varices in 50 cirrhotic patients |
| [16803599](https://pubmed.ncbi.nlm.nih.gov/16803599/) | 2006 | Review | Aliment Pharmacol Ther | Recent advances in managing bleeding gastric varices; tissue adhesives are first-line where available |
| [8807700](https://pubmed.ncbi.nlm.nih.gov/8807700/) | 1996 | Review | Scott Med J | Overview of variceal bleeding management |
| [12196788](https://pubmed.ncbi.nlm.nih.gov/12196788/) | 2002 | Open pilot study | Gastrointest Endosc | Human fibrin glue for acute bleeding from gastric varices |

**Glanzmann thrombasthenia (rank 2):** The only paper retrieved ([11964147](https://pubmed.ncbi.nlm.nih.gov/11964147/), 2002, Biochem J) is a basic-science study of thrombospondin-1 and the actin cytoskeleton in thrombin-activated platelets, not a clinical study.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/000505 | TachoSil | Not specified | Adults and children from 1 month of age: supportive treatment in surgery for improvement of haemostasis, to promote tissue sealing and for suture support in vascular su... | Cancelled |
| EMEA/H/C/004446 | VeraSeal | Not specified | Supportive treatment in adults where standard surgical techniques are insufficient: for improvement of haemostasis as suture support in vascular surgery | Cancelled |

---

## Safety Considerations

Please refer to the SmPC for safety information. No drug interaction records were found, and no knowledge-graph contraindications were identified.

---

## Conclusion and Next Steps

**Decision: Hold** (for the rank 1 prediction and the other platelet or bleeding disorder predictions); **esophageal disease is a research question** rather than a candidate ready to proceed.

**Rationale:**
- The top predictions rest on knowledge-graph scores alone, with no trials or literature, and there is no mechanism by which exogenous thrombin would correct intrinsic platelet defects.
- Esophageal disease has observational support (case series, cohorts, one 2024 comparative study) for endoscopic thrombin injection in varices, but the data mostly concern gastric varices, and the route is off-label. Both EU authorizations are cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and EU safety information (warnings, contraindications) from the product information
- For esophageal disease: confirmation of the design of the 2024 comparative study, and prospective or randomized data specific to esophageal varices
- Assessment of route compatibility (endoscopic injection versus approved topical use) and of an available, authorized thrombin product
- For the platelet and bleeding disorders: disease-specific evidence of any local haemostatic benefit before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

