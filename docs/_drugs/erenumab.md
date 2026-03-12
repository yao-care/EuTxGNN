---
layout: default
title: Erenumab
description: "Erenumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 221
evidence_level: L5
indication_count: 50
---

# Erenumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Erenumab |
| DrugBank ID | [DB14039](https://go.drugbank.com/drugs/DB14039) |
| Brand Names (EU) | Aimovig |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Aimovig is indicated for prophylaxis of migraine in adults who have at least 4 migraine days per month when initiating treatment with Aimovig.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine with brainstem aura | 99.89% | DL |
| 2 | migraine disorder | 99.88% | DL |
| 3 | atrophoderma vermiculata | 98.37% | DL |
| 4 | migraine with or without aura, susceptibility to | 98.33% | DL |
| 5 | ulerythema ophryogenesis | 97.53% | DL |
| 6 | amenorrhea (disease) | 97.43% | DL |
| 7 | antithrombin deficiency type 2 | 97.26% | DL |
| 8 | factor 5 excess with spontaneous thrombosis | 97.13% | DL |
| 9 | heparin cofactor 2 deficiency | 97.13% | DL |
| 10 | thrombophilia | 95.93% | DL |
| 11 | sciatic neuropathy | 93.52% | DL |
| 12 | severe nonproliferative diabetic retinopathy | 85.69% | DL |
| 13 | hemorrhagic disease of newborn | 81.02% | DL |
| 14 | HER2 positive breast carcinoma | 80.10% | DL |
| 15 | normal breast-like subtype of breast carcinoma | 77.55% | DL |
| 16 | progesterone-receptor positive breast cancer | 77.55% | DL |
| 17 | breast tumor luminal A or B | 77.19% | DL |
| 18 | progesterone-receptor negative breast cancer | 76.51% | DL |
| 19 | infectious bovine rhinotracheitis | 73.49% | DL |
| 20 | malignant catarrh | 73.49% | DL |

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
