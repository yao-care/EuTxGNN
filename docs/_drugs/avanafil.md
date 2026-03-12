---
layout: default
title: Avanafil
description: "Avanafil drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 57
evidence_level: L5
indication_count: 52
---

# Avanafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Avanafil |
| DrugBank ID | [DB06237](https://go.drugbank.com/drugs/DB06237) |
| Brand Names (EU) | Spedra |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 94.59% |

---

## Approved Indication (EMA)

Treatment of erectile dysfunction in adult men. In order for Spedra to be effective, sexual stimulation is required.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | amenorrhea (disease) | 94.59% | DL |
| 2 | erectile dysfunction (disease) | 93.42% | DL |
| 3 | hypoalphalipoproteinemia | 91.54% | DL |
| 4 | infectious bovine rhinotracheitis | 90.62% | DL |
| 5 | malignant catarrh | 90.62% | DL |
| 6 | Raynaud disease | 88.54% | DL |
| 7 | Ambras type hypertrichosis universalis congenita | 87.79% | DL |
| 8 | obsolete susceptibility to ischemic stroke | 87.28% | DL |
| 9 | malformation syndrome with odontal and/or periodontal component | 80.46% | DL |
| 10 | stroke disorder | 79.21% | DL |
| 11 | adrenal gland hyperfunction | 79.06% | DL |
| 12 | cytomegalovirus infection | 77.76% | DL |
| 13 | syndrome with a Dandy-Walker malformation as major feature | 77.38% | DL |
| 14 | duodenogastric reflux | 77.26% | DL |
| 15 | isolated genetic hair shaft abnormality | 76.89% | DL |
| 16 | duodenal obstruction | 75.85% | DL |
| 17 | ABri amyloidosis | 75.06% | DL |
| 18 | tinea manuum | 73.92% | DL |
| 19 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 72.34% | DL |
| 20 | hypertrichosis (disease) | 71.47% | DL |

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
