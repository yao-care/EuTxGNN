---
layout: default
title: Idelalisib
description: "Idelalisib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 290
evidence_level: L5
indication_count: 50
---

# Idelalisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Idelalisib |
| DrugBank ID | [DB09054](https://go.drugbank.com/drugs/DB09054) |
| Brand Names (EU) | Zydelig |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Zydelig is indicated in combination with an anti?CD20 monoclonal antibody (rituximab or ofatumumab) for the treatment of adult patients with chronic lymphocytic leukaemia (CLL):  who have received at least one prior therapy, or as first line treatment in the presence of 17p deletion or TP53 mutation in patients who are not eligible for any other therapies.  Zydelig is indicated as monotherapy for the treatment of adult patients with follicular lymphoma (FL) that is refractory to two prior lines 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | follicular lymphoma | 99.88% | DL |
| 2 | mantle cell lymphoma | 99.84% | DL |
| 3 | Hodgkins lymphoma | 99.79% | DL |
| 4 | acute lymphoblastic/lymphocytic leukemia | 99.79% | DL |
| 5 | B-cell neoplasm | 99.79% | DL |
| 6 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.69% | DL |
| 7 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.69% | DL |
| 8 | lymphoma, non-Hodgkin, familial | 99.62% | DL |
| 9 | Richter syndrome | 99.59% | DL |
| 10 | neoplasm of mature B-cells | 99.59% | DL |
| 11 | myeloid leukemia | 99.55% | DL |
| 12 | chronic myelogenous leukemia, BCR-ABL1 positive | 99.53% | DL |
| 13 | small intestinal Burkitt lymphoma | 99.51% | DL |
| 14 | colon adenocarcinoma | 99.51% | DL |
| 15 | small intestinal mucosa-associated lymphoid tissue lymphoma | 99.48% | DL |
| 16 | thyroid gland mucosa-associated lymphoid tissue lymphoma | 99.47% | DL |
| 17 | breast mucosa-associated lymphoid tissue lymphoma | 99.46% | DL |
| 18 | tonsillar lymphoma | 99.45% | DL |
| 19 | follicular lymphoma, susceptibility to, 1 | 99.36% | DL |
| 20 | MALT lymphoma | 99.27% | DL |

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
