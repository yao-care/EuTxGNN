---
layout: default
title: Baricitinib
description: "Baricitinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 69
evidence_level: L5
indication_count: 50
---

# Baricitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Baricitinib |
| DrugBank ID | [DB11817](https://go.drugbank.com/drugs/DB11817) |
| Brand Names (EU) | Olumiant |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Rheumatoid arthritis Baricitinib is indicated for the treatment of moderate to severe active rheumatoid arthritis in adult patients who have responded inadequately to, or who are intolerant to one or more disease modifying anti rheumatic drugs (DMARDs). Olumiant may be used as monotherapy or in combination with methotrexate. Atopic Dermatitis Olumiant is indicated for the treatment of moderate to severe atopic dermatitis in adult and paediatric patients 2 years of age and older who are candidate

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.97% | DL |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | DL |
| 3 | brachydactyly-syndactyly syndrome | 99.94% | DL |
| 4 | indolent plasma cell myeloma | 93.31% | DL |
| 5 | WHIM syndrome | 93.12% | DL |
| 6 | plasma cell myeloma | 91.83% | DL |
| 7 | myeloid leukemia | 91.01% | DL |
| 8 | Meester-Loeys syndrome | 88.21% | DL |
| 9 | ganglioneuroblastoma (disease) | 87.59% | DL |
| 10 | heparin cofactor 2 deficiency | 86.31% | DL |
| 11 | vertebral anomalies and variable endocrine and T-cell dysfunction | 84.68% | DL |
| 12 | retroperitoneal neoplasm | 84.34% | DL |
| 13 | osteoarthritis susceptibility | 83.87% | DL |
| 14 | factor 5 excess with spontaneous thrombosis | 82.80% | DL |
| 15 | antithrombin deficiency type 2 | 81.73% | DL |
| 16 | stroke disorder | 79.21% | DL |
| 17 | neuroblastoma | 79.17% | DL |
| 18 | amyotrohpic lateral sclerosis type 22 | 77.92% | DL |
| 19 | amyotrophic lateral sclerosis, susceptibility to | 77.39% | DL |
| 20 | amyotrophic lateral sclerosis | 74.66% | DL |

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
