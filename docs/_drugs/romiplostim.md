---
layout: default
title: Romiplostim
description: "romiplostim drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 505
evidence_level: L5
indication_count: 51
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Romiplostim |
| DrugBank ID | [DB05332](https://go.drugbank.com/drugs/DB05332) |
| Brand Names (EU) | Nplate |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Adults: Nplate is indicated for the treatment of primary immune thrombocytopenia  (ITP) in adult patients who are refractory to other treatments (e.g. corticosteroids, immunoglobulins). Paediatrics: Nplate is indicated for the treatment of chronic primary immune thrombocytopenia (ITP) in paediatric patients one year of age and older who are refractory to other treatments (e.g. corticosteroids, immunoglobulins).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 100.00% | DL |
| 2 | pseudo-von Willebrand disease | 100.00% | DL |
| 3 | Glanzmann thrombasthenia | 100.00% | DL |
| 4 | fetal and neonatal alloimmune thrombocytopenia | 99.99% | DL |
| 5 | Scott syndrome | 99.97% | DL |
| 6 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.95% | DL |
| 7 | bleeding diathesis due to a collagen receptor defect | 99.95% | DL |
| 8 | platelet-type bleeding disorder | 99.93% | DL |
| 9 | autosomal dominant macrothrombocytopenia | 99.88% | DL |
| 10 | Ehlers-Danlos syndrome, fibronectinemic type | 99.85% | DL |
| 11 | paroxysmal nocturnal hemoglobinuria | 99.64% | DL |
| 12 | proteinuria | 99.58% | DL |
| 13 | neurolymphomatosis | 99.57% | DL |
| 14 | mixed-type autoimmune hemolytic anemia | 99.56% | DL |
| 15 | drug-induced autoimmune hemolytic anemia | 99.53% | DL |
| 16 | neonatal autoimmune hemolytic anemia | 99.49% | DL |
| 17 | plasmacytoma | 99.49% | DL |
| 18 | primary CD59 deficiency | 99.44% | DL |
| 19 | Peyronie disease | 99.34% | DL |
| 20 | cold agglutinin disease | 99.26% | DL |

*Showing top 20 of 51 predictions.*

---


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
