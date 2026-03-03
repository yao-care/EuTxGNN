---
layout: default
title: Tacrolimus
description: "Tacrolimus drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 549
evidence_level: L5
indication_count: 50
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tacrolimus |
| DrugBank ID | [DB00864](https://go.drugbank.com/drugs/DB00864) |
| Brand Names (EU) | Advagraf |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.56% |

---

## Approved Indication (EMA)

Prophylaxis of transplant rejection in adult kidney or liver allograft recipients. Treatment of allograft rejection resistant to treatment with other immunosuppressive medicinal products in adult patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | atopic eczema | 99.56% | DL |
| 2 | seborrheic dermatitis | 99.26% | DL |
| 3 | parapsoriasis | 99.24% | DL |
| 4 | dermatitis, atopic | 99.23% | DL |
| 5 | dermatitis | 99.17% | DL |
| 6 | acute lichenoid pityriasis | 98.90% | DL |
| 7 | acrodermatitis chronica atrophicans | 98.73% | DL |
| 8 | rheumatoid arthritis | 98.71% | DL |
| 9 | acne keloid | 98.68% | DL |
| 10 | psoriasis | 98.66% | DL |
| 11 | neonatal dermatomyositis | 98.60% | DL |
| 12 | exanthem (disease) | 98.59% | DL |
| 13 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 98.57% | DL |
| 14 | amyopathic dermatomyositis | 98.48% | DL |
| 15 | bronchitis | 98.41% | DL |
| 16 | pityriasis lichenoides | 98.20% | DL |
| 17 | hydroa vacciniforme, familial | 98.20% | DL |
| 18 | brachydactyly-syndactyly syndrome | 97.83% | DL |
| 19 | pustulosis palmaris et plantaris | 97.76% | DL |
| 20 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.62% | DL |

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
