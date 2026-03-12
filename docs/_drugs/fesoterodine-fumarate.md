---
layout: default
title: Fesoterodine Fumarate
description: "Fesoterodine Fumarate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 243
evidence_level: L5
indication_count: 50
---

# Fesoterodine Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fesoterodine Fumarate |
| DrugBank ID | [DB06702](https://go.drugbank.com/drugs/DB06702) |
| Brand Names (EU) | Toviaz |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.87% |

---

## Approved Indication (EMA)

Treatment of the symptoms (increased urinary frequency and / or urgency and / or urgency incontinence) that may occur in patients with overactive-bladder syndrome.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | overactive bladder (disease) | 98.87% | DL |
| 2 | polycystic kidney disease 3 with or without polycystic liver disease | 91.13% | DL |
| 3 | thoracic malformation | 89.92% | DL |
| 4 | renal-hepatic-pancreatic dysplasia | 89.64% | DL |
| 5 | Joubert syndrome with renal defect | 88.48% | DL |
| 6 | adult familial nephronophthisis-spastic quadriparesia syndrome | 88.42% | DL |
| 7 | karyomegalic interstitial nephritis | 87.34% | DL |
| 8 | low compliance bladder | 86.46% | DL |
| 9 | faciodigitogenital syndrome | 84.84% | DL |
| 10 | attention deficit-hyperactivity disorder | 82.44% | DL |
| 11 | polycystic kidney disease | 79.91% | DL |
| 12 | congenital analbuminemia | 74.64% | DL |
| 13 | hyperamylasemia | 72.90% | DL |
| 14 | polyclonal hyperviscosity syndrome | 72.90% | DL |
| 15 | restless legs syndrome | 67.53% | DL |
| 16 | communication disorder | 66.95% | DL |
| 17 | tic disorder | 66.20% | DL |
| 18 | developmental disorder of mental health | 65.77% | DL |
| 19 | stereotypic movement disorder | 64.96% | DL |
| 20 | fetal nicotine spectrum disorder | 64.96% | DL |

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
