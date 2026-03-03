---
layout: default
title: Pazopanib
description: "Pazopanib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 443
evidence_level: L5
indication_count: 51
---

# Pazopanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pazopanib |
| DrugBank ID | [DB06589](https://go.drugbank.com/drugs/DB06589) |
| Brand Names (EU) | Votrient |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.78% |

---

## Approved Indication (EMA)

Renal-cell carcinoma (RCC) Votrient is indicated in adults for the first-line treatment of advanced renal-cell carcinoma (RCC) and for patients who have received prior cytokine therapy for advanced disease. Soft-tissue sarcoma (STS) Votrient is indicated for the treatment of adult patients with selective subtypes of advanced soft-tissue sarcoma (STS) who have received prior chemotherapy for metastatic disease or who have progressed within 12 months after (neo)adjuvant therapy. Efficacy and safet

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | clear cell renal carcinoma | 99.78% | DL |
| 2 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.63% | DL |
| 3 | unclassified renal cell carcinoma | 99.63% | DL |
| 4 | renal cell carcinoma associated with neuroblastoma | 99.63% | DL |
| 5 | liposarcoma | 99.59% | DL |
| 6 | childhood kidney cell carcinoma | 99.54% | DL |
| 7 | ovarian myxoid liposarcoma | 99.51% | DL |
| 8 | heart fibrosarcoma | 99.37% | DL |
| 9 | fibroblastic neoplasm | 99.35% | DL |
| 10 | kidney fibrosarcoma | 99.33% | DL |
| 11 | renal cell carcinoma (disease) | 99.31% | DL |
| 12 | dermatofibrosarcoma protuberans | 99.29% | DL |
| 13 | conventional fibrosarcoma | 99.28% | DL |
| 14 | low grade fibromyxoid sarcoma | 99.26% | DL |
| 15 | renal carcinoma | 99.25% | DL |
| 16 | angiolipoma | 99.25% | DL |
| 17 | collecting duct carcinoma | 99.12% | DL |
| 18 | bone fibrosarcoma | 99.04% | DL |
| 19 | renal pelvis carcinoma | 99.03% | DL |
| 20 | familial spontaneous pneumothorax | 99.00% | DL |

*Showing top 20 of 51 predictions.*

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
