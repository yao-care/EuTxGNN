---
layout: default
title: Obinutuzumab
description: "Obinutuzumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 414
evidence_level: L5
indication_count: 50
---

# Obinutuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Obinutuzumab |
| DrugBank ID | [DB08935](https://go.drugbank.com/drugs/DB08935) |
| Brand Names (EU) | Gazyvaro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.47% |

---

## Approved Indication (EMA)

Chronic lymphocytic leukaemia (CLL)&nbsp;Gazyvaro in combination with chlorambucil is indicated for the treatment of adult patients with previously untreated chronic lymphocytic leukaemia (CLL) and with comorbidities making them unsuitable for full-dose fludarabine based therapy.&nbsp;&nbsp;Follicular Lymphoma (FL)&nbsp;&nbsp;Gazyvaro in combination with chemotherapy, followed by Gazyvaro maintenance therapy in patients achieving a response, is indicated for the treatment of patients with previo

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute lymphoblastic/lymphocytic leukemia | 99.47% | DL |
| 2 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.21% | DL |
| 3 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.21% | DL |
| 4 | follicular lymphoma | 99.18% | DL |
| 5 | Richter syndrome | 99.17% | DL |
| 6 | mantle cell lymphoma | 98.75% | DL |
| 7 | metastatic neoplasm | 98.51% | DL |
| 8 | malignant spiradenoma | 98.47% | DL |
| 9 | neoplasm of mature B-cells | 98.08% | DL |
| 10 | small intestinal Burkitt lymphoma | 97.84% | DL |
| 11 | Langerhans cell histiocytosis | 97.81% | DL |
| 12 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 97.76% | DL |
| 13 | small intestinal mucosa-associated lymphoid tissue lymphoma | 97.75% | DL |
| 14 | chronic lymphocytic leukemia/small lymphocytic lymphoma | 97.73% | DL |
| 15 | breast mucosa-associated lymphoid tissue lymphoma | 97.72% | DL |
| 16 | tonsillar lymphoma | 97.67% | DL |
| 17 | B-cell neoplasm | 97.19% | DL |
| 18 | follicular lymphoma, susceptibility to, 1 | 97.09% | DL |
| 19 | histiocytic and dendritic cell neoplasm | 96.62% | DL |
| 20 | childhood carcinoid tumor | 96.55% | DL |

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
