---
layout: default
title: Estradiol
parent: AI Predictions (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Estradiol: predicted new indication Anovulation (evidence level L5). Approved use: Female contraception (Evra, for women aged 18 to 45)"
monitor_inn: "Estradiol"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "anovulation", "ovarian remnant syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 12", "partial trisomy/tetrasomy of the short arm of chromosome 5", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "luteoma of pregnancy", "partial autosomal trisomy/tetrasomy", "ovarian ectopic pregnancy"]
---

# Estradiol
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

# Estradiol: From Contraception and Gynaecological Conditions to Anovulation

## One-Sentence Summary

Estradiol is an estrogen hormone that appears in EU-authorised products for contraception, uterine fibroids and endometriosis.
The TxGNN model predicts it may be useful for **anovulation** (the top-ranked prediction, fragile X carrier syndrome, has no supporting evidence, so the best-supported prediction is reported here), with **2 clinical trials** and **about 20 publications** currently supporting this direction. Most of the publications are physiology reviews, not treatment studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Female contraception (Evra, for women aged 18 to 45) |
| Predicted New Indication | Anovulation (rank 2 of 10; the rank 1 prediction, symptomatic fragile X syndrome in female carriers, has no supporting evidence) |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L2 (provisional; the trial outcomes are unverified) |
| EU Market Status | Cancelled only (no currently valid authorisations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, estradiol is the main natural estrogen. It is part of the hypothalamic-pituitary-ovarian feedback axis that controls ovulation. Its efficacy in contraception and in gynaecological conditions such as uterine fibroids and endometriosis is established through the authorised products, and mechanistically it may be applicable to anovulation.

The link to anovulation is clearest in ovulation induction. Clomiphene citrate, a common ovulation-induction drug, can thin the endometrium and reduce cervical mucus quality through its antiestrogenic effects. Adding estradiol is a proposed way to offset these effects. Two registered trials test this idea, but neither has published results in the data compiled for this report. The supporting literature mainly describes the physiology of ovulation and PCOS rather than testing estradiol as a treatment.

The other predictions are weaker. Several chromosomal conditions (partial trisomy/tetrasomy) have no evidence or plausible mechanism. For ovarian remnant syndrome, luteoma of pregnancy and ovarian ectopic pregnancy, estradiol is more likely a diagnostic confounder or a risk factor than a treatment. Fragile X carrier symptoms and BPES-related ovarian insufficiency have a plausible indirect rationale (estrogen replacement in premature ovarian insufficiency), but this is an analyst inference with no supporting trials or literature.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | Randomised trial of clomiphene plus estradiol versus clomiphene alone for ovulation induction in infertile women; no results available |
| [NCT07398924](https://clinicaltrials.gov/study/NCT07398924) | N/A | Completed | 90 | Vaginal estradiol versus oral guaifenesin, alone or combined, during clomiphene ovulation induction; endpoints were endometrial thickness, cervical mucus and pregnancy rate; no outcome data provided |

## Literature Evidence

No randomised trials were identified. The most relevant publications are listed below (reviews and physiology articles).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16782289](https://pubmed.ncbi.nlm.nih.gov/16782289/) | 2006 | Review | Maturitas | Role of estrogens in ovarian stimulation and follicle development |
| [27566840](https://pubmed.ncbi.nlm.nih.gov/27566840/) | 2016 | Review | Human Reproduction Update | Interactions of androgens, FSH, AMH and estradiol in normal and polycystic ovaries |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Neuroendocrine control of ovulation; hypothalamic failure leads to anovulation |
| [22442260](https://pubmed.ncbi.nlm.nih.gov/22442260/) | 2012 | Review | Human Reproduction Update | Neuropeptides linking energy balance and ovulation |
| [15196714](https://pubmed.ncbi.nlm.nih.gov/15196714/) | 2004 | Review | Eur J Obstet Gynecol Reprod Biol | FSH and LH in ovulation induction for anovulatory disorders |
| [30388215](https://pubmed.ncbi.nlm.nih.gov/30388215/) | 2019 | Review | Biology of Reproduction | Biomarkers in abnormal uterine bleeding |

## EU Market Information

All three authorisations are cancelled.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000410 | Evra | Not specified | Female contraception. Evra is intended for women of fertile age. The safety and efficacy has been established in women aged 18 to 45 years. |
| EMEA/H/C/001213 | Zoely | Not specified | Oral contraception |
| EMEA/H/C/005267 | Ryeqo | Not specified | Treatment of moderate to severe symptoms of uterine fibroids; symptomatic treatment of endometriosis in women with previous medical or surgical treatment |

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The TxGNN knowledge graph links estradiol with possible contraindications in hypertension, liver failure and liver disease, gallbladder disease, kidney disease, congestive heart failure, epilepsy, diabetes mellitus and hyperglycaemia, inherited porphyria, hypothyroidism, adrenocortical insufficiency, systemic lupus erythematosus, asthma, osteoporosis, anxiety and neurotic disorders, and humoral hypercalcaemia of malignancy.
- **Drug Interactions**: 100 interactions were found. The ones shown are mostly Moderate, and one is Minor (cimetidine). They include antidiabetic drugs (acarbose, alogliptin, albiglutide, metformin, pioglitazone, acetohexamide, chlorpropamide, canagliflozin, dapagliflozin), corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), and others such as amoxicillin, aprepitant, clarithromycin and clotrimazole.

Please refer to the SmPC for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Anovulation is the only prediction with directly relevant trials, but the evidence is weak. One Phase 4 trial has an unknown status, the other is a non-phased trial, and neither has available results. The literature is mostly physiology reviews. No authorisation is currently valid in the EU, and the other nine predictions have no or implausible support.

**To proceed, the following is needed:**
- Published results from NCT02186782 and NCT07398924, or a systematic review of estradiol as an adjunct in clomiphene ovulation induction
- Mechanism of action data
- The official SmPC warnings and contraindications (required for the safety screening step)
- Clarification of whether a currently valid EU product and route of administration (for example vaginal) would be available
- A safety review of the knowledge-graph contraindications and drug interactions for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

