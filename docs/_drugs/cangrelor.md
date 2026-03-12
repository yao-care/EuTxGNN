---
layout: default
title: Cangrelor
description: "Cangrelor drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 110
evidence_level: L5
indication_count: 50
---

# Cangrelor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cangrelor |
| DrugBank ID | [DB06441](https://go.drugbank.com/drugs/DB06441) |
| Brand Names (EU) | Kengrexal |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.44% |

---

## Approved Indication (EMA)

Kengrexal, co-administered with acetylsalicylic acid (ASA), is indicated for the reduction of thrombotic cardiovascular events in adult patients with coronary artery disease undergoing percutaneous coronary intervention (PCI) who have not received an oral P2Y12 inhibitor prior to the PCI procedure and in whom oral therapy with P2Y12 inhibitors is not feasible or desirable.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hemoglobinopathy | 98.44% | DL |
| 2 | myocardial infarction | 98.03% | DL |
| 3 | partial deletion of the short arm of chromosome 16 | 97.81% | DL |
| 4 | beta-thalassemia with other manifestations | 97.77% | DL |
| 5 | hemolytic anemia due to glucophosphate isomerase deficiency | 97.63% | DL |
| 6 | pyruvate kinase deficiency of red cells | 97.54% | DL |
| 7 | pyropoikilocytosis, hereditary | 97.38% | DL |
| 8 | posteroinferior myocardial infarction | 97.38% | DL |
| 9 | posterolateral myocardial infarction | 97.38% | DL |
| 10 | septal myocardial infarction | 97.31% | DL |
| 11 | rheumatoid arthritis | 97.27% | DL |
| 12 | coronary thrombosis | 97.23% | DL |
| 13 | myocardial infarction (disease) | 96.77% | DL |
| 14 | coronary stenosis | 96.72% | DL |
| 15 | thrombotic disease | 96.41% | DL |
| 16 | gout | 96.06% | DL |
| 17 | congenital coronary artery anomaly | 95.98% | DL |
| 18 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 95.58% | DL |
| 19 | postoperative ventricular dysfunction | 95.24% | DL |
| 20 | brachydactyly-syndactyly syndrome | 95.05% | DL |

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
