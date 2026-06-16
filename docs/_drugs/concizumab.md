---
layout: default
title: Concizumab
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Concizumab
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

# Concizumab: From Hemophilia to Diabetic Cataract

## One-Sentence Summary

Concizumab is an anti-TFPI (Tissue Factor Pathway Inhibitor) monoclonal antibody under clinical development as a pro-coagulant agent, primarily targeting hemophilia and bleeding disorders.
The TxGNN model ranks **Diabetic Cataract** as its top repurposing prediction (score: 98.27%),
but there are currently **0 clinical trials** and **0 publications** supporting this direction — and the mechanistic rationale is critically weak, with strong indications that the prediction reflects a Knowledge Graph clustering artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Investigational — Hemophilia / Bleeding disorders (inferred from anti-TFPI pro-coagulant mechanism referenced in repurposing rationale) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.27% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on the contextual information embedded within the repurposing rationale, Concizumab is an anti-TFPI monoclonal antibody that promotes coagulation by blocking Tissue Factor Pathway Inhibitor (TFPI), thereby restoring hemostasis. Its clinical development is directed toward hereditary bleeding disorders, particularly hemophilia A and B with inhibitors.

Diabetic cataract arises from lens-specific metabolic injury: sorbitol accumulation via the polyol pathway, advanced glycation end-products (AGEs), and oxidative protein damage to lens crystallins. These pathways operate entirely within lens epithelial cell biology and have **no established mechanistic connection** to TFPI inhibition or the extrinsic coagulation cascade. While diabetes does involve coagulation dysregulation systemically, cataract formation itself is not driven by procoagulant or anticoagulant mechanisms, and lens opacity cannot be reversed by modulating hemostasis.

The high TxGNN score almost certainly reflects a **Knowledge Graph disease-ontology clustering artifact**: 9 of the top 10 predictions are cataract subtypes (diabetic, craniostenosis, immature, tetanic, T2DM-associated, mature, cortical, nuclear senile, and senile), with near-identical scores concentrated in the 0.981–0.983 range. This uniform score distribution across morphologically and etiologically distinct cataract subtypes is a hallmark of ICD-10 ontology node co-clustering in the KG, rather than a true pharmacological signal. These predictions should be collectively treated as false positives for this candidate.

> ⚠️ **Critical Safety Alert — Rank #9 Prediction (Antithrombin Deficiency Type 2):** The 9th-ranked prediction is a thrombophilic condition, not a repurposing target. Antithrombin Deficiency Type 2 is characterized by reduced natural anticoagulant activity and markedly elevated venous thromboembolism risk. Applying a **pro-coagulant** drug like Concizumab in this population would further potentiate thrombotic risk. The KG model appears to have interpreted co-occurrence of coagulation-pathway nodes as positive association; clinically, the relationship is **antagonistic and potentially dangerous**. This indication must be explicitly excluded and flagged as a contraindication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Concizumab across any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for Concizumab across any of the 10 predicted indications.

---

## Taiwan Market Information

Concizumab currently holds **0 marketing authorizations** in Taiwan and is **not marketed**. It remains an investigational product. No approved indication text, dosage form, or product registration data is available.

---

## Safety Considerations

Please refer to the investigational drug brochure (IB) or SmPC for safety information. No key warnings, contraindications, or drug interaction data were retrievable for this candidate at the time of this report.

> **Evaluator Note:** The absence of safety data (DG001: Blocking severity) prevents entry into standard S1 safety screening. Before any repurposing evaluation can proceed, the TFDA package insert or IB must be obtained and parsed for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top TxGNN predictions carry zero clinical or literature support (Evidence Level L5), the dominant cataract cluster is mechanistically inconsistent with Concizumab's pro-coagulant biology, and the tight score clustering across cataract subtypes confirms a KG disease-ontology artifact rather than a repurposing opportunity. One prediction (Antithrombin Deficiency Type 2, rank #9) represents an active safety concern and must be excluded from further consideration.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain TFDA package insert or IB to extract key warnings and contraindications — required before S1 safety screening can commence
- **Resolve DG002 (High):** Query DrugBank API for confirmed MOA data to enable mechanistic plausibility analysis for future candidate indications
- **Explicitly exclude rank #9:** Formally flag Antithrombin Deficiency Type 2 as a potential contraindication in the candidate screening record
- **Suppress KG cataract cluster:** Consider applying disease-ontology deduplication or cluster-aware filtering in the TxGNN pipeline to prevent similar false-positive groupings in future runs
- **Identify alternative repurposing directions:** Re-evaluate candidates outside the cataract cluster — mechanistically plausible targets for an anti-TFPI agent would include other thrombotic/hemorrhagic conditions, vascular thromboembolism phenotypes, or disseminated intravascular coagulation (DIC) where TFPI modulation has biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

