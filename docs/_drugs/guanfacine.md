---
layout: default
title: Guanfacine
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Guanfacine
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

# Guanfacine: From Hypertension to Tourette Syndrome

## One-Sentence Summary

Guanfacine is an alpha‑2A adrenergic agonist originally used to treat **hypertension**, and has since been repurposed elsewhere for ADHD. The TxGNN model predicts it may also be effective for **Tourette Syndrome**, a hypothesis already supported by **3 clinical trials** (including a completed Phase III RCT designed specifically to test guanfacine in Tourette syndrome/ADHD) and **20 publications**, several of which study guanfacine directly in tic disorders.

> ⚠️ Note on sourcing: This Evidence Pack contains no DrugBank MOA record and no EU/Taiwan license data for Guanfacine (`original_moa`, `original_indications`, and `licenses` are all empty). The "Hypertension" original indication above is drawn from a literature citation within this pack (PMID 30707118: *"Guanfacine is Food and Drug Administration approved for hypertension and attention-deficit hyperactivity disorder..."*), not from a confirmed regulatory source. This should be verified against an official label before use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension *(per literature citation, not confirmed via EU/Taiwan regulatory license data — see note above)* |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently unavailable for Guanfacine (flagged as a High-severity data gap in this Evidence Pack). Based on information recovered from the associated literature evidence, however, Guanfacine is consistently described as a selective **alpha‑2A adrenergic receptor agonist**. Several guanfacine-specific studies in this pack (e.g. PMID 7559307, PMID 12469007) describe its action on central noradrenergic signalling, particularly in the prefrontal cortex (PFC).

The repurposing rationale for Tourette syndrome centers on this same PFC mechanism: alpha‑2A agonism is believed to strengthen prefrontal inhibitory control circuits and dampen excessive cortico-striato-thalamic activity — the circuit implicated in the generation of motor and vocal tics. This is mechanistically continuous with guanfacine's already-established (though off-label in many markets) use for ADHD and tic-spectrum conditions, and is consistent with real-world clinical practice, where guanfacine is already widely used adjunctively for tic disorders.

Tourette syndrome and ADHD are also highly comorbid conditions with overlapping neurobiology, which is reflected in the evidence base: many of the clinical trials and publications in this pack (e.g. NCT00004376, PMID 7559307, PMID 23473832) study guanfacine in mixed ADHD + Tourette syndrome populations rather than Tourette syndrome in isolation. This convergence of an established pharmacological rationale, existing off-label clinical use, and a dedicated completed Phase III trial is why the TxGNN prediction for Tourette syndrome is considered mechanistically reasonable rather than a purely model-driven association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004376](https://clinicaltrials.gov/study/NCT00004376) | Phase 3 | Completed | 35 | Randomized, double-blind, placebo-controlled evaluation of guanfacine's safety and efficacy in children/adolescents with Tourette syndrome or another chronic tic disorder, with or without comorbid ADHD. |
| [NCT01547000](https://clinicaltrials.gov/study/NCT01547000) | Phase 4 | Completed | 34 | Multi-site pilot study of tolerability and efficacy of extended-release guanfacine (Intuniv) in children with Tourette Disorder. |
| [NCT01172288](https://clinicaltrials.gov/study/NCT01172288) | Phase 2 | Completed | 31 | Trial of N-acetylcysteine (not guanfacine) for pediatric tic disorders; guanfacine is referenced only as an existing comparator therapy — indirect relevance only (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12469007](https://pubmed.ncbi.nlm.nih.gov/12469007/) | 2002 | RCT | Clinical Neuropharmacology | 4-week double-blind, placebo-controlled trial of guanfacine in 24 children with Tourette syndrome; improved tic severity and select neuropsychological measures. |
| [7559307](https://pubmed.ncbi.nlm.nih.gov/7559307/) | 1995 | Clinical Experience | J Am Acad Child Adolesc Psychiatry | Early open-label experience showing guanfacine improved comorbid ADHD symptoms in Tourette syndrome without worsening tics. |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Review/Guideline | Eur Child Adolesc Psychiatry | ESSTS European clinical guidelines v2.0 for Tourette syndrome pharmacological treatment; includes alpha-2 agonists such as guanfacine. |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | AAN systematic review of tic-disorder treatments, evaluating efficacy and risk of available pharmacotherapies. |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Narrative Review | Medicine | Review of Phase III/IV pharmacological trials for Tourette syndrome across age groups. |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | J Psychopharmacol | Assessment of evidence quality for pharmacological treatments of Tourette syndrome. |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Review | Eur J Paediatr Neurol | Review of current pharmacological options for Tourette syndrome with comorbid ADHD. |
| [37378108](https://pubmed.ncbi.nlm.nih.gov/37378108/) | 2023 | Case Series | Cureus | Combination of guanfacine and aripiprazole produced significant tic improvement in 3 Tourette syndrome patients. |
| [30899317](https://pubmed.ncbi.nlm.nih.gov/30899317/) | 2019 | Case Report | Ann Gen Psychiatry | Guanfacine monotherapy effective for ADHD/ASD comorbid with Tourette syndrome. |
| [16229000](https://pubmed.ncbi.nlm.nih.gov/16229000/) | 2006 | Case Series (Safety) | Movement Disorders | Reports syncope in 4 children with Tourette syndrome treated with guanfacine, attributed to drug-induced hypotension/bradycardia. |

---

## EU Market Information

Guanfacine currently has **no European Union marketing authorization** on record in this Evidence Pack (`market_status`: Not Marketed; `total_licenses`: 0). No product-level authorization data is available to summarize.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, and structured DDI records) is not available in this Evidence Pack, and a DDI query returned no results. **Please refer to the SmPC for safety information** once a marketing authorization or product label becomes available.

That said, several safety signals specific to guanfacine emerge from the literature evidence collected for this candidate and are worth flagging for a future formal safety review:
- **Cardiovascular effects**: Syncope has been reported in children with Tourette syndrome treated with guanfacine, attributed to drug-induced hypotension or bradycardia (PMID 16229000).
- **Overdose/combination risk**: A case of sinus pause has been reported when guanfacine was combined with olanzapine in overdose (PMID 31447925), suggesting caution with co-administered CNS/cardiac-active agents.

This candidate also carries a **Blocking**-severity data gap (official TFDA/EU label warnings and contraindications not yet retrieved), which currently prevents this candidate from completing a formal S1 safety review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Guanfacine's repurposing for Tourette syndrome is supported by a completed Phase III RCT specifically testing the drug in this population, a confirmatory completed Phase IV pilot study, and an unusually deep literature base (including guanfacine-specific RCT and case evidence, plus European clinical guidelines recommending alpha-2 agonists for tic disorders). This is a mechanistically coherent extension of guanfacine's known noradrenergic activity and its established off-label use in tic-spectrum disorders. However, the absence of official label safety data and the lack of any current EU marketing authorization mean this candidate cannot yet proceed past guarded evaluation.

**To proceed, the following is needed:**
- Official SmPC/product label data (warnings, contraindications) — currently a Blocking data gap
- Confirmed DrugBank mechanism-of-action documentation — currently a High-severity data gap
- A defined EU regulatory pathway, since Guanfacine has no current EU marketing authorization
- A structured formal DDI review (current query returned no results)
- Additional confirmatory RCT data, as the only completed Phase III trial (NCT00004376, n=35) is over two decades old

**For context:** TxGNN's top-ranked prediction for Guanfacine by raw score is *faciodigitogenital syndrome*, and other high-scoring predictions include *chondromyxoid fibroma*, *variably protease-sensitive prionopathy*, and *migraine with brainstem aura* — all classified L5/Hold, with no identifiable mechanistic link or supporting evidence. A second well-evidenced candidate, *specific developmental disorder* (ADHD-spectrum, also L1/Proceed with Guardrails), largely overlaps with Guanfacine's known existing ADHD use rather than representing a genuinely new indication, which is why Tourette syndrome was selected as the primary focus of this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

