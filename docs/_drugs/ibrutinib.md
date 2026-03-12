---
layout: default
title: Ibrutinib
description: "Ibrutinib drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 284
evidence_level: L5
indication_count: 52
---

# Ibrutinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ibrutinib |
| DrugBank ID | [DB09053](https://go.drugbank.com/drugs/DB09053) |
| Brand Names (EU) | Imbruvica |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 95.02% |

---

## Approved Indication (EMA)

Imbruvica in combination with rituximab, cyclophosphamide, doxorubicin, vincristine, and prednisolone (IMBRUVICA + R-CHOP) alternating with R-DHAP (or R-DHAOx) without Imbruvica, followed by Imbruvica monotherapy, is indicated for the treatment of adult patients with previously untreated mantle cell lymphoma (MCL) who would be eligible for autologous stem cell transplantation (ASCT).Imbruvica as a single agent is indicated for the treatment of adult patients with relapsed or refractory MCL.Imbru

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | mantle cell lymphoma | 95.02% | DL |
| 2 | polyclonal hypergammaglobulinemia | 91.75% | DL |
| 3 | monoclonal paraproteinemia disease | 91.16% | DL |
| 4 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 88.43% | DL |
| 5 | small intestinal mucosa-associated lymphoid tissue lymphoma | 88.36% | DL |
| 6 | small intestinal Burkitt lymphoma | 88.32% | DL |
| 7 | breast mucosa-associated lymphoid tissue lymphoma | 88.07% | DL |
| 8 | tonsillar lymphoma | 88.05% | DL |
| 9 | marginal zone lymphoma | 87.96% | DL |
| 10 | extracutaneous mastocytoma | 87.74% | DL |
| 11 | neoplasm of mature B-cells | 86.55% | DL |
| 12 | familial thrombocytosis | 85.84% | DL |
| 13 | lymphoma, non-Hodgkin, familial | 85.59% | DL |
| 14 | Richter syndrome | 85.26% | DL |
| 15 | macroglobulinemia | 84.90% | DL |
| 16 | B-cell neoplasm | 84.53% | DL |
| 17 | follicular lymphoma, susceptibility to, 1 | 83.55% | DL |
| 18 | lymphoplasmacytic lymphoma | 83.33% | DL |
| 19 | metastatic neoplasm | 83.10% | DL |
| 20 | malignant spiradenoma | 82.99% | DL |

*Showing top 20 of 52 predictions.*

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
