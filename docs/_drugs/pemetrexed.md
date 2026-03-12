---
layout: default
title: Pemetrexed
description: "pemetrexed drug repurposing predictions from TxGNN. Evidence level L3 with 51 predicted indications."
parent: Observational Evidence (L3)
nav_order: 451
evidence_level: L3
indication_count: 51
---

# Pemetrexed
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pemetrexed |
| DrugBank ID | [DB00642](https://go.drugbank.com/drugs/DB00642) |
| Brand Names (EU) | Pemetrexed Fresenius Kabi |
| Evidence Level | L3 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Malignant pleural mesothelioma Pemetrexed Fresenius Kabi in combination with cisplatin is indicated for the treatment of chemotherapy naïve patients with unresectable malignant pleural mesothelioma. Non-small cell lung cancer Pemetrexed Fresenius Kabi in combination with cisplatin is indicated for the first line treatment of patients with locally advanced or metastatic non-small cell lung cancer other than predominantly squamous cell histology. Pemetrexed Fresenius Kabi is indicated as monothera

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malignant peritoneal mesothelioma | 99.99% | DL |
| 2 | pleural adenomatoid tumor | 99.99% | DL |
| 3 | pleural mesothelioma | 99.99% | DL |
| 4 | pleural epithelioid mesothelioma | 99.99% | DL |
| 5 | pleural sarcomatoid mesothelioma | 99.99% | DL |
| 6 | pleural biphasic mesothelioma | 99.99% | DL |
| 7 | pericardium cancer | 99.99% | DL |
| 8 | well differentiated papillary mesothelioma | 99.99% | DL |
| 9 | lymphohistiocytoid mesothelioma | 99.99% | DL |
| 10 | malignant mesothelioma (disease) | 99.98% | DL |
| 11 | iminoglycinuria | 99.97% | DL |
| 12 | male infertility with teratozoospermia due to single gene mutation | 99.96% | DL |
| 13 | rhabdomyosarcoma (disease) | 99.93% | DL |
| 14 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.93% | DL |
| 15 | extrahepatic bile duct rhabdomyosarcoma | 99.92% | DL |
| 16 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.92% | DL |
| 17 | parameningeal embryonal rhabdomyosarcoma | 99.92% | DL |
| 18 | prostate embryonal rhabdomyosarcoma | 99.92% | DL |
| 19 | liver sarcoma | 99.91% | DL |
| 20 | liposarcoma | 99.90% | DL |

*Showing top 20 of 51 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| pericardium cancer | L3 | 3 | 0 | 2 Phase 2 trial(s) |

---
## About TxGNN Predictions

### Prediction Sources

| Source | Description |
|--------|-------------|
| **KG** | Knowledge Graph - Network topology-based associations |
| **DL** | Deep Learning - Neural network score prediction |

### Evidence Levels

| Level | Definition |
|:-----:|------------|
| L1 | Multiple Phase 3 RCTs / Systematic Reviews |
| L2 | Single RCT or multiple Phase 2 trials |
| L3 | Observational studies / Large case series |
| L4 | Preclinical / Mechanistic / Case reports |
| **L5** | AI prediction only (current) |

---

## Clinical Validation Needed

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Research Use Only:</strong> These predictions are computational hypotheses that require clinical validation. They should NOT be used for clinical decision-making.
</div>

### Next Steps for Validation

1. **Literature Review**: Search PubMed for existing evidence
2. **Clinical Trial Search**: Check ClinicalTrials.gov for ongoing studies
3. **Mechanistic Analysis**: Evaluate biological plausibility
4. **Preclinical Studies**: Conduct in vitro/in vivo validation
5. **Clinical Trials**: Design and conduct human studies

---

## Data Access

- **FHIR API**: `/fhir/ClinicalUseDefinition/`
- **CSV Download**: [All Predictions](/downloads/)
- **GitHub**: [yao-care/EuTxGNN](https://github.com/yao-care/EuTxGNN)

---

## Citation

If using this data, please cite:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

<div style="background: #f8f9fa; padding: 1rem; border-radius: 4px; font-size: 0.9rem;">
<strong>Disclaimer:</strong> This report is for research purposes only and does not constitute medical advice. Drug repurposing predictions require rigorous clinical validation before any therapeutic application.
</div>
