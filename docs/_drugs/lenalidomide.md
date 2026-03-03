---
layout: default
title: Lenalidomide
description: "Lenalidomide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 338
evidence_level: L5
indication_count: 51
---

# Lenalidomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lenalidomide |
| DrugBank ID | [DB00480](https://go.drugbank.com/drugs/DB00480) |
| Brand Names (EU) | Lenalidomide Mylan, Revlimid |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.49% |

---

## Approved Indication (EMA)

Multiple myeloma Revlimid as monotherapy is indicated for the maintenance treatment of adult patients with newly diagnosed multiple myeloma who have undergone autologous stem cell transplantation. Revlimid as combination therapy with dexamethasone, or bortezomib and dexamethasone, or melphalan and prednisone (see section 4.2) is indicated for the treatment of adult patients with previously untreated multiple myeloma who are not eligible for transplant. Revlimid in combination with dexamethasone 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myeloid leukemia | 99.49% | DL |
| 2 | myelodysplastic syndrome | 99.45% | DL |
| 3 | unclassified myelodysplastic syndrome | 99.43% | DL |
| 4 | refractory cytopenia of childhood | 99.35% | DL |
| 5 | aregenerative anemia | 99.32% | DL |
| 6 | severe congenital hypochromic anemia with ringed sideroblasts | 99.28% | DL |
| 7 | partial deletion of the long arm of chromosome 5 | 99.27% | DL |
| 8 | lymphosarcoma | 98.12% | DL |
| 9 | lymph node cancer | 97.82% | DL |
| 10 | blast phase chronic myelogenous leukemia, BCR-ABL1 positive | 96.74% | DL |
| 11 | ganglioneuroblastoma (disease) | 95.97% | DL |
| 12 | acute lymphoblastic leukemia (disease) | 95.93% | DL |
| 13 | vertebral anomalies and variable endocrine and T-cell dysfunction | 95.69% | DL |
| 14 | neuroblastoma | 95.56% | DL |
| 15 | retroperitoneal neoplasm | 95.48% | DL |
| 16 | indolent plasma cell myeloma | 94.83% | DL |
| 17 | plasma cell myeloma | 94.77% | DL |
| 18 | Ewing sarcoma | 93.73% | DL |
| 19 | acute lymphoblastic/lymphocytic leukemia | 92.67% | DL |
| 20 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 92.39% | DL |

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
