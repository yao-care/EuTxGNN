---
layout: default
title: Vildagliptin
parent: High Evidence (L1-L2)
nav_order: 646
evidence_level: L2
indication_count: 10
---

# Vildagliptin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Vildagliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor originally developed to improve glycemic control in **Type 2 Diabetes Mellitus**. Among the ten diseases TxGNN scored highest for this drug, most (ranks 1–8) are pure AI associations with zero supporting evidence and are explicitly flagged in the model's own rationale as lacking any mechanistic plausibility. The one candidate with real evidence is **Type 1 Diabetes Mellitus** (rank 10), supported by **1 completed randomized controlled trial**, several mechanistic/clinical studies, and preclinical data — this report focuses on that candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (consistently established across the literature in this pack; no formal EU/Taiwan marketing-authorization record is available in this dataset) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.37% (rank 6549 of all drug-disease pairs) |
| Evidence Level | L2 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** TxGNN's top 8 scoring predictions for vildagliptin (classic stiff person syndrome, focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and four lipodystrophy variants) each score >99.7% but have **zero** clinical trials or literature, and the pack's own mechanistic rationale for each explicitly states "no known mechanistic relevance to DPP-4 inhibition" — these are Hold/L5 by definition and are not discussed further. Rank 9 (pancreatic agenesis) returned literature but on inspection it concerns DPP-4 inhibitor *safety in existing T2DM patients*, not treatment of pancreatic agenesis. Type 1 Diabetes Mellitus (rank 10) is the only candidate with genuine supporting evidence and is used as the subject of this report.

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not provided directly in this Evidence Pack, but the literature consistently identifies vildagliptin as a selective, orally active DPP-4 inhibitor. By blocking degradation of the incretin hormones GLP-1 and GIP, it raises their circulating levels, enhances glucose-dependent insulin secretion, and suppresses inappropriate glucagon secretion — the mechanism underlying its approved use in Type 2 Diabetes.

Type 1 Diabetes Mellitus is pathophysiologically distinct (autoimmune β-cell destruction vs. insulin resistance in T2DM), so the rationale is not a simple "same disease family" argument. Instead, several mechanistic and clinical studies in this pack suggest incretin-pathway modulation may have direct relevance in T1DM: vildagliptin has been shown to sustain glucagon counterregulation during hypoglycemia and suppress glucagon during hyperglycemia in T1DM patients (PMID 22855332), and a double-blind RCT combining vildagliptin with rapamycin investigated whether this combination could restore residual β-cell function in long-standing T1DM (PMID 33124663). Preclinical rodent studies further report β-cell neogenesis and reduced oxidative stress with vildagliptin in T1DM models (PMID 25395211, 23523961).

A caveat is important: the ClinicalTrials.gov result set returned by the knowledge-graph query for "Type 1 Diabetes Mellitus" contained 50 trials, but the large majority (e.g., NCT00099918, NCT00120536, NCT00106340) are standard vildagliptin-in-T2DM trials that appear to be mislabeled by the knowledge graph rather than genuine T1DM studies — this is explicitly flagged in the source rationale. Only a small subset of trials and publications genuinely concern T1DM populations; these are the ones presented below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06021119](https://clinicaltrials.gov/study/NCT06021119) | Phase 3 | Completed | 50 | Add-on vildagliptin to reduce Ramadan Iftar-related glycemic excursions in adolescents/young adults with T1DM on the MiniMed™ 780G advanced hybrid closed-loop system |
| [NCT01147276](https://clinicaltrials.gov/study/NCT01147276) | Phase 4 | Completed | 28 | Examines whether DPP-4 inhibition with vildagliptin affects the glucagon counterregulatory response to hypoglycemia in T1DM |
| [NCT06348706](https://clinicaltrials.gov/study/NCT06348706) | Phase 3 | Completed | 60 | Effect of DPP-4 inhibitor supplementation on non-alcoholic steatohepatitis (NASH) in adolescents with T1DM |

*Note: The remaining trials returned by the knowledge graph for this disease (e.g., NCT00099918, NCT04916093, NCT00120536) are Type 2 Diabetes trials and were excluded here as likely mislabeling artifacts — see rationale above.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT (double-blind) | J Clin Endocrinol Metab | Rapamycin plus vildagliptin investigated for restoring β-cell function in long-standing T1DM |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | RCT | Diabetes Obes Metab | Vildagliptin add-on therapy evaluated for MMP-14 levels, liver stiffness, and subclinical atherosclerosis in adolescents with T1DM and NASH |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Clinical study | Horm Metab Res | Effect of vildagliptin on glucagon concentration during meals in patients with T1DM |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | Cohort/Interventional | Diabetol Metab Syndr | Adjunctive oral vildagliptin mitigates Iftar-related glycemic excursions in T1DM adolescents/young adults on closed-loop insulin therapy |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | Mechanistic clinical study | J Clin Endocrinol Metab | Vildagliptin reduces glucagon during hyperglycemia and sustains glucagon counterregulation during hypoglycemia in T1DM |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Review | Expert Opin Investig Drugs | Reviews DPP-4 inhibitors' role in modulating β-cell function in T1DM and in diabetic kidney disease |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Preclinical (animal) | Curr Pharm Biotechnol | Vildagliptin induces β-cell neogenesis and improves lipid profile in a later phase of experimental T1DM |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Preclinical (animal) | Arch Med Res | Vildagliptin ameliorates oxidative stress and pancreatic β-cell destruction in T1D rats |
| [29510081](https://pubmed.ncbi.nlm.nih.gov/29510081/) | 2018 | Preclinical (animal) | Can J Physiol Pharmacol | Vildagliptin/pioglitazone combination improved overall glycemic control in T1D rats |
| [30333575](https://pubmed.ncbi.nlm.nih.gov/30333575/) | 2018 | Preclinical (animal) | Scientific Reports | Oral DPP-4 inhibitor plus quercetin formulation improves metabolic homeostasis in T1D rats |

---

## EU Market Information

No EU or Taiwan marketing authorization records for vildagliptin are present in this Evidence Pack (`market_status`: Not marketed, `total_licenses`: 0). This should be independently verified against current EMA/national registers before proceeding, as it directly affects the feasibility of any label-extension pathway.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is genuine, if limited, evidence for vildagliptin in T1DM — including one double-blind RCT (rapamycin + vildagliptin) and consistent mechanistic data on glucagon counterregulation and β-cell preservation — which distinguishes it clearly from the other nine candidates in this pack, all of which are unsupported AI associations or tangential safety-only literature. However, a **Blocking** data gap on TFDA/EMA warnings and contraindications (DG001) currently prevents a full safety review, and the drug's marketing status in this jurisdiction is unresolved.

**To proceed, the following is needed:**
- Resolve DG001: obtain SmPC/label warnings and contraindications for vildagliptin from EMA
- Resolve DG002: confirm formal mechanism-of-action documentation via DrugBank API
- Confirm current EU/Taiwan marketing authorization status (dataset shows "Not marketed," which should be cross-checked)
- Manually re-verify the knowledge-graph disease tagging on the excluded T2DM-labeled trials, since a majority of automatically returned "T1DM" trials were mislabeled T2DM studies
- Assess feasibility given the small sample sizes of the directly relevant trials (N=28–60)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

