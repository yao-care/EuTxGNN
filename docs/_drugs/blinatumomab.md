---
layout: default
title: Blinatumomab
description: "Blinatumomab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 85
evidence_level: L5
indication_count: 50
---

# Blinatumomab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Blinatumomab |
| DrugBank ID | [DB09052](https://go.drugbank.com/drugs/DB09052) |
| Brand Names (EU) | Blincyto |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.20% |

---

## Approved Indication (EMA)

Blincyto is indicated as monotherapy for the treatment of adults with CD19 positive relapsed or refractory B‑cell precursor acute lymphoblastic leukaemia (ALL). Patients with Philadelphia chromosome-positive B-cell precursor ALL should have failed treatment with at least 2 tyrosine kinase inhibitors (TKIs) and have no alternative treatment options. Blincyto is indicated as monotherapy for the treatment of adults with Philadelphia chromosome-negative CD19 positive B-cell precursor ALL in first or

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 95.20% | DL |
| 2 | Glanzmann thrombasthenia | 95.02% | DL |
| 3 | pseudo-von Willebrand disease | 94.13% | DL |
| 4 | drug-induced osteoporosis | 92.70% | DL |
| 5 | severe nonproliferative diabetic retinopathy | 89.25% | DL |
| 6 | psoriasis | 88.92% | DL |
| 7 | Ledderhose disease | 88.41% | DL |
| 8 | hemorrhagic disorder due to a constitutional thrombocytopenia | 87.88% | DL |
| 9 | penile fibromatosis | 87.80% | DL |
| 10 | bleeding diathesis due to a collagen receptor defect | 87.72% | DL |
| 11 | infantile digital fibromatosis | 87.27% | DL |
| 12 | bronchitis | 87.23% | DL |
| 13 | fetal and neonatal alloimmune thrombocytopenia | 87.21% | DL |
| 14 | palmar fibromatosis | 87.03% | DL |
| 15 | indolent plasma cell myeloma | 86.58% | DL |
| 16 | plasma cell myeloma | 86.48% | DL |
| 17 | HER2 positive breast carcinoma | 86.19% | DL |
| 18 | Scott syndrome | 85.64% | DL |
| 19 | pityriasis lichenoides | 85.56% | DL |
| 20 | inherited thrombophilia | 85.17% | DL |

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
