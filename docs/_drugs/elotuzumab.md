---
layout: default
title: Elotuzumab
description: "Elotuzumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 201
evidence_level: L5
indication_count: 50
---

# Elotuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Elotuzumab |
| DrugBank ID | [DB06317](https://go.drugbank.com/drugs/DB06317) |
| Brand Names (EU) | Empliciti |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.62% |

---

## Approved Indication (EMA)

Empliciti is indicated in combination with lenalidomide and dexamethasone for the treatment of multiple myeloma in adult patients who have received at least one prior therapy (see sections 4.2 and 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | indolent plasma cell myeloma | 98.62% | DL |
| 2 | plasma cell myeloma | 98.00% | DL |
| 3 | lipoma of colon | 76.32% | DL |
| 4 | cecum villous adenoma | 76.07% | DL |
| 5 | colonic lymphangioma | 75.67% | DL |
| 6 | colon leiomyoma | 75.35% | DL |
| 7 | rectosigmoid junction neoplasm | 75.30% | DL |
| 8 | cecum neuroendocrine tumor G1 | 75.28% | DL |
| 9 | cecal disease | 74.83% | DL |
| 10 | benign neoplasm of cecum | 74.70% | DL |
| 11 | cavernous hemangioma of colon | 73.91% | DL |
| 12 | uterine ligament adenocarcinoma | 73.22% | DL |
| 13 | endocervical carcinoma | 70.79% | DL |
| 14 | adenoid cystic carcinoma of the cervix uteri | 70.61% | DL |
| 15 | uterine ligament serous adenocarcinoma | 70.48% | DL |
| 16 | bronchitis | 70.25% | DL |
| 17 | bronchial neoplasm (disease) | 69.57% | DL |
| 18 | minimally invasive lung adenocarcinoma | 69.03% | DL |
| 19 | signet ring cell variant cervical mucinous adenocarcinoma | 68.70% | DL |
| 20 | intestinal variant cervical mucinous adenocarcinoma | 68.50% | DL |

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
