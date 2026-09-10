---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
---

# Pravastatin
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a well-established HMG-CoA reductase inhibitor (statin), classically used to treat hypercholesterolemia and dyslipidemia. The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with **1 clinical trial** and **13 publications** currently retrieved, though the underlying mechanistic rationale is notably weaker than for typical (heterozygous) familial hypercholesterolemia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (no EU license entries); Pravastatin is a statin (HMG-CoA reductase inhibitor), classically indicated for hypercholesterolemia/dyslipidemia |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, Pravastatin is a hydrophilic HMG-CoA reductase inhibitor (statin class). Its efficacy in hypercholesterolemia/dyslipidemia is well established, acting primarily through upregulation of hepatic LDL receptors (LDLR), which increases clearance of circulating LDL cholesterol.

Homozygous Familial Hypercholesterolemia (HoFH) results from near-complete loss of functional LDL receptors (biallelic LDLR, APOB, or PCSK9 mutations). Because statins depend on residual LDLR activity to lower LDL-C, their efficacy in HoFH is inherently limited — statins are typically used only as adjunct therapy alongside LDL-apheresis or PCSK9 inhibitors (e.g., alirocumab), rather than as primary treatment. This is reflected in the evidence pack: the sole retrieved clinical trial (NCT03510715) actually evaluates alirocumab, not pravastatin, in pediatric HoFH patients, and no literature directly demonstrates pravastatin monotherapy efficacy in HoFH. The mechanistic rationale is therefore considerably weaker than for classical (heterozygous) familial hypercholesterolemia, where residual LDLR function allows statins to act more directly.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (not pravastatin) in children/adolescents (8–17y) with HoFH on background therapy, assessing LDL-C reduction at Week 12. Relevance graded "C" — pravastatin is not the studied agent. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of statin therapy (incl. pravastatin) in pediatric familial hypercholesterolemia; HoFH-specific data limited |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidemia management guideline; positions statins as background therapy in severe hypercholesterolemia including HoFH |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | In vitro (iPSC hepatocyte) | Stem Cell Res Ther | iPSC-derived LDLR-deficient hepatocyte model for FH enabling CRISPR correction studies; mechanistic relevance to HoFH LDLR biology |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Genetics/Case study | Iran Biomed J | Identifies novel LDLRAP1 splice-site variant causing autosomal recessive FH; illustrates genetic basis of HoFH-spectrum disease |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review noting pravastatin was inferior to atorvastatin/simvastatin/rosuvastatin in LDL-lowering trials — comparator evidence, not HoFH-specific |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin review listing HoFH among statin-class indications for LDL-C reduction |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Review of ezetimibe, often combined with statins in refractory hypercholesterolemia including HoFH |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Ezetimibe as add-on to statins for patients not reaching LDL-C goals — relevant to HoFH combination-therapy context |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology/therapeutic review of atorvastatin in hyperlipidemias; comparator statin, not pravastatin/HoFH-specific |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Review of atorvastatin in primary hypercholesterolemia and mixed dyslipidemias; comparator statin literature |

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are flagged as a Blocking data gap — DG001 — and could not be retrieved for this evidence pack.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.95%) for HoFH, the mechanistic rationale is weak — HoFH patients have near-complete LDLR deficiency, which limits statins' primary mode of action, and the only retrieved clinical trial actually studies alirocumab rather than pravastatin. Evidence level is L3 (indirect/background literature), the drug has no recorded EU marketing authorization in this dataset, and a Blocking safety data gap (DG001) prevents any S1 safety screening.

**To proceed, the following is needed:**
- TFDA/EMA SmPC warnings and contraindications (Blocking gap DG001)
- Confirmed mechanism of action data (High-severity gap DG002)
- Pravastatin-specific (not just statin-class) efficacy/safety data in HoFH, ideally as an adjunct to PCSK9 inhibitors/apheresis
- Verification of current EU marketing/authorization status (currently 0 licenses on record)

**Note:** This same evidence pack contains a related, more mechanistically sound candidate — *hypercholesterolemia, autosomal dominant* (rank 6) — with **L1 evidence** and a **"Proceed with Guardrails"** recommendation, since this indication (classical LDLR/APOB/PCSK9-driven FH, typically heterozygous) directly matches pravastatin's established LDLR-upregulation mechanism. That candidate may warrant separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

