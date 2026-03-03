---
layout: default
title: Temsirolimus
description: "Temsirolimus drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 566
evidence_level: L5
indication_count: 51
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Temsirolimus |
| DrugBank ID | [DB06287](https://go.drugbank.com/drugs/DB06287) |
| Brand Names (EU) | Torisel |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.54% |

---

## Approved Indication (EMA)

Renal-cell carcinoma Torisel is indicated for the first-line treatment of adult patients with advanced renal-cell carcinoma (RCC) who have at least three of six prognostic risk factors. Mantle-cell lymphoma Torisel is indicated for the treatment of adult patients with relapsed and / or refractory mantle-cell lymphoma (MCL).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | liposarcoma | 99.54% | DL |
| 2 | ovarian myxoid liposarcoma | 99.47% | DL |
| 3 | clear cell renal carcinoma | 99.39% | DL |
| 4 | vulva sarcoma | 99.09% | DL |
| 5 | uterine corpus myxoid leiomyosarcoma | 98.88% | DL |
| 6 | anus leiomyosarcoma | 98.77% | DL |
| 7 | uterine corpus epithelioid leiomyosarcoma | 98.76% | DL |
| 8 | small intestinal sarcoma | 98.64% | DL |
| 9 | retroperitoneal sarcoma | 98.60% | DL |
| 10 | leiomyosarcoma | 98.60% | DL |
| 11 | renal cell carcinoma associated with neuroblastoma | 98.53% | DL |
| 12 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 98.53% | DL |
| 13 | unclassified renal cell carcinoma | 98.53% | DL |
| 14 | childhood kidney cell carcinoma | 98.09% | DL |
| 15 | spindle cell liposarcoma | 97.66% | DL |
| 16 | mixed endometrial stromal and smooth muscle tumor | 97.24% | DL |
| 17 | dermatofibrosarcoma protuberans | 97.23% | DL |
| 18 | angiolipoma | 96.72% | DL |
| 19 | childhood malignant neoplasm | 96.57% | DL |
| 20 | familial rhabdoid tumor | 96.55% | DL |

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
