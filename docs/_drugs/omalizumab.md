---
layout: default
title: Omalizumab
description: "omalizumab drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 421
evidence_level: L1
indication_count: 50
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Omalizumab |
| DrugBank ID | [DB00043](https://go.drugbank.com/drugs/DB00043) |
| Brand Names (EU) | Xolair |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Allergic asthma Xolair is indicated in adults, adolescents and children (6 to &lt;12&nbsp;years of age). Xolair treatment should only be considered for patients with convincing IgE (immunoglobulin E) mediated asthma. Adults and adolescents (12&nbsp;years of age and older) Xolair is indicated as add-on therapy to improve asthma control in patients with severe persistent allergic asthma who have a positive skin test or in vitro reactivity to a perennial aeroallergen and who have reduced lung funct

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 100.00% | DL |
| 2 | atopic eczema | 99.97% | DL |
| 3 | obstructive lung disease | 99.97% | DL |
| 4 | allergic asthma | 99.97% | DL |
| 5 | dermatitis | 99.97% | DL |
| 6 | intrinsic asthma | 99.97% | DL |
| 7 | bronchial neoplasm (disease) | 99.95% | DL |
| 8 | acne keloid | 99.94% | DL |
| 9 | acrodermatitis chronica atrophicans | 99.93% | DL |
| 10 | hydroa vacciniforme, familial | 99.93% | DL |
| 11 | neonatal dermatomyositis | 99.93% | DL |
| 12 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.92% | DL |
| 13 | amyopathic dermatomyositis | 99.92% | DL |
| 14 | indolent plasma cell myeloma | 99.89% | DL |
| 15 | plasma cell myeloma | 99.86% | DL |
| 16 | chronic obstructive pulmonary disease | 99.81% | DL |
| 17 | compensatory emphysema | 99.80% | DL |
| 18 | interstitial emphysema | 99.80% | DL |
| 19 | hyperlucent lung | 99.80% | DL |
| 20 | tracheal stenosis | 99.77% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| allergic asthma | L1 | 20 | 19 | 4 Phase 3 trial(s), 2 Phase 2 trial(s), 2 RCT(s) |
| dermatitis | L1 | 19 | 20 | 3 Phase 2 trial(s), 5 review(s)/meta-analysis |
| atopic eczema | L1 | 18 | 18 | 3 Phase 2 trial(s), 2 RCT(s), 1 review(s)/meta-ana |
| obstructive lung disease | L1 | 20 | 1 | 5 Phase 3 trial(s), 3 Phase 2 trial(s) |
| intrinsic asthma | L1 | 11 | 5 | 2 Phase 3 trial(s), 2 Phase 2 trial(s) |
| bronchitis | L2 | 2 | 5 | 2 Phase 2 trial(s) |
| bronchial neoplasm (disease) | L2 | 2 | 0 | AI prediction only |

---

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
