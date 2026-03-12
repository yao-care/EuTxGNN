---
layout: default
title: Dupilumab
description: "Dupilumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 188
evidence_level: L5
indication_count: 50
---

# Dupilumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dupilumab |
| DrugBank ID | [DB12159](https://go.drugbank.com/drugs/DB12159) |
| Brand Names (EU) | Dupixent |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Atopic dermatitis Adults and adolescentsDupixent is indicated for the treatment of moderate-to-severe atopic dermatitis in adults and adolescents 12 years and older who are candidates for systemic therapy. Children 6 months to 11 years of ageDupixent is indicated for the treatment of severe atopic dermatitis in children 6 months to 11 years old who are candidates for systemic therapy. Asthma Adults and adolescentsDupixent is indicated in adults and adolescents 12 years and older as add-on mainte

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 99.92% | DL |
| 2 | dermatitis | 99.71% | DL |
| 3 | acne keloid | 99.61% | DL |
| 4 | exanthem (disease) | 99.57% | DL |
| 5 | neonatal dermatomyositis | 99.56% | DL |
| 6 | acrodermatitis chronica atrophicans | 99.54% | DL |
| 7 | amyopathic dermatomyositis | 99.53% | DL |
| 8 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.52% | DL |
| 9 | hydroa vacciniforme, familial | 99.50% | DL |
| 10 | atopic eczema | 99.28% | DL |
| 11 | severe nonproliferative diabetic retinopathy | 99.10% | DL |
| 12 | postinfectious vasculitis | 98.76% | DL |
| 13 | post-bacterial disorder | 98.75% | DL |
| 14 | infective urethral stricture | 98.74% | DL |
| 15 | post-infectious syndrome | 98.73% | DL |
| 16 | infection-related hemolytic uremic syndrome | 98.71% | DL |
| 17 | Chagas cardiomyopathy | 98.69% | DL |
| 18 | otitis externa | 98.41% | DL |
| 19 | pityriasis simplex | 98.24% | DL |
| 20 | bronchial neoplasm (disease) | 98.19% | DL |

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
