---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

Using no specific skill here — this is a direct, fully-specified report-writing task (exact template already given verbatim), not a coding/build task that maps to any available skill (txgnn-pipeline covers model training/deployment, not report authoring; data-report applies to raw CLI output, not JSON synthesis). Proceeding to draft the report directly from the Evidence Pack.

A note before the report: this Evidence Pack is a "multi" candidate (`TW-DB11834-multi`) with **10** TxGNN-ranked candidate indications, not one. Two of them — **psoriasis** (rank 3) and **ulcerative colitis** (rank 6) — carry real clinical trial and literature evidence (L1); the other eight are L5 model-only signals explicitly flagged in their own `repurposing_rationale` as lacking any mechanistic or empirical support. The pack's own rank-3 rationale states psoriasis is not a new hypothesis but a "rediscovery" of Guselkumab's already-approved indication (Tremfya), caused by the `original_indications` data gap. I therefore built the report around the one candidate that is both genuinely new and evidence-backed — **ulcerative colitis** — and used the rank-3 text (sourced from the pack itself, not external knowledge) to fill the "Original Indication" gap. The other eight low-evidence candidates are summarized transparently near the end rather than omitted.

---

# Guselkumab: From Psoriasis to Ulcerative Colitis

## One-Sentence Summary

> Guselkumab is an anti-IL-23p19 monoclonal antibody originally developed and approved for moderate-to-severe plaque psoriasis.
> The TxGNN model predicts it may also be effective for **Ulcerative Colitis**,
> a prediction now corroborated by **17 clinical trials** and **20 publications**, including a completed Phase 3 registration program (QUASAR).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (Tremfya) — inferred from the pack's own rank-3 rationale, since `original_indications` and `taiwan_regulatory.licenses` are empty (Data Gap DG001/DG002) |
| Predicted New Indication | Ulcerative Colitis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (0 authorizations on file in this registry) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Guselkumab is not available in the source registry (Data Gap DG002). Based on information contained in the Evidence Pack itself, Guselkumab is a human IgG1 monoclonal antibody that selectively binds the p19 subunit of interleukin-23 (IL-23), neutralizing IL-23 signalling and, per recent literature, also binding CD64. IL-23 sits upstream of the Th17 axis and is a shared pathogenic driver across several immune-mediated inflammatory diseases (IMIDs), not just psoriasis.

Psoriasis and ulcerative colitis are both chronic, IL-23/Th17-driven inflammatory diseases — one of the skin, one of the intestinal mucosa. This shared pathway is precisely why IL-23 inhibitors developed for psoriasis (e.g., ustekinumab, risankizumab, guselkumab) have systematically progressed into inflammatory bowel disease programs. For Guselkumab specifically, the mechanistic hypothesis has already moved past "prediction": the Phase 2b/3 QUASAR program demonstrated induction and maintenance efficacy in moderately-to-severely active UC, and regulatory approvals for this indication followed in 2024–2025 in several jurisdictions (consistent with literature PMID 41324615, "Guselkumab... was approved for the treatment of moderately-to-severely active UC in 2024/5").

In other words, the TxGNN embedding similarity between psoriasis and ulcerative colitis is not a speculative leap — it reflects a real, clinically validated mechanistic and therapeutic overlap (the IL-23/Th17 axis), and the model's high score for this pairing is directionally correct.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Phase 2b | Active, not recruiting | 577 | QUASAR combination sub-study: guselkumab + golimumab induction/maintenance vs. active/placebo control in moderate-severe UC |
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Phase 2b/3 | Active, not recruiting | 1,064 | Pivotal QUASAR program evaluating guselkumab efficacy/safety in moderate-severe UC |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Phase 3 | Active, not recruiting | 418 | Randomized, double-blind, placebo-controlled subcutaneous induction therapy in moderate-severe UC |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Phase 2 | Completed | 214 | Proof-of-concept: guselkumab + golimumab combination therapy efficacy/safety in moderate-severe UC |
| [NCT06408935](https://clinicaltrials.gov/study/NCT06408935) | Phase 3b | Recruiting | 112 | Open-label study of transmural healing (MaRIA score) with guselkumab in Crohn's disease (mechanistic support) |
| [NCT06663332](https://clinicaltrials.gov/study/NCT06663332) | Phase 3 | Recruiting | 196 | Long-term extension safety study of subcutaneous guselkumab in pediatric UC, Crohn's disease, and juvenile PsA |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Phase 3 | Active, not recruiting | 112 | Randomized study of guselkumab efficacy, safety and pharmacokinetics in pediatric moderate-severe UC |
| [NCT07102368](https://clinicaltrials.gov/study/NCT07102368) | N/A | Recruiting | 400 | Real-world evidence study of guselkumab effectiveness and patient-reported outcomes in UC/Crohn's disease |
| [NCT07245394](https://clinicaltrials.gov/study/NCT07245394) | N/A | Recruiting | 200 | SHIFT-IBD: switching to guselkumab in ustekinumab-exposed IBD patients with inadequate response |
| [NCT06916390](https://clinicaltrials.gov/study/NCT06916390) | Phase 4 | Not yet recruiting | 20 | Guselkumab plus dietary intervention for pouchitis after UC-related ileal pouch-anal anastomosis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | RCT | Lancet | QUASAR Phase 3 double-blind, randomized, placebo-controlled induction and maintenance trials establishing guselkumab efficacy in moderate-severe UC |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | RCT | Gastroenterology | QUASAR Phase 2b induction study confirming efficacy/safety in patients with prior inadequate response to advanced therapy |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Guideline | Gastroenterology | AGA Living Clinical Practice Guideline on pharmacological management of moderate-severe UC |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Network Meta-analysis | Gastroenterology | 2024 AGA evidence synthesis comparing advanced therapies (including guselkumab) for moderate-severe UC |
| [40407729](https://pubmed.ncbi.nlm.nih.gov/40407729/) | 2025 | Network Meta-analysis | Aliment Pharmacol Ther | Comparative efficacy of biologics/small molecules as UC maintenance therapy |
| [39137239](https://pubmed.ncbi.nlm.nih.gov/39137239/) | 2025 | Network Meta-analysis | Inflamm Bowel Dis | Comparative efficacy of biologics/small molecules on patient-reported outcomes and quality of life in UC |
| [39367678](https://pubmed.ncbi.nlm.nih.gov/39367678/) | 2024 | Network Meta-analysis | Aliment Pharmacol Ther | Histologic and histo-endoscopic improvement/remission with advanced UC therapies |
| [41324615](https://pubmed.ncbi.nlm.nih.gov/41324615/) | 2025 | Expert Opinion | Expert Opin Biol Ther | Evaluation of guselkumab for UC treatment; notes approval for moderate-severe UC in 2024/2025 |
| [39800899](https://pubmed.ncbi.nlm.nih.gov/39800899/) | 2025 | Review | Ann Pharmacother | Summary of evidence and pharmacologic profile of guselkumab for moderate-severe UC |
| [37069321](https://pubmed.ncbi.nlm.nih.gov/37069321/) | 2023 | Review | Nat Rev Gastroenterol Hepatol | Mechanistic review of IL-12/IL-23 pathway inhibition in inflammatory bowel disease |

---

## EU Market Information

No marketing authorization records are present in this Evidence Pack (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`, `licenses: []`). This appears to be a data completeness gap rather than a confirmed absence of authorization, since Guselkumab (Tremfya) is independently known to be approved in multiple jurisdictions for psoriasis, psoriatic arthritis, and — per the literature evidence above — ulcerative colitis and Crohn's disease. **This section should be re-verified against the official EMA/national registry before any decision is finalized.**

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and DDI data are all marked `[Data Gap]` / `not_found` in this pack — see Data Gap DG001, severity: Blocking, which prevents entry into the S1 safety pre-screening stage.)*

---

## Other TxGNN Signals (Not Actioned)

For completeness: this pack scored 10 candidate indications for Guselkumab. Beyond psoriasis (a rediscovery of the known indication) and ulcerative colitis (covered above), the remaining eight are AI-only signals (L5, decision stage S0, recommendation **Hold**) with zero supporting clinical trials or literature, and each one's own mechanistic rationale explicitly states there is no known biological connection to IL-23 inhibition:

- Drug-induced osteoporosis
- Severe nonproliferative diabetic retinopathy
- Diabetic retinopathy
- Renal osteodystrophy
- Congenital hypotrichosis with juvenile macular dystrophy
- Primary release disorder of platelets
- Glanzmann thrombasthenia
- Non-renal secondary hyperparathyroidism

These should remain on Hold pending any future evidence and are not part of this evaluation's recommendation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Ulcerative colitis is supported by a completed Phase 3 registration program (QUASAR, published in *Lancet* 2025) plus multiple independent network meta-analyses and an AGA clinical guideline — this meets L1 evidence criteria and is already reflected in real-world regulatory approvals (2024–2025). However, two Blocking/High-severity data gaps (TFDA/EMA label warnings and confirmed MOA) mean the safety dossier is not yet complete enough for an unconditional "Go."

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications to complete S1 safety pre-screening
- Resolve DG002 (High): confirm mechanism of action directly from DrugBank/EMA SmPC rather than inference
- Verify actual EU/Taiwan marketing authorization status — the `未上市` / 0-license result in this pack conflicts with known external approvals and should be re-queried
- Complete a formal drug-drug interaction (DDI) query — current status is `not_found`, not confirmed-absent
- Clarify `original_indications` (currently empty) to remove ambiguity between "known indication" and "new indication" in future evidence packs for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

