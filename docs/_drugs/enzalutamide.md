---
layout: default
title: Enzalutamide
description: "Enzalutamide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 215
evidence_level: L5
indication_count: 51
---

# Enzalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Enzalutamide |
| DrugBank ID | [DB08899](https://go.drugbank.com/drugs/DB08899) |
| Brand Names (EU) | Enzalutamide Accordpharma, Xtandi |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Treatment of prostate cancer.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | prostate cancer/brain cancer susceptibility | 99.71% | DL |
| 2 | prostate leiomyoma | 99.57% | DL |
| 3 | Brenner tumor | 99.55% | DL |
| 4 | fibroma of prostate | 99.53% | DL |
| 5 | benign reproductive system neoplasm | 99.53% | DL |
| 6 | male reproductive organ cancer | 99.51% | DL |
| 7 | benign prostate phyllodes tumor | 99.48% | DL |
| 8 | prostate cancer | 98.50% | DL |
| 9 | benign neoplasm of prostate | 98.37% | DL |
| 10 | prostate neoplasm | 98.37% | DL |
| 11 | prostate phyllodes tumor | 98.37% | DL |
| 12 | nonpapillary renal cell carcinoma | 98.08% | DL |
| 13 | palmoplantar keratoderma-sclerodactyly syndrome | 98.05% | DL |
| 14 | female breast carcinoma | 97.53% | DL |
| 15 | renal carcinoma | 97.53% | DL |
| 16 | peripheral neuropathy-myopathy-hoarseness-hearing loss syndrome | 97.53% | DL |
| 17 | liposarcoma | 97.30% | DL |
| 18 | renal cell carcinoma (disease) | 97.27% | DL |
| 19 | renal cell carcinoma associated with neuroblastoma | 97.12% | DL |
| 20 | unclassified renal cell carcinoma | 97.12% | DL |

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
