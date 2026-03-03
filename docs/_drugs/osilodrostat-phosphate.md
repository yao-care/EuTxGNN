---
layout: default
title: Osilodrostat Phosphate
description: "Osilodrostat Phosphate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 427
evidence_level: L5
indication_count: 50
---

# Osilodrostat Phosphate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Osilodrostat Phosphate |
| DrugBank ID | [DB11837](https://go.drugbank.com/drugs/DB11837) |
| Brand Names (EU) | Isturisa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.19% |

---

## Approved Indication (EMA)

Isturisa is indicated for the treatment of endogenous Cushing’s syndrome in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | familial generalized lentiginosis | 98.19% | DL |
| 2 | acromelanosis | 98.05% | DL |
| 3 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 98.05% | DL |
| 4 | gastrocutaneous syndrome | 97.96% | DL |
| 5 | leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome | 97.88% | DL |
| 6 | Moynahan syndrome | 97.77% | DL |
| 7 | rhabdoid tumor | 97.76% | DL |
| 8 | X-linked lymphoproliferative disease due to SH2D1A deficiency | 97.68% | DL |
| 9 | osteopathia striata-pigmentary dermopathy-white forelock syndrome | 97.66% | DL |
| 10 | peripheral nerve schwannoma | 97.51% | DL |
| 11 | schwannoma of twelfth cranial nerve | 97.40% | DL |
| 12 | sympathetic neurilemmoma | 97.37% | DL |
| 13 | microcystic/reticular schwannoma | 97.33% | DL |
| 14 | trigeminal schwannoma | 97.33% | DL |
| 15 | ACTH-dependent Cushing syndrome | 97.28% | DL |
| 16 | A20 haploinsufficiency | 97.20% | DL |
| 17 | benign neoplasm of adrenal gland | 97.12% | DL |
| 18 | immune dysregulation with inflammatory bowel disease | 96.96% | DL |
| 19 | Steel syndrome | 96.84% | DL |
| 20 | hemophagocytic syndrome associated with an infection | 96.47% | DL |

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
