---
layout: default
title: Bexarotene
description: "Bexarotene drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 79
evidence_level: L5
indication_count: 50
---

# Bexarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bexarotene |
| DrugBank ID | [DB00307](https://go.drugbank.com/drugs/DB00307) |
| Brand Names (EU) | Targretin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Targretin capsules are indicated for the treatment of skin manifestations of advanced stage cutaneous T-cell lymphoma (CTCL) patients refractory to at least one systemic treatment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary cutaneous T-cell lymphoma | 99.86% | DL |
| 2 | primary cutaneous B-cell lymphoma | 99.44% | DL |
| 3 | primary cutaneous T-cell non-Hodgkin lymphoma | 99.38% | DL |
| 4 | Sezary syndrome | 99.29% | DL |
| 5 | lymphosarcoma | 99.12% | DL |
| 6 | lymph node cancer | 98.90% | DL |
| 7 | granulomatous slack skin disease | 98.64% | DL |
| 8 | primary organ-specific lymphoma | 97.18% | DL |
| 9 | folliculotropic mycosis fungoides | 96.69% | DL |
| 10 | localized pagetoid reticulosis | 95.62% | DL |
| 11 | myelodysplastic syndrome | 95.02% | DL |
| 12 | acute lymphoblastic leukemia (disease) | 94.53% | DL |
| 13 | refractory cytopenia of childhood | 94.50% | DL |
| 14 | unclassified myelodysplastic syndrome | 94.16% | DL |
| 15 | acute lymphoblastic/lymphocytic leukemia | 93.75% | DL |
| 16 | partial deletion of the long arm of chromosome 5 | 93.69% | DL |
| 17 | T-cell prolymphocytic leukemia | 93.69% | DL |
| 18 | lymphoma | 93.63% | DL |
| 19 | Crohn's colitis | 93.63% | DL |
| 20 | lipoid nephrosis | 93.19% | DL |

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
