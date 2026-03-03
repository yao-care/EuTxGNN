---
layout: default
title: Burosumab
description: "Burosumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 102
evidence_level: L5
indication_count: 51
---

# Burosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Burosumab |
| DrugBank ID | [DB14012](https://go.drugbank.com/drugs/DB14012) |
| Brand Names (EU) | Crysvita |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 96.93% |

---

## Approved Indication (EMA)

Crysvita is indicated for the treatment of X-linked hypophosphataemia, in children and adolescents aged 1 to 17 years with radiographic evidence of bone disease, and in adults. Crysvita is indicated for the treatment of FGF23-related hypophosphataemia in tumour-induced osteomalacia associated with phosphaturic mesenchymal tumours that cannot be curatively resected or localised in children and adolescents aged 1 to 17 years and in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | renal osteodystrophy | 96.93% | DL |
| 2 | impaired renal function disease | 95.92% | DL |
| 3 | non-renal secondary hyperparathyroidism | 95.78% | DL |
| 4 | bone remodeling disease | 95.49% | DL |
| 5 | hyperparathyroidism, transient neonatal | 95.05% | DL |
| 6 | severe nonproliferative diabetic retinopathy | 94.58% | DL |
| 7 | diabetic retinopathy | 93.96% | DL |
| 8 | diabetic cataract | 90.64% | DL |
| 9 | hypocalcemic rickets | 89.65% | DL |
| 10 | cortical cataract | 87.73% | DL |
| 11 | nuclear senile cataract | 87.73% | DL |
| 12 | immature cataract | 87.52% | DL |
| 13 | craniostenosis cataract | 87.52% | DL |
| 14 | diabetes mellitus type 2 associated cataract | 87.52% | DL |
| 15 | mature cataract | 87.52% | DL |
| 16 | tetanic cataract | 87.52% | DL |
| 17 | senile cataract | 87.47% | DL |
| 18 | familial primary hyperparathyroidism | 87.33% | DL |
| 19 | epiglottitis | 86.35% | DL |
| 20 | gastric linitis plastica | 85.46% | DL |

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
