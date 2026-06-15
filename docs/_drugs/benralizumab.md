---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Severe Eosinophilic Asthma to Dermatitis

## One-Sentence Summary

Benralizumab is an anti-IL-5 receptor alpha (IL-5Rα) monoclonal antibody approved globally for severe eosinophilic asthma, but not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Dermatitis** (particularly atopic dermatitis and eosinophil-dominant subtypes such as DRESS),
with **6 clinical trials** and **20 publications** currently supporting this direction — including one terminated Phase 2 RCT (HILLIER) with a negative primary endpoint and an active mechanistic signal confirmed in skin tissue.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (globally approved; not approved in Taiwan) |
| Predicted New Indication | Dermatitis (Atopic Dermatitis / Eosinophilic Subtypes) |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, benralizumab is an afucosylated anti-IL-5Rα monoclonal antibody that binds to the IL-5 receptor alpha subunit expressed on eosinophils and basophils, triggering near-complete cell depletion through enhanced antibody-dependent cell-mediated cytotoxicity (ADCC). This mechanism forms the basis of its proven efficacy in severe eosinophilic asthma, where airway eosinophilia drives chronic inflammation.

The connection to dermatitis rests on an analogous pathophysiological process: atopic dermatitis (AD) skin lesions frequently show significant eosinophil infiltration, and IL-5Rα-bearing cells have been directly confirmed in AD skin biopsies (PMID 40781582). In theory, depleting tissue eosinophils could reduce itch, epidermal damage, and Th2-driven inflammation in eosinophil-prominent presentations. This rationale is strongest for DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms), where eosinophils are a primary — not secondary — driver, and a dedicated Phase 2 trial is planned (NCT06734884).

However, typical AD is primarily driven by the IL-4/IL-13/Th2 cytokine axis; eosinophils serve as downstream effectors rather than the key initiating signal. This fundamental limitation explains why the HILLIER Phase 2 RCT (NCT04605094, n=194) was terminated early for insufficient efficacy: benralizumab depleted IL-5Rα+ cells in skin (confirmed mechanistically) but this did not translate into clinical improvement on the primary endpoint. The prediction therefore carries a meaningful mechanistic caveat for broad AD, while remaining scientifically interesting for eosinophil-dominant dermatitis subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | HILLIER study: Benralizumab vs placebo in moderate-to-severe atopic dermatitis (16 weeks + 36-week extension). Terminated early due to insufficient efficacy on primary endpoint. The most pivotal direct trial — provides definitive negative evidence for typical AD. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Mechanistic proof-of-concept study evaluating benralizumab's effects on eosinophils, basophils, and type 2 innate lymphoid cells (ILC2) in AD skin. Small sample (n=20) but directly confirms target engagement. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not Yet Recruiting | 96 | Efficacy and safety of benralizumab in DRESS — a severe eosinophil-driven drug hypersensitivity reaction. Highest mechanistic relevance; adequately powered (n=96); completion expected 2029. This trial is the highest-priority signal for targeted repurposing. |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Phase 2 | Recruiting | 30 | Dupilumab add-on for hypereosinophilic syndrome (HES) with partial response to eosinophil-depleting biologics (including benralizumab). Relevant to severe eosinophilic presentations with skin involvement. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | N/A | Completed | 28 | Observational retrospective study of benralizumab in severe eosinophilic asthma (Spain individualized access program). Provides real-world safety and tolerability data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | Phase 2 RCT | JEADV | HILLIER trial results: Benralizumab failed to improve signs and symptoms of moderate-to-severe AD. Primary endpoint not met. Critical negative evidence that shifts the indication toward eosinophil-dominant subtypes only. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Phase 2 RCT Summary | Immunotherapy | Plain language summary of HILLIER results confirming lack of effect in broad moderate-to-severe AD population. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Translational/Mechanistic | Clinical and Translational Allergy | Benralizumab depletes IL-5Rα-bearing cells in AD skin lesions — confirms mechanistic target engagement in tissue despite negative HILLIER clinical outcome. Crucial for understanding responder subpopulations. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Mechanistic | J Allergy Clin Immunol Global | Effect of benralizumab on skin inflammation after intradermal allergen challenge in AD patients — provides mechanistic insight into local eosinophil suppression and allergen response. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Safety Review | J Allergy Clin Immunol Pract | Safety review of 7 FDA-approved biologics including benralizumab for atopic diseases during pregnancy; summarizes maternal and fetal outcome data. Relevant for special population considerations. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunology and Allergy Clinics NA | Review of biologics (including benralizumab) for allergic rhinitis, asthma, and atopic dermatitis in pregnancy and lactation. Highlights knowledge gaps and safety profile. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie select | Updated landscape of targeted biologics for atopic diseases including benralizumab; covers safety signals around hypersensitivity reactions across the drug class. |
| [38074921](https://pubmed.ncbi.nlm.nih.gov/38074921/) | 2024 | Case Report | Respirology Case Reports | Dual biologic therapy (benralizumab or mepolizumab + dupilumab) in comorbid severe asthma and atopic dermatitis — real-world outcomes in two patients with overlapping disease. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case Report (Adverse Event) | Therapie | Benralizumab-induced interstitial granulomatous dermatitis — a paradoxical skin reaction. Safety signal relevant when targeting dermatitis as a new indication. |
| [38035014](https://pubmed.ncbi.nlm.nih.gov/38035014/) | 2023 | Pharmacovigilance | Frontiers in Pharmacology | FAERS disproportionality analysis: anti-type 2 immunity biologics (including benralizumab) are associated with a signal for parasitic/helminth infections. Relevant to immunosuppression risk assessment. |

---

## Safety Considerations

Please refer to the SmPC for comprehensive safety information. No Taiwan TFDA package insert warnings or contraindications were available in this Evidence Pack.

The following signals are identified from the available literature:

- **Paradoxical skin reaction**: A case report (PMID 36270814) documents benralizumab-induced interstitial granulomatous dermatitis — a paradoxical adverse skin reaction that is particularly relevant when dermatitis is the target indication.
- **Vaccine response**: Benralizumab has been associated with modestly lower post-vaccination SARS-CoV-2 immunity (PMID 38878020), suggesting partial modulation of adaptive immune responses.
- **Parasitic infection risk**: Pharmacovigilance data (PMID 38035014) shows a safety signal for helminth infections across anti-type 2 immunity biologics, including benralizumab. Screening for parasitic infection before initiation is recommended in endemic regions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HILLIER Phase 2 RCT (NCT04605094, n=194) failed to demonstrate meaningful clinical benefit of benralizumab in moderate-to-severe atopic dermatitis and was terminated early — providing definitive evidence against broad AD repurposing. While target engagement in skin is mechanistically confirmed, eosinophils are secondary effectors in typical AD, not primary drivers, limiting therapeutic impact. The strongest remaining opportunity lies in eosinophil-dominant dermatitis subtypes (particularly DRESS), pending results from NCT06734884.

**To proceed, the following is needed:**

- Results from NCT06734884 (Phase 2, DRESS indication, n=96, completion 2029) — this is the highest-priority data gap for targeted repurposing
- Patient stratification biomarkers (peripheral blood eosinophil count, skin IL-5Rα expression, IgE level) to define responder subpopulations before any new trial design
- Taiwan regulatory pathway assessment: benralizumab is not approved by TFDA; any repurposing trial would require an IND application and, ultimately, a new drug application
- Complete TFDA SmPC and package insert review for safety signal characterization (Data Gap DG001 — currently blocking S1 safety evaluation)
- MOA documentation from DrugBank API to close Data Gap DG002 and support mechanistic dossier for regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

