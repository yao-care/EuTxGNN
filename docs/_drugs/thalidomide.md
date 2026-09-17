---
layout: default
title: Thalidomide
parent: High Evidence (L1-L2)
nav_order: 587
evidence_level: L2
indication_count: 10
---

# Thalidomide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Thalidomide: From Immunomodulatory/Anti-angiogenic Agent to Neuroblastoma

## One-Sentence Summary

Thalidomide's original approved indication is not on file in this evidence pack (Blocking data gap), though the included literature describes its history as a sedative later repurposed as an immunomodulatory/anti-angiogenic agent for multiple myeloma and erythema nodosum leprosum. Of the **10 candidate indications** screened by TxGNN for this drug, the best-supported one is **Neuroblastoma**, backed by **3 clinical trials** and **8 directly relevant publications** (xenograft, case-report, and mechanistic evidence for its anti-angiogenic activity). Most of the other predicted indications in this batch have little to no supporting evidence, and two are flagged as likely knowledge-graph false positives driven by thalidomide's well-known teratogenic signal rather than a genuine treatment relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — drug not currently EU-authorized; no original-indication record provided) |
| Predicted New Indication | Neuroblastoma |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L2 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from an authoritative source (e.g., DrugBank) is not available for this drug (High-severity data gap, DG002). Based on the literature collected in this evidence pack, thalidomide is described as an immunomodulatory drug (IMiD) with anti-angiogenic activity, acting through inhibition of bFGF/VEGF-driven neovascularization and, mechanistically, through binding to cereblon (CRBN), which modulates the CRL4–CRBN ubiquitin ligase complex and downstream transcription factors such as Ikaros.

For the neuroblastoma prediction specifically, the rationale is that thalidomide's anti-angiogenic mechanism (bFGF/VEGF inhibition) has been demonstrated effective in neuroblastoma xenograft models, and the cereblon (CRBN) pathway has separately been linked to N-myc suppression — a gene central to high-risk neuroblastoma biology. This gives the prediction a coherent mechanistic story beyond simple embedding similarity: anti-angiogenic therapy is a recognized strategy in pediatric solid tumors with limited treatment options, and neuroblastoma's known vascular dependence (higher microvessel density correlating with worse prognosis) provides a plausible biological bridge.

It is worth noting, however, that formal confirmation of thalidomide's original approved indication is missing from this pack. The historical association with multiple myeloma and erythema nodosum leprosum, referenced incidentally in several of the collected publications, should be treated as background context rather than a verified regulatory fact until DG001/DG002 are resolved.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357500](https://clinicaltrials.gov/study/NCT00357500) | Phase 2 | Completed | 101 | Oral 5-drug anti-angiogenic (metronomic) regimen — thalidomide, celecoxib, fenofibrate, etoposide, cyclophosphamide — in patients with relapsed or progressive cancer, including neuroblastoma; graded "A" relevance as a direct trial in this population. |
| [NCT00098865](https://clinicaltrials.gov/study/NCT00098865) | Phase 2 | Completed | 15 | Pilot study combining thalidomide with temozolomide in children with relapsed/progressive brain tumors or recurrent neuroblastoma, based on thalidomide's anti-angiogenic activity; graded "B" (population skews toward brain tumors). |
| [NCT00049296](https://clinicaltrials.gov/study/NCT00049296) | Phase 1 | Completed | 26 | Pharmacokinetic trial combining thalidomide with docetaxel in advanced cancer, based on anti-angiogenic therapeutic principles; small sample, PK-focused rather than efficacy-driven. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24123865](https://pubmed.ncbi.nlm.nih.gov/24123865/) | 2014 | Phase II trial (published results) | Pediatric Blood & Cancer | Published outcomes of the multi-agent oral antiangiogenic (metronomic) regimen in children with recurrent/progressive cancer, consistent with NCT00357500. |
| [18024879](https://pubmed.ncbi.nlm.nih.gov/18024879/) | 2007 | Case report | J Clin Oncol | "Successful antiangiogenic therapy for neuroblastoma with thalidomide" — a direct positive clinical case. |
| [14612937](https://pubmed.ncbi.nlm.nih.gov/14612937/) | 2003 | Preclinical (xenograft) | International Journal of Oncology | Thalidomide shown anti-angiogenic in a neuroblastoma xenograft model, foundational preclinical rationale. |
| [29423589](https://pubmed.ncbi.nlm.nih.gov/29423589/) | 2018 | Preclinical | Pediatric Surgery International | Thalidomide potentiates etoposide-induced apoptosis in murine neuroblastoma via suppression of NF-κB activation. |
| [15707702](https://pubmed.ncbi.nlm.nih.gov/15707702/) | 2005 | Review (mechanistic) | Cancer Treatment Reviews | Reviews antiangiogenic strategies in neuroblastoma, noting high vascular index correlates with poor prognosis. |
| [23982484](https://pubmed.ncbi.nlm.nih.gov/23982484/) | 2013 | Preclinical/mechanistic | Cancer Immunology, Immunotherapy | Lenalidomide (thalidomide analogue) overcomes NK-cell suppression caused by neuroblastoma microenvironment cytokines (IL-6, TGFβ1). |
| [27329811](https://pubmed.ncbi.nlm.nih.gov/27329811/) | 2016 | Mechanistic | Biochemical and Biophysical Research Communications | Nuclear cereblon (CRBN) modulates Ikaros transcriptional activity in human neuroblastoma cells — direct mechanistic support for the CRBN pathway rationale. |
| [36549117](https://pubmed.ncbi.nlm.nih.gov/36549117/) | 2023 | Preclinical (drug design) | European Journal of Medicinal Chemistry | Structure-activity study using a thalidomide-derived PROTAC to degrade AURKA in neuroblastoma, leveraging the same CRBN-binding moiety. |

---

## Other Predicted Indications Screened

TxGNN generated 10 candidate indications for this drug. For context on the overall repurposing screen, the remaining 9 are summarized below (Neuroblastoma, the primary candidate above, is rank 4):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 1 | Ganglioneuroblastoma | 98.96% | L5 | Hold | No clinical trials or literature; theoretical neural-crest-tumor analogy only, based purely on knowledge-graph embedding similarity. |
| 2 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 98.95% | L5 | Hold | No identifiable pharmacological rationale and no evidence; recommend manual review of the underlying KG node semantics. |
| 3 | Retroperitoneal neoplasm | 98.68% | L4 | Hold | Evidence limited to unrelated case reports (Castleman disease, histiocytic sarcoma) and one irrelevant apixaban VTE-prophylaxis trial. |
| 5 | Brachydactyly-syndactyly syndrome | 94.22% | L5 | Hold | ⚠️ Likely KG false positive — matches thalidomide's well-known teratogenic limb-malformation signal (phocomelia), not a treatment relationship. |
| 6 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 93.20% | L5 | Hold | ⚠️ Likely KG false positive — phenotype overlaps with thalidomide embryopathy (rhizomelic limb shortening), not a treatment relationship. |
| 7 | Rheumatoid arthritis | 92.40% | L3 | Research Question | Mechanistic rationale (TNF-α inhibition, anti-angiogenesis) is present, but direct clinical evidence is limited to small open-label studies from the 1980s–1990s; most listed trials target other diseases (Sjögren's, sarcoidosis). |
| 8 | Myeloid leukemia | 90.54% | Not yet graded | Pending | Substantial literature on IMiDs/thalidomide in AML and MDS (anti-angiogenesis, cereblon pathway) plus several completed Phase 2 trials in MDS-related anemia; worth prioritizing for full evidence grading. |
| 9 | Indolent plasma cell myeloma | 88.46% | Not yet graded | Pending | One completed Phase 2 trial (UARK 98-036, n=83) plus a substantial published series on thalidomide in smoldering/indolent myeloma; appears to have a richer evidence base than its current "pending" status reflects — worth prioritizing. |
| 10 | Acute lymphoblastic leukemia | 74.75% | L4 | Hold | Most cited trials/literature involve lenalidomide (a thalidomide analogue) rather than thalidomide itself; some literature reports thalidomide-*associated* secondary leukemia, i.e., an adverse outcome, not a therapeutic benefit. |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) from the official regulatory label were not available in this evidence pack. This is logged as a **Blocking** data gap (DG001) that must be resolved before this candidate can pass S1 safety pre-screening.

Please refer to the SmPC for complete safety information once retrieved.

Separately, it is worth noting that thalidomide's well-documented teratogenic risk (limb malformations) appears to actively confound the TxGNN predictions themselves: two of the ten candidate indications in this batch (Brachydactyly-syndactyly syndrome; Colobomatous microphthalmia-rhizomelic dysplasia syndrome, see table above) closely mirror the phenotype of thalidomide embryopathy and are very likely knowledge-graph artifacts derived from the drug's known adverse-effect associations rather than genuine treatment signals. Given thalidomide's history, a pregnancy-risk-management/controlled-distribution requirement should be treated as a default assumption pending confirmation from the official SmPC.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the Neuroblastoma candidate)

**Rationale:**
- Neuroblastoma is supported by 2 completed Phase 2 trials, 1 completed Phase 1 PK trial, and a coherent body of preclinical (xenograft, murine) and mechanistic (CRBN/N-myc, anti-angiogenic) literature, consistent with an L2 evidence level.
- Drug-level safety documentation is a Blocking data gap, and thalidomide's known teratogenicity requires dedicated risk-management review before any development pathway is pursued — hence "Guardrails" rather than an unconditional "Go."

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve official TFDA/EMA SmPC warnings and contraindications.
- Resolve DG002 (High): retrieve DrugBank/authoritative MOA data to confirm the anti-angiogenic/CRBN mechanistic rationale.
- Confirm publication status and efficacy outcomes for the neuroblastoma subgroups of NCT00357500 and NCT00098865.
- Define a pregnancy-prevention / controlled-distribution risk management plan given thalidomide's teratogenic history.
- Manually review and most likely exclude the two KG-flagged false-positive indications (brachydactyly-syndactyly syndrome; colobomatous microphthalmia-rhizomelic dysplasia syndrome) from further pipeline consideration.
- Consider prioritizing "Indolent plasma cell myeloma" and "Myeloid leukemia" for full evidence grading, as their underlying literature base appears richer than their current "pending" scoring status suggests.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

