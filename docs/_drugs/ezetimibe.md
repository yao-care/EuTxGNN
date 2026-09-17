---
layout: default
title: Ezetimibe
parent: High Evidence (L1-L2)
nav_order: 245
evidence_level: L1
indication_count: 10
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor originally developed for hypercholesterolemia and mixed dyslipidemia, typically used alone or combined with a statin.
The TxGNN model's top-ranked prediction is **Hyperlipoproteinemia**, with **50 clinical trials** and **19 publications** identified —
though as the evidence itself notes, this is essentially a validation of the drug's already-established core indication rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / Mixed Dyslipidemia (established use; no marketing-authorization license text available in this dataset) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the DrugBank record for this drug (data gap). Based on the evidence pack's own repurposing rationale, however, ezetimibe's known pharmacology is well established: it selectively inhibits the NPC1L1 (Niemann-Pick C1-Like 1) transporter at the intestinal brush border, blocking dietary and biliary cholesterol absorption and thereby lowering LDL-cholesterol.

Hyperlipoproteinemia is a broad clinical term for elevated lipoprotein/cholesterol levels — essentially the same disease space as ezetimibe's known, already-approved use. The evidence source itself flags this explicitly: this is the drug's **existing core indication surfacing as a high-confidence prediction**, not a new therapeutic direction. It functions as a sanity-check / positive-control case for the TxGNN model rather than a discovery.

Mechanistically the fit is direct and non-speculative: NPC1L1 inhibition reduces LDL-C, which is precisely the pathophysiological target in hyperlipoproteinemia. The same logic extends to the closely related "familial hypercholesterolemia" prediction (rank 2), where ezetimibe is already guideline-recommended as add-on therapy when statins alone are insufficient. Worth noting separately: among the lower-ranked candidates, "HIV infectious disease" (rank 5) is evidence-backed but reflects treatment of antiretroviral-associated dyslipidemia rather than any antiviral effect — a distinction to keep clear if that signal is pursued later.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Efficacy/safety of ezetimibe/simvastatin + extended-release niacin in Type IIa/IIb hyperlipidemia |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg added to atorvastatin or simvastatin in homozygous familial hypercholesterolemia |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | Long-term (52-week) safety/tolerability of ezetimibe+rosuvastatin in Japanese patients with inadequate LDL-C control |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | PRECISE-IVUS: coronary plaque regression, cholesterol absorption vs. synthesis inhibitor (surrogate endpoint) |
| [NCT00651560](https://clinicaltrials.gov/study/NCT00651560) | Phase 3 | Completed | 167 | Vytorin (ezetimibe/simvastatin) vs. atorvastatin, ATP-III goal attainment in dyslipidemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate coadministration in mixed hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration, cholesterol-lowering efficacy/safety in mixed hyperlipidemia |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completed | 4105 | Post-marketing surveillance of ezetimibe safety/tolerability/efficacy in Filipino patients |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | Completed | 11332 | 12-week designated drug-use investigation of Zetia (Japan), mono- and combination therapy |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completed | 1794 | 52-week long-term designated drug-use investigation of Zetia (Japan) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM Phase 3 trial: obicetrapib + ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH; notes many patients fail to reach LDL-C goals on current therapies incl. ezetimibe |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Familial hypercholesterolemia overview; ezetimibe among core LDL-C-lowering treatments |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH epidemiology, underdiagnosis, and treatment overview |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | FH global burden, diagnosis, risk estimation, and management approaches |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Comprehensive FH primer covering genetics, diagnosis, and treatment |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Review/Guidance | European Heart Journal | EAS consensus statement on FH underdiagnosis/undertreatment and clinician guidance |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors in context of statin-intolerant/FH patients |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis, and treatment of postprandial hyperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C/ApoB-lowering therapies beyond statins and ezetimibe |

---

## EU Market Information

Ezetimibe currently has **no marketing authorization on file** in this dataset (0 licenses, market status: Not Marketed). No authorization number, product name, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base easily meets the L1 threshold (multiple completed Phase 3 RCTs directly testing ezetimibe, including combination and long-term safety trials), but this reflects confirmation of ezetimibe's already-established lipid-lowering indication rather than a novel repurposing opportunity — the guardrail is against treating this as new clinical territory.

**To proceed, the following is needed:**
- TFDA/EMA SmPC warnings, precautions, and contraindications (currently a blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank
- Verification of actual marketing-authorization status in the target jurisdiction, since this dataset shows zero licenses on file for an otherwise globally marketed drug
- Clarification of whether "Hyperlipoproteinemia" should be treated as a label-extension question at all, given its substantial overlap with ezetimibe's existing approved use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

