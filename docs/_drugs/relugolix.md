---
layout: default
title: Relugolix
description: "Relugolix drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 486
evidence_level: L5
indication_count: 50
---

# Relugolix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Relugolix |
| DrugBank ID | [DB11853](https://go.drugbank.com/drugs/DB11853) |
| Brand Names (EU) | Orgovyx |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.13% |

---

## Approved Indication (EMA)

Ryeqo is indicated in adult women of reproductive age for: - treatment of moderate to severe symptoms of uterine fibroids, - symptomatic treatment of endometriosis in women with a history of previous medical or surgical treatment for their endometriosis.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 96.13% | DL |
| 2 | Smouldering systemic mastocytosis | 96.11% | DL |
| 3 | systemic mastocytosis | 96.08% | DL |
| 4 | lymphoadenopathic mastocytosis with eosinophilia | 95.92% | DL |
| 5 | multiple endocrine neoplasia | 95.32% | DL |
| 6 | gastrin secretion abnormality | 94.95% | DL |
| 7 | leprosy | 94.53% | DL |
| 8 | hypertrichosis (disease) | 93.20% | DL |
| 9 | malformation syndrome with odontal and/or periodontal component | 93.04% | DL |
| 10 | syndrome with a Dandy-Walker malformation as major feature | 92.90% | DL |
| 11 | Ambras type hypertrichosis universalis congenita | 92.76% | DL |
| 12 | isolated genetic hair shaft abnormality | 92.72% | DL |
| 13 | Legionnaires' disease | 92.54% | DL |
| 14 | HIV infectious disease | 91.86% | DL |
| 15 | multidrug-resistant tuberculosis | 91.41% | DL |
| 16 | coronary artery disease | 91.32% | DL |
| 17 | Plasmodium falciparum malaria | 90.97% | DL |
| 18 | anomalous left coronary artery from the pulmonary artery | 90.94% | DL |
| 19 | abnormality of glucagon secretion | 90.69% | DL |
| 20 | simian immunodeficiency virus infection | 90.58% | DL |

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
