---
layout: default
title: Prasterone
description: "Prasterone drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 467
evidence_level: L5
indication_count: 51
---

# Prasterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Prasterone |
| DrugBank ID | [DB01708](https://go.drugbank.com/drugs/DB01708) |
| Brand Names (EU) | Intrarosa |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Intrarosa is indicated for the treatment of vulvar and vaginal atrophy in postmenopausal women having moderate to severe symptoms.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | heparin cofactor 2 deficiency | 99.99% | DL |
| 2 | factor 5 excess with spontaneous thrombosis | 99.98% | DL |
| 3 | antithrombin deficiency type 2 | 99.98% | DL |
| 4 | thrombophilia | 99.91% | DL |
| 5 | pediatric systemic lupus erythematosus | 99.25% | DL |
| 6 | severe nonproliferative diabetic retinopathy | 99.25% | DL |
| 7 | thrombophilia due to protein S deficiency, autosomal recessive | 99.13% | DL |
| 8 | scleroderma (disease) | 99.11% | DL |
| 9 | complement component 4a deficiency | 99.05% | DL |
| 10 | pseudo-von Willebrand disease | 99.01% | DL |
| 11 | primary release disorder of platelets | 99.01% | DL |
| 12 | acne (disease) | 98.54% | DL |
| 13 | anus disease | 97.79% | DL |
| 14 | granulomatous disease, chronic, autosomal recessive, 5 | 97.37% | DL |
| 15 | inflammatory bowel disease | 97.26% | DL |
| 16 | granulomatous disease with defect in neutrophil chemotaxis | 97.20% | DL |
| 17 | fetal and neonatal alloimmune thrombocytopenia | 97.05% | DL |
| 18 | peeling skin syndrome | 97.00% | DL |
| 19 | spondyloarthropathy, susceptibility to | 96.97% | DL |
| 20 | diabetic retinopathy | 96.90% | DL |

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
