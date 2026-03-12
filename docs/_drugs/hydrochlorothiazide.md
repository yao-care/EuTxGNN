---
layout: default
title: Hydrochlorothiazide
description: "Hydrochlorothiazide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 281
evidence_level: L5
indication_count: 51
---

# Hydrochlorothiazide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Hydrochlorothiazide |
| DrugBank ID | [DB00999](https://go.drugbank.com/drugs/DB00999) |
| Brand Names (EU) | Hydrochlorothiazide, Tolucombi |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.42% |

---

## Approved Indication (EMA)

Treatment of essential hypertension. PritorPlus fixed-dose combination (40 mg telmisartan / 12.5 mg hydrochlorothiazide, 80mg telmisartan / 12.5 mg hydrochlorothiazide) is indicated in patients whose blood pressure is not adequately controlled on telmisartan alone. PritorPlus fixed-dose combination (80 mg telmisartan / 25 mg hydrochlorothiazide) is indicated in patients whose blood pressure is not adequately controlled on PritorPlus (80 mg telmisartan / 12.5 mg hydrochlorothiazide) or patients w

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malignant hypertensive renal disease | 98.42% | DL |
| 2 | malignant renovascular hypertension | 98.42% | DL |
| 3 | pulmonary hypertension owing to lung disease and/or hypoxia | 98.35% | DL |
| 4 | pulmonary hypertension with unclear multifactorial mechanism | 98.35% | DL |
| 5 | hypertensive disorder | 98.28% | DL |
| 6 | Braddock syndrome | 97.92% | DL |
| 7 | chronic pulmonary heart disease | 97.80% | DL |
| 8 | congestive heart failure | 93.70% | DL |
| 9 | acute pulmonary heart disease | 93.17% | DL |
| 10 | primary hereditary glaucoma | 90.87% | DL |
| 11 | open-angle glaucoma | 86.16% | DL |
| 12 | hypotrichosis simplex of the scalp | 74.54% | DL |
| 13 | congenital hypotrichosis milia | 72.80% | DL |
| 14 | distal myopathy, Tateyama type | 70.46% | DL |
| 15 | chronic kidney disease | 69.85% | DL |
| 16 | hypertrophic cardiomyopathy due to intensive athletic training | 67.51% | DL |
| 17 | hypertrophic cardiomyopathy | 66.83% | DL |
| 18 | end stage renal failure | 65.88% | DL |
| 19 | cirrhotic cardiomyopathy | 65.18% | DL |
| 20 | diffuse alopecia areata | 65.03% | DL |

*Showing top 20 of 51 predictions.*

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
