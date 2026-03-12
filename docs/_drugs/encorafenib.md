---
layout: default
title: Encorafenib
description: "Encorafenib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 208
evidence_level: L5
indication_count: 50
---

# Encorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Encorafenib |
| DrugBank ID | [DB11718](https://go.drugbank.com/drugs/DB11718) |
| Brand Names (EU) | Braftovi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.61% |

---

## Approved Indication (EMA)

MelanomaEncorafenib in combination with binimetinib is indicated for the treatment of adult patients with unresectable or metastatic melanoma with a BRAF V600 mutation.Colorectal cancer (CRC)Encorafenib in combination with cetuximab is indicated for the treatment of adult patients with metastatic colorectal cancer (CRC) &nbsp;with a BRAF V600E mutation, who have received prior systemic therapy.Non-small cell lung cancer (NSCLC)Encorafenib in combination with binimetinib is indicated for the trea

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | metastatic melanoma | 97.61% | DL |
| 2 | choroideremia | 97.10% | DL |
| 3 | non-cutaneous melanoma | 96.55% | DL |
| 4 | epithelioid cell melanoma | 96.45% | DL |
| 5 | eyelid melanoma | 96.40% | DL |
| 6 | scrotum melanoma | 96.09% | DL |
| 7 | choroidal dystrophy, central areolar | 96.07% | DL |
| 8 | amelanotic skin melanoma | 95.59% | DL |
| 9 | lentigo maligna melanoma | 95.59% | DL |
| 10 | malignant melanoma of the mucosa | 95.59% | DL |
| 11 | CDK4 linked melanoma | 95.59% | DL |
| 12 | acral lentiginous melanoma (disease) | 95.59% | DL |
| 13 | superficial spreading melanoma | 95.59% | DL |
| 14 | nodular malignant melanoma | 95.59% | DL |
| 15 | balloon cell malignant melanoma | 95.59% | DL |
| 16 | intestinal obstruction in the newborn due to guanylate cyclase 2C deficiency | 93.98% | DL |
| 17 | bilateral parasagittal parieto-occipital polymicrogyria | 86.25% | DL |
| 18 | borderline ovarian serous tumor | 85.88% | DL |
| 19 | rete ovarii cystadenoma | 85.25% | DL |
| 20 | ovarian mucinous cystadenofibroma | 85.13% | DL |

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
