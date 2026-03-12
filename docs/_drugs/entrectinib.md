---
layout: default
title: Entrectinib
description: "Entrectinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 214
evidence_level: L5
indication_count: 50
---

# Entrectinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Entrectinib |
| DrugBank ID | [DB11986](https://go.drugbank.com/drugs/DB11986) |
| Brand Names (EU) | Rozlytrek |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.58% |

---

## Approved Indication (EMA)

Rozlytrek as monotherapy is indicated for the treatment of adult and paediatric patients 12 years of age and older with solid tumours expressing a neurotrophic tyrosine receptor kinase (NTRK) gene fusion,  who have a disease that is locally advanced, metastatic or where surgical resection is likely to result in severe morbidity, and who have not received a prior NTRK inhibitor who have no satisfactory treatment options.  Rozlytrek as monotherapy is indicated for the treatment of adult patients w

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 98.58% | DL |
| 2 | amenorrhea (disease) | 98.37% | DL |
| 3 | thrombocytopenia | 98.11% | DL |
| 4 | cytomegalovirus infection | 97.97% | DL |
| 5 | pulmonary hypertension | 97.87% | DL |
| 6 | marcothrombocytopenia with mitral valve insufficiency | 97.80% | DL |
| 7 | hereditary thrombocytopenia with normal platelets | 97.79% | DL |
| 8 | female breast carcinoma | 97.76% | DL |
| 9 | transient neonatal thrombocytopenia | 97.76% | DL |
| 10 | infectious bovine rhinotracheitis | 97.74% | DL |
| 11 | malignant catarrh | 97.74% | DL |
| 12 | myeloid leukemia | 97.69% | DL |
| 13 | dense granule disease | 97.66% | DL |
| 14 | kyphoscoliotic heart disease | 97.51% | DL |
| 15 | HER2 positive breast carcinoma | 97.36% | DL |
| 16 | thrombotic disease | 97.00% | DL |
| 17 | hyperthyroidism | 97.00% | DL |
| 18 | collagenopathy | 96.64% | DL |
| 19 | lymphocytic hypereosinophilic syndrome | 96.56% | DL |
| 20 | platelet storage pool deficiency | 96.54% | DL |

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
