---
layout: default
title: Trastuzumab
description: "Trastuzumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 602
evidence_level: L5
indication_count: 50
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Trastuzumab |
| DrugBank ID | [DB00072](https://go.drugbank.com/drugs/DB00072) |
| Brand Names (EU) | Kanjinti |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.95% |

---

## Approved Indication (EMA)

Metastatic breast cancer Kanjinti is indicated for the treatment of adult patients with HER2 positive metastatic breast cancer (MBC):  as monotherapy for the treatment of those patients who have received at least two chemotherapy regimens for their metastatic disease. Prior chemotherapy must have included at least an anthracycline and a taxane unless patients are unsuitable for these treatments. Hormone-receptor positive patients must also have failed hormonal therapy, unless patients are unsuit

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 99.95% | DL |
| 2 | progesterone-receptor positive breast cancer | 99.90% | DL |
| 3 | normal breast-like subtype of breast carcinoma | 99.90% | DL |
| 4 | progesterone-receptor negative breast cancer | 99.90% | DL |
| 5 | breast tumor luminal A or B | 99.90% | DL |
| 6 | malignant cutaneous granular cell skin tumor | 99.48% | DL |
| 7 | ectomesenchymoma | 99.48% | DL |
| 8 | human herpesvirus 8-related tumor | 99.46% | DL |
| 9 | middle ear neuroendocrine tumor | 99.44% | DL |
| 10 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.04% | DL |
| 11 | prostatic urethra urothelial carcinoma | 99.04% | DL |
| 12 | esotropia | 99.02% | DL |
| 13 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.01% | DL |
| 14 | renal pelvis papillary urothelial carcinoma | 98.97% | DL |
| 15 | cervical neuroblastoma | 98.75% | DL |
| 16 | schwannoma of jugular foramen | 98.74% | DL |
| 17 | benign neoplasm of buccal mucosa | 98.73% | DL |
| 18 | inner ear neoplasm | 98.72% | DL |
| 19 | benign neoplasm of hypopharynx | 98.72% | DL |
| 20 | jugular foramen meningioma | 98.71% | DL |

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
