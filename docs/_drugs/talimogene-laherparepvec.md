---
layout: default
title: Talimogene Laherparepvec
description: "Talimogene Laherparepvec drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 555
evidence_level: L5
indication_count: 50
---

# Talimogene Laherparepvec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Talimogene Laherparepvec |
| DrugBank ID | [DB13896](https://go.drugbank.com/drugs/DB13896) |
| Brand Names (EU) | Imlygic |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.20% |

---

## Approved Indication (EMA)

Imlygic is indicated for the treatment of adults with unresectable melanoma that is regionally or distantly metastatic (Stage IIIB, IIIC and IVM1a) with no bone, brain, lung or other visceral disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | CMM7 | 99.20% | DL |
| 2 | pediatric leptomeningeal melanoma | 99.15% | DL |
| 3 | epithelioid cell uveal melanoma | 99.13% | DL |
| 4 | melanoma | 99.08% | DL |
| 5 | glottis squamous cell carcinoma | 99.07% | DL |
| 6 | lung occult squamous cell carcinoma | 99.05% | DL |
| 7 | rectal cloacogenic carcinoma | 99.01% | DL |
| 8 | gallbladder adenosquamous carcinoma | 99.01% | DL |
| 9 | non-small cell squamous lung carcinoma | 99.00% | DL |
| 10 | external ear basal cell carcinoma | 98.99% | DL |
| 11 | urethral verrucous carcinoma | 98.95% | DL |
| 12 | dental pulp calcification | 98.95% | DL |
| 13 | vulvar melanoma (disease) | 98.95% | DL |
| 14 | supraglottis squamous cell carcinoma | 98.94% | DL |
| 15 | adenosquamous prostate carcinoma | 98.94% | DL |
| 16 | larynx verrucous carcinoma | 98.93% | DL |
| 17 | squamous cell bile duct carcinoma | 98.92% | DL |
| 18 | pancreatic adenosquamous carcinoma | 98.92% | DL |
| 19 | non-keratinizing sinonasal squamous cell carcinoma | 98.90% | DL |
| 20 | squamous cell intraepithelial neoplasia | 98.89% | DL |

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
