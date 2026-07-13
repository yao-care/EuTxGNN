---
layout: default
title: Lebrikizumab
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From Atopic Dermatitis to Dermatitis

## One-Sentence Summary

Lebrikizumab is a high-affinity IgG4 monoclonal antibody that selectively inhibits interleukin-13 (IL-13), globally approved for moderate-to-severe atopic dermatitis by the FDA and EMA in 2023, but currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **Dermatitis** (atopic dermatitis) — the highest-evidence prediction in this report —
with **29 clinical trials** and **20 publications** supporting this direction, representing an evidence level of **L1** and a Taiwan regulatory gap, not an efficacy concern.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atopic dermatitis (FDA/EMA approved 2023; not yet filed in Taiwan) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 95.97% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 (Taiwan) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lebrikizumab selectively binds to IL-13 with high affinity, preventing the formation of the IL-4Rα/IL-13Rα1 heterodimer signaling complex downstream. IL-13 is the central pathogenic cytokine in atopic dermatitis: it directly suppresses epidermal barrier proteins such as filaggrin (FLG) and loricrin (LOR), activates the IL-31/TSLP itch sensitization pathway, and sustains chronic Th2 lymphocyte infiltration in skin tissue. By blocking this upstream driver, lebrikizumab simultaneously addresses barrier disruption, inflammation, and pruritus. Detailed Taiwan-specific mechanism of action data is currently unavailable pending DrugBank API query resolution (Data Gap DG002), but the global pharmacological rationale is comprehensively established across the Phase 2 and Phase 3 clinical program.

The TxGNN prediction for dermatitis is not a speculative hypothesis but a confirmation of clinically validated efficacy. Multiple Phase 3 pivotal trials (ADvocate1, ADvocate2, ADhere, ADjoin) across thousands of patients have demonstrated statistically significant and clinically meaningful improvements in EASI-75, IGA 0/1, and pruritus scores. The NEJM publication of the dual pivotal trial results in 2023 (PMID 36920778) represents one of the strongest regulatory packages for a biologic in inflammatory dermatology in recent years. Global regulators — FDA (October 2023) and EMA (2023) — have both issued approvals.

Taiwan's "未上市" (not marketed) status for lebrikizumab reflects the absence of a TFDA NDA filing, not any unresolved question about efficacy or safety. The drug's selective IL-13 mechanism differentiates it from dupilumab (dual IL-4/IL-13 blockade) by demonstrating a notably lower rate of treatment-associated conjunctivitis in indirect comparisons, which may represent a clinical advantage for certain patient populations. Taiwan patients with moderate-to-severe atopic dermatitis who are inadequately controlled on topical therapies currently lack access to this approved treatment option.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04146363](https://clinicaltrials.gov/study/NCT04146363) | Phase 3 | Completed | 424 | ADvocate1: 52-week double-blind monotherapy trial; confirmed EASI-75 and IGA 0/1 at Week 16 and Week 52; primary pivotal trial for FDA/EMA NDA submission |
| [NCT04178967](https://clinicaltrials.gov/study/NCT04178967) | Phase 3 | Completed | 445 | ADvocate2: 52-week double-blind monotherapy trial (second pivotal arm); results consistent with ADvocate1, jointly supporting regulatory approval |
| [NCT04250337](https://clinicaltrials.gov/study/NCT04250337) | Phase 3 | Completed | 228 | ADhere: 16-week double-blind trial of lebrikizumab in combination with topical corticosteroids; EASI-75 significantly exceeded placebo + TCS arm |
| [NCT04760314](https://clinicaltrials.gov/study/NCT04760314) | Phase 3 | Completed | 286 | ADhere-J: Combination-with-TCS trial in Japanese patients; efficacy and safety consistent with global studies — directly relevant to East Asian populations |
| [NCT04250350](https://clinicaltrials.gov/study/NCT04250350) | Phase 3 | Completed | 206 | ADore: 52-week open-label study in adolescents (≥12 to <18 years, ≥40 kg); pediatric safety and efficacy confirmed, supporting label extension |
| [NCT04392154](https://clinicaltrials.gov/study/NCT04392154) | Phase 3 | Completed | 1153 | ADjoin: Long-term safety and efficacy extension up to 33 months; largest study in the lebrikizumab program, providing 2-year durability data |
| [NCT05149313](https://clinicaltrials.gov/study/NCT05149313) | Phase 3 | Completed | 331 | Phase 3 in patients not adequately controlled with cyclosporine or for whom cyclosporine is medically inadvisable; addresses important treatment-refractory population |
| [NCT02340234](https://clinicaltrials.gov/study/NCT02340234) | Phase 2 | Completed | 212 | Key proof-of-concept trial: double-blind 12-week study in adults with TCS-inadequate AD; established mechanism, dose selection, and Phase 3 design rationale |
| [NCT03443024](https://clinicaltrials.gov/study/NCT03443024) | Phase 2 | Completed | 280 | Dose-ranging trial confirming optimal 250 mg Q2W induction / Q4W maintenance regimen for Phase 3 program |
| [NCT04626297](https://clinicaltrials.gov/study/NCT04626297) | Phase 3 | Completed | 254 | Vaccine response sub-study: assessed impact of lebrikizumab on immunogenicity of non-live vaccines — no clinically meaningful impairment observed |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36920778](https://pubmed.ncbi.nlm.nih.gov/36920778/) | 2023 | Phase 3 RCT | N Engl J Med | ADvocate1&2 dual pivotal trial report: EASI-75 at Week 52 reached 43.1–51.4%; IGA 0/1 at Week 16 ~38%; primary and secondary endpoints met |
| [36994947](https://pubmed.ncbi.nlm.nih.gov/36994947/) | 2023 | Phase 3 RCT | Br J Dermatol | 52-week extended results from both ADvocate trials; durable response maintained across induction and maintenance phases |
| [36630140](https://pubmed.ncbi.nlm.nih.gov/36630140/) | 2023 | Phase 3 RCT | JAMA Dermatol | ADhere: lebrikizumab + TCS vs placebo + TCS; EASI-75 at 16 weeks significantly superior in combination arm; confirms TCS add-on benefit |
| [37318750](https://pubmed.ncbi.nlm.nih.gov/37318750/) | 2023 | Phase 3 RCT | Dermatol Ther | ADore: 52-week adolescent results; safety and efficacy consistent with adult pivotal data, supporting pediatric label |
| [40549127](https://pubmed.ncbi.nlm.nih.gov/40549127/) | 2025 | Phase 3 RCT | Dermatol Ther | ADjoin 2-year data: maintained clinical response through 104 weeks; favorable long-term safety including low injection-site reactions |
| [39018058](https://pubmed.ncbi.nlm.nih.gov/39018058/) | 2024 | Living Systematic Review + NMA | JAMA Dermatol | Network meta-analysis comparing lebrikizumab to dupilumab, tralokinumab, upadacitinib, baricitinib, abrocitinib; lebrikizumab ranked among top-tier options |
| [37678577](https://pubmed.ncbi.nlm.nih.gov/37678577/) | 2023 | Systematic Review + NMA | J Allergy Clin Immunol | Comprehensive NMA of AD systemic treatments; lebrikizumab demonstrated superior EASI-75 and IGA vs placebo with favorable comparative safety |
| [39629076](https://pubmed.ncbi.nlm.nih.gov/39629076/) | 2024 | Systematic Review | Front Pharmacol | Meta-analysis across Phase 2/3 RCTs confirming efficacy and safety profile in adolescents and adults with moderate-to-severe AD |
| [37195407](https://pubmed.ncbi.nlm.nih.gov/37195407/) | 2023 | Pooled Safety Analysis | Am J Clin Dermatol | Integrated safety analysis across 8 clinical trials (N>2,000); confirmed low conjunctivitis incidence (a key differentiator vs dupilumab) |
| [32101256](https://pubmed.ncbi.nlm.nih.gov/32101256/) | 2020 | Phase 2 RCT | JAMA Dermatol | Phase 2b dose-ranging study: IL-13 blockade with lebrikizumab demonstrated significant EASI reduction vs placebo; established proof-of-concept for Phase 3 |

---

## Taiwan Regulatory Status

No Taiwan (TFDA) marketing authorization data is on file. Lebrikizumab (brand name: **Ebglyss**, Eli Lilly) holds the following global approvals for moderate-to-severe atopic dermatitis in adults and adolescents (≥12 years, ≥40 kg):

| Regulatory Body | Approval Year | Approved Indication |
|----------------|---------------|---------------------|
| U.S. FDA | 2023 | Moderate-to-severe atopic dermatitis in adults and adolescents ≥12 years when systemic therapy is appropriate |
| EMA (European Union) | 2023 | Moderate-to-severe atopic dermatitis in adults and adolescents ≥12 years who are candidates for systemic therapy |

A Taiwan TFDA NDA filing has not yet been initiated; no domestic authorization exists as of this report date.

---

## Safety Considerations

- **Key Observations from Phase 3 Program**: Conjunctivitis incidence with lebrikizumab is notably lower than dupilumab in indirect comparisons — a clinically meaningful differentiator attributed to selective IL-13 (vs dual IL-4/IL-13) blockade. Mild-to-moderate injection site reactions are the most commonly reported adverse event.
- **Drug Interactions**: No drug-drug interaction data was identified in the current query (DDI query status: not found).

> TFDA package insert warnings and contraindications for Taiwan are not yet available (Data Gap DG001). For complete safety information, refer to the FDA-approved prescribing information or EMA SmPC for Ebglyss.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lebrikizumab has achieved L1 evidence (multiple completed Phase 3 RCTs including dual pivotal trials published in the NEJM), with global regulatory approvals from both the FDA and EMA in 2023. The TxGNN prediction for dermatitis is confirmed by this robust clinical evidence base. The Taiwan "未上市" status is a regulatory filing gap — Taiwan patients with moderate-to-severe atopic dermatitis inadequately controlled on topical therapies are currently unable to access an EMA/FDA-validated treatment option.

**To proceed, the following is needed:**

- **TFDA NDA submission**: File a Taiwan NDA using the existing FDA/EMA pivotal dossier (ADvocate1&2, ADhere, ADjoin); a bridging study leveraging ADhere-J (Japanese Phase 3, n=286) may support East Asian data requirements
- **Safety documentation**: Resolve Data Gap DG001 by downloading and parsing the TFDA package insert PDF once available; obtain Taiwan-specific risk management plan
- **MOA documentation**: Complete DrugBank API query for full mechanism of action text (Data Gap DG002)
- **NHI reimbursement strategy**: Evaluate cost-effectiveness submission pathway under Taiwan National Health Insurance, given the availability of dupilumab as a comparator
- **Real-world evidence planning**: Consider post-approval observational registry in Taiwan to capture local AD patient characteristics and treatment response patterns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

