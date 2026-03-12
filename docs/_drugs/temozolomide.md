---
layout: default
title: Temozolomide
description: "Temozolomide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 565
evidence_level: L5
indication_count: 50
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Temozolomide |
| DrugBank ID | [DB00853](https://go.drugbank.com/drugs/DB00853) |
| Brand Names (EU) | Temomedac |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.36% |

---

## Approved Indication (EMA)

Temomedac hard capsules is indicated for the treatment of:  adult patients with newly diagnosed glioblastoma multiforme concomitantly with radiotherapy (RT) and subsequently as monotherapy treatment; children from the age of three years, adolescents and adult patients with malignant glioma, such as glioblastoma multiforme or anaplastic astrocytoma, showing recurrence or progression after standard therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | adult astrocytic tumour | 99.36% | DL |
| 2 | cauda equina neoplasm | 99.30% | DL |
| 3 | astrocytoma (excluding glioblastoma) | 99.29% | DL |
| 4 | childhood cerebral astrocytoma | 97.49% | DL |
| 5 | cerebellar astrocytoma | 97.44% | DL |
| 6 | subependymal giant cell astrocytoma | 97.43% | DL |
| 7 | brain glioblastoma | 97.42% | DL |
| 8 | diencephalic astrocytomas | 97.35% | DL |
| 9 | astrocytic tumor | 97.25% | DL |
| 10 | high grade astrocytic tumor | 97.17% | DL |
| 11 | low grade astrocytic tumor | 96.48% | DL |
| 12 | brain astrocytoma | 96.31% | DL |
| 13 | childhood astrocytic tumor | 96.08% | DL |
| 14 | low-grade astrocytoma | 96.05% | DL |
| 15 | neural glioblastoma | 95.99% | DL |
| 16 | mesenchymal glioblastoma | 95.99% | DL |
| 17 | classical glioblastoma | 95.99% | DL |
| 18 | brain stem glioma | 95.88% | DL |
| 19 | adult glioblastoma | 95.83% | DL |
| 20 | ependymal tumor of brain | 95.63% | DL |

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
