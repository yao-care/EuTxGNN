---
layout: default
title: Ceftolozane
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozane: From Complicated Urinary Tract Infections to Gonococcal Urethritis

## One-Sentence Summary

Ceftolozane is a novel semisynthetic cephalosporin (β-lactam) antibiotic, clinically deployed as the Ceftolozane/tazobactam combination (Zerbaxa), approved in the US and EU for complicated urinary tract infections (cUTI) and complicated intra-abdominal infections (cIAI) — though not currently registered in Taiwan.

The TxGNN model predicts it may be effective for **Gonococcal Urethritis**, with a prediction score of **99.89%**; however, **no clinical trials** and **no publications** currently exist in this data set to support this direction, placing the evidence entirely at the model-prediction tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Complicated urinary tract infections (cUTI) including pyelonephritis; complicated intra-abdominal infections (cIAI) — as Ceftolozane/tazobactam combination |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not registered |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Ceftolozane is a β-lactam antibiotic of the cephalosporin class. Its primary mechanism involves inhibiting bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs) — particularly PBP1b, PBP1c, and PBP3 — thereby disrupting peptidoglycan crosslinking and triggering cell lysis. It is always co-administered with tazobactam, a β-lactamase inhibitor that shields Ceftolozane from enzymatic degradation by extended-spectrum β-lactamases (ESBLs). The combination demonstrates exceptional potency against multidrug-resistant *Pseudomonas aeruginosa* and other difficult gram-negative pathogens.

The mechanistic link to gonococcal urethritis is conceptually plausible. *Neisseria gonorrhoeae* is a gram-negative diplococcus that possesses PBPs and is theoretically susceptible to β-lactam antibiotics targeting the same pathway. Furthermore, treatment-resistant gonorrhea — including strains failing ceftriaxone, the current first-line therapy — represents an urgent unmet public health need. Some in vitro data (not captured in this data set) suggest Ceftolozane achieves low MIC values against *N. gonorrhoeae*, making it a candidate of interest for drug-resistant gonococcal infections.

That said, translating in vitro susceptibility to clinical utility for urethritis requires additional considerations: the standard of care for uncomplicated gonorrhea is oral or single-dose IM therapy, whereas Ceftolozane/tazobactam is administered intravenously, limiting its practicality in outpatient STI settings. The TxGNN score of 99.89% most likely reflects the model's recognition of the shared gram-negative pathogen class between approved and predicted indications, rather than indication-specific clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ceftolozane in Gonococcal Urethritis.

---

## Literature Evidence

Currently no related literature available for Ceftolozane in Gonococcal Urethritis.

---

## Taiwan Market Information

Ceftolozane is currently **not registered** in Taiwan. The Taiwan FDA (TFDA) has issued no marketing authorizations for Ceftolozane or Ceftolozane/tazobactam products. Safety data including prescribing warnings and contraindications from the TFDA package insert are therefore unavailable and represent a blocking data gap (DG001).

---

## Safety Considerations

Please refer to the Ceftolozane/tazobactam SmPC (EU) or US Prescribing Information for safety information. Key safety data including TFDA warnings, contraindications, and drug-drug interactions were not available in this evidence pack and must be retrieved before clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic rationale connecting Ceftolozane's PBP-inhibitory activity to *N. gonorrhoeae* is pharmacologically coherent — and the public health urgency of drug-resistant gonorrhea provides genuine motivation — the complete absence of clinical trials and published literature (L5 evidence) means this prediction cannot advance beyond a research hypothesis at this time. Additionally, the IV-only route of administration creates a practical barrier for an outpatient STI indication.

**To proceed, the following is needed:**

- **MIC / in vitro susceptibility data**: Obtain or commission minimum inhibitory concentration studies of Ceftolozane against clinical *N. gonorrhoeae* isolates, with priority on ceftriaxone-resistant strains
- **MOA confirmation (DG002)**: Retrieve full mechanism of action and PBP-binding profile from DrugBank to confirm coverage of *N. gonorrhoeae*-specific PBP variants
- **TFDA prescribing information (DG001)**: Download and parse TFDA SmPC equivalent to identify contraindications and warnings before any safety assessment can proceed
- **Route compatibility assessment**: Evaluate whether IV Ceftolozane/tazobactam is clinically appropriate for the urethritis indication (outpatient vs. hospitalized patients)
- **Systematic literature review**: Search for Ceftolozane activity against sexually transmitted gram-negative pathogens outside the current data set (e.g., ESCMID, IDSA conference abstracts)
- **Regulatory precedent scan**: Review whether any regulatory agency has evaluated Ceftolozane/tazobactam for STI indications as part of a drug-resistant gonorrhea emergency use pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

