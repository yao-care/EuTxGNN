---
layout: default
title: Besilesomab
description: "Besilesomab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 77
evidence_level: L5
indication_count: 50
---

# Besilesomab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Besilesomab |
| DrugBank ID | [DB13979](https://go.drugbank.com/drugs/DB13979) |
| Brand Names (EU) | Scintimun |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.52% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only and the approved indication is scintigraphic imaging, in conjunction with other appropriate imaging modalities, for determining the location of inflammation/infection in peripheral bone in adults with suspected osteomyelitis. Scintimun should not be used for the diagnosis of diabetic foot infection.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 98.52% | DL |
| 2 | diabetes mellitus type 2 associated cataract | 98.46% | DL |
| 3 | immature cataract | 98.46% | DL |
| 4 | craniostenosis cataract | 98.46% | DL |
| 5 | mature cataract | 98.46% | DL |
| 6 | tetanic cataract | 98.46% | DL |
| 7 | nuclear senile cataract | 98.43% | DL |
| 8 | cortical cataract | 98.43% | DL |
| 9 | senile cataract | 98.37% | DL |
| 10 | diabetic retinopathy | 98.20% | DL |
| 11 | severe nonproliferative diabetic retinopathy | 97.92% | DL |
| 12 | antithrombin deficiency type 2 | 97.76% | DL |
| 13 | factor 5 excess with spontaneous thrombosis | 97.70% | DL |
| 14 | heparin cofactor 2 deficiency | 97.65% | DL |
| 15 | thrombophilia | 97.38% | DL |
| 16 | diffuse gastric adenocarcinoma | 95.46% | DL |
| 17 | hemorrhagic disease of newborn | 95.19% | DL |
| 18 | gastric carcinoma | 94.83% | DL |
| 19 | gastric adenocarcinoma and proximal polyposis of the stomach | 94.77% | DL |
| 20 | signet ring cell gastric adenocarcinoma | 94.66% | DL |

*Showing top 20 of 50 predictions.*

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
