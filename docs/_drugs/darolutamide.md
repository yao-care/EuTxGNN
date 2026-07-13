---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is a next-generation androgen receptor (AR) antagonist approved in multiple countries for the treatment of prostate cancer (nmCRPC and mHSPC), though it is not yet registered in Taiwan.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **no clinical trials** and **no publications** currently supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate Cancer (not registered in Taiwan) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Darolutamide is a selective androgen receptor (AR) antagonist with a distinctive diarylthiohydantoin structure that confers low CNS penetration, minimal off-target hormonal activity, and a favorable drug–drug interaction profile compared to earlier-generation anti-androgens. It is approved for non-metastatic castration-resistant prostate cancer (nmCRPC) and metastatic hormone-sensitive prostate cancer (mHSPC) in combination with androgen deprivation therapy (ADT).

The proposed link between AR antagonism and HoFH draws on the observation that androgen signaling participates in hepatic LDL receptor (LDLR) expression and whole-body cholesterol metabolism. Androgen deprivation therapy is already known to alter lipid profiles — typically elevating LDL and lowering HDL — confirming that AR signaling does interact with cholesterol homeostasis pathways. Theoretically, modulating AR activity could influence hepatic lipid handling.

However, Homozygous Familial Hypercholesterolemia is caused by biallelic loss-of-function mutations in the *LDLR* gene, resulting in near-absent LDLR protein activity. AR antagonism has no known mechanism to rescue mutant LDLR function, upregulate alternative LDL clearance pathways, or compensate for LDLR deficiency. No preclinical data (in vitro or in vivo) demonstrates that darolutamide reduces LDL in LDLR-deficient models. The high TxGNN score (99.11%) most likely reflects an indirect mathematical connection through shared lipid metabolism nodes in the knowledge graph, rather than a genuine biological signal. **This prediction should be treated as a potential graph artifact rather than a clinically actionable hypothesis.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Darolutamide is approved for prostate cancer and is classified as an antineoplastic targeted therapy. It is **not** a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Non-steroidal androgen receptor antagonist (2nd-generation, diarylthiohydantoin class) |
| Myelosuppression Risk | Low (myelosuppression is not a primary mechanism-related toxicity of AR antagonists; not expected in standard use) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT/AST), cardiovascular status and blood pressure, fatigue/fall risk assessment in elderly patients |
| Handling Protection | Standard antineoplastic handling precautions recommended per institutional cytotoxic drug policy |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN model output (L5 evidence) with no supporting clinical trials or published literature for the HoFH indication. The biological rationale is mechanistically unsound — HoFH is a monogenic disease driven by LDLR loss-of-function, a target that AR antagonism cannot address — making this prediction very likely a knowledge graph artifact rather than a clinically actionable signal. Of note, 4 of the top 10 TxGNN predictions for darolutamide are veterinary or animal diseases (SIV, FIV, IBR, malignant catarrh), further suggesting this prediction run may reflect systematic graph-level noise rather than drug-specific biological insight.

**To proceed, the following is needed:**
- Obtain detailed MOA and pharmacology data from DrugBank (Data Gap DG002) to anchor any mechanistic hypothesis
- Obtain SmPC / prescribing information to complete the safety profile and identify key warnings and contraindications (Data Gap DG001)
- Consult a lipid metabolism specialist to independently assess whether any AR–LDLR mechanistic link could support hypothesis generation
- If interest persists, commission targeted in vitro studies using LDLR-deficient hepatocyte models (e.g., HepG2-LDLR-KO) before any clinical translation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

