---
layout: default
title: Susoctocog Alfa
description: "Susoctocog Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 548
evidence_level: L5
indication_count: 50
---

# Susoctocog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Susoctocog Alfa |
| DrugBank ID | [DB11606](https://go.drugbank.com/drugs/DB11606) |
| Brand Names (EU) | Obizur |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Treatment of bleeding episodes in patients with acquired haemophilia caused by antibodies to Factor VIII. Obizur is indicated in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.94% | DL |
| 2 | pseudo-von Willebrand disease | 99.93% | DL |
| 3 | Glanzmann thrombasthenia | 99.88% | DL |
| 4 | hemophilia | 99.74% | DL |
| 5 | acquired coagulation factor deficiency | 99.64% | DL |
| 6 | Scott syndrome | 99.60% | DL |
| 7 | acquired hemophilia | 99.19% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 99.17% | DL |
| 9 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.17% | DL |
| 10 | congenital factor XIII deficiency | 99.15% | DL |
| 11 | adenosine deaminase deficiency | 99.04% | DL |
| 12 | factor XIII, A subunit, deficiency | 98.84% | DL |
| 13 | prothrombin deficiency | 98.69% | DL |
| 14 | congenital factor VII deficiency | 98.38% | DL |
| 15 | reticular dysgenesis | 98.37% | DL |
| 16 | hemorrhagic disorder due to a platelet anomaly | 98.30% | DL |
| 17 | severe combined immunodeficiency due to LCK deficiency | 98.20% | DL |
| 18 | platelet-type bleeding disorder | 98.09% | DL |
| 19 | fetal and neonatal alloimmune thrombocytopenia | 97.73% | DL |
| 20 | hemophilia A with vascular abnormality | 97.46% | DL |

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
