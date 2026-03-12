---
layout: default
title: Lasmiditan Succinate
description: "Lasmiditan Succinate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 331
evidence_level: L5
indication_count: 50
---

# Lasmiditan Succinate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lasmiditan Succinate |
| DrugBank ID | [DB11732](https://go.drugbank.com/drugs/DB11732) |
| Brand Names (EU) | Rayvow |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

RAYVOW is indicated for the acute treatment of the headache phase of migraine attacks, with or without aura in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.94% | DL |
| 2 | migraine with brainstem aura | 99.92% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.61% | DL |
| 4 | atrophoderma vermiculata | 99.59% | DL |
| 5 | ulerythema ophryogenesis | 99.46% | DL |
| 6 | sciatic neuropathy | 96.51% | DL |
| 7 | monogenic obesity | 88.83% | DL |
| 8 | obesity disorder | 87.57% | DL |
| 9 | obsolete hypertelorism (disease) | 86.37% | DL |
| 10 | hypervitaminosis | 86.15% | DL |
| 11 | amenorrhea (disease) | 84.73% | DL |
| 12 | frontorhiny | 82.74% | DL |
| 13 | proximal 16p11.2 microdeletion syndrome | 80.01% | DL |
| 14 | lesion of sciatic nerve | 79.64% | DL |
| 15 | anxiety | 75.04% | DL |
| 16 | tendinitis | 73.69% | DL |
| 17 | myositis fibrosa | 71.50% | DL |
| 18 | idiopathic granulomatous myositis | 71.50% | DL |
| 19 | trigeminal autonomic cephalalgia | 68.27% | DL |
| 20 | headache disorder | 66.06% | DL |

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
