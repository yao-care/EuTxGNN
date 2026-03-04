---
layout: default
title: Rimegepant
description: "rimegepant drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 494
evidence_level: L1
indication_count: 50
---

# Rimegepant
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rimegepant |
| DrugBank ID | [DB12457](https://go.drugbank.com/drugs/DB12457) |
| Brand Names (EU) | Vydura |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.95% |

---

## Approved Indication (EMA)

Vydura is indicated for the  Acute treatment of migraine with or without aura in adults; Preventative treatment of episodic migraine in adults who have at least 4 migraine attacks per month.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.95% | DL |
| 2 | migraine with brainstem aura | 99.94% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.87% | DL |
| 4 | atrophoderma vermiculata | 99.76% | DL |
| 5 | ulerythema ophryogenesis | 99.70% | DL |
| 6 | heparin cofactor 2 deficiency | 99.64% | DL |
| 7 | antithrombin deficiency type 2 | 99.57% | DL |
| 8 | factor 5 excess with spontaneous thrombosis | 99.56% | DL |
| 9 | thrombophilia | 98.97% | DL |
| 10 | Prinzmetal angina | 98.81% | DL |
| 11 | sciatic neuropathy | 97.27% | DL |
| 12 | homozygous familial hypercholesterolemia | 96.68% | DL |
| 13 | obsolete susceptibility to ischemic stroke | 96.10% | DL |
| 14 | stroke disorder | 95.60% | DL |
| 15 | ABri amyloidosis | 94.80% | DL |
| 16 | amenorrhea (disease) | 93.85% | DL |
| 17 | hypoalphalipoproteinemia | 93.12% | DL |
| 18 | sagittal sinus thrombosis | 92.87% | DL |
| 19 | lesion of sciatic nerve | 91.56% | DL |
| 20 | brain stem infarction | 89.58% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| migraine disorder | L1 | 20 | 1 | 4 Phase 3 trial(s), 2 Phase 2 trial(s) |

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
