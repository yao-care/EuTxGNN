---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is an oral multi-kinase inhibitor targeting VEGFR2, MET, AXL, and RET, internationally established for the treatment of advanced renal cell carcinoma and other solid tumors, though not recorded in the local regulatory database.
The TxGNN model predicts it may be effective for **Liposarcoma** as its highest-ranked new repurposing candidate,
with **1 clinical trial** and **1 publication** currently providing direct sarcoma-domain evidence; separately, the drug carries **extensive Phase 3 support** (L1) across renal carcinoma subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in local regulatory database |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| EU Market Status | Not marketed (local registry) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not captured in the local regulatory database. Based on known pharmacological information, cabozantinib is a small-molecule tyrosine kinase inhibitor that simultaneously blocks VEGFR2 (anti-angiogenic), MET (tumour growth and invasion), AXL (immune evasion and EMT), and RET. This multi-target profile distinguishes it from single-pathway VEGFR inhibitors and underpins its clinical superiority in several renal cancer trials (METEOR, CheckMate 9ER, CABOSUN).

Liposarcoma—particularly the MDM2-amplified well-differentiated and dedifferentiated subtypes—is known to overexpress VEGFR2 and demonstrate MET pathway hyperactivation. These molecular features are directly targetable by cabozantinib's VEGFR2/MET dual inhibition, providing a mechanistically coherent basis for the TxGNN prediction. Additionally, AXL overexpression in dedifferentiated liposarcoma contributes to epithelial-mesenchymal transition (EMT) and resistance to conventional chemotherapy (doxorubicin/ifosfamide); cabozantinib's AXL inhibitory component may help reverse this resistance mechanism and sensitise tumours to treatment.

The biological overlap between liposarcoma's known molecular drivers (VEGF/MET/AXL axes) and cabozantinib's established kinase targets makes this prediction scientifically plausible. The ongoing Phase 2 trial combining cabozantinib with immune checkpoint inhibitors in soft tissue sarcoma further reflects real-world investigator recognition of this rationale, even though dedicated liposarcoma-specific Phase 3 data remain absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomised trial comparing cabozantinib + ipilimumab + nivolumab versus ipilimumab + nivolumab alone in advanced soft tissue sarcoma (including liposarcoma subgroup); assesses whether adding cabozantinib to dual checkpoint blockade improves outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Trial | American Journal of Clinical Oncology | Phase 1 study of neoadjuvant cabozantinib combined with radiation therapy in extremity soft tissue sarcomas; demonstrated the safety profile of concurrent use, addressing prior concerns about fistula or visceral perforation risk |

---

## EU Market Information

No authorizations are recorded for cabozantinib in the local regulatory database. This likely reflects a data pipeline gap rather than an absence of international approvals; clinicians should consult the EMA SmPC for Cabometyx® (cabozantinib) for full prescribing information.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-kinase inhibitor (VEGFR2, MET, AXL, RET); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate (less myelosuppressive than cytotoxic chemotherapy; thrombocytopenia and neutropenia reported; Grade 3–4 haematological events less common than with platinum or taxane regimens) |
| Emetogenicity Classification | Low (oral administration; nausea is common but typically Grade 1–2; no routine prophylactic antiemetic required per low-emetogenicity guidelines) |
| Monitoring Items | Complete blood count (CBC), liver function (ALT/AST/bilirubin), renal function (creatinine, urea), blood pressure (hypertension is a class effect), thyroid function, wound healing assessment, urine protein |
| Handling Protection | Standard oral antineoplastic precautions apply; cytotoxic handling guidelines (PPE, dedicated dispensing) are recommended per institutional policy |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cabozantinib's mechanistic profile (VEGFR2/MET/AXL inhibition) aligns with known molecular drivers of liposarcoma, and the TxGNN model assigns a near-maximal prediction score of 99.83%. However, existing evidence is currently limited to one Phase 2 trial enrolling a broad soft tissue sarcoma population (with liposarcoma as a subgroup) and a single Phase 1 safety study—placing the liposarcoma indication firmly at L3. This is insufficient for a direct clinical recommendation but justifies a structured research programme.

Separately, the data pack reveals that cabozantinib has **L1-level evidence for renal carcinoma** (multiple completed Phase 3 trials: METEOR, CheckMate 9ER, COSMIC-313), representing its most evidence-rich pathway and the likely basis for its international regulatory approvals.

**To proceed toward a liposarcoma indication, the following is needed:**

- A dedicated Phase 1b/2 basket or expansion cohort trial in liposarcoma (particularly MDM2-amplified subtypes) evaluating cabozantinib monotherapy or combination with immune checkpoint inhibitors
- Biomarker profiling of target patient population to confirm VEGFR2, MET, and AXL expression levels in liposarcoma tissue
- Subgroup analysis from NCT05836571 (once results are available in 2026) to extract liposarcoma-specific response data
- Full mechanism of action documentation and local regulatory submission to populate the safety database
- Review of the EMA SmPC for Cabometyx® to complete the contraindication and DDI profiling currently listed as data gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

