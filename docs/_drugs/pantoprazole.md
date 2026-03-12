---
layout: default
title: Pantoprazole
description: "Pantoprazole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 438
evidence_level: L5
indication_count: 50
---

# Pantoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pantoprazole |
| DrugBank ID | [DB00213](https://go.drugbank.com/drugs/DB00213) |
| Brand Names (EU) | Somac Control |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.87% |

---

## Approved Indication (EMA)

Short-term treatment of reflux symptoms (e.g. heartburn, acid regurgitation) in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | peptic esophagitis | 99.87% | DL |
| 2 | multiple endocrine neoplasia | 99.81% | DL |
| 3 | active peptic ulcer disease | 99.69% | DL |
| 4 | peptic ulcer perforation | 99.63% | DL |
| 5 | gastrojejunal ulcer | 99.63% | DL |
| 6 | duodenogastric reflux | 99.27% | DL |
| 7 | esophagitis (disease) | 99.24% | DL |
| 8 | duodenal obstruction | 99.21% | DL |
| 9 | duodenal ulcer (disease) | 99.18% | DL |
| 10 | acne (disease) | 98.35% | DL |
| 11 | gastric ulcer (disease) | 98.05% | DL |
| 12 | Zollinger-Ellison syndrome | 97.92% | DL |
| 13 | Smouldering systemic mastocytosis | 97.38% | DL |
| 14 | gastrin secretion abnormality | 96.77% | DL |
| 15 | lymphoadenopathic mastocytosis with eosinophilia | 96.60% | DL |
| 16 | gastroduodenitis | 96.47% | DL |
| 17 | peptic ulcer disease | 93.12% | DL |
| 18 | systemic mastocytosis | 92.63% | DL |
| 19 | abnormality of glucagon secretion | 84.85% | DL |
| 20 | leather-bottle stomach | 84.77% | DL |

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
