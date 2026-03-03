---
layout: default
title: Rituximab
description: "Rituximab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 501
evidence_level: L5
indication_count: 52
---

# Rituximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rituximab |
| DrugBank ID | [DB00073](https://go.drugbank.com/drugs/DB00073) |
| Brand Names (EU) | Blitzima, Ituxredi, MabThera |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 96.08% |

---

## Approved Indication (EMA)

MabThera is indicated in adults for the following indications: Non Hodgkin’s lymphoma (NHL) MabThera is indicated for the treatment of previously untreated adult patients with stage III?IV follicular lymphoma in combination with chemotherapy. MabThera maintenance therapy is indicated for the treatment of adult follicular lymphoma patients responding to induction therapy. MabThera monotherapy is indicated for treatment of adult patients with stage III?IV follicular lymphoma who are chemoresistant

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | follicular lymphoma | 96.08% | DL |
| 2 | Richter syndrome | 95.26% | DL |
| 3 | acute lymphoblastic/lymphocytic leukemia | 94.82% | DL |
| 4 | mantle cell lymphoma | 94.72% | DL |
| 5 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 93.57% | DL |
| 6 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 93.57% | DL |
| 7 | metastatic neoplasm | 93.29% | DL |
| 8 | malignant spiradenoma | 93.15% | DL |
| 9 | neoplasm of mature B-cells | 92.77% | DL |
| 10 | small intestinal Burkitt lymphoma | 92.65% | DL |
| 11 | small intestinal mucosa-associated lymphoid tissue lymphoma | 92.33% | DL |
| 12 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 92.27% | DL |
| 13 | breast mucosa-associated lymphoid tissue lymphoma | 92.19% | DL |
| 14 | B-cell neoplasm | 92.17% | DL |
| 15 | tonsillar lymphoma | 92.07% | DL |
| 16 | Langerhans cell histiocytosis | 91.63% | DL |
| 17 | lymphoma, non-Hodgkin, familial | 90.51% | DL |
| 18 | follicular lymphoma, susceptibility to, 1 | 90.28% | DL |
| 19 | lymphoma | 89.31% | DL |
| 20 | histiocytic and dendritic cell neoplasm | 89.03% | DL |

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
