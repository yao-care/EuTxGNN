---
layout: default
title: Darunavir
description: "Darunavir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 158
evidence_level: L5
indication_count: 50
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Darunavir |
| DrugBank ID | [DB01264](https://go.drugbank.com/drugs/DB01264) |
| Brand Names (EU) | Prezista |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Symtuza is indicated for the treatment of human immunodeficiency virus type 1 (HIV?1) infection in adults and adolescents (aged 12 years and older with body weight at least 40 kg). Genotypic testing should guide the use of Symtuza.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.98% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.97% | DL |
| 3 | simian immunodeficiency virus infection | 99.97% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.97% | DL |
| 5 | AIDS | 99.58% | DL |
| 6 | obsolete familial combined hyperlipidemia | 99.19% | DL |
| 7 | congenital human immunodeficiency virus | 98.97% | DL |
| 8 | AIDS related complex | 98.97% | DL |
| 9 | fibroma of prostate | 97.74% | DL |
| 10 | Brenner tumor | 97.53% | DL |
| 11 | benign reproductive system neoplasm | 97.52% | DL |
| 12 | benign prostate phyllodes tumor | 97.35% | DL |
| 13 | male reproductive organ cancer | 96.83% | DL |
| 14 | prostate cancer/brain cancer susceptibility | 96.25% | DL |
| 15 | prostate leiomyoma | 96.24% | DL |
| 16 | breast fibrocystic disease | 92.38% | DL |
| 17 | chronic hepatitis C virus infection | 91.23% | DL |
| 18 | benign mammary dysplasia | 91.05% | DL |
| 19 | apocrine adenosis of breast | 91.01% | DL |
| 20 | blunt duct adenosis of breast | 91.01% | DL |

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
