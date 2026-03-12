---
layout: default
title: Pentosan Polysulfate Sodium
description: "Pentosan Polysulfate Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 453
evidence_level: L5
indication_count: 50
---

# Pentosan Polysulfate Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pentosan Polysulfate Sodium |
| DrugBank ID | [DB00686](https://go.drugbank.com/drugs/DB00686) |
| Brand Names (EU) | Elmiron |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Elmiron is indicated for the treatment of bladder pain syndrome characterized by either glomerulations or Hunner’s lesions in adults with moderate to severe pain, urgency and frequency of micturition.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.71% | DL |
| 2 | Glanzmann thrombasthenia | 99.65% | DL |
| 3 | pseudo-von Willebrand disease | 99.62% | DL |
| 4 | heparin-induced thrombocytopenia (disease) | 98.75% | DL |
| 5 | fetal and neonatal alloimmune thrombocytopenia | 98.73% | DL |
| 6 | autosomal dominant macrothrombocytopenia | 97.75% | DL |
| 7 | hemoglobinopathy | 97.73% | DL |
| 8 | autoimmune hemolytic anemia | 97.69% | DL |
| 9 | autoimmune thrombocytopenic | 97.57% | DL |
| 10 | bleeding diathesis due to a collagen receptor defect | 97.47% | DL |
| 11 | hemorrhagic disorder due to a constitutional thrombocytopenia | 97.45% | DL |
| 12 | rheumatoid arthritis | 97.30% | DL |
| 13 | platelet-type bleeding disorder | 97.24% | DL |
| 14 | acquired aplastic anemia | 97.04% | DL |
| 15 | partial deletion of the short arm of chromosome 16 | 96.85% | DL |
| 16 | penile fibromatosis | 96.69% | DL |
| 17 | disorder of GPI anchor biosynthesis | 96.66% | DL |
| 18 | beta-thalassemia with other manifestations | 96.64% | DL |
| 19 | bone Paget disease | 96.59% | DL |
| 20 | hemolytic anemia due to glucophosphate isomerase deficiency | 96.57% | DL |

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
