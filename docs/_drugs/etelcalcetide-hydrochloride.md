---
layout: default
title: Etelcalcetide Hydrochloride
description: "Etelcalcetide Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 230
evidence_level: L5
indication_count: 50
---

# Etelcalcetide Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Etelcalcetide Hydrochloride |
| DrugBank ID | [DB12865](https://go.drugbank.com/drugs/DB12865) |
| Brand Names (EU) | Parsabiv |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.42% |

---

## Approved Indication (EMA)

Parsabiv is indicated for the treatment of secondary hyperparathyroidism (SHPT) in adult patients with chronic kidney disease (CKD) on haemodialysis therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hyperphosphatemia (disease) | 99.42% | DL |
| 2 | esophageal varices with bleeding | 99.35% | DL |
| 3 | esophageal varices without bleeding | 99.35% | DL |
| 4 | varicose disease | 99.09% | DL |
| 5 | glaucoma | 98.92% | DL |
| 6 | pancreatitis | 98.85% | DL |
| 7 | primary hyperoxaluria | 98.74% | DL |
| 8 | primary immunodeficiency syndrome due to p14 deficiency | 98.61% | DL |
| 9 | severe congenital neutropenia | 97.92% | DL |
| 10 | Barth syndrome | 97.84% | DL |
| 11 | familial apolipoprotein C-II deficiency | 97.64% | DL |
| 12 | autosomal recessive severe congenital neutropenia due to JAGN1 deficiency | 97.46% | DL |
| 13 | cyclic hematopoiesis | 97.44% | DL |
| 14 | Steel syndrome | 97.40% | DL |
| 15 | familial hyperphosphatemic tumoral calcinosis/hyperphosphatemic hyperostosis syndrome | 97.40% | DL |
| 16 | tumoral calcinosis, hyperphosphatemic, familial | 97.31% | DL |
| 17 | autosomal recessive severe congenital neutropenia due to G6PC3 deficiency | 97.11% | DL |
| 18 | autosomal recessive severe congenital neutropenia due to CSF3R deficiency | 97.05% | DL |
| 19 | autosomal recessive severe congenital neutropenia due to CXCR2 deficiency | 96.93% | DL |
| 20 | X-linked severe congenital neutropenia | 96.80% | DL |

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
