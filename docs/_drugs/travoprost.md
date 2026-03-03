---
layout: default
title: Travoprost
description: "Travoprost drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 605
evidence_level: L5
indication_count: 50
---

# Travoprost
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Travoprost |
| DrugBank ID | [DB00287](https://go.drugbank.com/drugs/DB00287) |
| Brand Names (EU) | Izba |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Decrease of elevated intraocular pressure in adult patients with ocular hypertension or open-angle glaucoma (see section 5.1). Decrease of elevated intraocular pressure in paediatric patients aged 3 years to &lt; 18 years with ocular hypertension or paediatric glaucoma.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | visceral calciphylaxis | 100.00% | DL |
| 2 | arterial thoracic outlet syndrome | 100.00% | DL |
| 3 | venous thoracic outlet syndrome | 100.00% | DL |
| 4 | neurogenic thoracic outlet syndrome | 100.00% | DL |
| 5 | vascular disease | 100.00% | DL |
| 6 | angiodysplasia of stomach | 100.00% | DL |
| 7 | blue toe syndrome | 100.00% | DL |
| 8 | lymphangiectasis | 100.00% | DL |
| 9 | idiopathic spontaneous coronary artery dissection | 100.00% | DL |
| 10 | hemangioendothelioma | 100.00% | DL |
| 11 | hypotrichosis simplex of the scalp | 100.00% | DL |
| 12 | atheroembolism of kidney | 100.00% | DL |
| 13 | arterial dissection-lentiginosis syndrome | 100.00% | DL |
| 14 | congenital hypotrichosis milia | 100.00% | DL |
| 15 | diffuse alopecia areata | 100.00% | DL |
| 16 | alopecia | 100.00% | DL |
| 17 | hypertrichosis (disease) | 100.00% | DL |
| 18 | open-angle glaucoma | 100.00% | DL |
| 19 | primary hereditary glaucoma | 100.00% | DL |
| 20 | malformation syndrome with odontal and/or periodontal component | 100.00% | DL |

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
