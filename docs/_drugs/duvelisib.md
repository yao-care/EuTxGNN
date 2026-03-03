---
layout: default
title: Duvelisib
description: "Duvelisib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 190
evidence_level: L5
indication_count: 50
---

# Duvelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Duvelisib |
| DrugBank ID | [DB11952](https://go.drugbank.com/drugs/DB11952) |
| Brand Names (EU) | Copiktra |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Copiktra monotherapy is indicated for the treatment of adult patients with:   Relapsed or refractory chronic lymphocytic leukaemia (CLL) after at least two prior therapies.  Follicular lymphoma (FL) that is refractory to at least two prior  systemic therapies.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Hodgkins lymphoma | 99.94% | DL |
| 2 | myeloid leukemia | 99.94% | DL |
| 3 | follicular lymphoma | 99.92% | DL |
| 4 | acute lymphoblastic/lymphocytic leukemia | 99.91% | DL |
| 5 | chronic myelogenous leukemia, BCR-ABL1 positive | 99.91% | DL |
| 6 | Ewing sarcoma | 99.88% | DL |
| 7 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.87% | DL |
| 8 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.87% | DL |
| 9 | mantle cell lymphoma | 99.84% | DL |
| 10 | ganglioneuroblastoma (disease) | 99.82% | DL |
| 11 | B-cell neoplasm | 99.80% | DL |
| 12 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.80% | DL |
| 13 | retroperitoneal neoplasm | 99.80% | DL |
| 14 | Richter syndrome | 99.79% | DL |
| 15 | neuroblastoma | 99.78% | DL |
| 16 | blast phase chronic myelogenous leukemia, BCR-ABL1 positive | 99.73% | DL |
| 17 | neoplasm of mature B-cells | 99.73% | DL |
| 18 | small intestinal Burkitt lymphoma | 99.67% | DL |
| 19 | lymphoma, non-Hodgkin, familial | 99.66% | DL |
| 20 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 99.66% | DL |

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
