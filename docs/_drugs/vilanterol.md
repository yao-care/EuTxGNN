---
layout: default
title: Vilanterol
description: "vilanterol drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 633
evidence_level: L2
indication_count: 50
---

# Vilanterol
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vilanterol |
| DrugBank ID | [DB09082](https://go.drugbank.com/drugs/DB09082) |
| Brand Names (EU) | Vilanterol |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Asthma indication: Relvar Ellipta is indicated in the regular treatment of asthma in adults and adolescents aged 12 years and older, where use of a combination product (long-acting beta2-agonist and inhaled corticosteroid) is appropriate:  patients not adequately controlled with inhaled corticosteroids and “as needed” inhaled short acting beta2-agonists. patients already adequately controlled on both inhaled corticosteroid and long-acting beta2-agonist.  COPD indication: Relvar Ellipta is indica

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 100.00% | DL |
| 2 | obstructive lung disease | 99.97% | DL |
| 3 | chronic obstructive pulmonary disease | 99.76% | DL |
| 4 | hyperlucent lung | 99.72% | DL |
| 5 | compensatory emphysema | 99.72% | DL |
| 6 | interstitial emphysema | 99.72% | DL |
| 7 | tracheal stenosis | 99.68% | DL |
| 8 | bronchial neoplasm (disease) | 99.63% | DL |
| 9 | congenital lobar emphysema | 99.58% | DL |
| 10 | respiratory malformation | 99.52% | DL |
| 11 | tracheal calcification | 99.47% | DL |
| 12 | pulmonary emphysema | 99.47% | DL |
| 13 | laryngotracheitis | 99.37% | DL |
| 14 | Rienhoff syndrome | 99.35% | DL |
| 15 | susceptibility to respiratory infections associated with CD8alpha chain mutation | 99.29% | DL |
| 16 | COPD, severe early onset | 99.25% | DL |
| 17 | allergic asthma | 96.77% | DL |
| 18 | intrinsic asthma | 96.61% | DL |
| 19 | Laubry-Pezzi syndrome | 95.66% | DL |
| 20 | tracheal disease | 95.62% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| bronchitis | L2 | 6 | 5 | 1 Phase 2 trial(s), 1 RCT(s) |

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
