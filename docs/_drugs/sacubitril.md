---
layout: default
title: Sacubitril
description: "Sacubitril drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 514
evidence_level: L5
indication_count: 50
---

# Sacubitril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sacubitril |
| DrugBank ID | [DB09292](https://go.drugbank.com/drugs/DB09292) |
| Brand Names (EU) | Sacubitril |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.58% |

---

## Approved Indication (EMA)

Paediatric heart failure Neparvis is indicated in children and adolescents aged one year or older for treatment of symptomatic chronic heart failure with left ventricular systolic dysfunction (see section 5.1). Adult heart failure Neparvis is indicated in adult patients for treatment of symptomatic chronic heart failure with reduced&nbsp;ejection fraction (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | brain small vessel disease 1 with or without ocular anomalies | 99.58% | DL |
| 2 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 99.57% | DL |
| 3 | diabetic nephropathy | 99.50% | DL |
| 4 | rheumatoid arthritis | 99.35% | DL |
| 5 | hemoglobinopathy | 99.18% | DL |
| 6 | sclerosing cholangitis | 98.92% | DL |
| 7 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.92% | DL |
| 8 | homozygous familial hypercholesterolemia | 98.87% | DL |
| 9 | partial deletion of the short arm of chromosome 16 | 98.85% | DL |
| 10 | beta-thalassemia with other manifestations | 98.83% | DL |
| 11 | blindness (disorder) | 98.80% | DL |
| 12 | pyropoikilocytosis, hereditary | 98.78% | DL |
| 13 | migraine disorder | 98.75% | DL |
| 14 | migraine with brainstem aura | 98.65% | DL |
| 15 | brachydactyly-syndactyly syndrome | 98.65% | DL |
| 16 | pyruvate kinase deficiency of red cells | 98.64% | DL |
| 17 | hemolytic anemia due to glucophosphate isomerase deficiency | 98.63% | DL |
| 18 | gout | 98.60% | DL |
| 19 | postmenopausal osteoporosis | 98.56% | DL |
| 20 | myocardial infarction | 98.49% | DL |

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
