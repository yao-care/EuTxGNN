---
layout: default
title: Pertuzumab
description: "pertuzumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 456
evidence_level: L5
indication_count: 50
---

# Pertuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pertuzumab |
| DrugBank ID | [DB06366](https://go.drugbank.com/drugs/DB06366) |
| Brand Names (EU) | Perjeta |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Early breast cancer (EBC) Phesgo is indicated for use in combination with chemotherapy in:  the neoadjuvant treatment of adult patients with HER2-positive, locally advanced, inflammatory, or early stage breast cancer at high risk of recurrence the adjuvant treatment of adult patients with HER2-positive early breast cancer at high risk of recurrence  Metastatic breast cancer (MBC) Phesgo is indicated for use in combination with docetaxel in adult patients with HER2-positive metastatic or locally 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 99.97% | DL |
| 2 | normal breast-like subtype of breast carcinoma | 99.93% | DL |
| 3 | progesterone-receptor positive breast cancer | 99.93% | DL |
| 4 | progesterone-receptor negative breast cancer | 99.93% | DL |
| 5 | breast tumor luminal A or B | 99.93% | DL |
| 6 | ectomesenchymoma | 99.71% | DL |
| 7 | malignant cutaneous granular cell skin tumor | 99.71% | DL |
| 8 | human herpesvirus 8-related tumor | 99.70% | DL |
| 9 | middle ear neuroendocrine tumor | 99.68% | DL |
| 10 | prostatic urethra urothelial carcinoma | 99.51% | DL |
| 11 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.51% | DL |
| 12 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.49% | DL |
| 13 | renal pelvis papillary urothelial carcinoma | 99.47% | DL |
| 14 | esotropia | 99.45% | DL |
| 15 | drug-induced osteoporosis | 99.33% | DL |
| 16 | cervical neuroblastoma | 99.18% | DL |
| 17 | schwannoma of jugular foramen | 99.18% | DL |
| 18 | inner ear neoplasm | 99.18% | DL |
| 19 | benign neoplasm of buccal mucosa | 99.17% | DL |
| 20 | benign neoplasm of hypopharynx | 99.17% | DL |

*Showing top 20 of 50 predictions.*

---


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
