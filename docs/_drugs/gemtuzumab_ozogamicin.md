---
layout: default
title: Gemtuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Gemtuzumab Ozogamicin
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

# Gemtuzumab Ozogamicin: From CD33+ Acute Myeloid Leukemia to Alkylating-Agent-Related AML/MDS

## One-Sentence Summary

Gemtuzumab ozogamicin (Mylotarg) is an anti-CD33 antibody-drug conjugate originally developed for CD33-positive acute myeloid leukemia (AML). Across the 10 candidate indications screened by TxGNN, the most clinically actionable signal is **alkylating-agent-related (therapy-related) AML/MDS**, essentially a same-biology extension of its existing target population, while a biologically plausible but less mature signal also emerged for **myeloid blast-phase CML**. The drug's single highest TxGNN score (Richter syndrome, 98.06%) is explicitly flagged in the evidence pack itself as unsupported model noise with zero trial or literature backing, so it is not carried forward as the lead candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CD33-positive Acute Myeloid Leukemia (per literature references in this evidence pack; no formal Taiwan/EU marketing authorization on file for this product) |
| Predicted New Indication | Acute Myeloid Leukemia / Myelodysplastic Syndrome related to alkylating agents (therapy-related AML/MDS) |
| TxGNN Prediction Score | 93.86% (rank 10 of 10 candidates reviewed; most clinically credible signal, not the top statistical score) |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Why not the top-scored prediction?** TxGNN's highest-ranked candidate, Richter syndrome (98.06%), has zero supporting clinical trials or literature, and the evidence pack's own mechanistic review labels it likely knowledge-graph noise (Richter syndrome tumors are typically CD19/CD20-driven, not CD33). The same applies to bulbar polio, malignant spiradenoma, 5q35 microduplication syndrome, and neuralgic amyotrophy — see "Other Predictions Reviewed" below.

---

## Why is This Prediction Reasonable?

The source record marks the drug's mechanism of action as a data gap, but the literature captured in this evidence pack consistently and repeatedly describes gemtuzumab ozogamicin as a humanized anti-CD33 monoclonal antibody conjugated to the cytotoxic agent calicheamicin (PMID 15454492, 21993666, 11466696) — approved as Mylotarg for CD33-positive AML, where the antibody delivers the calicheamicin payload directly to CD33-expressing leukemic blasts.

Alkylating-agent-related (therapy-related) AML/MDS shares the identical cell-surface biology as de novo CD33+ AML — it is the same disease category arising after prior cytotoxic/alkylating chemotherapy exposure, not a new mechanistic hypothesis. This is why it reaches the most advanced internal decision stage (S2, "Proceed with Guardrails") in the evidence pack despite having only a single supporting review article and no dedicated trials: the therapeutic rationale is a population extension of the existing label, not novel pharmacology.

A second, less mature signal exists for myeloid blast-phase chronic myeloid leukemia (CML, BCR-ABL1 positive). CML in chronic phase does not typically express CD33, but cohort and mechanistic studies in this pack (PMID 21993666, 22534616) show that CD33 (Siglec-3) becomes expressed on leukemic stem cells once CML progresses to myeloid blast phase, and combination regimens containing gemtuzumab ozogamicin have shown activity in that setting. This is biologically plausible but remains at an earlier evaluation stage (S1, "Research Question") because no trial has tested gemtuzumab ozogamicin as a defined intervention specifically in CML blast phase — the supporting trials mostly enrolled mixed AML/CML/MDS populations.

---

## Clinical Trial Evidence

*No dedicated trials are registered for alkylating-agent-related AML/MDS specifically; supporting evidence for this population is derived from the drug's existing CD33+ AML trial base and the review article below.*

**Related signal — Myeloid blast-phase CML (BCR-ABL1 positive):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038831](https://clinicaltrials.gov/study/NCT00038831) | Phase 1/2 | Completed | 47 | Mylotarg + melphalan/fludarabine as reduced-intensity conditioning before allogeneic transplant in high-risk AML/CML/MDS; mixed population, not CML-specific endpoint |
| [NCT00038805](https://clinicaltrials.gov/study/NCT00038805) | Phase 2/3 | Terminated (n=3) | 3 | Mylotarg + nonmyeloablative chemo before allogeneic transplant in high-risk ALL/CML/MDS; terminated with minimal enrollment, weak evidentiary weight |
| [NCT03589729](https://clinicaltrials.gov/study/NCT03589729) | Phase 2 | Recruiting | 100 | Evaluates dexrazoxane cardioprotection in regimens containing gemtuzumab ozogamicin for AML/MDS/CML myeloid blast phase; not a GO-efficacy trial |

---

## Literature Evidence

**Related signal — Myeloid blast-phase CML (BCR-ABL1 positive):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35536916](https://pubmed.ncbi.nlm.nih.gov/35536916/) | 2022 | Review | Expert Rev Hematol | Systematic review of CML myeloid blast phase (CML-MBP) management, noting its clinical/histological overlap with AML and shared treatment approaches |
| [17353625](https://pubmed.ncbi.nlm.nih.gov/17353625/) | 2007 | Review | Gan to Kagaku Ryoho | Review of hematological malignancy therapy in older adults; describes gemtuzumab ozogamicin as a CD33-targeting immunoconjugate for AML |
| [15487459](https://pubmed.ncbi.nlm.nih.gov/15487459/) | 2004 | Review | Am J Clin Pathol | Overview of targeted cancer therapies, including BCR-ABL-directed and antibody-based approaches in CML and other malignancies |
| [21993666](https://pubmed.ncbi.nlm.nih.gov/21993666/) | 2012 | Cohort/preclinical | Haematologica | CD34+/CD38- CML leukemic stem cells express CD33 (Siglec-3) and respond to gemtuzumab ozogamicin in vitro — direct mechanistic support |
| [22534616](https://pubmed.ncbi.nlm.nih.gov/22534616/) | 2012 | Cohort | Clin Lymphoma Myeloma Leuk | Fludarabine/cytarabine ± gemtuzumab ozogamicin in relapsed/refractory AML, high-risk MDS, and CML myeloid blast phase (n=107); 21% CR |
| [15454492](https://pubmed.ncbi.nlm.nih.gov/15454492/) | 2005 | Cohort/mechanistic | Blood | CD33 expression level determines gemtuzumab ozogamicin cytotoxicity — mechanistic basis for target-dependent activity |
| [15886328](https://pubmed.ncbi.nlm.nih.gov/15886328/) | 2005 | Cohort | Blood | Safety/efficacy of single-agent gemtuzumab ozogamicin in pediatric CD33+ AML |
| [34764108](https://pubmed.ncbi.nlm.nih.gov/34764108/) | 2021 | Case series | BMJ Case Rep | Gemtuzumab ozogamicin + blinatumomab used in refractory mixed-phenotype blast crisis of CML |
| [11895761](https://pubmed.ncbi.nlm.nih.gov/11895761/) | 2002 | Case report | Blood | Hepatic sinusoidal obstruction (veno-occlusive disease) following gemtuzumab ozogamicin therapy — key hepatotoxicity signal |
| [25721896](https://pubmed.ncbi.nlm.nih.gov/25721896/) | 2015 | Preclinical | Leukemia | CD33-directed CAR-T cells show potent preclinical activity against AML, corroborating CD33 as a valid myeloid target |

**Related signal — Alkylating-agent-related AML/MDS:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18565291](https://pubmed.ncbi.nlm.nih.gov/18565291/) | 2008 | Review | Ugeskrift for Laeger | Reviews monoclonal antibodies integrated into hematology practice, including anti-CD33 gemtuzumab ozogamicin for AML |

---

## EU Market Information

Not currently marketed in this jurisdiction — 0 marketing authorizations on file, market status recorded as "Not marketed." No licensed product, dosage form, or approved indication text is available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-CD33 antibody linked to the cytotoxic agent calicheamicin) |
| Myelosuppression Risk | High — intrinsic to its cytotoxic payload and hematologic target population; literature in this pack also documents hepatic veno-occlusive disease/sinusoidal obstruction as a major associated toxicity (PMID 11895761) |
| Emetogenicity Classification | Low to Moderate (consistent with antibody-drug conjugate class) |
| Monitoring Items | CBC with differential, liver function tests (bilirubin, transaminases — VOD/SOS risk), renal function, infusion-related reaction monitoring |
| Handling Protection | Cytotoxic drug handling precautions required due to the calicheamicin payload |

---

## Safety Considerations

Please refer to the SmPC for safety information — key warnings, contraindications, and drug interaction data are not available in the source record for this product (DG001, Blocking severity: TFDA/label warnings and contraindications missing).

Note: literature in this evidence pack independently documents hepatic sinusoidal obstruction/veno-occlusive disease as an associated risk (PMID 11895761), which should be factored into any future formal safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The case carries a Blocking-severity data gap — no TFDA/SmPC warning or contraindication data is available (DG001), and the product has no marketing authorization in this jurisdiction — so a formal S1 safety review cannot yet proceed regardless of indication-level evidence. Among the indication candidates, alkylating-agent-related AML/MDS is the most defensible (label-adjacent population, internally staged S2/"Proceed with Guardrails"), and myeloid blast-phase CML is a credible secondary research question (S1), but neither can advance past Hold until the case-level safety gate is cleared.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, contraindications, and drug interaction data (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank or the manufacturer's label (DG002, High)
- A dedicated trial or registry analysis of gemtuzumab ozogamicin specifically in therapy-related AML/MDS and in CML myeloid blast phase, since current supporting trials enrolled mixed populations
- Re-validation of the disease-ontology mapping for "metastatic neoplasm" and the other zero-evidence, high-score predictions (Richter syndrome, bulbar polio, malignant spiradenoma, 5q35 microduplication syndrome, neuralgic amyotrophy/amyotrophic neuralgia), which should not be pursued further without new evidence

---

### Appendix: Other Predictions Reviewed and Not Pursued

| Disease | TxGNN Score | Evidence | Reason Not Pursued |
|---------|------------|----------|---------------------|
| Richter syndrome | 98.06% | None | CD19/CD20-driven B-cell lymphoma; no CD33 biology; likely knowledge-graph noise |
| Bulbar polio | 97.92% | None | Viral neurological disease; no biological link to a CD33-targeted ADC |
| Metastatic neoplasm | 97.26% | 29 trials / 2 papers (all CD33+ AML-specific) | Disease label too broad; underlying evidence is CD33+ AML trials mismatched to this generic tag |
| Malignant spiradenoma | 97.23% | None | Rare sweat-gland tumor with no reported CD33 expression |
| 5q35 microduplication syndrome | 97.16% | None | Congenital chromosomal disorder, non-neoplastic; no mechanistic link |
| Neuralgic amyotrophy / amyotrophic neuralgia | 95.74% / 95.40% | None | Peripheral immune-inflammatory neuropathy (duplicate synonym entries); unrelated to CD33 |
| Acute lymphoblastic/lymphocytic leukemia | 95.09% | 3 trials (grade C, not GO-specific) | CD33 expression limited to rare mixed-phenotype/CD33-co-expressing ALL subsets; most ALL is CD33-negative |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

