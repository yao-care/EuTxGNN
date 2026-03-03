---
layout: default
title: Bosutinib (As Monohydrate)
description: "Bosutinib (As Monohydrate) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 88
evidence_level: L5
indication_count: 50
---

# Bosutinib (As Monohydrate)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bosutinib (As Monohydrate) |
| DrugBank ID | [DB06616](https://go.drugbank.com/drugs/DB06616) |
| Brand Names (EU) | Bosulif |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.75% |

---

## Approved Indication (EMA)

Bosulif is indicated for the treatment of:• Adult and paediatric patients aged 6 years and older with newly-diagnosed (ND) chronic phase (CP) Philadelphia chromosome-positive chronic myelogenous leukaemia (Ph+ CML).• Adult and paediatric patients aged 6 years and older with CP Ph+ CML previously treated with one or more tyrosine kinase inhibitor(s) [TKI(s)] and for whom imatinib, nilotinib and dasatinib are not considered appropriate treatment options.• Adult patients with accelerated phase (AP)

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myeloid leukemia | 98.75% | DL |
| 2 | thrombocytopenia | 98.62% | DL |
| 3 | marcothrombocytopenia with mitral valve insufficiency | 98.46% | DL |
| 4 | hereditary thrombocytopenia with normal platelets | 98.45% | DL |
| 5 | transient neonatal thrombocytopenia | 98.34% | DL |
| 6 | dense granule disease | 98.31% | DL |
| 7 | platelet storage pool deficiency | 97.43% | DL |
| 8 | plasma cell myeloma | 96.82% | DL |
| 9 | HER2 positive breast carcinoma | 96.72% | DL |
| 10 | indolent plasma cell myeloma | 96.47% | DL |
| 11 | thrombotic disease | 96.08% | DL |
| 12 | female breast carcinoma | 96.05% | DL |
| 13 | primary cutaneous T-cell lymphoma | 95.63% | DL |
| 14 | malignant catarrh | 95.42% | DL |
| 15 | infectious bovine rhinotracheitis | 95.42% | DL |
| 16 | cytomegalovirus infection | 95.36% | DL |
| 17 | progesterone-receptor negative breast cancer | 95.34% | DL |
| 18 | progesterone-receptor positive breast cancer | 95.21% | DL |
| 19 | normal breast-like subtype of breast carcinoma | 95.21% | DL |
| 20 | breast tumor luminal A or B | 95.14% | DL |

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
