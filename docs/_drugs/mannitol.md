---
layout: default
title: Mannitol
description: "Mannitol drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 362
evidence_level: L5
indication_count: 52
---

# Mannitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mannitol |
| DrugBank ID | [DB00742](https://go.drugbank.com/drugs/DB00742) |
| Brand Names (EU) | Bronchitol |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Bronchitol is indicated for the treatment of cystic fibrosis (CF) in adults aged 18 years and above as an add-on therapy to best standard of care.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.97% | DL |
| 2 | congestive heart failure | 99.90% | DL |
| 3 | acute pulmonary heart disease | 99.88% | DL |
| 4 | exercise-induced malignant hyperthermia | 99.86% | DL |
| 5 | malignant hyperthermia, susceptibility to | 99.80% | DL |
| 6 | familial periodic paralysis | 99.75% | DL |
| 7 | hypokalemic periodic paralysis | 99.72% | DL |
| 8 | congenital multicore myopathy with external ophthalmoplegia | 99.72% | DL |
| 9 | moderate multiminicore disease with hand involvement | 99.71% | DL |
| 10 | pseudotumor cerebri | 99.70% | DL |
| 11 | nephrogenic diabetes insipidus | 99.70% | DL |
| 12 | King-Denborough syndrome | 99.69% | DL |
| 13 | central core myopathy | 99.69% | DL |
| 14 | renal tubule disease | 99.68% | DL |
| 15 | Senior-Boichis syndrome | 99.65% | DL |
| 16 | psychomotor regression-oculomotor apraxia-movement disorder-nephropathy syndrome | 99.65% | DL |
| 17 | malignant hyperthermia of anesthesia | 99.62% | DL |
| 18 | intracranial hypertension | 99.59% | DL |
| 19 | RHYNS syndrome | 99.56% | DL |
| 20 | cranioectodermal dysplasia | 99.54% | DL |

*Showing top 20 of 52 predictions.*

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
