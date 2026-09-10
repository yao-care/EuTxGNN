---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Methylphenidate
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

Using no specialized skill here — this is a direct content-generation task governed entirely by the report template already supplied in the prompt, so I'm following that template directly.

A structural note before the report: `predicted_indications[0]` ("faciodigitogenital syndrome") has **no supporting evidence at all** (0 trials, 0 literature) and its own `scoring` fields are literally `"pending"` — it's an unscored placeholder, not a real candidate. Per the evaluation framework's own evidence-level rules, an unscored/no-evidence entry can't be reported as if it were validated. I've built the report around **rank 3 — "specific developmental disorder"** — the only candidate in this pack with a completed RCT, a real evidence level (L2), and an actual recommendation (Proceed with Guardrails). All 10 screened candidates are still listed in a triage table so nothing is hidden.

---

# Methylphenidate: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

> Methylphenidate is a CNS stimulant established as first-line pharmacotherapy for Attention-Deficit/Hyperactivity Disorder (ADHD).
> The TxGNN model predicts it may also be effective for **Specific Developmental Disorder** (e.g., childhood apraxia of speech, developmental learning disorders),
> with **17 clinical trials** and **18 publications** currently associated with this direction — though most of this evidence comes from ADHD populations with developmental-disorder comorbidity rather than the target condition itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local marketing-authorization data (0 licenses on file). Methylphenidate's established indication — ADHD, referenced throughout the underlying literature — is a global clinical fact, not derived from a license text in this evidence pack. |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap, DG002). Based on the pharmacology reflected in the underlying evidence, methylphenidate inhibits the dopamine transporter (DAT) and norepinephrine transporter (NET), increasing prefrontal cortical dopamine/norepinephrine signaling and thereby improving attention and executive function — this is well established for its approved use in ADHD.

Specific developmental disorders — such as childhood apraxia of speech and learning disorders — frequently co-occur with ADHD and share overlapping deficits in executive function, motor planning, and attentional control. The mechanistic hypothesis is that methylphenidate's pro-dopaminergic effect could extend benefit beyond core ADHD symptoms into these comorbid developmental domains.

However, this extrapolation has an important caveat flagged directly in the evidence review: **the indication boundary is blurred**. Most supporting trials actually enrolled ADHD populations (with developmental disorders as a comorbid or secondary feature) rather than testing methylphenidate as a primary treatment for a developmental disorder in isolation. The one trial that does test methylphenidate as a primary intervention for a developmental-disorder-specific outcome (childhood apraxia of speech) is a small (n=18), single completed Phase 2 RCT — supportive, but not yet definitive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05185583](https://clinicaltrials.gov/study/NCT05185583) | Phase 2 | Completed | 18 | Double-blind, randomised, placebo-controlled crossover trial of methylphenidate directly targeting speech intelligibility in children with childhood apraxia of speech (CAS), ages 6–12. |
| [NCT04647500](https://clinicaltrials.gov/study/NCT04647500) | N/A | Completed | 45 | Effects of dopaminergic modulation via methylphenidate on memory and executive processes in 22q11.2 deletion syndrome, a neurodevelopmental condition with high ADHD comorbidity. |
| [NCT07024303](https://clinicaltrials.gov/study/NCT07024303) | Early Phase 1 | Not yet recruiting | 20 | Compares medication vs. behavioral treatment (and combination) for challenging behavior in children/adolescents with autism. |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART-design trial comparing methylphenidate vs. amphetamine (and alpha-2 agonists) for ADHD in children/youth with autism spectrum disorder. |
| [NCT05974241](https://clinicaltrials.gov/study/NCT05974241) | Phase 4 | Completed | 36 | Crossover study of methylphenidate vs. aripiprazole for irritability in children with ADHD and emotion dysregulation. |
| [NCT01363544](https://clinicaltrials.gov/study/NCT01363544) | Phase 2/3 | Completed | 112 | Exercise and neurofeedback intervention study in ADHD (a developmental disorder); methylphenidate is a comparator, not the primary intervention. |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1,398 | ADDUCE project — large 2-year safety study of methylphenidate's chronic effects on growth, neurological, psychiatric, and cardiovascular systems in children/adults. |
| [NCT02167048](https://clinicaltrials.gov/study/NCT02167048) | Phase 1/2 | Active, not recruiting | 52 | Double-blind crossover comparing low-dose vs. normal-dose psychostimulants on executive function (working memory, attention, cognitive flexibility) in ADHD. |
| [NCT01554046](https://clinicaltrials.gov/study/NCT01554046) | N/A | Completed | 40 | Familial response to methylphenidate (Ritalin IR) in ADHD — symptom improvement and side-effect profile within families. |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Examines reinforcing/self-medication mechanisms of smoking in adult ADHD, with stimulant medication as a modulating factor. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8719499](https://pubmed.ncbi.nlm.nih.gov/8719499/) | 1996 | Cohort | Clinical EEG | QEEG-based discriminant functions distinguished children with specific developmental learning disorders from ADHD and normal populations, and predicted stimulant responder type. |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Review | Neuropharmacology | Overview of ADHD neurobiology — genetic basis, frontal-lobe/caudate/cerebellar structural differences — underpinning the dopaminergic rationale for stimulant use. |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | Clinical EEG and Neuroscience | Review of quantitative EEG use in childhood ADHD and learning disabilities, including personalized-medicine framing for treatment response prediction. |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Longitudinal MRI study | Prog Neuropsychopharmacol Biol Psychiatry | Age-dependent effects of cumulative methylphenidate exposure on brain structure and symptom improvement in youth with ADHD (n=89) vs. controls (n=91). |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Longitudinal PET study | Psychiatry Clin Neurosci | Dual-tracer PET study of extended-release methylphenidate's effects on dopamine and norepinephrine transporter binding in adults with ADHD. |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Review | J Attention Disorders | Reviews methylphenidate's cellular/molecular mechanisms and developmental consequences, comparing adult vs. juvenile brain effects. |
| [20483462](https://pubmed.ncbi.nlm.nih.gov/20483462/) | 2010 | Retrospective study | Psychiatry Research | EEG coherence differences between good and poor methylphenidate responders in children with combined-type ADHD. |
| [25989180](https://pubmed.ncbi.nlm.nih.gov/25989180/) | 2015 | Genetic association study | Genes Brain Behav | LPHN3 gene variants linked to ADHD susceptibility and methylphenidate pharmacogenetic response. |
| [19487194](https://pubmed.ncbi.nlm.nih.gov/19487194/) | 2009 | Review | Phil Trans R Soc Lond B | Frames ADHD impulsiveness as a timing-function deficit; documents normalization of temporal-processing deficits with methylphenidate. |
| [36899043](https://pubmed.ncbi.nlm.nih.gov/36899043/) | 2023 | Qualitative study | Scientific Reports | French qualitative study on adolescent and psychiatrist perspectives regarding methylphenidate use in ADHD. |

---

## Other Candidate Indications Evaluated (Screening Summary)

This evidence pack scored 10 candidate indications for methylphenidate. Only rank 3 above reached an actionable recommendation; the rest are documented here for completeness and transparency.

| Rank | Disease | Evidence Level | Recommendation | Note |
|------|---------|----------------|-----------------|------|
| 1 | Faciodigitogenital syndrome | Unscored | — | No clinical trials or literature; scoring fields incomplete. Not a usable candidate. |
| 2 | Chondromyxoid fibroma | L5 | Hold | Benign cartilage tumor; no mechanistic link to a CNS stimulant. |
| 4 | Dysthymic disorder | L4 | Research Question | Case-series-level evidence only, as antidepressant augmentation in ADHD-comorbid low mood; no RCTs. |
| 5 | Trichotillomania | L4 | Hold | ⚠️ **Signal runs opposite to the prediction** — multiple case reports describe methylphenidate *inducing or worsening* hair-pulling, not treating it. Should be tracked as an adverse-effect signal, not a repurposing opportunity. |
| 6 | Cerebellar ataxia | L4 | Research Question | Case-report evidence for treating comorbid attentional symptoms in hereditary ataxias (e.g., Joubert syndrome); not a treatment for the ataxia itself. |
| 7 | Autosomal dominant cerebellar ataxia | L5 | Hold | Sole reference is a DAT-PET imaging/pathophysiology study, not treatment evidence. |
| 8 | Spinocerebellar degeneration with slow eye movements | L5 | Hold | Imaging/pathophysiology literature only; no therapeutic rationale. |
| 9 | Benign paroxysmal torticollis of infancy | L5 | Hold | No trials or literature; no plausible mechanistic link. |
| 10 | Insomnia (disease) | L3 | Research Question | ⚠️ **Mechanistic contradiction** — methylphenidate is a stimulant whose typical adverse effect is insomnia. Supporting trials mostly address wakefulness/apathy (e.g., Alzheimer's, MS fatigue) rather than treating insomnia itself; likely reflects TxGNN conflating "arousal modulation" with "insomnia treatment." |

---

## Safety Considerations

Please refer to the SmPC for formal safety information — key warnings, contraindications, and drug-interaction data are all marked as gaps in this evidence pack (DG001, Blocking severity: cannot complete S1 safety pre-screening without the TFDA/EMA label text).

**Safety signals surfaced during evidence review (not from formal label data):**
- **Trichotillomania induction**: Multiple case reports (PMID 21586916, 28492426, 28394174, 31984712) describe new-onset or worsened hair-pulling behavior during methylphenidate treatment — an adverse-effect signal, distinct from any therapeutic claim.
- **Insomnia**: Insomnia is a well-documented stimulant-class adverse effect of methylphenidate itself; this should be treated as a known side effect requiring monitoring, not conflated with a therapeutic indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the "specific developmental disorder" candidate only)

**Rationale:**
A completed, blinded Phase 2 RCT directly targets a developmental-disorder subtype (childhood apraxia of speech), supported by additional trials in comorbid neurodevelopmental populations (22q11.2 deletion syndrome, autism spectrum disorder). However, the indication boundary with core ADHD is not clean, and formal safety/label data (DG001) is currently missing, so this cannot yet clear a full safety gate. All other 9 candidates in this pack are Hold or Research Question and are not recommended for further action at this time.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent label data (warnings, contraindications, DDI) — currently a **Blocking** data gap (DG001)
- Structured mechanism-of-action data from DrugBank (DG002)
- A trial designed with "specific developmental disorder" (non-ADHD-comorbid) as the primary population and endpoint, to resolve the current indication-boundary ambiguity
- Explicit review of the trichotillomania and insomnia signals as safety considerations before any guarded expansion of use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

