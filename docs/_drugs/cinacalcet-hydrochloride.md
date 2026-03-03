---
layout: default
title: Cinacalcet Hydrochloride
description: "Cinacalcet Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 136
evidence_level: L5
indication_count: 50
---

# Cinacalcet Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cinacalcet Hydrochloride |
| DrugBank ID | [DB01012](https://go.drugbank.com/drugs/DB01012) |
| Brand Names (EU) | Mimpara |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.48% |

---

## Approved Indication (EMA)

Secondary hyperparathyroidism Adults Treatment of secondary hyperparathyroidism (HPT) in adult patients with end stage renal disease (ESRD) on maintenance dialysis therapy. Paediatric population Treatment of secondary hyperparathyroidism (HPT) in children aged 3 years and older with end stage renal disease (ESRD) on maintenance dialysis therapy in whom secondary HPT is not adequately controlled with standard of care therapy. Mimpara may be used as part of a therapeutic regimen including phosphat

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 98.48% | DL |
| 2 | common cold | 95.39% | DL |
| 3 | female breast carcinoma | 94.23% | DL |
| 4 | multiple endocrine neoplasia | 93.73% | DL |
| 5 | headache disorder | 93.08% | DL |
| 6 | trigeminal autonomic cephalalgia | 92.16% | DL |
| 7 | hypertrichosis (disease) | 91.66% | DL |
| 8 | subarachnoid hemorrhage (disease) | 91.39% | DL |
| 9 | pulmonary hypertension | 91.21% | DL |
| 10 | obsolete familial combined hyperlipidemia | 90.80% | DL |
| 11 | malformation syndrome with odontal and/or periodontal component | 90.64% | DL |
| 12 | kyphoscoliotic heart disease | 90.50% | DL |
| 13 | syndrome with a Dandy-Walker malformation as major feature | 90.48% | DL |
| 14 | Ambras type hypertrichosis universalis congenita | 90.06% | DL |
| 15 | breast fibrocystic disease | 89.71% | DL |
| 16 | isolated genetic hair shaft abnormality | 89.64% | DL |
| 17 | mycotic corneal ulcer | 89.14% | DL |
| 18 | prostate neoplasm | 88.77% | DL |
| 19 | fibroma of prostate | 88.77% | DL |
| 20 | benign reproductive system neoplasm | 88.21% | DL |

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
