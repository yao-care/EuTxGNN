---
layout: default
title: Octreotide Hydrochloride
description: "Octreotide Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 416
evidence_level: L5
indication_count: 50
---

# Octreotide Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Octreotide Hydrochloride |
| DrugBank ID | [DB00104](https://go.drugbank.com/drugs/DB00104) |
| Brand Names (EU) | Oczyesa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.58% |

---

## Approved Indication (EMA)

Oczyesa is indicated for maintenance treatment in adult patients with acromegaly who have responded to and tolerated treatment with somatostatin analogues.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | vulvar inverted follicular keratosis | 99.58% | DL |
| 2 | seborrheic keratosis | 99.55% | DL |
| 3 | nephrotic syndrome ocular anomalies | 98.84% | DL |
| 4 | Addison disease | 98.74% | DL |
| 5 | membranoproliferative glomerulonephritis, X-linked | 98.72% | DL |
| 6 | familial idiopathic steroid-resistant nephrotic syndrome with diffuse mesangial sclerosis | 98.57% | DL |
| 7 | familial idiopathic steroid-resistant nephrotic syndrome with minimal changes | 98.57% | DL |
| 8 | adrenocortical insufficiency | 98.47% | DL |
| 9 | primary hypereosinophilic syndrome | 98.43% | DL |
| 10 | autosomal recessive familial Mediterranean fever | 98.31% | DL |
| 11 | primary hereditary glaucoma | 98.23% | DL |
| 12 | secondary hypereosinophilic syndrome | 98.09% | DL |
| 13 | familial nephrotic syndrome | 98.05% | DL |
| 14 | open-angle glaucoma | 97.97% | DL |
| 15 | familial Mediterranean fever, autosomal dominant | 97.82% | DL |
| 16 | retinal telangiectasia | 97.82% | DL |
| 17 | renal-hepatic-pancreatic dysplasia | 97.70% | DL |
| 18 | Smouldering systemic mastocytosis | 97.67% | DL |
| 19 | gout | 97.53% | DL |
| 20 | lymphoadenopathic mastocytosis with eosinophilia | 97.47% | DL |

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
