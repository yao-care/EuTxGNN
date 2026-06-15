---
layout: default
title: Brinzolamide
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Brinzolamide
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide (AZOPT®) is a topical carbonic anhydrase II inhibitor widely used to reduce elevated intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** with a prediction score of **99.48%**,
however **no clinical trials** and **no publications** specifically targeting this genetic subtype have been identified — the biological rationale relies entirely on mechanistic extrapolation from the extensive open-angle glaucoma evidence base.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L4 (Mechanistic inference; no hereditary glaucoma-specific trials or literature) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Brinzolamide is a highly selective inhibitor of carbonic anhydrase II (CA II), the enzyme that catalyzes CO₂ hydration to bicarbonate in the ciliary body epithelium. By blocking this step, brinzolamide disrupts active ion transport into the posterior chamber, reducing aqueous humor production and thereby lowering IOP by up to 18% from baseline. This mechanism is independent of the aqueous outflow pathway — meaning it works regardless of what is causing the drainage obstruction.

Primary hereditary glaucoma encompasses a spectrum of genetically defined subtypes, including juvenile open-angle glaucoma (MYOC mutations), adult-onset hereditary glaucoma (OPTN mutations), and congenital glaucoma (CYP1B1 mutations causing trabecular meshwork and Schlemm's canal developmental defects). Despite their diverse genetic origins, all these subtypes converge on the same downstream pathology: elevated IOP from impaired trabecular meshwork function and increased aqueous outflow resistance. Since brinzolamide reduces aqueous production rather than improving outflow, it addresses the IOP endpoint irrespective of the genetic aetiology — making the mechanistic extrapolation from sporadic OAG to hereditary glaucoma biologically sound.

The TxGNN knowledge graph prediction (99.48%) reflects this pharmacological overlap. The extensive Phase 3 RCT evidence base in primary open-angle glaucoma (48+ registered trials, total enrollment exceeding 3,600 patients across completed studies) provides a strong indirect foundation. The key unanswered question is whether patients with congenital trabecular malformations show equivalent IOP-lowering response to CA inhibition compared to sporadic OAG populations — and whether paediatric systemic absorption risk for brinzolamide has been adequately characterised for neonatal and infant subpopulations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for primary hereditary glaucoma.

> **Context note:** Extensive Phase 3 RCT evidence exists for open-angle glaucoma (TxGNN ranks 2–4: "glaucoma 1, open angle", "glaucoma", "open angle glaucoma"), including multiple completed large-scale trials. The 10 most relevant trials for the broader glaucoma evidence base are summarised below for reference:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01309204](https://clinicaltrials.gov/study/NCT01309204) | Phase 3 | Completed | 1,184 | Largest OAG trial: Brinzolamide/Brimonidine fixed-dose combination non-inferior to concomitant use in IOP lowering |
| [NCT01297920](https://clinicaltrials.gov/study/NCT01297920) | Phase 3 | Completed | 1,062 | Brinzolamide 1%/Brimonidine 0.2% fixed combination vs. individual components TID in OAG; 3-month + 3-month safety extension |
| [NCT01297517](https://clinicaltrials.gov/study/NCT01297517) | Phase 3 | Completed | 1,001 | Fixed combination Brinzolamide/Brimonidine vs. monotherapy TID in OAG: efficacy and safety confirmed |
| [NCT05022004](https://clinicaltrials.gov/study/NCT05022004) | Phase 3 | Completed | 599 | Therapeutic equivalence of generic Brinzolamide 1% vs. Azopt® in primary OAG and ocular hypertension |
| [NCT02512042](https://clinicaltrials.gov/study/NCT02512042) | Phase 3 | Completed | 973 | Bioequivalence study of generic Brinzolamide vs. Azopt® in chronic OAG |
| [NCT02339584](https://clinicaltrials.gov/study/NCT02339584) | Phase 3 | Completed | 493 | Fixed combination Brinzolamide 10 mg/mL / Brimonidine 2 mg/mL BID vs. unfixed combination: IOP-lowering comparison |
| [NCT00314171](https://clinicaltrials.gov/study/NCT00314171) | Phase 3 | Completed | 437 | Core OAG/ocular hypertension safety and efficacy study |
| [NCT04944290](https://clinicaltrials.gov/study/NCT04944290) | Phase 3 | Completed | 447 | Generic Brinzolamide/Brimonidine 1% vs. Simbrinza® in primary OAG |
| [NCT01978600](https://clinicaltrials.gov/study/NCT01978600) | Phase 4 | Completed | 89 | 24-hour IOP control quality with Simbrinza™ — clinically relevant for day-round pressure management |
| [NCT00758342](https://clinicaltrials.gov/study/NCT00758342) | Phase 4 | Terminated | 37 | Brinzolamide 1% as adjunctive therapy in **chronic angle-closure glaucoma** — only direct trial in non-OAG subtype; terminated early, limited data |

---

## Literature Evidence

Currently no related literature available specifically for primary hereditary glaucoma.

> **Context note:** The broader open-angle glaucoma evidence base includes 20+ publications. The most relevant are:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | Systematic Review | Ophthalmology | Network meta-analysis of first-line medications for POAG; brinzolamide ranked among effective agents |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | RCT (Head-to-head) | Cureus | Brinzolamide/Timolol vs. Dorzolamide/Timolol in Indian POAG patients; Phase 3; confirms efficacy across ethnic populations |
| [38598266](https://pubmed.ncbi.nlm.nih.gov/38598266/) | 2024 | Comparative Study | J Ocul Pharmacol Ther | Brinzolamide-Brimonidine vs. Latanoprost-Timolol in POAG/OHT; 1-year prospective data |
| [31293419](https://pubmed.ncbi.nlm.nih.gov/31293419/) | 2019 | Systematic Review & Meta-analysis | Front Pharmacol | Brinzolamide as add-on to prostaglandin analogues or β-blockers; efficacy and safety confirmed across pooled studies |
| [25064721](https://pubmed.ncbi.nlm.nih.gov/25064721/) | 2014 | RCT | Ophthalmology | Twice-daily Brinzolamide/Brimonidine fixed combination vs. monotherapy in OAG/OHT — Phase 3 pivotal trial |
| [26648686](https://pubmed.ncbi.nlm.nih.gov/26648686/) | 2015 | Clinical Effectiveness | Clin Ophthalmol | Brinzolamide 1%/Brimonidine 0.2% fixed combination for POAG; adherence benefits of fixed-dose approach |
| [14565787](https://pubmed.ncbi.nlm.nih.gov/14565787/) | 2003 | Narrative Review | Drugs & Aging | Foundational review of brinzolamide as primary therapy in POAG and ocular hypertension; establishes 18% IOP reduction benchmark |
| [18312166](https://pubmed.ncbi.nlm.nih.gov/18312166/) | 2008 | Drug Review | Expert Opin Pharmacother | Brinzolamide mechanism, retinal blood flow improvement, and long-term OAG management |
| [35026861](https://pubmed.ncbi.nlm.nih.gov/35026861/) | 2022 | RCT | J Clin Pharm Ther | **Direct evidence in acute primary angle-closure:** Brinzolamide effective in sequential treatment of acute angle closure (131 eyes) — supports use beyond OAG |
| [39870471](https://pubmed.ncbi.nlm.nih.gov/39870471/) | 2025 | Case Report | BMJ Case Reports | ⚠️ Safety signal: Brinzolamide-induced ciliary body effusion causing secondary angle closure and myopic shift — important monitoring consideration |

---

## Taiwan Market Information

Brinzolamide is not currently approved or marketed in Taiwan. No regulatory authorizations are on record, and no approved indication text is available from this source.

> **Global context for reference:** Brinzolamide is internationally available as:
> - **AZOPT® 1%** (monotherapy, approved in USA, EU, and multiple markets for POAG/OHT)
> - **Simbrinza®** (Brinzolamide 1% / Brimonidine 0.2%, approved in USA and EU)
> - **Azarga®** (Brinzolamide 1% / Timolol 0.5%, approved in EU and other markets)
>
> This global approval profile is evidenced by the multinational clinical trial programme documented in ranks 2–4 of this report.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications) from Taiwan regulatory sources are not available for this candidate. No drug-drug interactions were identified in the database query.

The following safety signals are identified from clinical literature:

- **Drug-induced secondary angle closure (2025 case report):** PMID 39870471 describes brinzolamide-induced unilateral ciliary body effusion presenting as acute angle closure with myopic shift, resolving after drug cessation and atropine. **This is a clinically important consideration if brinzolamide is used in hereditary glaucoma patients with anatomically shallow anterior chambers or pre-existing angle-closure risk** — particularly relevant for CYP1B1-associated congenital glaucoma.
- **Sulfonamide class effects:** As a sulfonamide derivative, brinzolamide carries a class-level risk for hypersensitivity reactions in sulfonamide-sensitive patients.
- **Paediatric systemic absorption:** For congenital glaucoma subtypes requiring treatment in neonates and infants, systemic absorption of topical brinzolamide is of concern; punctal occlusion and lid closure technique are recommended.

Please refer to the current SmPC for complete safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Primary hereditary glaucoma shares the core pathophysiology of elevated IOP with sporadic open-angle glaucoma — the mechanistic basis for brinzolamide use is sound — but no clinical data exist specifically in genetically-defined hereditary glaucoma populations, making this purely an inference from the extensive OAG evidence base. The prediction score of 99.48% reflects knowledge graph proximity, not validated clinical efficacy in this subtype.

**To proceed, the following is needed:**

- Retrospective registry analysis or chart review in genetically-confirmed hereditary glaucoma patients (MYOC, OPTN, CYP1B1 mutation carriers) treated with CA inhibitors to characterise IOP response
- Paediatric pharmacokinetic data for brinzolamide in congenital glaucoma populations (neonatal/infant systemic exposure quantification)
- MOA documentation from DrugBank (currently unavailable) to formally establish CA II selectivity profile for regulatory submissions
- Taiwan TFDA package insert retrieval for local contraindication and warning data
- Evaluation of whether hereditary glaucoma subtype (developmental malformation vs. MYOC-linked adult-onset) affects CA inhibitor IOP-response magnitude
- If evidence is supportive: design a prospective sub-study within existing hereditary glaucoma registries (e.g., international GIGA consortium) to formally characterise brinzolamide response as adjunctive therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

