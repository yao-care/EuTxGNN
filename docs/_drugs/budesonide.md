---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a synthetic glucocorticoid (inhaled corticosteroid) clinically established for managing inflammatory airway diseases such as asthma and COPD, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with **2 clinical trials** and **20 publications** currently supporting this direction.
The evidence base is primarily preclinical and observational, placing this candidate at Evidence Level **L4**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan (globally used for asthma, COPD, and inflammatory bowel disease) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack. Based on known pharmacology described within the evidence, Budesonide is a glucocorticoid receptor (GR) agonist — the prototype inhaled corticosteroid (ICS) — that suppresses Th2 cytokines (IL-4, IL-5, IL-13) and IgE-mediated inflammatory responses. It inhibits eosinophilic airway inflammation, reduces mucus secretion, and lowers bronchial hyperreactivity.

Atopic eczema and allergic airway disease share a fundamentally common Th2-skewed inflammatory axis. Both conditions are components of the "atopic march," driven by IgE sensitisation, eosinophilic tissue infiltration, and epithelial barrier dysfunction. Since Budesonide's GR agonist mechanism directly targets these shared pathways, there is a plausible theoretical basis for efficacy in skin inflammation — the biological rationale is sound even without formal human trial evidence.

A 2024 preclinical study (PMID 38275852) demonstrated that Budesonide-loaded pH-sensitive Eudragit L100 nanoparticles formulated into hydrogels achieved improved dermal drug delivery to atopic lesion sites, exploiting the characteristic pH shift of inflamed skin. This novel delivery platform may overcome the poor penetration and systemic absorption concerns that historically limited Budesonide's topical dermal use. A veterinary randomised controlled trial also confirmed that a 0.025% Budesonide leave-on conditioner (Barazone) significantly reduced pruritus and skin lesion scores in dogs with atopic dermatitis, providing the closest analogue to a controlled efficacy signal in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy (not Budesonide) to prevent asthma and atopic disease in high-risk wheezing children — shares atopic disease background but offers no direct evidence for Budesonide in eczema |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Observational endotyping of severe paediatric asthma with atopic features (immune, metabolomics, microbiota) — no Budesonide intervention arm, no direct eczema treatment data |

> No clinical trials directly evaluating Budesonide for atopic eczema in humans are currently registered. Both retrieved trials are Grade C relevance.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical / Formulation | Gels (Basel) | Budesonide-loaded pH-sensitive nanoparticles in hydrogel form for atopic dermatitis — exploits atopic lesion pH change for targeted release; improved dermal delivery while reducing systemic adverse effects |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | Veterinary RCT | J Vet Pharmacol Ther | Barazone (0.025% budesonide conditioner) vs placebo in dogs with atopic dermatitis (n=29, crossover); significantly decreased skin lesion scores, pruritus, and improved quality of life |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical Study | Dermatology (Basel) | Topical glucocorticosteroids in children with atopic dermatitis — quantified systemic availability via IGF axis and bone turnover; highlights percutaneous absorption risk with Budesonide |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT Sub-analysis | Allergol Immunopathol | Differential Budesonide response in atopic vs non-atopic infants with recurrent wheezing — atopic status modifies ICS treatment response; relevant to patient stratification |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Observational / Patch Test | Dermatitis | Contact hypersensitivity to European standard and corticosteroid series including Budesonide in adolescents/adults with atopic dermatitis — key safety signal for sensitisation risk |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Observational | Contact Dermatitis | Patch testing of Budesonide in Italy (SIDAPA series 2018–2019) — decreasing trend of budesonide allergy noted; Budesonide remains the standard marker for corticosteroid hypersensitivity screening |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Observational | Contact Dermatitis | Contact sensitisation patterns in Asian atopic dermatitis patients — similar or higher sensitisation rates compared to non-AD population; corticosteroid allergy relevant |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Observational | J Am Acad Dermatol | Allergic contact dermatitis to personal care products and topical medications (including corticosteroids) in adults with atopic dermatitis — skin-barrier disruption amplifies sensitisation risk |
| [36713411](https://pubmed.ncbi.nlm.nih.gov/36713411/) | 2022 | Case Report | Front Immunol | Dupilumab resolved type 2 inflammatory disorders including eczema in IPEX syndrome — confirms central role of Th2/IL-4R axis in atopic eczema; supports GR-mediated Th2 suppression as a mechanistic rationale |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational Research | J Allergy Clin Immunol | Cutaneous ceramide synthesis dysregulation in paediatric eosinophilic esophagitis — links epithelial barrier dysfunction across skin and mucosal surfaces; shared pathology relevant to Budesonide's putative mechanism in atopic eczema |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Safety data (warnings, contraindications, drug interactions) were not available in this Evidence Pack. Before any clinical advancement, the current EMA or FDA SmPC for Budesonide must be reviewed, particularly regarding HPA-axis suppression with topical use, contact sensitisation risk in atopic patients, and systemic absorption via compromised skin barrier.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN model assigns a high prediction score (99.96%) for Budesonide in atopic eczema, supported by a plausible GR-agonist / Th2-suppression mechanism shared with established airway indications. However, the human clinical evidence base is absent — the only controlled efficacy signals come from a veterinary RCT and preclinical nanoparticle formulation work — placing this firmly at Evidence Level L4, insufficient for a direct development decision.

**To proceed, the following is needed:**

- **MOA & Safety Data**: Retrieve current Budesonide SmPC (EMA/FDA) for formal MOA, HPA-axis suppression data, contraindications, and drug interaction profile
- **Sensitisation Risk Assessment**: Conduct systematic review of Budesonide contact allergy rates specifically in atopic dermatitis populations, given impaired skin barrier amplifies sensitisation risk (relevant PMIDs: 24603519, 33931866, 30053491)
- **Proof-of-Concept Design**: Design a Phase 2 RCT using novel topical Budesonide delivery (nanoparticle hydrogel formulation per PMID 38275852) to demonstrate skin bioavailability and anti-inflammatory efficacy with minimal systemic absorption
- **Comparator Benchmark**: Establish head-to-head comparison versus established topical corticosteroids (mometasone furoate, fluticasone propionate) and newer non-steroidal topicals (tacrolimus, pimecrolimus) to define the benefit-risk niche
- **Regulatory Pathway Clarification**: Evaluate whether the novel formulation qualifies as a new drug application (505(b)(2) or EMA Article 10a) before resource investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

