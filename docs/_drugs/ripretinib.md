---
layout: default
title: Ripretinib
description: "Ripretinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 496
evidence_level: L5
indication_count: 50
---

# Ripretinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ripretinib |
| DrugBank ID | [DB14840](https://go.drugbank.com/drugs/DB14840) |
| Brand Names (EU) | Qinlock |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.84% |

---

## Approved Indication (EMA)

Qinlock is indicated for the treatment of adult patients with advanced gastrointestinal stromal tumour (GIST) who have received prior treatment with three or more kinase inhibitors, including imatinib.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 98.84% | DL |
| 2 | HER2 positive breast carcinoma | 98.32% | DL |
| 3 | malignant catarrh | 98.32% | DL |
| 4 | infectious bovine rhinotracheitis | 98.32% | DL |
| 5 | cytomegalovirus infection | 98.23% | DL |
| 6 | amenorrhea (disease) | 97.79% | DL |
| 7 | progesterone-receptor negative breast cancer | 97.63% | DL |
| 8 | normal breast-like subtype of breast carcinoma | 97.59% | DL |
| 9 | progesterone-receptor positive breast cancer | 97.59% | DL |
| 10 | breast tumor luminal A or B | 97.55% | DL |
| 11 | thrombocytopenia | 97.10% | DL |
| 12 | marcothrombocytopenia with mitral valve insufficiency | 97.07% | DL |
| 13 | hereditary thrombocytopenia with normal platelets | 97.06% | DL |
| 14 | transient neonatal thrombocytopenia | 97.04% | DL |
| 15 | dense granule disease | 97.00% | DL |
| 16 | pulmonary hypertension | 96.85% | DL |
| 17 | kyphoscoliotic heart disease | 96.79% | DL |
| 18 | homozygous familial hypercholesterolemia | 96.79% | DL |
| 19 | amyotrophic lateral sclerosis | 96.63% | DL |
| 20 | axial spondylometaphyseal dysplasia | 96.37% | DL |

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
