---
layout: default
title: Human Thrombin
description: "Human Thrombin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 280
evidence_level: L5
indication_count: 50
---

# Human Thrombin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Human Thrombin |
| DrugBank ID | [DB11571](https://go.drugbank.com/drugs/DB11571) |
| Brand Names (EU) | Human thrombin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.95% |

---

## Approved Indication (EMA)

TachoSil is indicated in adults and children from 1 month of age for supportive treatment in surgery for improvement of haemostasis, to promote tissue sealing and for suture support in vascular surgery where standard techniques are insufficient. TachoSil is indicated in adults for supportive sealing of the dura mater to prevent postoperative cerebrospinal leakage following neurological surgery (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 96.95% | DL |
| 2 | Glanzmann thrombasthenia | 96.64% | DL |
| 3 | pseudo-von Willebrand disease | 96.52% | DL |
| 4 | non-syndromic esophageal malformation | 91.68% | DL |
| 5 | hemorrhagic disorder due to a constitutional thrombocytopenia | 91.66% | DL |
| 6 | bleeding diathesis due to a collagen receptor defect | 91.55% | DL |
| 7 | Scott syndrome | 91.50% | DL |
| 8 | esophageal disease | 86.54% | DL |
| 9 | fetal and neonatal alloimmune thrombocytopenia | 86.21% | DL |
| 10 | platelet-type bleeding disorder | 86.13% | DL |
| 11 | hemophilia | 83.72% | DL |
| 12 | hereditary thrombocytosis with transverse limb defect | 83.66% | DL |
| 13 | flood factor deficiency | 83.63% | DL |
| 14 | familial thrombomodulin anomalies | 83.61% | DL |
| 15 | acquired coagulation factor deficiency | 83.45% | DL |
| 16 | severe nonproliferative diabetic retinopathy | 83.11% | DL |
| 17 | thrombocytopenia due to immune destruction | 83.08% | DL |
| 18 | Ehlers-Danlos syndrome, fibronectinemic type | 82.35% | DL |
| 19 | congenital factor V deficiency | 81.69% | DL |
| 20 | neonatal thrombocytopenia | 81.40% | DL |

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
