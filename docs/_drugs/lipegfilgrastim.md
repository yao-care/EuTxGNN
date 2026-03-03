---
layout: default
title: Lipegfilgrastim
description: "Lipegfilgrastim drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 346
evidence_level: L5
indication_count: 50
---

# Lipegfilgrastim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lipegfilgrastim |
| DrugBank ID | [DB13200](https://go.drugbank.com/drugs/DB13200) |
| Brand Names (EU) | Lonquex |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Lonquex is indicated in adults and in children 2 years of age and older for reduction in the duration of neutropenia and the incidence of febrile neutropenia in patients treated with cytotoxic chemotherapy for malignancy (with the exception of chronic myeloid leukaemia and myelodysplastic syndromes).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.93% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 99.91% | DL |
| 3 | pseudo-von Willebrand disease | 99.91% | DL |
| 4 | Glanzmann thrombasthenia | 99.91% | DL |
| 5 | diabetic retinopathy | 99.75% | DL |
| 6 | hemorrhagic disorder due to a constitutional thrombocytopenia | 98.99% | DL |
| 7 | thrombocytopenia due to immune destruction | 98.96% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 98.93% | DL |
| 9 | Scott syndrome | 98.75% | DL |
| 10 | drug-induced osteoporosis | 98.64% | DL |
| 11 | fetal and neonatal alloimmune thrombocytopenia | 98.49% | DL |
| 12 | neonatal thrombocytopenia | 98.19% | DL |
| 13 | HER2 positive breast carcinoma | 97.85% | DL |
| 14 | dermatitis | 97.80% | DL |
| 15 | autoimmune thrombocytopenic | 97.67% | DL |
| 16 | diabetic cataract | 97.63% | DL |
| 17 | platelet-type bleeding disorder | 97.55% | DL |
| 18 | seborrheic dermatitis | 96.89% | DL |
| 19 | acrodermatitis chronica atrophicans | 96.78% | DL |
| 20 | Ehlers-Danlos syndrome, fibronectinemic type | 96.75% | DL |

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
