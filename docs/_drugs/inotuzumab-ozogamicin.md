---
layout: default
title: Inotuzumab Ozogamicin
description: "Inotuzumab Ozogamicin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 303
evidence_level: L5
indication_count: 50
---

# Inotuzumab Ozogamicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Inotuzumab Ozogamicin |
| DrugBank ID | [DB05889](https://go.drugbank.com/drugs/DB05889) |
| Brand Names (EU) | Besponsa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.24% |

---

## Approved Indication (EMA)

Besponsa is indicated as monotherapy for the treatment of adults with relapsed or refractory CD22-positive B cell precursor acute lymphoblastic leukaemia (ALL). Adult patients with Philadelphia chromosome positive (Ph+) relapsed or refractory B cell precursor ALL should have failed treatment with at least 1 tyrosine kinase inhibitor (TKI).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 98.24% | DL |
| 2 | HER2 positive breast carcinoma | 97.77% | DL |
| 3 | normal breast-like subtype of breast carcinoma | 96.79% | DL |
| 4 | progesterone-receptor positive breast cancer | 96.79% | DL |
| 5 | breast tumor luminal A or B | 96.75% | DL |
| 6 | progesterone-receptor negative breast cancer | 96.68% | DL |
| 7 | severe nonproliferative diabetic retinopathy | 92.05% | DL |
| 8 | primary release disorder of platelets | 91.51% | DL |
| 9 | pseudo-von Willebrand disease | 89.85% | DL |
| 10 | infectious bovine rhinotracheitis | 89.69% | DL |
| 11 | malignant catarrh | 89.69% | DL |
| 12 | kidney pelvis sarcomatoid transitional cell carcinoma | 89.55% | DL |
| 13 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 89.35% | DL |
| 14 | prostatic urethra urothelial carcinoma | 89.34% | DL |
| 15 | renal pelvis papillary urothelial carcinoma | 89.00% | DL |
| 16 | Glanzmann thrombasthenia | 88.58% | DL |
| 17 | transitional cell carcinoma | 87.95% | DL |
| 18 | cytomegalovirus infection | 86.65% | DL |
| 19 | amenorrhea (disease) | 86.62% | DL |
| 20 | benign neoplasm of tongue | 85.39% | DL |

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
