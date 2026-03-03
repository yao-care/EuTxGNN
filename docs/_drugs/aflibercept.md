---
layout: default
title: Aflibercept
description: "Aflibercept drug repurposing predictions from TxGNN. Evidence level L5 with 54 predicted indications."
parent: AI Predictions (L5)
nav_order: 21
evidence_level: L5
indication_count: 54
---

# Aflibercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **54**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aflibercept |
| DrugBank ID | [DB08885](https://go.drugbank.com/drugs/DB08885) |
| Brand Names (EU) | Eyluxvi, Opuviz, Yesafili, Zaltrap |
| Evidence Level | L5 |
| Predicted Indications | 54 |
| Top Prediction Score | 99.38% |

---

## Approved Indication (EMA)

Treatment of metastatic colorectal cancer (MCRC).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | esotropia | 99.38% | DL |
| 2 | esophageal varices with bleeding | 97.56% | DL |
| 3 | esophageal varices without bleeding | 97.56% | DL |
| 4 | varicose disease | 96.95% | DL |
| 5 | urethral calculus | 95.97% | DL |
| 6 | adenosine deaminase deficiency | 95.76% | DL |
| 7 | hemorrhagic disease of newborn | 95.56% | DL |
| 8 | ectomesenchymoma | 94.52% | DL |
| 9 | malignant cutaneous granular cell skin tumor | 94.51% | DL |
| 10 | middle ear neuroendocrine tumor | 94.42% | DL |
| 11 | reticular dysgenesis | 94.34% | DL |
| 12 | severe combined immunodeficiency due to LCK deficiency | 94.19% | DL |
| 13 | human herpesvirus 8-related tumor | 94.13% | DL |
| 14 | lung fibrosis-immunodeficiency-46,XX gonadal dysgenesis syndrome | 93.68% | DL |
| 15 | non-severe combined immunodeficiency | 93.24% | DL |
| 16 | T-B+ severe combined immunodeficiency due to CD45 deficiency | 93.07% | DL |
| 17 | anemia of prematurity | 93.01% | DL |
| 18 | T-B+ severe combined immunodeficiency due to gamma chain deficiency | 93.00% | DL |
| 19 | Immunoerythromyeloid hypoplasia | 92.99% | DL |
| 20 | lipoma of the conjunctiva | 92.45% | DL |

*Showing top 20 of 54 predictions.*

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
