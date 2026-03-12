---
layout: default
title: Nonacog Beta Pegol
description: "Nonacog Beta Pegol drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 410
evidence_level: L5
indication_count: 50
---

# Nonacog Beta Pegol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nonacog Beta Pegol |
| DrugBank ID | [DB13933](https://go.drugbank.com/drugs/DB13933) |
| Brand Names (EU) | Refixia |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.64% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of bleeding in patients with haemophilia B (congenital factor IX deficiency). Refixia can be used for all age groups.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 98.64% | DL |
| 2 | Glanzmann thrombasthenia | 98.51% | DL |
| 3 | pseudo-von Willebrand disease | 98.22% | DL |
| 4 | hemorrhagic disorder due to a constitutional thrombocytopenia | 94.79% | DL |
| 5 | bleeding diathesis due to a collagen receptor defect | 94.52% | DL |
| 6 | Scott syndrome | 93.43% | DL |
| 7 | severe nonproliferative diabetic retinopathy | 91.40% | DL |
| 8 | fetal and neonatal alloimmune thrombocytopenia | 88.14% | DL |
| 9 | platelet-type bleeding disorder | 87.74% | DL |
| 10 | hereditary thrombocytosis with transverse limb defect | 86.42% | DL |
| 11 | familial thrombomodulin anomalies | 86.31% | DL |
| 12 | flood factor deficiency | 86.14% | DL |
| 13 | hemophilia | 86.09% | DL |
| 14 | acquired coagulation factor deficiency | 86.07% | DL |
| 15 | hemorrhagic disease of newborn | 83.63% | DL |
| 16 | diabetic retinopathy | 81.33% | DL |
| 17 | inherited thrombophilia | 80.41% | DL |
| 18 | Ehlers-Danlos syndrome, fibronectinemic type | 79.64% | DL |
| 19 | autosomal dominant macrothrombocytopenia | 77.21% | DL |
| 20 | methylcobalamin deficiency type cblG | 75.92% | DL |

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
