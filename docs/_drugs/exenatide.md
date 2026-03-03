---
layout: default
title: Exenatide
description: "Exenatide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 235
evidence_level: L5
indication_count: 50
---

# Exenatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Exenatide |
| DrugBank ID | [DB01276](https://go.drugbank.com/drugs/DB01276) |
| Brand Names (EU) | Byetta |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.21% |

---

## Approved Indication (EMA)

Byetta is indicated for treatment of type-2 diabetes mellitus in combination with:  metformin; sulphonylureas; thiazolidinediones; metformin and a sulphonylurea; metformin and a thiazolidinedione;  in adults who have not achieved adequate glycaemic control on maximally tolerated doses of these oral therapies. Byetta is also indicated as adjunctive therapy to basal insulin with or without metformin and / or pioglitazone in adults who have not achieved adequate glycaemic control with these agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary hereditary glaucoma | 96.21% | DL |
| 2 | open-angle glaucoma | 95.44% | DL |
| 3 | hypotrichosis simplex of the scalp | 92.85% | DL |
| 4 | congenital hypotrichosis milia | 92.42% | DL |
| 5 | headache disorder | 91.79% | DL |
| 6 | trigeminal autonomic cephalalgia | 90.72% | DL |
| 7 | diffuse alopecia areata | 90.72% | DL |
| 8 | alopecia | 90.20% | DL |
| 9 | obsolete rare pulmonary disease | 89.49% | DL |
| 10 | common cold | 86.79% | DL |
| 11 | glaucoma 1, open angle | 86.67% | DL |
| 12 | filariasis | 86.65% | DL |
| 13 | hyperplasia | 86.54% | DL |
| 14 | selective pituitary resistance to thyroid hormone | 85.15% | DL |
| 15 | gout | 85.14% | DL |
| 16 | thyroid gland disease | 85.13% | DL |
| 17 | toxic diffuse goiter | 83.56% | DL |
| 18 | digitalis poisoning | 83.51% | DL |
| 19 | renin-angiotensin-aldosterone system-blocker-induced angioedema | 83.35% | DL |
| 20 | thyroid crisis (disease) | 82.38% | DL |

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
