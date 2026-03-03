---
layout: default
title: Dexmedetomidine Hydrochloride
description: "Dexmedetomidine Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 171
evidence_level: L5
indication_count: 50
---

# Dexmedetomidine Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dexmedetomidine Hydrochloride |
| DrugBank ID | [DB00633](https://go.drugbank.com/drugs/DB00633) |
| Brand Names (EU) | Dexdor |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.60% |

---

## Approved Indication (EMA)

For sedation of adult intensive care unit patients requiring a sedation level not deeper than arousal in response to verbal stimulation (corresponding to Richmond Agitation-Sedation Scale (RASS) 0 to -3).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.60% | DL |
| 2 | migraine disorder | 99.49% | DL |
| 3 | migraine with brainstem aura | 99.35% | DL |
| 4 | headache disorder | 99.30% | DL |
| 5 | trigeminal autonomic cephalalgia | 99.09% | DL |
| 6 | pulmonary hypertension | 98.40% | DL |
| 7 | hypotrichosis simplex of the scalp | 98.35% | DL |
| 8 | migraine with or without aura, susceptibility to | 98.27% | DL |
| 9 | atrophoderma vermiculata | 98.26% | DL |
| 10 | congenital hypotrichosis milia | 98.24% | DL |
| 11 | diffuse alopecia areata | 98.14% | DL |
| 12 | ulerythema ophryogenesis | 98.04% | DL |
| 13 | alopecia | 97.91% | DL |
| 14 | kyphoscoliotic heart disease | 97.79% | DL |
| 15 | Tourette syndrome | 97.69% | DL |
| 16 | open-angle glaucoma | 97.66% | DL |
| 17 | primary hereditary glaucoma | 97.65% | DL |
| 18 | bronchial disease | 97.49% | DL |
| 19 | trichotillomania | 97.43% | DL |
| 20 | tendinitis | 97.20% | DL |

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
