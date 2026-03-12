---
layout: default
title: Mirabegron
description: "Mirabegron drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 385
evidence_level: L5
indication_count: 50
---

# Mirabegron
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mirabegron |
| DrugBank ID | [DB08893](https://go.drugbank.com/drugs/DB08893) |
| Brand Names (EU) | Betmiga |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.25% |

---

## Approved Indication (EMA)

Overactive bladder in adults&nbsp;  Betmiga prolonged-release tablets are indicated for symptomatic treatment of urgency, increased micturition frequency and/or urgency incontinence as may occur in adult patients with overactive bladder (OAB) syndrome.&nbsp;  Neurogenic detrusor overactivity in the paediatric population&nbsp;  Betmiga prolonged release tablets are indicated for treatment of neurogenic detrusor overactivity (NDO) in paediatric patients aged 3 to less than 18 years.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | overactive bladder (disease) | 93.25% | DL |
| 2 | thoracic malformation | 83.06% | DL |
| 3 | renal-hepatic-pancreatic dysplasia | 82.93% | DL |
| 4 | polycystic kidney disease 3 with or without polycystic liver disease | 82.20% | DL |
| 5 | Joubert syndrome with renal defect | 80.89% | DL |
| 6 | adult familial nephronophthisis-spastic quadriparesia syndrome | 80.32% | DL |
| 7 | esophageal varices without bleeding | 80.05% | DL |
| 8 | esophageal varices with bleeding | 80.05% | DL |
| 9 | hypotrichosis simplex of the scalp | 79.47% | DL |
| 10 | karyomegalic interstitial nephritis | 79.24% | DL |
| 11 | congenital hypotrichosis milia | 77.54% | DL |
| 12 | 16q24.1 microdeletion syndrome | 75.15% | DL |
| 13 | primary interstitial lung disease specific to childhood | 74.17% | DL |
| 14 | isolated pulmonary capillaritis | 73.40% | DL |
| 15 | low compliance bladder | 73.23% | DL |
| 16 | diffuse alopecia areata | 71.42% | DL |
| 17 | congenital pulmonary lymphangiectasia | 67.75% | DL |
| 18 | polycystic kidney disease | 66.72% | DL |
| 19 | varicose disease | 64.28% | DL |
| 20 | autosomal ichthyosis syndrome with fatal disease course | 63.51% | DL |

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
