---
layout: default
title: Sparsentan
description: "Sparsentan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 542
evidence_level: L5
indication_count: 50
---

# Sparsentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sparsentan |
| DrugBank ID | [DB12548](https://go.drugbank.com/drugs/DB12548) |
| Brand Names (EU) | Filspari |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 94.52% |

---

## Approved Indication (EMA)

Filspari is indicated for the treatment of adults with primary immunoglobulin A nephropathy (IgAN) with a urine protein excretion &gt; 1.0 g/day (or urine protein-to-creatinine ratio &gt; 0.75 g/g, see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | alopecia | 94.52% | DL |
| 2 | congenital hypotrichosis milia | 94.46% | DL |
| 3 | hypotrichosis simplex of the scalp | 94.32% | DL |
| 4 | diffuse alopecia areata | 94.22% | DL |
| 5 | angioedema | 93.01% | DL |
| 6 | lichen disease | 92.95% | DL |
| 7 | dermatitis | 91.78% | DL |
| 8 | potassium deficiency disease | 91.68% | DL |
| 9 | pulmonary arteriovenous malformation (disease) | 91.20% | DL |
| 10 | fetal erythroblastosis | 91.15% | DL |
| 11 | open-angle glaucoma | 91.10% | DL |
| 12 | lichen planus pemphigoides | 91.03% | DL |
| 13 | pulmonary arterial hypertension | 91.00% | DL |
| 14 | hypertrophic lichen planus | 90.92% | DL |
| 15 | annular atrophic lichen planus | 90.92% | DL |
| 16 | lichen planus pigmentosus | 90.92% | DL |
| 17 | primary hereditary glaucoma | 90.31% | DL |
| 18 | amyopathic dermatomyositis | 89.72% | DL |
| 19 | acrodermatitis chronica atrophicans | 89.71% | DL |
| 20 | psoriasis | 89.70% | DL |

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
