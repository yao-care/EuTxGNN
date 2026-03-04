---
layout: default
title: Parathyroid Hormone
description: "parathyroid hormone drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 439
evidence_level: L2
indication_count: 50
---

# Parathyroid Hormone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Parathyroid Hormone |
| DrugBank ID | [DB05829](https://go.drugbank.com/drugs/DB05829) |
| Brand Names (EU) | Natpar |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Natpar is indicated as adjunctive treatment of adult patients with chronic hypoparathyroidism who cannot be adequately controlled with standard therapy alone.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.98% | DL |
| 2 | migraine with brainstem aura | 99.97% | DL |
| 3 | amenorrhea (disease) | 99.97% | DL |
| 4 | Raynaud disease | 99.84% | DL |
| 5 | non-syndromic esophageal malformation | 99.80% | DL |
| 6 | migraine with or without aura, susceptibility to | 99.75% | DL |
| 7 | esophageal disease | 99.74% | DL |
| 8 | atrophoderma vermiculata | 99.68% | DL |
| 9 | ulerythema ophryogenesis | 99.59% | DL |
| 10 | erectile dysfunction (disease) | 99.07% | DL |
| 11 | esophageal ulcer | 99.01% | DL |
| 12 | sciatic neuropathy | 98.95% | DL |
| 13 | open-angle glaucoma | 98.77% | DL |
| 14 | primary hereditary glaucoma | 98.68% | DL |
| 15 | homozygous familial hypercholesterolemia | 98.67% | DL |
| 16 | postural orthostatic tachycardia syndrome | 98.66% | DL |
| 17 | lesion of sciatic nerve | 98.64% | DL |
| 18 | infectious bovine rhinotracheitis | 98.64% | DL |
| 19 | malignant catarrh | 98.64% | DL |
| 20 | antithrombin deficiency type 2 | 98.53% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| amenorrhea (disease) | L2 | 2 | 0 | AI prediction only |

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
