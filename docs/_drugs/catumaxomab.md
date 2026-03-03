---
layout: default
title: Catumaxomab
description: "Catumaxomab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 122
evidence_level: L5
indication_count: 50
---

# Catumaxomab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Catumaxomab |
| DrugBank ID | [DB06607](https://go.drugbank.com/drugs/DB06607) |
| Brand Names (EU) | Korjuny |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.64% |

---

## Approved Indication (EMA)

Korjuny is indicated for the intraperitoneal treatment of malignant ascites in adults with epithelial cellular adhesion molecule (EpCAM)-positive carcinomas, who are not eligible for further systemic anticancer therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 99.64% | DL |
| 2 | drug-induced osteoporosis | 99.58% | DL |
| 3 | diabetic retinopathy | 99.47% | DL |
| 4 | diabetic cataract | 98.45% | DL |
| 5 | kidney pelvis sarcomatoid transitional cell carcinoma | 98.29% | DL |
| 6 | prostatic urethra urothelial carcinoma | 98.27% | DL |
| 7 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 98.25% | DL |
| 8 | renal pelvis papillary urothelial carcinoma | 98.18% | DL |
| 9 | transitional cell carcinoma | 98.07% | DL |
| 10 | HER2 positive breast carcinoma | 97.47% | DL |
| 11 | cortical cataract | 97.22% | DL |
| 12 | nuclear senile cataract | 97.22% | DL |
| 13 | senile cataract | 97.19% | DL |
| 14 | immature cataract | 96.90% | DL |
| 15 | diabetes mellitus type 2 associated cataract | 96.90% | DL |
| 16 | mature cataract | 96.90% | DL |
| 17 | tetanic cataract | 96.90% | DL |
| 18 | craniostenosis cataract | 96.90% | DL |
| 19 | psoriasis | 96.50% | DL |
| 20 | normal breast-like subtype of breast carcinoma | 96.45% | DL |

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
