---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Alpelisib
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

# Alpelisib: From HR+/HER2- Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray) is a selective PI3Kα inhibitor approved in multiple international markets (EU, US) for hormone receptor-positive (HR+), HER2-negative advanced breast cancer carrying a PIK3CA mutation, in combination with fulvestrant; it has not received marketing authorization in Taiwan.
The TxGNN model predicts it may have activity in **Pulmonary Hypertension**, with **1 clinical trial** and **2 publications** identified — however, neither provides direct supportive evidence for this indication.
Critically, one of the identified publications reports alpelisib-induced interstitial lung disease (ILD) as an adverse event, constituting a significant safety signal that actively weighs against this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- advanced breast cancer with PIK3CA mutation (approved internationally; not marketed in Taiwan) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on known published information, Alpelisib is a highly selective inhibitor of the PI3Kα isoform (encoded by *PIK3CA*), blocking the PI3K/AKT/mTOR signaling cascade. Its efficacy in HR+/HER2- breast cancer is driven by the fact that *PIK3CA* activating mutations are the most common oncogenic alterations in this tumor type, and the SOLAR-1 Phase 3 trial (NCT02437318, 572 patients) established progression-free survival benefit when combined with fulvestrant.

The theoretical bridge to pulmonary hypertension lies in the PI3K/mTOR pathway's role in vascular smooth muscle cell proliferation and pulmonary vascular remodeling — pathological processes central to pulmonary arterial hypertension (PAH). Study PMID 31039672 provides indirect mechanistic context: PI3Kα pathway inhibition combined with doxorubicin in animal models causes biventricular atrophy and right ventricular dysfunction, demonstrating that this pathway has measurable effects on the cardiopulmonary interface. The knowledge graph may have connected these vascular remodeling biology nodes to generate the prediction.

However, this hypothesis carries a critical contradiction. PMID 35730191 documents a case of alpelisib-induced ILD in a breast cancer patient — meaning the drug itself can cause lung pathology. Using an agent that provokes pulmonary adverse events as a treatment for a pulmonary vascular disease would require extraordinary mechanistic justification and dedicated preclinical safety data that does not currently exist. The mechanistic support for this prediction remains highly speculative, and the safety signal constitutes a substantive barrier.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Multinational real-world cohort of HR+/HER2- advanced breast cancer patients treated with ribociclib or alpelisib (2018–2021); retrieved by drug name only — no pulmonary hypertension data |

> **Note:** The trial above was retrieved by drug name match and is entirely unrelated to pulmonary hypertension. It does not constitute supportive evidence for this repurposing direction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | **⚠ Adverse event report**: Alpelisib-induced interstitial lung disease in an advanced breast cancer patient — this is a pulmonary toxicity signal, not evidence of therapeutic benefit |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin causes biventricular atrophy and right ventricular dysfunction in animal models — documents cardiopulmonary harm from PI3Kα blockade, not therapeutic potential in PAH |

> **Important:** Both publications describe pulmonary or cardiovascular *harm* associated with PI3Kα inhibition. There is no publication reporting therapeutic benefit of alpelisib in pulmonary hypertension.

---

## Taiwan Market Information

Alpelisib currently holds **no marketing authorization in Taiwan** (市場狀態：未上市). No license data is available for tabulation.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα inhibitor (antineoplastic agent) |
| Myelosuppression Risk | Low (myelosuppression is not a primary toxicity; hyperglycemia and severe cutaneous reactions are dose-limiting concerns) |
| Emetogenicity Classification | Low |
| Monitoring Items | Fasting plasma glucose and HbA1c (before and during therapy), CBC with differential, liver function tests, renal function, skin assessment |
| Handling Protection | Standard oral anticancer agent precautions apply; tablets should not be crushed or split |

---

## Safety Considerations

- **Pulmonary Adverse Event Signal**: PMID 35730191 documents alpelisib-induced interstitial lung disease as a direct adverse event in a cancer patient. This is directly relevant to any proposed use in pulmonary disease and constitutes a negative safety signal.
- **Cardiovascular Signal**: PMID 31039672 demonstrates that PI3Kα pathway inhibition causes right ventricular dysfunction in preclinical models, raising concern for patients with pre-existing cardiopulmonary compromise (such as PAH patients).

All formal safety data (TFDA SmPC, contraindications, drug-drug interactions) are not available in this Evidence Pack. Please refer to the EMA or FDA-approved SmPC for Piqray for comprehensive safety and prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN probability score, the evidence base for alpelisib in pulmonary hypertension consists entirely of off-target drug name matches and — more importantly — two publications documenting pulmonary and cardiovascular *harm* from PI3Kα inhibition. There is no preclinical model, mechanistic study, or clinical observation suggesting therapeutic benefit in PAH; the existing signal runs in the opposite direction.

**To proceed, the following would be needed:**

- Dedicated preclinical evidence (in vitro endothelial/smooth muscle assays or PAH animal models) demonstrating that PI3Kα inhibition reduces pulmonary vascular remodeling at clinically achievable alpelisib concentrations
- A mechanistic explanation reconciling the ILD adverse event profile with hypothesized benefit in pulmonary vascular disease
- Formal MOA data retrieval from DrugBank (DB12015) to complete the mechanistic analysis
- TFDA SmPC or equivalent regulatory document to enable S1-level safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

