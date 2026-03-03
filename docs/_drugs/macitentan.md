---
layout: default
title: Macitentan
description: "Macitentan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 361
evidence_level: L5
indication_count: 50
---

# Macitentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Macitentan |
| DrugBank ID | [DB08932](https://go.drugbank.com/drugs/DB08932) |
| Brand Names (EU) | Opsumit |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.89% |

---

## Approved Indication (EMA)

Adults&nbsp;Opsumit, as monotherapy or in combination, is indicated for the long-term treatment of pulmonary arterial hypertension (PAH) in adult patients of WHO Functional Class (FC) II to III. Paediatric populationOpsumit, as monotherapy or in combination, is indicated for the long-term treatment of pulmonary arterial hypertension (PAH) in paediatric patients aged less than 18 years and bodyweight ≥ 40 kg with WHO Functional Class (FC) II to III. Opsumit, as monotherapy or in combination, is i

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary arteriovenous malformation (disease) | 98.89% | DL |
| 2 | pulmonary arterial hypertension associated with congenital heart disease | 98.75% | DL |
| 3 | pulmonary arterial hypertension associated with HIV infection | 98.59% | DL |
| 4 | pulmonary arterial hypertension associated with schistosomiasis | 98.59% | DL |
| 5 | pulmonary arterial hypertension associated with connective tissue disease | 98.59% | DL |
| 6 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 98.59% | DL |
| 7 | pulmonary arterial hypertension | 98.37% | DL |
| 8 | hypotrichosis simplex of the scalp | 98.24% | DL |
| 9 | congenital hypotrichosis milia | 97.82% | DL |
| 10 | diffuse alopecia areata | 97.62% | DL |
| 11 | alopecia | 93.73% | DL |
| 12 | malformation syndrome with odontal and/or periodontal component | 89.50% | DL |
| 13 | telangiectasia, hereditary hemorrhagic, | 89.02% | DL |
| 14 | syndrome with a Dandy-Walker malformation as major feature | 88.77% | DL |
| 15 | Ambras type hypertrichosis universalis congenita | 88.56% | DL |
| 16 | isolated genetic hair shaft abnormality | 88.45% | DL |
| 17 | hypertrichosis (disease) | 86.77% | DL |
| 18 | familial generalized lentiginosis | 83.82% | DL |
| 19 | acromelanosis | 83.33% | DL |
| 20 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 83.33% | DL |

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
