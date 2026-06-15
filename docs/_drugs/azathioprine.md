---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Organ Transplant Rejection to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a thiopurine prodrug immunosuppressant historically used for prevention of organ transplant rejection and severe autoimmune conditions, but is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (Crohn's Disease and Ulcerative Colitis)** — the highest-ranked prediction with clinical evidence (the top four TxGNN predictions are rare congenital structural syndromes mechanistically unrelated to immunosuppression and are assessed as model noise).
This direction is supported by **50 clinical trials** and **20 publications**, representing one of the most evidence-rich repurposing candidates in this dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Organ transplant rejection prevention / Autoimmune conditions |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's Disease / Ulcerative Colitis) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on well-established pharmacological knowledge, Azathioprine is a thiopurine prodrug that undergoes non-enzymatic conversion to 6-mercaptopurine (6-MP) and subsequent enzymatic metabolism to 6-thioguanine nucleotides (6-TGN). These active metabolites inhibit de novo purine synthesis and selectively induce T-lymphocyte apoptosis via the Rac1 GTPase pathway, thereby reducing key pro-inflammatory mediators including IL-2 and TNF-α. This mechanism is directly aligned with the immunopathology of IBD.

IBD encompasses Crohn's disease and ulcerative colitis — both driven by chronic mucosal T-cell dysregulation. Crohn's disease involves Th1-mediated transmural granulomatous inflammation throughout the gastrointestinal tract, while ulcerative colitis features Th2/Th17-driven mucosal inflammation confined to the colon. Because Azathioprine preferentially suppresses lymphocyte proliferation rather than innate immune function, it addresses the core adaptive immune dysregulation underlying both conditions without broadly abrogating infection defence. The mechanistic link between Azathioprine's known applications in other T-cell-mediated autoimmune diseases and the pathophysiology of IBD is strong and well-articulated.

Azathioprine carries over 45 years of clinical experience in IBD, underpinned by multiple completed Phase 3 RCTs and Cochrane systematic reviews confirming its role as a steroid-sparing maintenance therapy. Despite being absent from the Taiwan market, it holds regulatory approvals for IBD in the US, EU, and Japan. The TxGNN prediction score of 99.52% reflects the deep knowledge graph connectivity between Azathioprine's immune profile and the IBD disease node — consistent with decades of established global clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre RCT comparing AZA vs Mesalazine for prevention of postoperative recurrence in Crohn's Disease; designed to show superiority of AZA |
| [NCT01235689](https://clinicaltrials.gov/study/NCT01235689) | Phase 3 | Completed | 252 | Tight disease control strategy using CDAI, hs-CRP, and fecal calprotectin in moderate-to-severe Crohn's Disease improved mucosal healing rates at 48 weeks vs symptom-only monitoring |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Three-arm RCT (SONIC-like): IFX monotherapy vs IFX+AZA combination vs AZA monotherapy in immunomodulator/biologic-naïve Crohn's patients over 34 weeks |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind RCT: AZA vs Mesalazine for prevention of clinical relapse in postoperative Crohn's with moderate or severe endoscopic recurrence |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified RCT: weekly subcutaneous MTX vs daily oral AZA/6-MP for remission maintenance in low-risk paediatric Crohn's disease |
| [NCT02425865](https://clinicaltrials.gov/study/NCT02425865) | Phase 4 | Completed | 202 | Golimumab treat-to-target (In-TARGET) in moderate-to-severe UC failing corticosteroids and immunosuppressive therapy including AZA |
| [NCT03189888](https://clinicaltrials.gov/study/NCT03189888) | N/A | Completed | 33 | Prospective multicentre study of granulocyte-monocyte apheresis in steroid-dependent, AZA-intolerant or AZA-resistant moderate UC; defines the AZA-refractory population |
| [NCT00546546](https://clinicaltrials.gov/study/NCT00546546) | Phase 4 | Completed | 120 | Randomised comparison of early immunosuppressant strategy (within 6 months of diagnosis) vs conventional step-up in high-risk newly diagnosed Crohn's disease |
| [NCT02929706](https://clinicaltrials.gov/study/NCT02929706) | N/A | Unknown | 400 | NUDT15 R139C genotype-guided AZA dose optimisation to reduce thiopurine-induced leucopenia in IBD; randomised controlled design |
| [NCT07424040](https://clinicaltrials.gov/study/NCT07424040) | N/A | Not Yet Recruiting | 154 | IFX monotherapy vs IFX+AZA combination: comparative efficacy and long-term safety in paediatric Crohn's disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Updated Cochrane review confirming AZA/6-MP for maintenance of remission in UC; evaluates thiopurines against expanding newer therapeutic options |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down IFX+AZA combination vs AZA monotherapy as maintenance therapy in acute severe UC responding to IV corticosteroids |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Alimentary Pharmacology & Therapeutics | Meta-analysis demonstrating statistically significant efficacy of AZA and 6-MP for maintenance of remission in UC; resolves earlier controversy |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Cochrane review confirming AZA/6-MP as standard maintenance therapy in UC with ongoing comparative evaluation against newer biologics |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Comprehensive Review | Journal of Crohn's & Colitis | Expert consensus review of AZA, 6-MP, and thioguanine for steroid-free remission in IBD; covers efficacy, safety monitoring, and metabolite optimisation |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Mechanistic Review | Expert Review of Gastroenterology & Hepatology | Molecular mechanisms of AZA/6-MP in IBD including T-cell apoptosis via Rac1 pathway and autophagy induction; translational clinical implications |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Practice Review | World Journal of Gastroenterology | Optimising AZA/6-MP in IBD: therapeutic 6-TGN levels correlate with efficacy; elevated 6-MMP levels predict hepatotoxicity and myelotoxicity |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Experimental | Cell Reports Medicine | Blautia wexlerae colonisation decreases 6-MP bioavailability via gut microbiota metabolism, contributing to AZA therapy failure in IBD |
| [34913108](https://pubmed.ncbi.nlm.nih.gov/34913108/) | 2021 | Safety Review | Current Gastroenterology Reports | Comparative safety review of AZA/6-MP, MTX, anti-TNF, anti-integrin, IL-12/23 inhibitors, JAK inhibitors, and S1P modulators in IBD |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Review | Scandinavian Journal of Gastroenterology Supplement | AZA clinical efficacy and safety update in IBD; documents regulatory approval for long-term Crohn's disease therapy in the Netherlands |

---

## Taiwan Regulatory Information

Azathioprine is **not currently registered in Taiwan** (市場狀態：未上市). No Taiwan FDA authorization records exist for this drug.

| Item | Status |
|------|------|
| Taiwan FDA Market Status | Not Marketed |
| Number of Licensed Products | 0 |
| Global Approvals (Reference) | US FDA, EMA, PMDA Japan — approved for IBD |

The absence of Taiwan registration likely reflects a regulatory filing gap rather than safety or efficacy concerns. Azathioprine is included on the WHO Model List of Essential Medicines and has been commercially available internationally for over five decades.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and Cochrane systematic reviews confirm Azathioprine's efficacy for maintenance of remission in both Crohn's disease and ulcerative colitis, placing this indication firmly at Evidence Level L1. The immunosuppressive mechanism is directly applicable to IBD pathophysiology, and the drug has regulatory approval for this indication in all major markets — making the primary barrier in Taiwan a regulatory access issue rather than an evidence gap.

**To proceed, the following is needed:**
- Taiwan FDA market authorisation submission: formal regulatory filing required before clinical deployment
- Pharmacogenetic screening protocol: TPMT and NUDT15 genotyping prior to initiation, with particular attention to **NUDT15 R139C** (prevalence significantly higher in East Asian vs European populations, conferring elevated myelosuppression risk at standard doses)
- Taiwan-specific safety monitoring plan: baseline and periodic CBC with differential, liver function tests, and renal function panels
- TFDA product monograph and warning label data: extract from full prescribing information (Blocking data gap DG001)
- Dose adjustment guidelines for East Asian pharmacogenomic risk stratification, informed by NUDT15 genotype
- Post-marketing surveillance plan capturing Taiwan-specific safety signals in the IBD population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

