---
layout: default
title: Larotrectinib Sulfate
description: "Larotrectinib Sulfate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 330
evidence_level: L5
indication_count: 50
---

# Larotrectinib Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Larotrectinib Sulfate |
| DrugBank ID | [DB14723](https://go.drugbank.com/drugs/DB14723) |
| Brand Names (EU) | Vitrakvi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.24% |

---

## Approved Indication (EMA)

Vitrakvi as monotherapy is indicated for the treatment of adult and paediatric patients with solid tumours that display a Neurotrophic Tyrosine Receptor Kinase (NTRK) gene fusion,  who have a disease that is locally advanced, metastatic or where surgical resection is likely to result in severe morbidity, and who have no satisfactory treatment options.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 99.24% | DL |
| 2 | HER2 positive breast carcinoma | 99.14% | DL |
| 3 | cytomegalovirus infection | 99.00% | DL |
| 4 | infectious bovine rhinotracheitis | 98.86% | DL |
| 5 | malignant catarrh | 98.86% | DL |
| 6 | progesterone-receptor negative breast cancer | 98.66% | DL |
| 7 | normal breast-like subtype of breast carcinoma | 98.63% | DL |
| 8 | progesterone-receptor positive breast cancer | 98.63% | DL |
| 9 | breast tumor luminal A or B | 98.61% | DL |
| 10 | thrombocytopenia | 98.56% | DL |
| 11 | pulmonary hypertension | 98.44% | DL |
| 12 | marcothrombocytopenia with mitral valve insufficiency | 98.33% | DL |
| 13 | hereditary thrombocytopenia with normal platelets | 98.32% | DL |
| 14 | transient neonatal thrombocytopenia | 98.27% | DL |
| 15 | dense granule disease | 98.23% | DL |
| 16 | amyotrophic lateral sclerosis | 98.23% | DL |
| 17 | kyphoscoliotic heart disease | 98.22% | DL |
| 18 | homozygous familial hypercholesterolemia | 98.18% | DL |
| 19 | amenorrhea (disease) | 98.14% | DL |
| 20 | hyperthyroidism | 98.06% | DL |

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
