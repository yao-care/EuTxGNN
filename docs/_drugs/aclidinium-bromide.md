---
layout: default
title: Aclidinium Bromide
description: "Aclidinium Bromide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 17
evidence_level: L5
indication_count: 50
---

# Aclidinium Bromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aclidinium Bromide |
| DrugBank ID | [DB08897](https://go.drugbank.com/drugs/DB08897) |
| Brand Names (EU) | Bretaris Genuair |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 89.36% |

---

## Approved Indication (EMA)

Bretaris Genuair is indicated as a maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | open-angle glaucoma | 89.36% | DL |
| 2 | primary hereditary glaucoma | 88.95% | DL |
| 3 | migraine disorder | 86.15% | DL |
| 4 | migraine with brainstem aura | 85.36% | DL |
| 5 | irritable bowel syndrome | 84.56% | DL |
| 6 | headache disorder | 83.48% | DL |
| 7 | trigeminal autonomic cephalalgia | 82.74% | DL |
| 8 | glaucoma 1, open angle | 79.57% | DL |
| 9 | gastroduodenitis | 79.52% | DL |
| 10 | dermatitis | 79.28% | DL |
| 11 | obsolete rare pulmonary disease | 79.06% | DL |
| 12 | peptic ulcer disease | 78.54% | DL |
| 13 | dysthymic disorder | 78.03% | DL |
| 14 | acrodermatitis chronica atrophicans | 77.56% | DL |
| 15 | common cold | 77.20% | DL |
| 16 | neonatal dermatomyositis | 76.63% | DL |
| 17 | hydroa vacciniforme, familial | 75.98% | DL |
| 18 | atrophoderma vermiculata | 75.62% | DL |
| 19 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 75.60% | DL |
| 20 | amyopathic dermatomyositis | 75.26% | DL |

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
