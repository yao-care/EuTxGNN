---
layout: default
title: Tivozanib
description: "Tivozanib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 589
evidence_level: L5
indication_count: 50
---

# Tivozanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tivozanib |
| DrugBank ID | [DB11800](https://go.drugbank.com/drugs/DB11800) |
| Brand Names (EU) | Fotivda |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.81% |

---

## Approved Indication (EMA)

Fotivda is indicated for the first line treatment of adult patients with advanced renal cell carcinoma (RCC) and for adult patients who are VEGFR and mTOR pathway inhibitor-naïve following disease progression after one prior treatment with cytokine therapy for advanced RCC. Treatment of advanced renal cell carcinoma.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | endocervical carcinoma | 99.81% | DL |
| 2 | uterine ligament adenocarcinoma | 99.80% | DL |
| 3 | adenoid cystic carcinoma of the cervix uteri | 99.80% | DL |
| 4 | uterine ligament serous adenocarcinoma | 99.79% | DL |
| 5 | signet ring cell variant cervical mucinous adenocarcinoma | 99.77% | DL |
| 6 | cervical adenosquamous carcinoma, glassy cell variant | 99.77% | DL |
| 7 | uterine ligament endometrioid adenocarcinoma | 99.77% | DL |
| 8 | uterine ligament mucinous adenocarcinoma | 99.77% | DL |
| 9 | intestinal variant cervical mucinous adenocarcinoma | 99.77% | DL |
| 10 | cervical mucinous adenocarcinoma, minimal deviation variant | 99.76% | DL |
| 11 | endocervical type cervical mucinous adenocarcinoma | 99.76% | DL |
| 12 | uterine ligament clear cell adenocarcinoma | 99.76% | DL |
| 13 | nasopharyngeal teratoma | 99.61% | DL |
| 14 | mesonephric adenocarcinoma | 99.59% | DL |
| 15 | pre-malignant neoplasm | 99.56% | DL |
| 16 | odontogenic cyst | 99.56% | DL |
| 17 | epiglottis neoplasm | 99.51% | DL |
| 18 | tumor of testis and paratestis | 99.51% | DL |
| 19 | benign neoplasm of floor of mouth | 99.50% | DL |
| 20 | benign neoplasm of hypopharynx | 99.50% | DL |

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
