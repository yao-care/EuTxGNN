---
layout: default
title: Dopamine
description: "Dopamine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 179
evidence_level: L5
indication_count: 50
---

# Dopamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dopamine |
| DrugBank ID | [DB00988](https://go.drugbank.com/drugs/DB00988) |
| Brand Names (EU) | Dopamine |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.14% |

---

## Approved Indication (EMA)

Treatment of hypotension in haemodynamically unstable neonates, infants and children &lt; 18 years

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypotensive disorder | 97.14% | DL |
| 2 | postural orthostatic tachycardia syndrome | 88.00% | DL |
| 3 | variably protease-sensitive prionopathy | 86.87% | DL |
| 4 | multiple system atrophy | 84.79% | DL |
| 5 | hypotrichosis simplex of the scalp | 83.41% | DL |
| 6 | gastroduodenitis | 81.75% | DL |
| 7 | congenital hypotrichosis milia | 80.91% | DL |
| 8 | common cold | 80.36% | DL |
| 9 | diffuse alopecia areata | 76.95% | DL |
| 10 | peptic ulcer disease | 75.04% | DL |
| 11 | rhinitis | 72.13% | DL |
| 12 | obsolete neurogenic bladder (disease) | 69.00% | DL |
| 13 | osteoarthritis susceptibility | 68.63% | DL |
| 14 | alopecia | 67.77% | DL |
| 15 | acromesomelic dysplasia, Hunter-Thompson type | 64.79% | DL |
| 16 | trigeminal autonomic cephalalgia | 62.59% | DL |
| 17 | headache disorder | 61.70% | DL |
| 18 | mitral valve prolapse, myxomatous | 60.18% | DL |
| 19 | sclerocornea, autosomal dominant | 59.21% | DL |
| 20 | fibrosis of extraocular muscles, congenital, with synergistic divergence | 58.63% | DL |

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
