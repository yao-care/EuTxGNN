---
layout: default
title: Evinacumab
description: "Evinacumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 233
evidence_level: L5
indication_count: 50
---

# Evinacumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Evinacumab |
| DrugBank ID | [DB15354](https://go.drugbank.com/drugs/DB15354) |
| Brand Names (EU) | Evkeeza |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.52% |

---

## Approved Indication (EMA)

Evkeeza is indicated as an adjunct to diet and other low-density lipoprotein-cholesterol (LDL-C) lowering therapies for the treatment of adult and adolescent patients aged 12 years and older with homozygous familial hypercholesterolaemia (HoFH).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 98.52% | DL |
| 2 | immature cataract | 98.45% | DL |
| 3 | craniostenosis cataract | 98.45% | DL |
| 4 | diabetes mellitus type 2 associated cataract | 98.45% | DL |
| 5 | mature cataract | 98.45% | DL |
| 6 | tetanic cataract | 98.45% | DL |
| 7 | cortical cataract | 98.42% | DL |
| 8 | nuclear senile cataract | 98.42% | DL |
| 9 | senile cataract | 98.36% | DL |
| 10 | diabetic retinopathy | 98.22% | DL |
| 11 | antithrombin deficiency type 2 | 98.03% | DL |
| 12 | factor 5 excess with spontaneous thrombosis | 97.98% | DL |
| 13 | severe nonproliferative diabetic retinopathy | 97.94% | DL |
| 14 | heparin cofactor 2 deficiency | 97.94% | DL |
| 15 | thrombophilia | 97.68% | DL |
| 16 | diffuse gastric adenocarcinoma | 95.62% | DL |
| 17 | hemorrhagic disease of newborn | 95.12% | DL |
| 18 | gastric carcinoma | 94.95% | DL |
| 19 | gastric adenocarcinoma and proximal polyposis of the stomach | 94.93% | DL |
| 20 | bronchitis | 94.87% | DL |

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
