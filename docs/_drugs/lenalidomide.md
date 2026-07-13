---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Lenalidomide
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

# Lenalidomide: From Multiple Myeloma / del(5q) MDS to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide is an oral immunomodulatory drug (IMiD) originally approved in multiple countries for multiple myeloma and transfusion-dependent anemia due to low-risk myelodysplastic syndrome (MDS) with del(5q) cytogenetic abnormality — though it carries no Taiwan regulatory registration at this time.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** (encompassing AML and the broader MDS spectrum beyond del(5q)),
with **multiple completed Phase 2/3 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma; del(5q) MDS (global approvals — not registered in Taiwan) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lenalidomide exerts its anti-cancer activity primarily through the cereblon (CRBN)–CRL4A E3 ubiquitin ligase complex. By binding CRBN, lenalidomide redirects the ligase to ubiquitinate and proteasomally degrade key transcription factors — most notably IKZF1 (Ikaros) and CK1α (encoded by *CSNK1A1* at chromosomal locus 5q31.2). The resulting loss of these proteins drives selective apoptosis in malignant hematopoietic cells while sparing most normal progenitors. In parallel, lenalidomide enhances NK cell–mediated cytotoxicity, suppresses regulatory T cells (Tregs), and inhibits pro-tumorigenic cytokines including TNF-α and VEGF, creating a multi-pronged anti-tumor immune environment.

The mechanistic connection to myeloid leukemia is most directly established in the del(5q) AML subtype. In cells carrying a 5q31.2 deletion, haploinsufficiency of *CSNK1A1* leaves only one functional CK1α allele. Lenalidomide-driven CK1α degradation pushes these cells below a critical threshold, triggering p53-dependent selective apoptosis — while normal cells with two intact alleles produce sufficient residual CK1α and are relatively spared. This biology directly underpins lenalidomide's established efficacy in del(5q) MDS (globally approved) and provides a biologically grounded rationale for extension into del(5q) AML.

Beyond the del(5q) subtype, the close biological relationship between MDS and AML — both arising from clonal hematopoietic stem cell disorders, with MDS frequently progressing to AML — supports applying lenalidomide across the broader myeloid leukemia spectrum. Multiple clinical programs have combined lenalidomide with hypomethylating agents (azacitidine) and conventional chemotherapy (MEC: mitoxantrone, etoposide, cytarabine), or employed it as post-remission maintenance, demonstrating active clinical investigation in AML across multiple lines of therapy and patient age groups.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00179621](https://clinicaltrials.gov/study/NCT00179621) | Phase 3 | Completed | 205 | Multicenter randomized double-blind placebo-controlled 3-arm study comparing lenalidomide 10 mg vs 5 mg vs placebo in transfusion-dependent low/intermediate-1 risk MDS with del(5q); highest-quality evidence in myeloid disease |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | MEC (mitoxantrone, etoposide, cytarabine) + lenalidomide in relapsed/refractory AML adults; provides direct efficacy and safety data for lenalidomide in AML combination therapy |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | 3-arm randomized trial of lenalidomide alone, sequential azacitidine + lenalidomide, or azacitidine alone in elderly (≥65 y) newly diagnosed AML |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | Completed | 37 | Sequential azacitidine and lenalidomide in relapsed/refractory AML; primary endpoint CR/CRi rate |
| [NCT02538965](https://clinicaltrials.gov/study/NCT02538965) | Phase 2 | Completed | 17 | Single-agent lenalidomide in pediatric relapsed/refractory AML (≥2nd relapse or refractory to ≥2 induction attempts); assessed morphological complete response within first 4 cycles |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | Unknown | 60 | Azacitidine + lenalidomide as MRD-monitored maintenance in elderly/unfit AML patients; MRD-guided strategy based on Chinese registry data |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML in first remission; investigated immune mechanism of disease-free survival benefit |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2 | Active, Not Recruiting | 282 | Randomized Phase II/III: azacitidine ± lenalidomide vs ± vorinostat in higher-risk MDS and CMML; large comparative dataset with long follow-up |
| [NCT01442714](https://clinicaltrials.gov/study/NCT01442714) | Phase 2 | Terminated | 33 | Azacitidine + lenalidomide in elderly previously treated AML; early termination limits conclusions but combination safety data remain informative |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | Completed | 51 | Sequential idarubicin + cytarabine followed by lenalidomide in MDS (RAEB-2) or untreated AML; evaluated safety, response rates, and response duration |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic Review & Meta-analysis | Hematology | Pooled analysis of azacitidine + lenalidomide in AML, high-risk MDS, and CMML; evaluated overall response rate, CR rate, and adverse event profile |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | Systematic Review & Meta-analysis | Cancer Manag Res | Comprehensive review of lenalidomide efficacy and safety specifically in AML; addressed controversy over whether lenalidomide significantly improves response and OS |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Mechanistic Study | Cell Mol Biol Lett | Identified KDM5C histone demethylase as a CRBN stabilizer; KDM5C enhances AML cell sensitivity to lenalidomide by maintaining CRBN protein levels — clarifies resistance mechanism |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospective Phase 2 (Azalena Trial) | Haematologica | Azacitidine + lenalidomide + donor lymphocyte infusions as first salvage for post-transplant relapse of AML, MDS, and CMML; 50 patients enrolled, prospective design |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS 2023 update on diagnosis, risk stratification, and management; covers lenalidomide's established role and current guideline positioning |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Review / Trial Report | Leukemia | Critical appraisal of azacitidine + lenalidomide combination rationale in advanced MDS/AML; discusses epigenetic and immunological synergism |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | Retrospective Cohort | Blood | ⚠️ **Safety Warning**: Lenalidomide exposure selectively promotes TP53-mutated therapy-related myeloid neoplasms through clonal positive selection pressure (n=416 t-MN patients) |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Comprehensive review of lenalidomide as a novel AML treatment; summarizes clinical trial results and mechanistic rationale across AML subtypes |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase 1 Trial | Bone Marrow Transplant | Lenalidomide maintenance post-allogeneic transplant in unfavorable-risk AML and high-risk MDS; dose-escalation (5–15 mg) safety study, n=16 |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | Prospective Study | Front Immunol | Azacitidine + low-dose lenalidomide as post-allo-HSCT relapse prophylaxis in AML (ChiCTR2200061803); reports efficacy and tolerability with MRD guidance |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunomodulatory agent (IMiD) — not a conventional cytotoxic; anti-leukemic activity via CRBN-mediated degradation of IKZF1 and CK1α (targeted mechanism) |
| Myelosuppression Risk | High — thrombocytopenia and neutropenia are the primary dose-limiting toxicities observed across del(5q) MDS and AML clinical trials |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (weekly for first 8 weeks, then monthly); serum creatinine / eGFR — dose adjustment required when CrCl < 60 mL/min (lenalidomide is renally excreted); liver function tests |
| Handling Protection | Standard oral oncology precautions; teratogenic risk mandatory prevention program required (REMS in the US; Pregnancy Prevention Programme in EU/EMA) — thalidomide structural analogue with confirmed Category X teratogenicity |

---

## Safety Considerations

No Taiwan regulatory warnings, contraindications, or drug-drug interaction data are available in this Evidence Pack. Two critical safety signals are identified from the published literature:

- **Therapy-related secondary malignancy**: Retrospective analysis of 416 therapy-related myeloid neoplasm patients (PMID 35512188) found that lenalidomide exposure selectively promotes outgrowth of TP53-mutated clones through positive selection pressure, increasing the risk of therapy-related myeloid neoplasms. This finding must be proactively disclosed in informed consent for any off-label or investigational use.

- **Secondary B-cell acute lymphoblastic leukemia (B-ALL)**: Multiple case series and cohort studies report secondary B-ALL following lenalidomide-containing regimens, particularly in the setting of autologous stem cell transplant with lenalidomide maintenance (PMID 32880627, PMID 33512465). Active longitudinal surveillance for lineage switch is warranted.

Please refer to the current SmPC and/or US Prescribing Information for complete, up-to-date safety details.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for lenalidomide in myeloid leukemia meets L1 criteria, anchored by two completed Phase 3 RCTs in myeloid disease (NCT00179621, n=205; NCT01029262, n=239), multiple completed Phase 2 trials directly in AML (including NCT03118466 and NCT01358734), and a systematic review with meta-analysis (PMID 31221030). The mechanistic rationale — CRBN-mediated CK1α degradation with haploinsufficiency amplification in del(5q) cells — is among the most precisely characterized in drug repurposing. However, the absence of Taiwan regulatory data, the documented secondary malignancy risk (TP53 clonal selection; secondary B-ALL), and the lack of formal MOA documentation in the Evidence Pack necessitate structured guardrails before clinical application.

**To proceed, the following is needed:**
- Obtain TFDA prescribing information or SmPC: key warnings, contraindications, and drug-drug interaction profile (resolve Data Gap DG001)
- Retrieve DrugBank MOA documentation to formally characterize the mechanism for regulatory submissions (resolve Data Gap DG002)
- Define patient selection criteria by cytogenetic subtype (del(5q) vs. non-del(5q)) to optimize the therapeutic index
- Establish a secondary malignancy surveillance protocol: periodic molecular testing for TP53 clonal evolution and B-ALL lineage monitoring
- Clarify the regulatory pathway for compassionate use, named-patient access, or clinical trial enrollment in Taiwan (given current non-marketing status)
- Implement a mandatory pregnancy prevention program before any clinical use, consistent with global REMS/PPP requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

