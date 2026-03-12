---
layout: default
title: Latanoprost
description: "Latanoprost drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 332
evidence_level: L5
indication_count: 50
---

# Latanoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Latanoprost |
| DrugBank ID | [DB00654](https://go.drugbank.com/drugs/DB00654) |
| Brand Names (EU) | Catiolanze |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Catiolanze is indicated for the reduction of elevated intraocular pressure (IOP) in adult patients with open angle glaucoma or ocular hypertension. Catiolanze is indicated for the reduction of elevated IOP in children from 4 years of age and adolescents with elevated IOP and paediatric glaucoma. &nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary hereditary glaucoma | 99.88% | DL |
| 2 | open-angle glaucoma | 99.86% | DL |
| 3 | visceral calciphylaxis | 99.83% | DL |
| 4 | hypotrichosis simplex of the scalp | 99.81% | DL |
| 5 | venous thoracic outlet syndrome | 99.78% | DL |
| 6 | arterial thoracic outlet syndrome | 99.78% | DL |
| 7 | neurogenic thoracic outlet syndrome | 99.72% | DL |
| 8 | congenital hypotrichosis milia | 99.71% | DL |
| 9 | angiodysplasia of stomach | 99.70% | DL |
| 10 | blue toe syndrome | 99.69% | DL |
| 11 | lymphangiectasis | 99.67% | DL |
| 12 | hemangioendothelioma | 99.67% | DL |
| 13 | vascular disease | 99.65% | DL |
| 14 | atheroembolism of kidney | 99.65% | DL |
| 15 | idiopathic spontaneous coronary artery dissection | 99.64% | DL |
| 16 | diffuse alopecia areata | 99.59% | DL |
| 17 | arterial dissection-lentiginosis syndrome | 99.56% | DL |
| 18 | alopecia | 99.38% | DL |
| 19 | congestive heart failure | 99.28% | DL |
| 20 | acute pulmonary heart disease | 99.24% | DL |

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
