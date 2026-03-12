---
layout: default
title: Mecasermin
description: "Mecasermin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 365
evidence_level: L5
indication_count: 51
---

# Mecasermin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mecasermin |
| DrugBank ID | [DB01277](https://go.drugbank.com/drugs/DB01277) |
| Brand Names (EU) | Increlex |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.59% |

---

## Approved Indication (EMA)

For the long-term treatment of growth failure in children and adolescents with severe primary insulin-like-growth-factor-1 deficiency (primary IGFD). Severe primary IGFD is defined by:  height standard deviation score ? -3.0 and; basal insulin-like growth factor-1 (IGF-1) levels below the 2.5th percentile for age and gender and; growth hormone (GH) sufficiency; exclusion of secondary forms of IGF-1 deficiency, such as malnutrition, hypothyroidism, or chronic treatment with pharmacologic doses of

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | monosomy X | 99.59% | DL |
| 2 | Wolman disease with hypolipoproteinemia and acanthocytosis | 99.09% | DL |
| 3 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 99.06% | DL |
| 4 | esophageal varices without bleeding | 99.03% | DL |
| 5 | esophageal varices with bleeding | 99.03% | DL |
| 6 | autosomal ichthyosis syndrome with fatal disease course | 98.67% | DL |
| 7 | Gaucher disease | 98.48% | DL |
| 8 | varicose disease | 98.27% | DL |
| 9 | congenital pulmonary lymphangiectasia | 98.25% | DL |
| 10 | cholesteryl ester storage disease | 98.21% | DL |
| 11 | benign neoplasm of adrenal gland | 98.10% | DL |
| 12 | 16q24.1 microdeletion syndrome | 97.93% | DL |
| 13 | primary interstitial lung disease specific to childhood | 97.82% | DL |
| 14 | isolated pulmonary capillaritis | 97.73% | DL |
| 15 | familial apolipoprotein C-II deficiency | 97.38% | DL |
| 16 | Wolman disease | 97.21% | DL |
| 17 | Steel syndrome | 97.17% | DL |
| 18 | reticular dysgenesis | 97.12% | DL |
| 19 | lysosomal acid lipase deficiency | 97.03% | DL |
| 20 | Hurler syndrome | 97.00% | DL |

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
