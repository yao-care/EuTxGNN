---
layout: default
title: Alemtuzumab
description: "Alemtuzumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 26
evidence_level: L5
indication_count: 50
---

# Alemtuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Alemtuzumab |
| DrugBank ID | [DB00087](https://go.drugbank.com/drugs/DB00087) |
| Brand Names (EU) | Lemtrada |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.51% |

---

## Approved Indication (EMA)

Lemtrada is indicated for adult patients with relapsing-remitting multiple sclerosis (RRMS) with active disease defined by clinical or imaging features.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 96.51% | DL |
| 2 | hepatic infarction | 94.44% | DL |
| 3 | syndrome with combined immunodeficiency | 93.73% | DL |
| 4 | hepatic veno-occlusive disease | 93.14% | DL |
| 5 | kidney pelvis sarcomatoid transitional cell carcinoma | 93.09% | DL |
| 6 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 92.93% | DL |
| 7 | prostatic urethra urothelial carcinoma | 92.85% | DL |
| 8 | renal pelvis papillary urothelial carcinoma | 92.81% | DL |
| 9 | peliosis hepatis | 92.20% | DL |
| 10 | hemophagocytic syndrome associated with an infection | 89.93% | DL |
| 11 | acquired hemophagocytic lymphohistiocytosis associated with malignant disease | 89.93% | DL |
| 12 | stone in bladder diverticulum | 87.56% | DL |
| 13 | non-severe combined immunodeficiency | 87.56% | DL |
| 14 | chromhidrosis | 87.39% | DL |
| 15 | severe combined immunodeficiency (disease) | 86.73% | DL |
| 16 | cervical neuroblastoma | 86.71% | DL |
| 17 | schwannoma of jugular foramen | 86.64% | DL |
| 18 | benign neoplasm of tongue | 86.42% | DL |
| 19 | benign neoplasm of hypopharynx | 86.29% | DL |
| 20 | benign neoplasm of buccal mucosa | 86.27% | DL |

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
