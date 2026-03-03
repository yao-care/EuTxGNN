---
layout: default
title: Zanubrutinib
description: "Zanubrutinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 644
evidence_level: L5
indication_count: 50
---

# Zanubrutinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Zanubrutinib |
| DrugBank ID | [DB15035](https://go.drugbank.com/drugs/DB15035) |
| Brand Names (EU) | Brukinsa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.65% |

---

## Approved Indication (EMA)

Brukinsa&nbsp;as monotherapy is indicated for the treatment of adult patients with Waldenström’s macroglobulinaemia (WM) who have received at least one prior therapy, or in first line treatment for patients unsuitable for chemo-immunotherapy. Brukinsa&nbsp;as monotherapy is indicated for the treatment of adult patients with marginal zone lymphoma (MZL) who have received at least one prior anti-CD20-based therapy. Brukinsa&nbsp;as monotherapy is indicated for the treatment of adult patients with 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myeloid leukemia | 99.65% | DL |
| 2 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.38% | DL |
| 3 | ganglioneuroblastoma (disease) | 99.36% | DL |
| 4 | retroperitoneal neoplasm | 99.30% | DL |
| 5 | Ewing sarcoma | 99.27% | DL |
| 6 | neuroblastoma | 99.21% | DL |
| 7 | chronic myelogenous leukemia, BCR-ABL1 positive | 98.60% | DL |
| 8 | lymphosarcoma | 98.11% | DL |
| 9 | blast phase chronic myelogenous leukemia, BCR-ABL1 positive | 98.09% | DL |
| 10 | lymphoma, non-Hodgkin, familial | 98.00% | DL |
| 11 | acute lymphoblastic/lymphocytic leukemia | 97.86% | DL |
| 12 | mantle cell lymphoma | 97.70% | DL |
| 13 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 97.69% | DL |
| 14 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 97.69% | DL |
| 15 | lymph node cancer | 97.42% | DL |
| 16 | colon adenocarcinoma | 97.35% | DL |
| 17 | B-cell neoplasm | 97.05% | DL |
| 18 | plasmacytoma | 96.90% | DL |
| 19 | primary cutaneous T-cell non-Hodgkin lymphoma | 96.66% | DL |
| 20 | primary organ-specific lymphoma | 96.57% | DL |

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
