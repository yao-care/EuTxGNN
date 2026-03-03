---
layout: default
title: Nitric Oxide
description: "Nitric Oxide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 407
evidence_level: L5
indication_count: 50
---

# Nitric Oxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nitric Oxide |
| DrugBank ID | [DB00435](https://go.drugbank.com/drugs/DB00435) |
| Brand Names (EU) | INOmax |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.57% |

---

## Approved Indication (EMA)

INOmax, in conjunction with ventilatory support and other appropriate active substances, is indicated:  for the treatment of newborn infants ?34 weeks gestation with hypoxic respiratory failure associated with clinical or echocardiographic evidence of pulmonary hypertension, in order to improve oxygenation and to reduce the need for extracorporeal membrane oxygenation; as part of the treatment of peri- and post-operative pulmonary hypertension in adults and newborn infants, infants and toddlers,

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malformation syndrome with odontal and/or periodontal component | 99.57% | DL |
| 2 | hypertrichosis (disease) | 99.56% | DL |
| 3 | Ambras type hypertrichosis universalis congenita | 99.55% | DL |
| 4 | syndrome with a Dandy-Walker malformation as major feature | 99.53% | DL |
| 5 | isolated genetic hair shaft abnormality | 99.49% | DL |
| 6 | pulmonary arteriovenous malformation (disease) | 99.41% | DL |
| 7 | pulmonary arterial hypertension | 99.41% | DL |
| 8 | pulmonary arterial hypertension associated with congenital heart disease | 99.41% | DL |
| 9 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.29% | DL |
| 10 | pulmonary arterial hypertension associated with HIV infection | 99.29% | DL |
| 11 | pulmonary arterial hypertension associated with schistosomiasis | 99.29% | DL |
| 12 | pulmonary arterial hypertension associated with connective tissue disease | 99.29% | DL |
| 13 | hypotrichosis simplex of the scalp | 98.85% | DL |
| 14 | congenital hypotrichosis milia | 98.72% | DL |
| 15 | pulmonary hypertension, primary, autosomal recessive | 98.62% | DL |
| 16 | diffuse alopecia areata | 98.22% | DL |
| 17 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 98.20% | DL |
| 18 | 16q24.1 microdeletion syndrome | 98.05% | DL |
| 19 | primary interstitial lung disease specific to childhood | 97.94% | DL |
| 20 | isolated pulmonary capillaritis | 97.93% | DL |

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
