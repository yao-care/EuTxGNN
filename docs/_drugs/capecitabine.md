---
layout: default
title: Capecitabine
description: "capecitabine drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 112
evidence_level: L5
indication_count: 51
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Capecitabine |
| DrugBank ID | [DB01101](https://go.drugbank.com/drugs/DB01101) |
| Brand Names (EU) | Xeloda |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Xeloda is indicated for the adjuvant treatment of patients following surgery of stage III (Dukes' stage C) colon cancer. Xeloda is indicated for the treatment of metastatic colorectal cancer. Xeloda is indicated for first-line treatment of advanced gastric cancer in combination with a platinum-based regimen. Xeloda in combination with docetaxel is indicated for the treatment of patients with locally advanced or metastatic breast cancer after failure of cytotoxic chemotherapy. Previous therapy sh

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diffuse gastric adenocarcinoma | 99.97% | DL |
| 2 | gastric cancer | 99.95% | DL |
| 3 | gastric carcinoma | 99.94% | DL |
| 4 | gastric adenocarcinoma and proximal polyposis of the stomach | 99.94% | DL |
| 5 | microinvasive gastric cancer | 99.94% | DL |
| 6 | gastric tubular adenocarcinoma | 99.94% | DL |
| 7 | signet ring cell gastric adenocarcinoma | 99.94% | DL |
| 8 | gastric cardia adenocarcinoma | 99.91% | DL |
| 9 | carcinoma of stomach, salivary gland type | 99.91% | DL |
| 10 | gastric pylorus carcinoma | 99.91% | DL |
| 11 | gastric body carcinoma | 99.90% | DL |
| 12 | Epstein-Barr virus-associated gastric carcinoma | 99.90% | DL |
| 13 | malignant gastric granular cell tumor | 99.89% | DL |
| 14 | carcinoma in situ of gastric body | 99.89% | DL |
| 15 | benign neoplasm of stomach | 99.89% | DL |
| 16 | cardia cancer | 99.89% | DL |
| 17 | carcinoma in situ of gastric cardia | 99.89% | DL |
| 18 | gastric lymphoma | 99.89% | DL |
| 19 | pylorus cancer | 99.89% | DL |
| 20 | pyloric antrum cancer | 99.88% | DL |

*Showing top 20 of 51 predictions.*

---


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
