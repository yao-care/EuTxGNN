---
layout: default
title: Fingolimod
description: "Fingolimod drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 247
evidence_level: L5
indication_count: 50
---

# Fingolimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fingolimod |
| DrugBank ID | [DB08868](https://go.drugbank.com/drugs/DB08868) |
| Brand Names (EU) | Fingolimod |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.67% |

---

## Approved Indication (EMA)

Indicated as single disease modifying therapy in highly active relapsing remitting multiple sclerosis for the following groups of adult and paediatric patients aged 10 years and older: Patients with highly active disease despite a full and adequate course of treatment with at least one disease modifying therapy (for exceptions and information about washout periods see sections 4.4 and 5.1) or Patients with rapidly evolving severe relapsing remitting multiple sclerosis defined by 2 or more disabl

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 98.67% | DL |
| 2 | borderline ovarian serous tumor | 94.94% | DL |
| 3 | ovarian papillary cystadenoma | 94.62% | DL |
| 4 | malignant ovarian Brenner tumor | 94.59% | DL |
| 5 | rete ovarii cystadenoma | 94.57% | DL |
| 6 | serous neoplasm | 94.32% | DL |
| 7 | ovarian mucinous cystadenofibroma | 94.27% | DL |
| 8 | mucinous ovarian cystadenoma | 94.25% | DL |
| 9 | ovarian benign neoplasm | 94.22% | DL |
| 10 | ovarian surface papilloma | 94.05% | DL |
| 11 | Immunoerythromyeloid hypoplasia | 93.62% | DL |
| 12 | dermatofibrosarcoma protuberans | 93.53% | DL |
| 13 | non-severe combined immunodeficiency | 93.30% | DL |
| 14 | fibroblastic neoplasm | 92.61% | DL |
| 15 | mucinous ovarian cancer | 92.52% | DL |
| 16 | heart fibrosarcoma | 92.46% | DL |
| 17 | severe combined immunodeficiency (disease) | 92.28% | DL |
| 18 | conventional fibrosarcoma | 92.18% | DL |
| 19 | kidney fibrosarcoma | 91.97% | DL |
| 20 | low grade fibromyxoid sarcoma | 91.82% | DL |

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
