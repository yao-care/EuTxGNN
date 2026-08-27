---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2a (DrugBank DB00008) is a pegylated interferon-alpha antiviral agent historically developed and used for chronic hepatitis C virus infection. The TxGNN model also predicts it may be effective for **Hepatitis B Virus Infection**, with **50 clinical trials** and **20 publications** currently associated with this pairing. However, the depth of that evidence — including multiple completed Phase 3/4 trials that use peginterferon alfa-2a as an active "standard of care" comparator — suggests this is largely a **rediscovery of an already-established indication** rather than a genuinely novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (inferred from clinical trial/literature evidence; no formal TFDA/EMA license record is present in this registry) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (pending resolution of a Blocking safety data gap — see Conclusion) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Peginterferon alfa-2a is a pegylated recombinant interferon alfa-2a — part of the type I interferon class of antiviral/immunomodulatory agents. Its efficacy in chronic hepatitis C has been well established, and mechanistically it is plausible that the same activity would extend to chronic hepatitis B.

The proposed mechanistic link, drawn from the evidence base itself, is that interferon-alpha activates the JAK-STAT signalling pathway to induce interferon-stimulated genes (ISGs), which directly suppress HBV replication and promote immune-mediated clearance of hepatocytes harbouring cccDNA. Both hepatitis B and hepatitis C are hepatotropic viral infections targeted by the same broad-spectrum antiviral/immune-activating mechanism, which is the pharmacological basis for using one interferon formulation across both diseases.

Importantly, the scale of the clinical evidence base for this "prediction" is itself a signal worth flagging: many of the listed trials (e.g. head-to-head comparisons of PEGASYS vs. PEG-Intron, dose/duration optimisation studies, and combination regimens with entecavir/tenofovir) treat peginterferon alfa-2a as an **already-approved, guideline-recommended** therapy for chronic hepatitis B in the markets where those trials were run. In other words, TxGNN has largely reconstructed a known, globally approved indication (Pegasys is approved for chronic hepatitis B in the US, EU, and much of Asia-Pacific) rather than surfaced a new therapeutic hypothesis. The genuine open question for this specific registry is a **label/registration** one — whether the hepatitis B indication can be extended into the market tracked here — not a discovery question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01641926](https://clinicaltrials.gov/study/NCT01641926) | Phase 3 | Terminated | 402 | Multicenter, open-label comparison of PEG-Intron vs. PEGASYS in interferon-naïve HBeAg-positive and HBeAg-negative chronic hepatitis B; ended early. |
| [NCT00435825](https://clinicaltrials.gov/study/NCT00435825) | Phase 4 | Completed | 551 | 4-arm study of PEGASYS 90 vs. 180 mcg for 24 vs. 48 weeks; evaluated effect on HBeAg seroconversion and safety in HBeAg-positive chronic hepatitis B. |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | Peginterferon alfa-2a (48 wk) vs. adefovir dipivoxil (72 wk), both with initial lamivudine, in lamivudine-resistant HBeAg-positive chronic hepatitis B. |
| [NCT03181113](https://clinicaltrials.gov/study/NCT03181113) | N/A | Completed | 473 | Multicenter cohort assessing long-term benefit (HBsAg/HBeAg status, HBV DNA, ALT) for up to 5 years after standard peginterferon alfa therapy. |
| [NCT00877760](https://clinicaltrials.gov/study/NCT00877760) | Phase 4 | Completed | 184 | Evaluated whether a temporary peginterferon alfa-2a add-on to entecavir augments HBeAg seroconversion response. |
| [NCT01374308](https://clinicaltrials.gov/study/NCT01374308) | Phase 3 | Unknown | 160 | Compared a therapeutic HBV vaccine (NASVAC) against pegylated interferon monotherapy in chronic HBV infection. |
| [NCT00964665](https://clinicaltrials.gov/study/NCT00964665) | Phase 1/2 | Terminated | 141 | Dose-response and PK/PD evaluation in HBeAg-positive chronic hepatitis B, intended to support later Phase 3 design. |
| [NCT03957629](https://clinicaltrials.gov/study/NCT03957629) | N/A | Unknown | 186 | Combination tenofovir disoproxil fumarate + peginterferon alfa-2a vs. TDF alone in NA-experienced patients with HBV-related liver fibrosis. |
| [NCT01464281](https://clinicaltrials.gov/study/NCT01464281) | N/A | Unknown | 300 | Randomized study switching NA-treated patients (HBeAg loss, HBV DNA <200 IU/mL) to 48- vs. 96-week peginterferon alfa-2a for HBsAg clearance. |
| [NCT02732639](https://clinicaltrials.gov/study/NCT02732639) | Phase 3 | Completed | 31 | 48-week PEGASYS monotherapy in chronic hepatitis D (HBV/HDV co-infection setting), followed by 24-week treatment-free follow-up. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review/Meta-analysis | Antiviral Therapy | Individual-participant-data meta-analysis identifying optimal stopping rules for 40kD peginterferon alfa-2a therapy in chronic hepatitis B. |
| [15371578](https://pubmed.ncbi.nlm.nih.gov/15371578/) | 2004 | RCT | New England Journal of Medicine | Landmark RCT of peginterferon alfa-2a alone, lamivudine alone, and combination therapy in HBeAg-negative chronic hepatitis B. |
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | New England Journal of Medicine | Pivotal trial of peginterferon alfa-2a, lamivudine, and combination therapy for HBeAg-positive chronic hepatitis B. |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + peginterferon alfa-2a in HBeAg-positive immune-tolerant chronic HBV infection. |
| [29689122](https://pubmed.ncbi.nlm.nih.gov/29689122/) | 2018 | RCT (Phase 3) | Hepatology | PEG-B-ACTIVE study: peginterferon alfa-2a in HBeAg-positive immune-active children with chronic hepatitis B, randomized 2:1. |
| [22045673](https://pubmed.ncbi.nlm.nih.gov/22045673/) | 2011 | Cohort | Hepatology | Shorter durations/lower doses of peginterferon alfa-2a linked to inferior HBeAg seroconversion in genotypes B/C (n=544). |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Comprehensive review of chronic hepatitis B epidemiology, natural history, and treatment options including interferon-based therapy. |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Review of hepatitis B treatment goals and response monitoring across interferon and nucleos(t)ide analogue regimens. |
| [26198336](https://pubmed.ncbi.nlm.nih.gov/26198336/) | 2016 | Review | Gut and Liver | Reviews evidence for combining pegylated interferon with nucleos(t)ide therapy toward a functional cure of hepatitis B. |
| [16013986](https://pubmed.ncbi.nlm.nih.gov/16013986/) | 2005 | Review | Expert Opinion on Pharmacotherapy | Early review of peginterferon alfa-2a approval and trial data for chronic hepatitis B across the US, EU, and Asia-Pacific. |

---

## EU Market Information

No EU/TFDA marketing authorizations are currently on file for Peginterferon alfa-2a in this registry — market status is recorded as **未上市 (Not Marketed)** with **0 authorizations**. This is a real regulatory data point rather than a missing-data gap, and it should be confirmed against the current EMA product register before any registration decision is made.

---

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DDI query status: not found). Note that this is flagged in the data-gap log as a **Blocking** severity item (DG001 — TFDA label warnings/contraindications), meaning this candidate cannot formally enter the S1 safety screening stage until that data is obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The evidence level for hepatitis B virus infection is L1, supported by multiple completed Phase 3/4 trials (up to n=551), two pivotal NEJM RCTs, and a systematic review/meta-analysis on treatment stopping rules — this is a strong and mature evidence base.
- However, this evidence base largely reflects an **already-approved indication** for peginterferon alfa-2a (Pegasys) in comparator markets, so the practical question is one of label/registration extension rather than novel drug discovery.
- A **Blocking**-severity data gap (DG001: TFDA/EMA product label warnings and contraindications) currently prevents formal entry into the S1 safety review stage, and mechanism-of-action documentation (DG002, High severity) is also missing.

**To proceed, the following is needed:**
- Obtain the official EMA/TFDA Summary of Product Characteristics (SmPC) for Peginterferon alfa-2a (Pegasys) to resolve the Blocking gap (DG001) before any safety-stage review
- Query DrugBank/EMA for formal mechanism-of-action documentation to resolve the High-severity gap (DG002)
- Confirm current regulatory status in the target market to determine whether this candidate should be framed as a label-extension request rather than a novel repurposing submission
- Re-run the DDI query against a working data source (current query returned "not_found")
- QC the underlying TxGNN disease-node mapping — several lower-ranked predictions in this same evidence pack (e.g., "heart neoplasm," rank 8) show clear ontology-mapping errors, so any further reliance on this drug's other predicted indications should be manually verified first

---

*This report is generated for research purposes only and does not constitute medical advice. Repurposing candidates require full clinical validation and regulatory review before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

