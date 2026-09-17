---
layout: default
title: Zidovudine
parent: AI Predictions (L5)
nav_order: 658
evidence_level: L5
indication_count: 10
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Zidovudine: From HIV/AIDS Antiretroviral Therapy to Female Breast Carcinoma

## One-Sentence Summary

Zidovudine (AZT) is a nucleoside reverse transcriptase inhibitor (NRTI) originally developed and approved for the treatment of HIV-1 infection and AIDS. Among the TxGNN candidate predictions reviewed for this drug, the most scientifically credible and genuinely novel signal points to **Female Breast Carcinoma**, supported by **10 preclinical publications** describing antiproliferative and telomerase-inhibitory activity in human breast cancer cell lines and animal mammary tumor models — but **no dedicated clinical trials** have yet tested this indication.

> **Note on candidate selection:** The Evidence Pack contains 10 TxGNN-predicted indications for zidovudine. The single highest-scoring prediction ("feline acquired immunodeficiency syndrome," score 99.96%) and the second-ranked ("simian immunodeficiency virus infection") are veterinary/primate animal-model diseases, not human indications, and the pack's own rationale explicitly states they carry no direct translational meaning for human drug repurposing (both scored "Hold"). Two other top-10 entries ("congenital human immunodeficiency virus" and "AIDS related complex") are not true *new* indications — they largely overlap with zidovudine's original, already-approved use in HIV/AIDS (including the 1994 PACTG 076 mother-to-child transmission regimen); the pack flags `original_indications` as empty due to a data gap, not because these are novel repurposing candidates. The remaining low-ranked entries (neurodevelopmental disorder, obsolete hyperlipidemia term, fibroma of prostate, Brenner tumor, benign reproductive neoplasm) have little or no supporting evidence. **Female breast carcinoma (rank 9)** is therefore the only candidate in this set that is both a genuine new indication and backed by an identifiable, evidence-based mechanistic rationale, so it is used as the focus of this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection / AIDS (antiretroviral therapy) — established use; not covered by an EU marketing authorization on file |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 96.20% |
| Evidence Level | L4 (preclinical / mechanistic evidence only) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for zidovudine is not available in the Evidence Pack (`original_moa: [Data Gap]`). Based on well-established pharmacology confirmed across the pack's own literature evidence, zidovudine is a thymidine-analogue NRTI: it is phosphorylated intracellularly to its active triphosphate form, which is incorporated into viral DNA by HIV reverse transcriptase, causing chain termination. This mechanism has been proven effective in suppressing HIV replication and remains the basis of its approved antiretroviral use.

The connection to breast carcinoma is mechanistically distinct from the antiviral action but plausible: multiple in vitro and animal studies in this Evidence Pack show that zidovudine's triphosphate can also be incorporated into telomeric DNA repeats of rapidly dividing tumor cells, inhibiting telomerase activity and inducing senescence/apoptosis in breast cancer cell lines (e.g., MCF-7, MDA-MB-231) and in rat mammary tumor models. Because telomerase reactivation is a hallmark of cancer cell immortalization, a nucleoside analogue capable of disrupting telomere maintenance offers a coherent, if still early-stage, biological rationale for repurposing.

Importantly, one of the earliest papers (Wagner et al., 1997, PMID 9192804) notes that zidovudine was "originally designed as an antitumor agent" before its antiviral activity was discovered — meaning the oncology hypothesis predates its HIV indication rather than being a downstream coincidence. However, all supporting evidence to date is preclinical (cell culture and rodent models); no controlled human trials in breast cancer patients have been identified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35584347](https://pubmed.ncbi.nlm.nih.gov/35584347/) | 2022 | Cohort | JCO Global Oncology | In HIV-positive breast cancer patients receiving neoadjuvant chemotherapy, assessed whether relative dose intensity and pathologic complete response differ from HIV-negative patients (antiretroviral background includes zidovudine-containing regimens) |
| [9192804](https://pubmed.ncbi.nlm.nih.gov/9192804/) | 1997 | Preclinical (in vitro/animal) | Cancer Research | Zidovudine showed potent, preferential growth-inhibitory activity in cultured human breast cancer cells and rat mammary tumors; notes prior clinical case reports of response in advanced breast cancer when combined with methotrexate or cisplatin |
| [9533539](https://pubmed.ncbi.nlm.nih.gov/9533539/) | 1998 | Preclinical (in vitro) | Clinical Cancer Research | AZT inhibited growth, colony formation in soft agar, and telomerase activity in four breast cancer cell lines, with lower potency in normal breast cells |
| [10841805](https://pubmed.ncbi.nlm.nih.gov/10841805/) | 2000 | Preclinical (synthesis/in vitro) | Journal of Medicinal Chemistry | Synthesized AZT phosphoramidate monoester prodrugs with enhanced in vitro anti-breast cancer (MCF-7) activity compared to parent AZT |
| [11261835](https://pubmed.ncbi.nlm.nih.gov/11261835/) | 2001 | Preclinical (in vitro) | Breast Cancer Research and Treatment | Chronic in vitro AZT exposure induced senescence and apoptosis and reduced tumorigenicity of metastatic mouse mammary tumor cells |
| [16797627](https://pubmed.ncbi.nlm.nih.gov/16797627/) | 2006 | Preclinical (in vitro) | Toxicology and Applied Pharmacology | AZT combined with cisplatin increased p14ARF tumor-suppressor expression in an ovarian cancer cell line, suggesting a p53-pathway-linked chemosensitizing effect relevant to gynecologic/reproductive tumors |
| [21945463](https://pubmed.ncbi.nlm.nih.gov/21945463/) | 2011 | Preclinical (in vitro) | Bioorganic & Medicinal Chemistry | Novel AZT chloromethylphosphonate derivatives showed cytotoxic activity against MCF-7 breast cancer and KB oral cancer cell lines |
| [27633795](https://pubmed.ncbi.nlm.nih.gov/27633795/) | 2016 | Preclinical (in vitro/animal) | Oncology Reports | AZT exerted antitumoral effects through both telomeric and non-telomeric mechanisms in a mammary adenocarcinoma model |
| [32199136](https://pubmed.ncbi.nlm.nih.gov/32199136/) | 2020 | Preclinical (in vitro) | European Journal of Medicinal Chemistry | AZT-based cationic small-molecule derivatives with antibacterial/anticancer dual activity were shown to regulate metastasis of breast cancer cells |
| [32738968](https://pubmed.ncbi.nlm.nih.gov/32738968/) | 2020 | Preclinical (in vitro) | Bioorganic & Medicinal Chemistry Letters | Tellurium-containing AZT derivatives decreased proliferation and induced apoptosis in MDA-MB-231 triple-negative breast cancer cells |

## EU Market Information

Zidovudine currently has no marketing authorization on file in this Evidence Pack (market status: **Not marketed**, 0 authorizations). No EU product/license table can be generated at this time.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The breast carcinoma signal is biologically plausible and supported by a consistent body of preclinical work spanning over two decades (1997–2020), but it has never advanced into a controlled clinical trial in cancer patients, and no dosing, efficacy, or oncology-specific safety data exist. This places the candidate at an early hypothesis-generation stage rather than one ready for clinical development decisions.

**To proceed, the following is needed:**
- Zidovudine's official mechanism of action (MOA) and full DrugBank pharmacology profile (currently a data gap)
- TFDA/EMA label warnings and contraindications, particularly hematologic toxicity data relevant to combining AZT with cytotoxic chemotherapy regimens (currently a data gap, marked Blocking for safety review)
- A translational/pilot clinical study (Phase 1/2) evaluating zidovudine, alone or combined with existing chemotherapy, specifically in breast carcinoma patients
- Clarification of zidovudine's actual approved indications (the `original_indications` field is empty in this pack), since two other high-ranking predictions (congenital HIV transmission, AIDS-related complex) likely represent existing approved uses rather than new repurposing opportunities and should be reconciled against the drug's real label before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

