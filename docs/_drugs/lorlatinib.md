---
layout: default
title: Lorlatinib
description: "Lorlatinib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 353
evidence_level: L5
indication_count: 51
---

# Lorlatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lorlatinib |
| DrugBank ID | [DB12130](https://go.drugbank.com/drugs/DB12130) |
| Brand Names (EU) | Lorviqua |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.81% |

---

## Approved Indication (EMA)

Lorviqua as monotherapy is indicated for the treatment of adult patients with anaplastic lymphoma kinase (ALK)?positive advanced non?small cell lung cancer (NSCLC) previously not treated with an ALK inhibitor. Lorviqua as monotherapy is indicated for the treatment of adult patients with ALK?positive advanced NSCLC whose disease has progressed after:  alectinib or ceritinib as the first ALK tyrosine kinase inhibitor (TKI) therapy; or crizotinib and at least one other ALK TKI.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | fibromatosis, gingival | 99.81% | DL |
| 2 | fibroma of lung | 99.75% | DL |
| 3 | hamartoma of lung | 99.75% | DL |
| 4 | lung hilum carcinoma | 99.74% | DL |
| 5 | lung benign neoplasm | 99.74% | DL |
| 6 | pulmonary sulcus neoplasm | 99.73% | DL |
| 7 | lung germ cell tumor | 99.73% | DL |
| 8 | inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia | 99.72% | DL |
| 9 | junctional epidermolysis bullosa | 99.72% | DL |
| 10 | Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome | 99.69% | DL |
| 11 | ovarioleukodystrophy | 99.65% | DL |
| 12 | junctional epidermolysis bullosa, non-Herlitz type | 99.62% | DL |
| 13 | lung cancer | 99.60% | DL |
| 14 | dehydratase deficiency | 99.58% | DL |
| 15 | Ewing sarcoma | 97.61% | DL |
| 16 | amyotrohpic lateral sclerosis type 22 | 92.52% | DL |
| 17 | vertebral anomalies and variable endocrine and T-cell dysfunction | 91.92% | DL |
| 18 | ganglioneuroblastoma (disease) | 91.84% | DL |
| 19 | amyotrophic lateral sclerosis, susceptibility to | 91.26% | DL |
| 20 | axial spondylometaphyseal dysplasia | 90.54% | DL |

*Showing top 20 of 51 predictions.*

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
