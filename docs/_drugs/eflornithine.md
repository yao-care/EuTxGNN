---
layout: default
title: Eflornithine
parent: AI Predictions (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Eflornithine
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

# Eflornithine: From Human African Trypanosomiasis to Bovine Trypanosomiasis (and Monoclonal Gammopathy as a Secondary Hypothesis)

## One-Sentence Summary

Eflornithine (DB06243) is an ornithine decarboxylase (ODC) inhibitor already approved for human African trypanosomiasis (Gambian sleeping sickness). TxGNN's top-ranked prediction (esotropia, 99.85%) has **no supporting evidence and is assessed by the model's own rationale as a likely false positive**; among the ten candidates screened, only two — **bovine trypanosomiasis** and **monoclonal gammopathy** — advanced past initial screening (S1), each supported by **preclinical/mechanistic literature only** (2 and 9 publications respectively, **no clinical trials**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Human African Trypanosomiasis (per repurposing rationale; not separately recorded in structured `original_indications`) |
| Predicted New Indication | Trypanosomiasis, Bovine (primary candidate); Monoclonal Gammopathy (secondary candidate — see below) |
| TxGNN Prediction Score | 98.42% (bovine trypanosomiasis, rank 13,875 of model output) |
| Evidence Level | L4 (preclinical/mechanistic literature only, no clinical trials) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

Note: the model's #1-ranked prediction by raw score, **esotropia** (99.85%), is not used as the headline indication here because it has zero clinical trials, zero literature, and the evidence pack's own mechanistic rationale flags it as "an KG-embedding-similarity false positive." The two candidates below are the only ones that reached decision stage S1 ("Research Question").

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the literature captured here, eflornithine (DFMO, α-difluoromethylornithine) is an irreversible inhibitor of ornithine decarboxylase, the rate-limiting enzyme in polyamine biosynthesis. It is clinically established for late-stage human African trypanosomiasis (*Trypanosoma brucei gambiense*), where blocking parasite polyamine synthesis halts proliferation.

**Bovine trypanosomiasis** is caused by closely related trypanosome species (e.g., *T. congolense*, *T. vivax*) that share highly conserved polyamine metabolism pathways with *T. brucei*. This is the most mechanistically direct extension of the drug's approved use across host species rather than across disease categories, and is supported by *in vitro* evidence (PMID 32053698) showing eflornithine activity against blood parasites including trypanosomes, and mechanistic work on the trypanosomatid polyamine pathway (PMID 23525104).

**Monoclonal gammopathy** (a plasma-cell disorder and myeloma precursor) has a different rationale: multiple 1985–1995 studies show that human myeloma cell lines develop resistance to DFMO via ODC gene amplification/overexpression, demonstrating that the drug-target axis is pharmacologically active in plasma cells. This is evidence of target engagement, not of therapeutic efficacy — no study tested DFMO as a treatment for gammopathy itself, and the evidence base is three decades old with no contemporary follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for either candidate indication (bovine trypanosomiasis or monoclonal gammopathy).

---

## Literature Evidence

### Candidate 1: Trypanosomiasis, Bovine

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32053698](https://pubmed.ncbi.nlm.nih.gov/32053698/) | 2020 | Preclinical/In vitro | PLoS One | Eflornithine shows antitrypanosomal activity against blood parasites (Babesia, Theileria, related trypanosomatids); positioned as best-choice therapy for late-stage human African trypanosomiasis |
| [23525104](https://pubmed.ncbi.nlm.nih.gov/23525104/) | 2013 | Preclinical/Mechanistic | J Biol Chem | Characterizes polyamine biosynthesis as a key drug target in African trypanosomes; eflornithine inhibits the first step (spermidine synthesis) via ODC inhibition |

### Candidate 2: Monoclonal Gammopathy

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7646459](https://pubmed.ncbi.nlm.nih.gov/7646459/) | 1995 | In vitro/Mechanistic | Biochem J | DFMO-resistant human myeloma cells show long-term reduction of amplified ODC gene sequences after drug withdrawal |
| [3934157](https://pubmed.ncbi.nlm.nih.gov/3934157/) | 1985 | In vitro/Mechanistic | J Biol Chem | ODC is translationally regulated by polyamines in DFMO-resistant mouse myeloma cells |
| [3015379](https://pubmed.ncbi.nlm.nih.gov/3015379/) | 1986 | In vitro/Mechanistic | Cancer Research | Polyamines modulate etoposide cytotoxicity and DNA strand scission in myeloma (8226) and leukemia (L1210) cell lines |
| [3141118](https://pubmed.ncbi.nlm.nih.gov/3141118/) | 1988 | Cohort (biomarker) | Chemotherapy | Polyamine levels increase in blood/marrow mononuclear cells of leukemia/myeloma patients treated with MGBG despite DFMO co-administration |
| [3139580](https://pubmed.ncbi.nlm.nih.gov/3139580/) | 1988 | Cohort (biomarker) | Investigational New Drugs | IV DFMO alters circulating and marrow polyamine levels in refractory leukemia/myeloma patients (9 patients) |
| [1898373](https://pubmed.ncbi.nlm.nih.gov/1898373/) | 1991 | In vitro/Mechanistic | Biochem J | Quantifies ODC gene dosage and mRNA in DFMO-resistant human myeloma cells |
| [2501085](https://pubmed.ncbi.nlm.nih.gov/2501085/) | 1989 | In vitro/Mechanistic | EMBO J | DFMO-resistant mouse myeloma cells show ODC gene rearrangement with the immunoglobulin gamma-1 switch region |
| [3109382](https://pubmed.ncbi.nlm.nih.gov/3109382/) | 1987 | In vitro/Mechanistic | Biochem J | Human myeloma cells acquire DFMO resistance via ODC gene amplification (10-fold activity increase) |
| [3107550](https://pubmed.ncbi.nlm.nih.gov/3107550/) | 1987 | In vitro/Mechanistic | Biochem Biophys Res Commun | Human myeloma cells acquire DFMO resistance without ODC overproduction, via an alternative mechanism |

---

## Taiwan Market Information

Eflornithine is not marketed in Taiwan (0 authorizations on file). No TFDA license records are available in this evidence pack; TFDA package-insert warnings/contraindications remain an unresolved blocking data gap (see below).

---

## Safety Considerations

Please refer to the SmPC for safety information. No structured warnings, contraindications, or drug-interaction data were retrievable for eflornithine in this evidence pack (TFDA label lookup is flagged as a blocking data gap: DG001).

---

## Other Screened Candidates (Not Advanced)

Eight additional TxGNN-predicted indications (esotropia, neurotrophic keratopathy, congenital analbuminemia, hyperamylasemia, polyclonal hyperviscosity syndrome, blood group incompatibility, premalignant hematological system disease, congenital prothrombin deficiency) scored highly (98–99.9%) but returned **zero clinical trials and zero literature** on targeted search, and each rationale explicitly notes no known mechanistic link to ODC/polyamine biology. These remain at decision stage S0 (Hold) and are not pursued further.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both viable candidates (bovine trypanosomiasis, monoclonal gammopathy) are supported only by decades-old preclinical/mechanistic literature with no clinical trials — sufficient to frame a research question, but not to justify clinical development or a guardrailed pilot. The model's top-scored prediction (esotropia) has no evidentiary support and is assessed as a probable false positive.

**To proceed, the following is needed:**
- TFDA package-insert data (warnings, contraindications) — currently a blocking gap (DG001)
- DrugBank-sourced mechanism of action detail (DG002)
- Contemporary (post-1995) validation of the ODC/polyamine-myeloma link, ideally in patient-derived samples
- Assessment of regulatory pathway feasibility for bovine trypanosomiasis (veterinary use of a human-approved drug is a distinct approval track from clinical repurposing)
- Any available DDI/toxicity data, since the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

