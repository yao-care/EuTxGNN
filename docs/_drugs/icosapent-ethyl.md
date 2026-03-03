---
layout: default
title: Icosapent Ethyl
description: "Icosapent Ethyl drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 287
evidence_level: L5
indication_count: 51
---

# Icosapent Ethyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Icosapent Ethyl |
| DrugBank ID | [DB08887](https://go.drugbank.com/drugs/DB08887) |
| Brand Names (EU) | Vazkepa |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.09% |

---

## Approved Indication (EMA)

Indicated to reduce cardiovascular risk as an adjunct to statin therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hemoglobinopathy | 99.09% | DL |
| 2 | partial deletion of the short arm of chromosome 16 | 98.67% | DL |
| 3 | beta-thalassemia with other manifestations | 98.66% | DL |
| 4 | myocardial infarction | 98.60% | DL |
| 5 | hemolytic anemia due to glucophosphate isomerase deficiency | 98.55% | DL |
| 6 | pyruvate kinase deficiency of red cells | 98.44% | DL |
| 7 | pyropoikilocytosis, hereditary | 98.42% | DL |
| 8 | rheumatoid arthritis | 98.12% | DL |
| 9 | posterolateral myocardial infarction | 98.06% | DL |
| 10 | posteroinferior myocardial infarction | 98.06% | DL |
| 11 | septal myocardial infarction | 98.01% | DL |
| 12 | heart disease | 97.99% | DL |
| 13 | Jeune syndrome situs inversus | 97.92% | DL |
| 14 | Pierre Robin syndrome associated with a chromosomal anomaly | 97.86% | DL |
| 15 | pulmonary valve disease | 97.85% | DL |
| 16 | interventricular septum aneurysm | 97.85% | DL |
| 17 | orofacial clefting syndrome | 97.85% | DL |
| 18 | partial deletion of the long arm of chromosome 22 | 97.83% | DL |
| 19 | partial deletion of the long arm of chromosome 7 | 97.83% | DL |
| 20 | disorder of fucoglycosan synthesis | 97.83% | DL |

*Showing top 20 of 51 predictions.*

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
