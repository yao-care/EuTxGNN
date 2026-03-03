---
layout: default
title: Eravacycline
description: "Eravacycline drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 219
evidence_level: L5
indication_count: 50
---

# Eravacycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eravacycline |
| DrugBank ID | [DB12329](https://go.drugbank.com/drugs/DB12329) |
| Brand Names (EU) | Xerava |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.85% |

---

## Approved Indication (EMA)

Xerava is indicated in adolescents from the age of 12 years weighing at least 50 kg, and in adults, for the treatment of complicated intra-abdominal infections (cIAI). Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 96.85% | DL |
| 2 | laryngotracheitis | 86.51% | DL |
| 3 | bronchial neoplasm (disease) | 85.97% | DL |
| 4 | conjunctivitis | 85.88% | DL |
| 5 | sclerosing cholangitis | 84.42% | DL |
| 6 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 77.54% | DL |
| 7 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 77.46% | DL |
| 8 | brain small vessel disease 1 with or without ocular anomalies | 76.50% | DL |
| 9 | diabetic nephropathy | 76.05% | DL |
| 10 | rheumatoid arthritis | 73.27% | DL |
| 11 | rhinitis | 72.99% | DL |
| 12 | pityriasis simplex | 72.64% | DL |
| 13 | obstructive lung disease | 72.27% | DL |
| 14 | irritable bowel syndrome | 71.68% | DL |
| 15 | infective urethral stricture | 71.63% | DL |
| 16 | conjunctivitis (disease) | 71.31% | DL |
| 17 | hyperthyroidism | 71.28% | DL |
| 18 | post-bacterial disorder | 70.39% | DL |
| 19 | postinfectious vasculitis | 70.22% | DL |
| 20 | Chagas cardiomyopathy | 69.72% | DL |

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
