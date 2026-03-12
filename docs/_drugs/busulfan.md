---
layout: default
title: Busulfan
description: "Busulfan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 103
evidence_level: L5
indication_count: 50
---

# Busulfan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Busulfan |
| DrugBank ID | [DB01008](https://go.drugbank.com/drugs/DB01008) |
| Brand Names (EU) | Busulfan Fresenius Kabi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.62% |

---

## Approved Indication (EMA)

Busulfan Fresenius Kabi followed by cyclophosphamide (BuCy2) is indicated as conditioning treatment prior to conventional haematopoietic progenitor cell transplantation (HPCT) in adult patients when the combination is considered the best available option. Busulfan Fresenius Kabi followed by cyclophosphamide (BuCy4) or melphalan (BuMel) is indicated as conditioning treatment prior to conventional haematopoietic progenitor cell transplantation in paediatric patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myelodysplastic syndrome | 99.62% | DL |
| 2 | refractory cytopenia of childhood | 99.54% | DL |
| 3 | unclassified myelodysplastic syndrome | 99.53% | DL |
| 4 | partial deletion of the long arm of chromosome 5 | 99.51% | DL |
| 5 | aregenerative anemia | 99.49% | DL |
| 6 | severe congenital hypochromic anemia with ringed sideroblasts | 99.49% | DL |
| 7 | HIV infectious disease | 99.44% | DL |
| 8 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.22% | DL |
| 9 | seborrheic keratosis | 99.16% | DL |
| 10 | feline acquired immunodeficiency syndrome | 99.06% | DL |
| 11 | simian immunodeficiency virus infection | 99.06% | DL |
| 12 | rheumatoid arthritis | 99.04% | DL |
| 13 | obsolete familial combined hyperlipidemia | 99.02% | DL |
| 14 | female breast carcinoma | 98.86% | DL |
| 15 | primary cutaneous T-cell lymphoma | 98.84% | DL |
| 16 | vulvar inverted follicular keratosis | 98.75% | DL |
| 17 | multiple sclerosis | 98.67% | DL |
| 18 | granulomatous slack skin disease | 98.58% | DL |
| 19 | seborrheic dermatitis | 98.52% | DL |
| 20 | Crohn's colitis | 98.44% | DL |

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
