---
layout: default
title: Pegvisomant
description: "Pegvisomant drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 449
evidence_level: L5
indication_count: 51
---

# Pegvisomant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pegvisomant |
| DrugBank ID | [DB00082](https://go.drugbank.com/drugs/DB00082) |
| Brand Names (EU) | Somavert |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.63% |

---

## Approved Indication (EMA)

Treatment of adult patients with acromegaly who have had an inadequate response to surgery and/or radiation therapy and in whom an appropriate medical treatment with somatostatin analogues did not normalize IGF-I concentrations or was not tolerated. Treatment of adult patients with acromegaly who have had an inadequate response to surgery and/or radiation therapy and in whom an appropriate medical treatment with somatostatin analogues did not normalize IGF -I concentrations or was not tolerated.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | borderline ovarian serous tumor | 98.63% | DL |
| 2 | rete ovarii cystadenoma | 98.60% | DL |
| 3 | ovarian papillary cystadenoma | 98.60% | DL |
| 4 | pyelonephritis | 98.57% | DL |
| 5 | malignant ovarian Brenner tumor | 98.56% | DL |
| 6 | aleukemic mast cell leukemia | 98.56% | DL |
| 7 | ovarian mucinous cystadenofibroma | 98.54% | DL |
| 8 | ovarian benign neoplasm | 98.54% | DL |
| 9 | mucinous ovarian cystadenoma | 98.53% | DL |
| 10 | ovarian surface papilloma | 98.51% | DL |
| 11 | serous neoplasm | 98.47% | DL |
| 12 | mucinous ovarian cancer | 98.18% | DL |
| 13 | ovarian clear cell cancer | 97.95% | DL |
| 14 | mucosal melanoma | 97.74% | DL |
| 15 | benign shuddering attacks | 97.58% | DL |
| 16 | extrapyramidal and movement disease | 97.58% | DL |
| 17 | chronic tic disorder | 97.45% | DL |
| 18 | psychogenic movement disorders | 97.44% | DL |
| 19 | ovarian germ cell tumor | 97.34% | DL |
| 20 | primary orthostatic tremor | 97.30% | DL |

*Showing top 20 of 51 predictions.*

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
