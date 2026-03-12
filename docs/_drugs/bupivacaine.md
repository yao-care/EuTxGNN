---
layout: default
title: Bupivacaine
description: "Bupivacaine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 99
evidence_level: L5
indication_count: 50
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bupivacaine |
| DrugBank ID | [DB00297](https://go.drugbank.com/drugs/DB00297) |
| Brand Names (EU) | Exparel liposomal |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.49% |

---

## Approved Indication (EMA)

Exparel&nbsp;liposomal is indicated:  in adults as a brachial plexus block or femoral nerve block for treatment of post-operative pain. in adults and children aged 6 years or older as a field block for treatment of somatic post-operative pain from small- to medium-sized surgical wounds.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatitis | 99.49% | DL |
| 2 | acrodermatitis chronica atrophicans | 99.23% | DL |
| 3 | neonatal dermatomyositis | 99.15% | DL |
| 4 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.11% | DL |
| 5 | amyopathic dermatomyositis | 99.03% | DL |
| 6 | acne keloid | 98.98% | DL |
| 7 | hydroa vacciniforme, familial | 98.96% | DL |
| 8 | uterine polyp | 98.90% | DL |
| 9 | epulis | 98.90% | DL |
| 10 | polyp of vocal cord | 98.87% | DL |
| 11 | polyp of middle ear | 98.86% | DL |
| 12 | fibroepithelial polyp | 98.83% | DL |
| 13 | polyp of ureter | 98.82% | DL |
| 14 | polyp of frontal sinus | 98.82% | DL |
| 15 | neoplastic polyp | 98.81% | DL |
| 16 | polyp of vulva | 98.79% | DL |
| 17 | polyp of external auditory canal | 98.79% | DL |
| 18 | papillary conjunctivitis | 96.83% | DL |
| 19 | bronchitis | 95.71% | DL |
| 20 | nasal cavity polyp | 93.30% | DL |

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
