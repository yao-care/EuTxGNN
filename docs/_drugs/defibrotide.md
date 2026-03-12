---
layout: default
title: Defibrotide
description: "Defibrotide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 164
evidence_level: L5
indication_count: 50
---

# Defibrotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Defibrotide |
| DrugBank ID | [DB04932](https://go.drugbank.com/drugs/DB04932) |
| Brand Names (EU) | Defitelio |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.91% |

---

## Approved Indication (EMA)

Defitelio is indicated for the treatment of severe hepatic veno-occlusive disease (VOD) also known as sinusoidal obstructive syndrome (SOS) in haematopoietic stem-cell transplantation (HSCT) therapy. It is indicated in adults and in adolescents, children and infants over 1 month of age.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pseudo-von Willebrand disease | 99.91% | DL |
| 2 | primary release disorder of platelets | 99.91% | DL |
| 3 | Glanzmann thrombasthenia | 99.88% | DL |
| 4 | thrombotic thrombocytopenic purpura | 99.71% | DL |
| 5 | Scott syndrome | 99.67% | DL |
| 6 | bleeding diathesis due to a collagen receptor defect | 99.43% | DL |
| 7 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.39% | DL |
| 8 | congenital factor V deficiency | 99.30% | DL |
| 9 | fetal and neonatal alloimmune thrombocytopenia | 99.23% | DL |
| 10 | thrombocytopenic purpura | 99.22% | DL |
| 11 | inherited thrombophilia | 99.16% | DL |
| 12 | hepatic infarction | 99.14% | DL |
| 13 | peliosis hepatis | 98.98% | DL |
| 14 | familial apolipoprotein C-II deficiency | 98.79% | DL |
| 15 | syndrome with combined immunodeficiency | 98.75% | DL |
| 16 | platelet-type bleeding disorder | 98.69% | DL |
| 17 | Ehlers-Danlos syndrome, fibronectinemic type | 98.68% | DL |
| 18 | hepatic veno-occlusive disease | 98.67% | DL |
| 19 | flood factor deficiency | 98.64% | DL |
| 20 | methylcobalamin deficiency type cblG | 98.25% | DL |

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
