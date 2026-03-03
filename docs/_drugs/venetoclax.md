---
layout: default
title: Venetoclax
description: "Venetoclax drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 628
evidence_level: L5
indication_count: 50
---

# Venetoclax
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Venetoclax |
| DrugBank ID | [DB11581](https://go.drugbank.com/drugs/DB11581) |
| Brand Names (EU) | Venclyxto |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.68% |

---

## Approved Indication (EMA)

Venclyxto in combination with obinutuzumab is indicated for the treatment of adult patients with previously untreated chronic lymphocytic leukaemia (CLL) (see section 5.1). Venclyxto in combination with rituximab is indicated for the treatment of adult patients with CLL who have received at least one prior therapy. Venclyxto monotherapy is indicated for the treatment of CLL:  in the presence of 17p deletion or TP53 mutation in adult patients who are unsuitable for or have failed a B cell recepto

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute lymphoblastic/lymphocytic leukemia | 99.68% | DL |
| 2 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.55% | DL |
| 3 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.55% | DL |
| 4 | Richter syndrome | 99.51% | DL |
| 5 | Hodgkins lymphoma | 99.51% | DL |
| 6 | myeloid leukemia | 99.47% | DL |
| 7 | chronic myelogenous leukemia, BCR-ABL1 positive | 99.36% | DL |
| 8 | Ewing sarcoma | 99.21% | DL |
| 9 | follicular lymphoma | 99.15% | DL |
| 10 | metastatic neoplasm | 99.14% | DL |
| 11 | malignant spiradenoma | 99.12% | DL |
| 12 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 99.08% | DL |
| 13 | acute myeloid leukemia with CEBPA somatic mutations | 99.06% | DL |
| 14 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 99.05% | DL |
| 15 | salivary gland type cancer of the breast | 98.96% | DL |
| 16 | breast papillomatosis | 98.87% | DL |
| 17 | bulbar polio | 98.82% | DL |
| 18 | breast lipoma | 98.82% | DL |
| 19 | benign neoplasm of male breast | 98.81% | DL |
| 20 | diabetic mastopathy | 98.81% | DL |

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
