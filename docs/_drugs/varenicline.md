---
layout: default
title: Varenicline
description: "Varenicline drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 623
evidence_level: L5
indication_count: 50
---

# Varenicline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Varenicline |
| DrugBank ID | [DB01273](https://go.drugbank.com/drugs/DB01273) |
| Brand Names (EU) | Champix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Champix is indicated for smoking cessation in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.92% | DL |
| 2 | migraine with brainstem aura | 99.90% | DL |
| 3 | congenital hypotrichosis milia | 99.88% | DL |
| 4 | hypotrichosis simplex of the scalp | 99.88% | DL |
| 5 | diffuse alopecia areata | 99.87% | DL |
| 6 | alopecia | 99.86% | DL |
| 7 | open-angle glaucoma | 99.55% | DL |
| 8 | primary hereditary glaucoma | 99.55% | DL |
| 9 | headache disorder | 99.48% | DL |
| 10 | pulmonary hypertension | 99.33% | DL |
| 11 | atrophoderma vermiculata | 99.32% | DL |
| 12 | trigeminal autonomic cephalalgia | 99.28% | DL |
| 13 | ulerythema ophryogenesis | 99.28% | DL |
| 14 | kyphoscoliotic heart disease | 99.09% | DL |
| 15 | restless legs syndrome | 98.84% | DL |
| 16 | hypotrichosis of eyelid | 98.82% | DL |
| 17 | atypical coarctation of aorta | 98.78% | DL |
| 18 | migraine with or without aura, susceptibility to | 98.73% | DL |
| 19 | pseudopelade of Brocq | 98.71% | DL |
| 20 | pulmonary hypertension, primary, autosomal recessive | 98.52% | DL |

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
