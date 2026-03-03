---
layout: default
title: Andexanet Alfa
description: "Andexanet Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 39
evidence_level: L5
indication_count: 50
---

# Andexanet Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Andexanet Alfa |
| DrugBank ID | [DB14562](https://go.drugbank.com/drugs/DB14562) |
| Brand Names (EU) | Ondexxya |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.77% |

---

## Approved Indication (EMA)

For adult patients treated with a direct factor Xa (FXa) inhibitor (apixaban or rivaroxaban) when reversal of anticoagulation is needed due to life-threatening or uncontrolled bleeding.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Glanzmann thrombasthenia | 99.77% | DL |
| 2 | primary release disorder of platelets | 99.76% | DL |
| 3 | pseudo-von Willebrand disease | 99.65% | DL |
| 4 | hemophilia | 99.10% | DL |
| 5 | hemorrhagic disorder due to a constitutional thrombocytopenia | 98.99% | DL |
| 6 | bleeding diathesis due to a collagen receptor defect | 98.92% | DL |
| 7 | acquired coagulation factor deficiency | 98.85% | DL |
| 8 | Scott syndrome | 98.73% | DL |
| 9 | congenital prothrombin deficiency | 98.36% | DL |
| 10 | hereditary thrombocytosis with transverse limb defect | 97.16% | DL |
| 11 | familial thrombomodulin anomalies | 97.14% | DL |
| 12 | flood factor deficiency | 97.13% | DL |
| 13 | fetal and neonatal alloimmune thrombocytopenia | 96.59% | DL |
| 14 | platelet-type bleeding disorder | 96.18% | DL |
| 15 | methylcobalamin deficiency type cblG | 94.57% | DL |
| 16 | autosomal dominant macrothrombocytopenia | 93.91% | DL |
| 17 | drug-induced osteoporosis | 93.76% | DL |
| 18 | Ehlers-Danlos syndrome, fibronectinemic type | 93.11% | DL |
| 19 | renal osteodystrophy | 91.25% | DL |
| 20 | inherited thrombophilia | 91.01% | DL |

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
