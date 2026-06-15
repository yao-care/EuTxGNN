---
layout: default
title: Anidulafungin
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Anidulafungin
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

# Anidulafungin: From Invasive Candidiasis to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal administered intravenously, established for the treatment of invasive candidiasis and candidemia in critically ill and immunocompromised patients.
The TxGNN model ranks **Impetigo** as its top predicted repurposing candidate with a score of 98.85%, yet this prediction is mechanistically implausible — impetigo is a purely bacterial skin infection with no connection to Anidulafungin's antifungal mechanism.
Currently, **0 clinical trials** and **0 publications** support this specific repurposing direction, placing the evidence at Level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis / Candidemia (not registered in Taiwan) |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Anidulafungin is an echinocandin that selectively inhibits β-(1,3)-D-glucan synthase — the enzyme responsible for constructing the fungal cell wall. This target is absent in both mammalian and bacterial cells, making the drug exclusively active against fungi such as *Candida* and *Aspergillus* species.

Impetigo is a superficial bacterial skin infection caused by *Staphylococcus aureus* or *Streptococcus pyogenes*. There is no known biological pathway linking Anidulafungin's mechanism to bacterial pathogens or their toxins. The TxGNN high score most likely arises from non-specific co-occurrence signals in the "skin infection" comorbidity network within the knowledge graph — where immunocompromised patients treated with Anidulafungin for candidemia also carry diagnoses of concurrent bacterial skin conditions — rather than any direct therapeutic relationship.

Among all 10 top predictions in this Evidence Pack, the mechanistically most coherent candidate is **Pleural Empyema** (Rank 4). Fungal empyema in immunocompromised patients (transplant recipients, haematological malignancy patients) is a recognised clinical entity. Importantly, a pharmacokinetic study (PMID 29439960, 2018) demonstrates that Anidulafungin does penetrate pleural effusion in critically ill patients, providing drug-delivery confirmation. This direction remains an exploratory research question pending efficacy evidence, but merits scientific investigation unlike the top-ranked bacterial predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anidulafungin in impetigo.

---

## Literature Evidence

Currently no related literature available for Anidulafungin in impetigo.

---

## Additional Signal: Pleural Empyema (Rank 4)

Although the primary report focuses on the top prediction, the following pharmacokinetic evidence is the only clinically interpretable literature found across all 10 predictions, and warrants transparent disclosure:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29439960](https://pubmed.ncbi.nlm.nih.gov/29439960/) | 2018 | Pharmacokinetic / Observational | Antimicrobial Agents and Chemotherapy | Anidulafungin concentrations measured in ascites fluid (0.12–0.99 μg/mL) and pleural effusion (0.32–2.02 μg/mL) of 10 critically ill patients, confirming drug penetration into body cavities below simultaneous plasma levels |

> **Context:** This PK study does not demonstrate clinical efficacy in pleural empyema. It only confirms that Anidulafungin reaches the pleural space, which is a necessary but not sufficient condition for therapeutic activity against fungal empyema.

---

## Safety Considerations

Please refer to the SmPC for complete safety information. TFDA prescribing information and key warnings/contraindications were not available in this Evidence Pack and represent a blocking data gap for formal safety screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (impetigo) is mechanistically disconnected from Anidulafungin's mode of action — the drug targets the fungal cell wall and has no antibacterial activity whatsoever. The L5 evidence level (AI prediction only, zero supporting studies) means no repurposing pathway exists for this indication. The broader pattern across the top 10 predictions shows that most high-ranking outputs reflect knowledge graph topology artefacts (shared disease ontology nodes, ICU co-occurrence) rather than genuine pharmacological relationships.

**To proceed with any repurposing work, the following is needed:**

- **MOA confirmation:** Retrieve complete DrugBank entry (DB00362) to formally document mechanism and fill the MOA data gap
- **Safety baseline:** Download TFDA SmPC PDF and extract warnings, contraindications, and dose adjustments to resolve the blocking DG001 data gap
- **Redirect focus to fungal empyema:** The pleural empyema prediction (Rank 4, L4) is the only direction with mechanistic coherence and preliminary PK evidence; a structured literature review specifically on fungal pleural empyema management should be conducted
- **Efficacy data required:** The 2018 PK study (PMID 29439960) confirms drug exposure in pleural fluid but provides no efficacy endpoint; case series or retrospective cohort data on candidal empyema treatment with echinocandins are needed before this can advance to S1
- **Taiwan registration pathway:** If a fungal empyema indication is pursued, an out-of-country evidence package referencing EMA/FDA approvals for invasive candidiasis would be the regulatory entry point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

