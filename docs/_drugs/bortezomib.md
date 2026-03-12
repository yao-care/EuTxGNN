---
layout: default
title: Bortezomib
description: "Bortezomib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 86
evidence_level: L5
indication_count: 50
---

# Bortezomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bortezomib |
| DrugBank ID | [DB00188](https://go.drugbank.com/drugs/DB00188) |
| Brand Names (EU) | Velcade |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.10% |

---

## Approved Indication (EMA)

Velcade as monotherapy or in combination with pegylated liposomal doxorubicin or dexamethasone is indicated for the treatment of adult patients with progressive multiple myeloma who have received at least 1 prior therapy and who have already undergone or are unsuitable for haematopoietic stem cell transplantation. Velcade in combination with melphalan and prednisone is indicated for the treatment of adult patients with previously untreated multiple myeloma who are not eligible for high dose chem

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | vertebral anomalies and variable endocrine and T-cell dysfunction | 96.10% | DL |
| 2 | ganglioneuroblastoma (disease) | 96.01% | DL |
| 3 | retroperitoneal neoplasm | 95.64% | DL |
| 4 | neuroblastoma | 95.11% | DL |
| 5 | mantle cell lymphoma | 85.13% | DL |
| 6 | Hodgkins lymphoma | 85.09% | DL |
| 7 | myeloid leukemia | 83.77% | DL |
| 8 | lymphoma, non-Hodgkin, familial | 83.59% | DL |
| 9 | lymphosarcoma | 81.87% | DL |
| 10 | colon adenocarcinoma | 79.12% | DL |
| 11 | lymph node cancer | 77.96% | DL |
| 12 | dermatofibrosarcoma protuberans | 77.01% | DL |
| 13 | B-cell neoplasm | 76.99% | DL |
| 14 | primary organ-specific lymphoma | 72.60% | DL |
| 15 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 71.17% | DL |
| 16 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 71.17% | DL |
| 17 | acute lymphoblastic/lymphocytic leukemia | 69.96% | DL |
| 18 | Ewing sarcoma | 69.72% | DL |
| 19 | primary cutaneous T-cell non-Hodgkin lymphoma | 68.75% | DL |
| 20 | composite lymphoma | 67.94% | DL |

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
