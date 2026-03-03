---
layout: default
title: Sunitinib
description: "Sunitinib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 547
evidence_level: L5
indication_count: 51
---

# Sunitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sunitinib |
| DrugBank ID | [DB01268](https://go.drugbank.com/drugs/DB01268) |
| Brand Names (EU) | Sunitinib Accord, Sutent |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.87% |

---

## Approved Indication (EMA)

Gastrointestinal stromal tumour (GIST) Sutent is indicated for the treatment of unresectable and/or metastatic malignant gastrointestinal stromal tumour (GIST) in adults after failure of imatinib mesilate treatment due to resistance or intolerance. Metastatic renal cell carcinoma (MRCC) Sutent is indicated for the treatment of advanced/metastatic renal cell carcinoma (MRCC) in adults. Pancreatic neuroendocrine tumours (pNET) Sutent is indicated for the treatment of unresectable or metastatic, we

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | liposarcoma | 99.87% | DL |
| 2 | clear cell renal carcinoma | 99.84% | DL |
| 3 | ovarian myxoid liposarcoma | 99.84% | DL |
| 4 | unclassified renal cell carcinoma | 99.78% | DL |
| 5 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.78% | DL |
| 6 | renal cell carcinoma associated with neuroblastoma | 99.78% | DL |
| 7 | renal cell carcinoma (disease) | 99.74% | DL |
| 8 | dermatofibrosarcoma protuberans | 99.73% | DL |
| 9 | childhood kidney cell carcinoma | 99.72% | DL |
| 10 | angiolipoma | 99.67% | DL |
| 11 | renal carcinoma | 99.65% | DL |
| 12 | heart fibrosarcoma | 99.63% | DL |
| 13 | familial spontaneous pneumothorax | 99.63% | DL |
| 14 | fibroblastic neoplasm | 99.61% | DL |
| 15 | renal pelvis carcinoma | 99.60% | DL |
| 16 | kidney fibrosarcoma | 99.59% | DL |
| 17 | conventional fibrosarcoma | 99.57% | DL |
| 18 | low grade fibromyxoid sarcoma | 99.55% | DL |
| 19 | endocrine-cerebro-osteodysplasia syndrome | 99.54% | DL |
| 20 | uterine corpus perivascular epithelioid cell tumor | 99.43% | DL |

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
