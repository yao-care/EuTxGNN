---
layout: default
title: Teriflunomide
description: "Teriflunomide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 572
evidence_level: L5
indication_count: 50
---

# Teriflunomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Teriflunomide |
| DrugBank ID | [DB08880](https://go.drugbank.com/drugs/DB08880) |
| Brand Names (EU) | Aubagio |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.24% |

---

## Approved Indication (EMA)

AUBAGIO is indicated for the treatment of adult patients and paediatric patients aged 10 years and older with relapsing remitting multiple sclerosis (MS) (please refer to section 5.1 for important information on the population for which efficacy has been established).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 99.24% | DL |
| 2 | marcothrombocytopenia with mitral valve insufficiency | 98.13% | DL |
| 3 | hereditary thrombocytopenia with normal platelets | 98.13% | DL |
| 4 | transient neonatal thrombocytopenia | 98.10% | DL |
| 5 | thrombocytopenia | 98.01% | DL |
| 6 | dense granule disease | 97.80% | DL |
| 7 | penile fibromatosis | 97.28% | DL |
| 8 | Ledderhose disease | 97.23% | DL |
| 9 | multiple sclerosis | 97.17% | DL |
| 10 | chronic hepatitis C virus infection | 97.04% | DL |
| 11 | palmar fibromatosis | 96.86% | DL |
| 12 | CMM7 | 96.80% | DL |
| 13 | pediatric leptomeningeal melanoma | 96.72% | DL |
| 14 | melanoma | 96.69% | DL |
| 15 | epithelioid cell uveal melanoma | 96.65% | DL |
| 16 | progressive relapsing multiple sclerosis | 96.60% | DL |
| 17 | colonic neoplasm | 96.56% | DL |
| 18 | infantile digital fibromatosis | 96.50% | DL |
| 19 | cecum villous adenoma | 96.44% | DL |
| 20 | rectosigmoid junction neoplasm | 96.43% | DL |

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
