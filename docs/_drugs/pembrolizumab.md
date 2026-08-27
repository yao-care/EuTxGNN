---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: From Advanced Malignancies to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor monoclonal antibody used across multiple advanced malignancies (e.g., non-small-cell lung cancer, melanoma — confirmed only indirectly through literature retrieved for other candidates in this evidence pack, since structured original-indication and MOA fields are currently blank). The TxGNN model's top-ranked prediction (rank 1 of 10 returned) proposes potential relevance to **Gingival Fibromatosis**, a benign fibrous gum-tissue overgrowth condition, but this pairing is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment explicitly concludes there is no known biological link between this condition and the PD-1/PD-L1 pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a structured field in this evidence pack (`drug.original_indications` is empty; drug is unmarketed in the EU per `taiwan_regulatory`). Supporting literature retrieved for other candidates confirms established use in advanced NSCLC, melanoma, HNSCC, HCC, and MSI-H/dMMR colorectal cancer. |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pembrolizumab is not available in this evidence pack — this is flagged as a High-severity data gap (DG002), with remediation planned via a DrugBank API query. Based on literature returned elsewhere in this pack (e.g., PMID 27398650 "Pembrolizumab (Keytruda)"; PMID 26558876 "CTLA-4 and PD-1 Pathways"), pembrolizumab is known to act as a humanized IgG4 monoclonal antibody that blocks the PD-1/PD-L1 interaction, restoring T-cell–mediated anti-tumor immune activity in immunogenic, checkpoint-driven malignancies.

Gingival fibromatosis, however, is a benign, non-neoplastic fibrous connective-tissue overgrowth of the gums. It has no established tumor immune-evasion biology, no reported PD-L1 expression pattern, and no T-cell exhaustion phenotype — the biological axis pembrolizumab is designed to act on. The evidence pack's own `repurposing_rationale` for this candidate states plainly that there is "no known association with the PD-1/PD-L1 immune checkpoint pathway" and "no reasonable mechanism to explain efficacy." The high TxGNN score (99.40%) most likely reflects knowledge-graph embedding proximity rather than a biologically grounded pathway.

It is also worth noting that this evidence pack contains other candidates with markedly stronger support than the top-ranked one: "lung hilum carcinoma" (rank 4) and "lung germ cell tumor" (rank 8) both reach **L4 / Research Question** status, with mechanistically plausible links to pembrolizumab's known anti-tumor immunotherapy activity, even though the retrieved trials/literature for those two are still largely indirect (safety/adverse-event reports and broad "advanced solid tumor" basket trials rather than disease-specific efficacy data). This top-ranked candidate (Gingival Fibromatosis) is comparatively the weakest of the ten predictions returned, both mechanistically and evidentially.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Pembrolizumab currently has no EU marketing authorization on file in this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available to list.

---

## Cytotoxicity

*(Included because pembrolizumab is an antineoplastic agent — an immune checkpoint inhibitor used in cancer treatment, as evidenced by the oncology-focused literature retrieved for other candidates in this same evidence pack, e.g., PMID 27398650, PMID 26712084.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 immune checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors are not classically myelosuppressive; class safety literature in this pack focuses on immune-related adverse events rather than bone marrow toxicity (PMID 26874776, "Management of toxicities of immune checkpoint inhibitors") |
| Emetogenicity Classification | Low — immunotherapy agents are generally low-emetogenic compared with cytotoxic chemotherapy |
| Monitoring Items | Immune-related adverse event (irAE) surveillance: thyroid function, liver function, pulmonary/colitis symptoms, skin reactions, and neurologic/endocrine monitoring (PMID 32126176, "Neurologic complications of immune checkpoint inhibitors"; PMID 26874776). No structured haematological, hepatic, or renal monitoring protocol is available in the current evidence pack. |
| Handling Protection | Standard IV biologic/monoclonal antibody handling precautions apply; pembrolizumab is not classified as a hazardous cytotoxic drug requiring special cytotoxic-handling protocols (unlike conventional chemotherapy agents) |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` are marked as data gaps in the evidence pack, and no drug-drug interaction records were found — `query_status: not_found`. This gap is flagged as Blocking (DG001) for progressing to S1 safety evaluation; remediation requires downloading and parsing the TFDA product label.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Gingival Fibromatosis) has no clinical trial or literature support, and the evidence pack's own mechanistic analysis finds no plausible biological link to pembrolizumab's PD-1/PD-L1 mechanism of action. Combined with the drug's unmarketed status in the EU and a Blocking-severity gap in safety/label data, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action data via DrugBank API query (per DG002)
- TFDA/EMA label warnings, contraindications, and drug interaction data (per DG001, Blocking priority — required before any S1 safety evaluation)
- Independent mechanistic or preclinical rationale connecting PD-1/PD-L1 biology to gingival fibromatosis before any further evaluation of this specific candidate
- Consider redirecting evaluation effort toward the pack's higher-evidence candidates — "lung hilum carcinoma" (rank 4) and "lung germ cell tumor" (rank 8), both already at L4 / Research Question status — which show markedly stronger (if still indirect) mechanistic and literature support than the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

