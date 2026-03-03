---
layout: default
title: Selinexor
description: "Selinexor drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 521
evidence_level: L5
indication_count: 50
---

# Selinexor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Selinexor |
| DrugBank ID | [DB11942](https://go.drugbank.com/drugs/DB11942) |
| Brand Names (EU) | Nexpovio |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.22% |

---

## Approved Indication (EMA)

NEXPOVIO is indicated  in combination with bortezomib and dexamethasone for the treatment of adult patients with multiple myeloma who have received at least one prior therapy. in combination with dexamethasone for the treatment of multiple myeloma in adult patients who have received at least four prior therapies and whose disease is refractory to at least two proteasome inhibitors, two immunomodulatory agents and an anti-CD38 monoclonal antibody, and who have demonstrated disease progression on 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 99.22% | DL |
| 2 | HER2 positive breast carcinoma | 98.13% | DL |
| 3 | progesterone-receptor negative breast cancer | 97.20% | DL |
| 4 | progesterone-receptor positive breast cancer | 97.18% | DL |
| 5 | normal breast-like subtype of breast carcinoma | 97.18% | DL |
| 6 | breast tumor luminal A or B | 97.11% | DL |
| 7 | squamous cell lung carcinoma | 96.91% | DL |
| 8 | gestational trophoblastic neoplasm | 96.54% | DL |
| 9 | cervical neuroblastoma | 96.33% | DL |
| 10 | schwannoma of jugular foramen | 96.32% | DL |
| 11 | benign neoplasm of floor of mouth | 96.28% | DL |
| 12 | epiglottis neoplasm | 96.25% | DL |
| 13 | benign neoplasm of tongue | 96.24% | DL |
| 14 | benign neoplasm of hypopharynx | 96.24% | DL |
| 15 | benign neoplasm of buccal mucosa | 96.23% | DL |
| 16 | jugular foramen meningioma | 96.23% | DL |
| 17 | neoplasm of major salivary gland | 96.23% | DL |
| 18 | nasal cavity inverting papilloma | 96.22% | DL |
| 19 | vestibulocochlear nerve neoplasm | 96.21% | DL |
| 20 | inner ear neoplasm | 96.21% | DL |

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
