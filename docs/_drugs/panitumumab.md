---
layout: default
title: Panitumumab
description: "Panitumumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 437
evidence_level: L5
indication_count: 51
---

# Panitumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Panitumumab |
| DrugBank ID | [DB01269](https://go.drugbank.com/drugs/DB01269) |
| Brand Names (EU) | Vectibix |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.13% |

---

## Approved Indication (EMA)

Vectibix is indicated for the treatment of adult patients with wild-type RAS metastatic colorectal cancer (mCRC):  in first-line in combination with Folfox or Folfiri. in second-line in combination with Folfiri for patients who have received first-line fluoropyrimidine-based chemotherapy (excluding irinotecan). as monotherapy after failure of fluoropyrimidine-, oxaliplatin-, and irinotecan-containing chemotherapy regimens.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 99.13% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 99.05% | DL |
| 3 | diabetic retinopathy | 98.96% | DL |
| 4 | diabetic cataract | 98.90% | DL |
| 5 | nuclear senile cataract | 98.81% | DL |
| 6 | cortical cataract | 98.81% | DL |
| 7 | craniostenosis cataract | 98.77% | DL |
| 8 | mature cataract | 98.77% | DL |
| 9 | diabetes mellitus type 2 associated cataract | 98.77% | DL |
| 10 | immature cataract | 98.77% | DL |
| 11 | tetanic cataract | 98.77% | DL |
| 12 | senile cataract | 98.75% | DL |
| 13 | rectal cloacogenic carcinoma | 98.11% | DL |
| 14 | gallbladder adenosquamous carcinoma | 98.05% | DL |
| 15 | adenosquamous prostate carcinoma | 98.01% | DL |
| 16 | external ear basal cell carcinoma | 98.00% | DL |
| 17 | urethral verrucous carcinoma | 98.00% | DL |
| 18 | squamous cell carcinoma | 97.99% | DL |
| 19 | pancreatic adenosquamous carcinoma | 97.98% | DL |
| 20 | HER2 positive breast carcinoma | 97.98% | DL |

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
