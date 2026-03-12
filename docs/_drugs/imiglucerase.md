---
layout: default
title: Imiglucerase
description: "Imiglucerase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 294
evidence_level: L5
indication_count: 50
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Imiglucerase |
| DrugBank ID | [DB00053](https://go.drugbank.com/drugs/DB00053) |
| Brand Names (EU) | Cerezyme |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.52% |

---

## Approved Indication (EMA)

Cerezyme (imiglucerase) is indicated for use as longterm enzyme replacement therapy in patients with a confirmed diagnosis of non-neuronopathic (Type 1) or chronic neuronopathic (Type 3) Gaucher disease who exhibit clinically significant nonneurological manifestations of the disease. The non-neurological manifestations of Gaucher disease include one or more of the following conditions:  anaemia after exclusion of other causes, such as iron deficiency Thrombocytopenia Bone disease after exclusion

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Hurler syndrome | 99.52% | DL |
| 2 | Gaucher disease | 99.40% | DL |
| 3 | Scheie syndrome | 99.29% | DL |
| 4 | benign neoplasm of adrenal gland | 99.28% | DL |
| 5 | autosomal ichthyosis syndrome with fatal disease course | 99.24% | DL |
| 6 | cholesteryl ester storage disease | 99.12% | DL |
| 7 | lysosomal storage disease with skeletal involvement | 98.94% | DL |
| 8 | Wolman disease with hypolipoproteinemia and acanthocytosis | 98.93% | DL |
| 9 | Wolman disease | 98.78% | DL |
| 10 | proximal myopathy with extrapyramidal signs | 98.54% | DL |
| 11 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 98.49% | DL |
| 12 | Tay-Sachs disease | 98.41% | DL |
| 13 | familial apolipoprotein C-II deficiency | 98.37% | DL |
| 14 | adult Krabbe disease | 98.36% | DL |
| 15 | encephalopathy due to prosaposin deficiency | 98.30% | DL |
| 16 | Krabbe disease | 98.15% | DL |
| 17 | X-linked lymphoproliferative disease due to SH2D1A deficiency | 98.13% | DL |
| 18 | Cushing disease due to pituitary adenoma | 98.09% | DL |
| 19 | lysosomal acid lipase deficiency | 97.98% | DL |
| 20 | metachromatic leukodystrophy | 97.97% | DL |

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
