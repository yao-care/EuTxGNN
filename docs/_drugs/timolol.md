---
layout: default
title: Timolol
description: "Timolol drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 582
evidence_level: L5
indication_count: 50
---

# Timolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Timolol |
| DrugBank ID | [DB00373](https://go.drugbank.com/drugs/DB00373) |
| Brand Names (EU) | Timolol |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.64% |

---

## Approved Indication (EMA)

Reduction of intraocular pressure (IOP) in patients with open-angle glaucoma or ocular hypertension who are insufficiently responsive to topical beta-blockers or prostaglandin analogues.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary hereditary glaucoma | 98.64% | DL |
| 2 | open-angle glaucoma | 98.16% | DL |
| 3 | closed-angle glaucoma | 97.23% | DL |
| 4 | malignant renovascular hypertension | 94.45% | DL |
| 5 | malignant hypertensive renal disease | 94.45% | DL |
| 6 | pulmonary hypertension with unclear multifactorial mechanism | 93.71% | DL |
| 7 | pulmonary hypertension owing to lung disease and/or hypoxia | 93.71% | DL |
| 8 | hypertensive disorder | 93.65% | DL |
| 9 | Braddock syndrome | 92.57% | DL |
| 10 | chronic pulmonary heart disease | 87.80% | DL |
| 11 | glaucoma 1, open angle | 86.50% | DL |
| 12 | angle-closure glaucoma | 85.50% | DL |
| 13 | congenital glaucoma | 78.88% | DL |
| 14 | aqueous misdirection | 76.72% | DL |
| 15 | traumatic glaucoma | 76.72% | DL |
| 16 | glaucomatous atrophy of optic disc | 74.72% | DL |
| 17 | faciodigitogenital syndrome | 73.75% | DL |
| 18 | neovascular glaucoma | 73.08% | DL |
| 19 | distal myopathy, Tateyama type | 71.79% | DL |
| 20 | trichotillomania | 71.00% | DL |

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
