---
layout: default
title: Vonicog Alfa
description: "Vonicog Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 639
evidence_level: L5
indication_count: 50
---

# Vonicog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vonicog Alfa |
| DrugBank ID | [DB12872](https://go.drugbank.com/drugs/DB12872) |
| Brand Names (EU) | Veyvondi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Prevention and treatment of haemorrhage or surgical bleeding in adults (age 18 years and older) with von Willebrand disease (VWD), when desmopressin (DDAVP) treatment alone is ineffective or contraindicated. Veyvondi should not be used in the treatment of Haemophilia A.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.98% | DL |
| 2 | Glanzmann thrombasthenia | 99.98% | DL |
| 3 | pseudo-von Willebrand disease | 99.97% | DL |
| 4 | hemophilia | 99.95% | DL |
| 5 | Scott syndrome | 99.95% | DL |
| 6 | acquired coagulation factor deficiency | 99.94% | DL |
| 7 | Von Willebrand disease, X-linked form | 99.92% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 99.92% | DL |
| 9 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.92% | DL |
| 10 | flood factor deficiency | 99.90% | DL |
| 11 | hereditary thrombocytosis with transverse limb defect | 99.87% | DL |
| 12 | familial thrombomodulin anomalies | 99.87% | DL |
| 13 | von Willebrand disease | 99.85% | DL |
| 14 | inherited thrombophilia | 99.81% | DL |
| 15 | small bowel Crohn disease | 99.79% | DL |
| 16 | methylcobalamin deficiency type cblG | 99.79% | DL |
| 17 | esophageal ulcer | 99.78% | DL |
| 18 | gastritis | 99.72% | DL |
| 19 | thrombotic thrombocytopenic purpura | 99.66% | DL |
| 20 | hemorrhagic disorder due to a coagulation factors defect | 99.61% | DL |

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
