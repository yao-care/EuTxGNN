---
layout: default
title: Binimetinib
description: "Binimetinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 84
evidence_level: L5
indication_count: 50
---

# Binimetinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Binimetinib |
| DrugBank ID | [DB11967](https://go.drugbank.com/drugs/DB11967) |
| Brand Names (EU) | Mektovi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.06% |

---

## Approved Indication (EMA)

MelanomaBinimetinib in combination with encorafenib is indicated for the treatment of adult patients with unresectable or metastatic melanoma with a BRAF V600 mutation.Non-small cell lung cancer (NSCLC)Binimetinib in combination with encorafenib is indicated for the treatment of adult patients with advanced non-small cell lung cancer with a BRAF V600E mutation.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | metastatic melanoma | 99.06% | DL |
| 2 | choroideremia | 98.63% | DL |
| 3 | non-cutaneous melanoma | 98.60% | DL |
| 4 | epithelioid cell melanoma | 98.57% | DL |
| 5 | eyelid melanoma | 98.54% | DL |
| 6 | scrotum melanoma | 98.42% | DL |
| 7 | malignant melanoma of the mucosa | 98.19% | DL |
| 8 | nodular malignant melanoma | 98.19% | DL |
| 9 | superficial spreading melanoma | 98.19% | DL |
| 10 | lentigo maligna melanoma | 98.19% | DL |
| 11 | amelanotic skin melanoma | 98.19% | DL |
| 12 | acral lentiginous melanoma (disease) | 98.19% | DL |
| 13 | balloon cell malignant melanoma | 98.19% | DL |
| 14 | CDK4 linked melanoma | 98.19% | DL |
| 15 | choroidal dystrophy, central areolar | 98.16% | DL |
| 16 | intestinal obstruction in the newborn due to guanylate cyclase 2C deficiency | 97.96% | DL |
| 17 | amyotrophic lateral sclerosis | 91.75% | DL |
| 18 | bilateral parasagittal parieto-occipital polymicrogyria | 91.69% | DL |
| 19 | Mills syndrome | 91.04% | DL |
| 20 | amyotrophic lateral sclerosis, susceptibility to | 90.68% | DL |

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
