---
layout: default
title: Apalutamide
description: "Apalutamide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 43
evidence_level: L5
indication_count: 51
---

# Apalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Apalutamide |
| DrugBank ID | [DB11901](https://go.drugbank.com/drugs/DB11901) |
| Brand Names (EU) | Erleada |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.43% |

---

## Approved Indication (EMA)

Erleada is indicated:  in adult men for the treatment of non metastatic castration resistant prostate cancer (nmCRPC) who are at high risk of developing metastatic disease. in adult men for the treatment of metastatic hormone-sensitive prostate cancer (mHSPC) in combination with androgen deprivation therapy (ADT).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | prostate cancer/brain cancer susceptibility | 98.43% | DL |
| 2 | prostate leiomyoma | 97.77% | DL |
| 3 | Brenner tumor | 97.58% | DL |
| 4 | prostate cancer | 97.56% | DL |
| 5 | benign reproductive system neoplasm | 97.52% | DL |
| 6 | fibroma of prostate | 97.50% | DL |
| 7 | prostate phyllodes tumor | 97.46% | DL |
| 8 | benign neoplasm of prostate | 97.45% | DL |
| 9 | male reproductive organ cancer | 97.41% | DL |
| 10 | benign prostate phyllodes tumor | 97.21% | DL |
| 11 | palmoplantar keratoderma-sclerodactyly syndrome | 97.05% | DL |
| 12 | female breast carcinoma | 96.67% | DL |
| 13 | peripheral neuropathy-myopathy-hoarseness-hearing loss syndrome | 96.07% | DL |
| 14 | renal cell carcinoma (disease) | 94.46% | DL |
| 15 | renal pelvis carcinoma | 94.27% | DL |
| 16 | CMM7 | 93.85% | DL |
| 17 | renal carcinoma | 93.68% | DL |
| 18 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 93.63% | DL |
| 19 | renal cell carcinoma associated with neuroblastoma | 93.63% | DL |
| 20 | unclassified renal cell carcinoma | 93.63% | DL |

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
