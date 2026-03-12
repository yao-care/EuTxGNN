---
layout: default
title: Reteplase
description: "reteplase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 490
evidence_level: L5
indication_count: 50
---

# Reteplase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Reteplase |
| DrugBank ID | [DB00015](https://go.drugbank.com/drugs/DB00015) |
| Brand Names (EU) | Rapilysin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Rapilysin is indicated for the thrombolytic treatment of suspected myocardial infarction with persistent ST elevation or recent left bundle branch block within 12 hours after the onset of acute-myocardial-infarction (AMI) symptoms.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myocardial infarction | 99.94% | DL |
| 2 | coronary thrombosis | 99.90% | DL |
| 3 | posteroinferior myocardial infarction | 99.90% | DL |
| 4 | posterolateral myocardial infarction | 99.90% | DL |
| 5 | septal myocardial infarction | 99.90% | DL |
| 6 | congenital coronary artery anomaly | 99.80% | DL |
| 7 | hemoglobinopathy | 99.72% | DL |
| 8 | coronary stenosis | 99.62% | DL |
| 9 | myocardial infarction (disease) | 99.59% | DL |
| 10 | heparin cofactor 2 deficiency | 99.51% | DL |
| 11 | partial deletion of the short arm of chromosome 16 | 99.30% | DL |
| 12 | beta-thalassemia with other manifestations | 99.26% | DL |
| 13 | antithrombin deficiency type 2 | 99.25% | DL |
| 14 | hemolytic anemia due to glucophosphate isomerase deficiency | 99.24% | DL |
| 15 | factor 5 excess with spontaneous thrombosis | 99.22% | DL |
| 16 | pyropoikilocytosis, hereditary | 99.19% | DL |
| 17 | pyruvate kinase deficiency of red cells | 99.12% | DL |
| 18 | thrombophilia | 99.07% | DL |
| 19 | pulmonary embolism (disease) | 98.14% | DL |
| 20 | primary release disorder of platelets | 95.78% | DL |

*Showing top 20 of 50 predictions.*

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
