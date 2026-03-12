---
layout: default
title: Eptifibatide
description: "eptifibatide drug repurposing predictions from TxGNN. Evidence level L4 with 51 predicted indications."
parent: Preclinical Evidence (L4)
nav_order: 217
evidence_level: L4
indication_count: 51
---

# Eptifibatide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eptifibatide |
| DrugBank ID | [DB00063](https://go.drugbank.com/drugs/DB00063) |
| Brand Names (EU) | Eptifibatide Accord, Integrilin |
| Evidence Level | L4 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Integrilin is intended for use with acetylsalicylic acid and unfractionated heparin. Integrilin is indicated for the prevention of early myocardial infarction in patients presenting with unstable angina or non-Q-wave myocardial infarction with the last episode of chest pain occurring within 24 hours and with ECG changes and / or elevated cardiac enzymes. Patients most likely to benefit from Integrilin treatment are those at high risk of developing myocardial infarction within the first 3-4 days 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.99% | DL |
| 2 | sickle cell-hemoglobin d disease syndrome | 99.98% | DL |
| 3 | sickle cell-beta-thalassemia disease syndrome | 99.98% | DL |
| 4 | sickle cell-hemoglobin c disease syndrome | 99.98% | DL |
| 5 | sickle cell-hemoglobin E disease syndrome | 99.98% | DL |
| 6 | hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | 99.98% | DL |
| 7 | hemoglobinopathy | 99.98% | DL |
| 8 | female breast carcinoma | 99.97% | DL |
| 9 | beta-thalassemia with other manifestations | 99.97% | DL |
| 10 | partial deletion of the short arm of chromosome 16 | 99.96% | DL |
| 11 | pyropoikilocytosis, hereditary | 99.96% | DL |
| 12 | hemolytic anemia due to glucophosphate isomerase deficiency | 99.96% | DL |
| 13 | brachydactyly-syndactyly syndrome | 99.96% | DL |
| 14 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.95% | DL |
| 15 | pyruvate kinase deficiency of red cells | 99.95% | DL |
| 16 | sickle cell disease and related diseases | 99.94% | DL |
| 17 | sickle cell anemia | 99.89% | DL |
| 18 | hereditary persistence of fetal hemoglobin | 99.86% | DL |
| 19 | gout | 99.86% | DL |
| 20 | myocardial infarction | 99.85% | DL |

*Showing top 20 of 51 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| hemoglobinopathy | L4 | 1 | 0 | AI prediction only |

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
