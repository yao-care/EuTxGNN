---
layout: default
title: Azacitidine
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Azacitidine
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

# Azacitidine: From Myelodysplastic Syndrome to Aregenerative Anemia

> **Note on prediction selection:** The highest-ranked TxGNN prediction (Rank 1: bulbar polio, 98.59%) was set aside due to extremely low biological plausibility — no known mechanistic link between DNMT inhibition and poliovirus infection exists, and no clinical or preclinical evidence supports this pairing. This report focuses on **Rank 5: Aregenerative Anemia**, which carries the highest evidence level (L2) among all actionable predictions and a "Proceed with Guardrails" recommendation.

---

## One-Sentence Summary

Azacitidine is a hypomethylating agent (DNA methyltransferase inhibitor) globally approved for myelodysplastic syndromes (MDS) and acute myeloid leukemia (AML) in adults, but currently not approved in Taiwan.
The TxGNN model predicts it may be effective for **Aregenerative Anemia** — a category encompassing aplastic, hypoplastic, and sideroblastic anemias within the MDS spectrum —
with **27 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MDS (intermediate-2/high-risk) and AML with 20–30% blasts — EU/US approved; **not approved in Taiwan** |
| Predicted New Indication | Aregenerative Anemia |
| TxGNN Prediction Score | 97.88% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from the TFDA dossier is not currently available. Based on established pharmacology, azacitidine is a nucleoside analogue that incorporates into DNA and RNA, blocking DNMT1, DNMT3A, and DNMT3B activity and causing progressive DNA hypomethylation over successive replication cycles. This demethylation reactivates silenced tumor suppressor genes, rescues the differentiation of arrested hematopoietic progenitor cells, and triggers apoptosis in abnormal clones — making it the backbone of first-line treatment for higher-risk MDS and AML worldwide (NCCN, ELN, ESMO guidelines).

Aregenerative anemia overlaps substantially with MDS in clinical presentation. Refractory anemia subtypes (RARS, RCMD) and aplastic/hypoplastic bone marrow failure share a common underlying thread: epigenetic dysregulation of hematopoietic stem cell differentiation with consequent impaired erythropoiesis. Azacitidine's mechanism directly addresses this pathway. The AVIDA registry confirmed real-world use of azacitidine across all MDS subtypes, including the large proportion presenting primarily as transfusion-dependent anemia. A translational case series (PMID 34781359) further extended the mechanistic reach: azacitidine restored erythropoiesis in pyridoxine-refractory X-linked sideroblastic anemia by upregulating ALAS2 expression through promoter demethylation — demonstrating activity beyond classical MDS into a congenital aregenerative form.

The strongest supporting trial is NCT00454480, a Phase 2/3 program enrolling 2,000 older patients with high-risk MDS and AML, where a substantial proportion presented with profound anemia as the predominant disease manifestation. Together with prospective meta-analyses of azacitidine in lower-risk transfusion-dependent MDS (PMID 29118268), this creates an L2 evidence foundation that justifies a conditional "Proceed with Guardrails" decision pending Taiwan-specific regulatory data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Largest AZA-containing MDS/AML program in older patients; includes high-risk MDS subtypes with profound anemia; provides robust safety and efficacy baseline |
| [NCT00392353](https://clinicaltrials.gov/study/NCT00392353) | Phase 1/2 | Active, not recruiting | 135 | Vorinostat + azacitidine in MDS/AML; dual epigenetic approach; includes anemia-predominant MDS patients |
| [NCT02158936](https://clinicaltrials.gov/study/NCT02158936) | Phase 3 | Terminated | 356 | Eltrombopag + azacitidine in IPSS Int-1/2 and high-risk MDS; large randomized trial terminated early; generates meaningful anemia/thrombocytopenia correction data |
| [NCT01928537](https://clinicaltrials.gov/study/NCT01928537) | Phase 3 | Completed | 67 | Rigosertib vs physician's choice after AZA/DAC failure in MDS with excess blasts; provides AZA response-rate baseline in anemic MDS population |
| [NCT01839240](https://clinicaltrials.gov/study/NCT01839240) | Phase 1 | Completed | 50 | AZA + HiDAC + mitoxantrone in high-risk AML (partly MDS-evolved); azacitidine priming to sensitize cells to subsequent chemotherapy |
| [NCT01065129](https://clinicaltrials.gov/study/NCT01065129) | Phase 1 | Completed | 28 | Plerixafor + G-CSF + azacitidine in MDS; stem cell mobilization alongside demethylation in bone marrow failure with anemia |
| [NCT02553941](https://clinicaltrials.gov/study/NCT02553941) | Phase 1b | Completed | 21 | Ibrutinib + azacitidine in higher-risk MDS; novel immune modulation approach in transfusion-dependent patients |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | Completed | 37 | Lenalidomide + azacitidine in advanced MDS; combination epigenetic-immunomodulatory strategy for anemia-driven MDS |
| [NCT01016600](https://clinicaltrials.gov/study/NCT01016600) | Phase 1/2 | Completed | 31 | AZA + lenalidomide in AML; partly includes MDS-evolved AML with prior refractory anemia |
| [NCT00398047](https://clinicaltrials.gov/study/NCT00398047) | Phase 2 | Terminated | 3 | AZA + darbepoetin alfa + G-CSF in MDS; rationale: boost erythropoiesis alongside demethylation; terminated due to poor accrual — no efficacy conclusions |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34781359](https://pubmed.ncbi.nlm.nih.gov/34781359/) | 2022 | Case series / Translational | Blood Advances | Azacitidine restored erythropoiesis in pyridoxine-refractory X-linked sideroblastic anemia via ALAS2 promoter demethylation — direct evidence in a congenital aregenerative anemia |
| [38023359](https://pubmed.ncbi.nlm.nih.gov/38023359/) | 2023 | Translational | Experimental and Therapeutic Medicine | Glutathione enhances synergistic killing by venetoclax + azacitidine in MDS-RAEB (refractory anemia with excess blasts) via cell cycle regulation |
| [36309981](https://pubmed.ncbi.nlm.nih.gov/36309981/) | 2023 | Phase 1b | American Journal of Hematology | Venetoclax + azacitidine in R/R MDS; safety and efficacy in heavily pretreated patients with bone marrow failure |
| [29118268](https://pubmed.ncbi.nlm.nih.gov/29118268/) | 2018 | Meta-analysis | The Oncologist | Meta-analysis of AZA in lower-risk transfusion-dependent MDS after ESA failure; transfusion independence and hematologic improvement as primary endpoints |
| [27107658](https://pubmed.ncbi.nlm.nih.gov/27107658/) | 2016 | Retrospective multicenter | Leukemia Research | Azacitidine vs decitabine head-to-head in RAEB (n=88); comparative efficacy in refractory anemia with excess blasts |
| [26855506](https://pubmed.ncbi.nlm.nih.gov/26855506/) | 2016 | Prospective pilot | Indian J Hematol Blood Transfus | Low-dose cytarabine + azacitidine in elderly AML/MDS-RAEB2 (n=29); feasibility in frail patients with profound anemia |
| [21947085](https://pubmed.ncbi.nlm.nih.gov/21947085/) | 2012 | Pilot study (prospective) | Annals of Hematology | AZA + low-dose cytarabine in newly diagnosed RAEB (n=18); response rate and safety data in anemia-predominant MDS |
| [21431628](https://pubmed.ncbi.nlm.nih.gov/21431628/) | 2011 | Review | Advances in Therapy | AZA for AML with 20–30% blasts and multilineage dysplasia (EU-approved indication); evidence review supporting anemia correction in this border MDS/AML subtype |
| [24195247](https://pubmed.ncbi.nlm.nih.gov/24195247/) | 2013 | Review | Revue Médicale de Bruxelles | Comprehensive review of refractory anemias as MDS; treatment landscape including azacitidine positioning across IPSS risk groups |
| [27976488](https://pubmed.ncbi.nlm.nih.gov/27976488/) | 2017 | Case report | Pediatric Transplantation | Azacitidine as bridge to allogeneic HCT in pediatric Fanconi anemia + AML; demonstrates tolerability in profound bone marrow failure with constitutional anemia |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA methyltransferase inhibitor / Hypomethylating nucleoside analogue |
| Myelosuppression Risk | **High** — neutropenia, thrombocytopenia, and anemia are very common (incidence >30%); CBC with differential must be monitored before each treatment cycle and dose-adjusted accordingly |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (before each cycle), liver function tests (AST/ALT/bilirubin), serum creatinine and BUN, electrolytes |
| Handling Protection | Must comply with cytotoxic drug handling regulations; protective equipment required during preparation and administration |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azacitidine's established mechanism of action directly targets epigenetic dysregulation of hematopoiesis — the central pathology of aregenerative anemia in the MDS spectrum — and is supported by the largest MDS/AML trial program available (n=2,000) plus specific case-series evidence in sideroblastic anemia; the L2 evidence level justifies conditional advancement, provided Taiwan-specific regulatory and safety gaps are addressed.

**To proceed, the following is needed:**
- Taiwan TFDA SmPC or EU/US SmPC review for complete warnings, contraindications, and drug interaction profile (currently blocking — DG001)
- Formal mechanism of action documentation for Taiwan regulatory submission (DG002)
- Precise definition of the target aregenerative anemia subtype (aplastic, MDS-RARS/RCMD, sideroblastic) and corresponding patient population
- Clarification of adult vs. pediatric application scope and appropriate dosing stratification
- Pharmacovigilance plan aligned with Taiwan regulatory requirements for an unapproved drug
- Consider compassionate use application or investigator-initiated trial registration in Taiwan as a near-term pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

