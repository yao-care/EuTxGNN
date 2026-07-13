---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Larotrectinib
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

# Larotrectinib: From NTRK Fusion-Positive Solid Tumors to Multiple Endocrine Neoplasia

## One-Sentence Summary

Larotrectinib (Vitrakvi) is a first-in-class, highly selective TRK inhibitor approved by the FDA and EMA for the treatment of NTRK gene fusion-positive solid tumors across all tissue types in a tumor-agnostic manner.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, with **1 Phase 2 clinical trial** and **2 publications** currently supporting this direction.
This prediction rests on the rare co-occurrence of NTRK gene rearrangements within MEN-associated tumors; mechanistic alignment is indirect and requires prospective molecular subgroup confirmation before clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NTRK fusion-positive solid tumors (FDA/EMA approved; not marketed in Taiwan) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Larotrectinib is a potent and highly selective small molecule inhibitor of tropomyosin receptor kinases A, B, and C (TRKA/B/C), encoded by the NTRK1, NTRK2, and NTRK3 genes respectively. TRK fusions arise from chromosomal rearrangements that generate constitutively active oncoproteins driving uncontrolled cell proliferation. Larotrectinib binds the ATP pocket of TRK kinases and blocks downstream RAS/MAPK and PI3K/AKT signaling. Its tumor-agnostic approval means efficacy is defined by the molecular lesion — an in-frame NTRK fusion — rather than by tumor histotype.

Multiple Endocrine Neoplasia (MEN) is a group of inherited syndromes leading to tumors across multiple endocrine glands. MEN2A and MEN2B are classically driven by activating germline mutations in the RET proto-oncogene — a kinase that Larotrectinib does not directly target — which substantially limits mechanistic alignment for the broad MEN population. However, MEN-associated papillary thyroid carcinoma (PTC) and sporadic endocrine tumors occasionally harbor NTRK rearrangements (e.g., ETV6-NTRK3, TPR-NTRK1). In this rare molecular subgroup, Larotrectinib's tumor-agnostic mechanism is directly applicable.

The prediction is therefore biologically plausible only within a narrow NTRK fusion-positive subset of MEN-associated neoplasms. For the predominant RET-mutant MEN2 phenotype, there is no direct mechanistic rationale. Prospective next-generation sequencing of MEN tumor specimens to establish NTRK fusion prevalence is a prerequisite before this prediction can be acted upon clinically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | Active, Not Recruiting | 6,452 | NCI-MATCH large umbrella basket trial evaluating genetically directed therapies in patients with advanced refractory solid tumors, lymphomas, and myelomas. Arm Z1A specifically enrolls NTRK fusion-positive patients and could theoretically include MEN-associated tumors harboring NTRK rearrangements. However, MEN is not a designated histotype, the MEN-specific subgroup size is unknown, and no MEN-focused efficacy data have been reported from this trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | Comprehensive review of the kinase inhibitor landscape for advanced thyroid cancer — a core MEN-associated malignancy. Covers FDA-approved multikinase inhibitors (vandetanib, cabozantinib, sorafenib, lenvatinib) and mutation-specific approvals. Establishes the clinical context for molecularly targeted therapy in endocrine neoplasms, relevant to evaluating NTRK-directed treatment in MEN-associated PTC. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Basic Research / Mechanism Study | NPJ Precision Oncology | Characterizes adaptive resistance mechanisms to selective RET inhibitors (selpercatinib) in medullary thyroid carcinoma — the hallmark MEN2 tumor. A patient developed resistance via secondary activation of an alternative oncogene. This work highlights the potential clinical role of bypass kinase pathways in RET-driven tumors, providing mechanistic context for why NTRK pathway activation might emerge or co-exist in MEN tumor evolution. |

---

## Taiwan Market Information

Larotrectinib is currently **not marketed in Taiwan**. No TFDA marketing authorizations have been issued. Clinicians seeking access would need to apply through compassionate use or special import channels.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — highly selective TRK kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to Moderate — neutropenia, anemia, and thrombocytopenia observed in clinical trials, but generally less severe and less frequent than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (baseline and periodic), liver function tests (ALT/AST), neurological symptoms (dizziness, gait disturbance, paresthesia — on-target CNS TRK effects), weight and nutritional status |
| Handling Protection | Standard oral antineoplastic handling precautions apply; cytotoxic drug preparation area not required for oral targeted agents, but follow institutional guidelines for handling and disposal |

---

## Safety Considerations

Please refer to the SmPC for safety information. TFDA labeling warnings, contraindications, and drug-drug interaction data were not available in this Evidence Pack. Clinicians should note that as a CYP3A4 substrate, Larotrectinib has known interactions with strong CYP3A4 inhibitors and inducers per the international SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
MEN is predominantly a RET-driven syndrome, and Larotrectinib's primary target (NTRK) does not overlap with the core driver oncogene in MEN2. The single supporting clinical trial (NCI-MATCH) is a large basket study not designed to evaluate MEN as a histotype, and the two literature items provide only indirect contextual evidence from the broader thyroid cancer and RET-resistance biology space — neither directly demonstrates Larotrectinib efficacy in MEN. Until NTRK fusion prevalence in MEN-associated tumors is established, this prediction remains a scientific hypothesis without sufficient evidence to proceed.

**To proceed, the following is needed:**
- **Molecular epidemiology**: Determine the frequency of NTRK gene fusions in MEN1- and MEN2-associated tumors (papillary thyroid carcinoma, pheochromocytoma, pancreatic NETs) via comprehensive genomic profiling cohort studies
- **Mechanistic clarification**: Assess whether RET/TRK signaling cross-talk or bypass occurs in RET-inhibitor-resistant MEN tumors, which would strengthen the therapeutic rationale
- **NCI-MATCH subgroup analysis**: Obtain any published or unpublished MEN-related subgroup data from Arm Z1A of NCT02465060
- **Taiwan TFDA label retrieval**: Download and review the official prescribing information to complete the safety profile (DG001)
- **DrugBank MOA data**: Retrieve complete mechanism of action and pharmacokinetic data for DB14723 (DG002)
- **Regulatory pathway assessment**: If NTRK fusion rate in MEN tumors is found to be clinically meaningful, evaluate whether the existing tumor-agnostic approval pathway allows enrollment without a new indication filing in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

