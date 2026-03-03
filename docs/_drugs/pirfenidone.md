---
layout: default
title: Pirfenidone
description: "Pirfenidone drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 460
evidence_level: L5
indication_count: 52
---

# Pirfenidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pirfenidone |
| DrugBank ID | [DB04951](https://go.drugbank.com/drugs/DB04951) |
| Brand Names (EU) | Esbriet, Pirfenidone axunio (previously Pirfenidone AET) |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Pirfenidone AET is indicated in adults for the treatment of mild to moderate idiopathic pulmonary fibrosis (IPF).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | extracutaneous mastocytoma | 99.71% | DL |
| 2 | dermatofibrosarcoma protuberans | 99.41% | DL |
| 3 | aggressive systemic mastocytosis | 99.33% | DL |
| 4 | heart fibrosarcoma | 99.29% | DL |
| 5 | conventional fibrosarcoma | 99.26% | DL |
| 6 | autosomal recessive familial Mediterranean fever | 99.25% | DL |
| 7 | kidney fibrosarcoma | 99.24% | DL |
| 8 | hepatic infarction | 99.24% | DL |
| 9 | fibroblastic neoplasm | 99.23% | DL |
| 10 | low grade fibromyxoid sarcoma | 99.19% | DL |
| 11 | hepatic veno-occlusive disease | 99.04% | DL |
| 12 | peliosis hepatis | 98.88% | DL |
| 13 | Kimura disease | 98.83% | DL |
| 14 | syndrome with combined immunodeficiency | 98.79% | DL |
| 15 | X-linked lymphoproliferative syndrome | 98.77% | DL |
| 16 | leishmaniasis, diffuse cutaneous | 98.75% | DL |
| 17 | familial rhabdoid tumor | 98.73% | DL |
| 18 | Castleman disease | 98.70% | DL |
| 19 | benign PEComa | 98.67% | DL |
| 20 | lymphangiomyoma | 98.67% | DL |

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
