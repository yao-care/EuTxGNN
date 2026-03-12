---
layout: default
title: Mogamulizumab
description: "Mogamulizumab drug repurposing predictions from TxGNN. Evidence level L5 with 58 predicted indications."
parent: AI Predictions (L5)
nav_order: 388
evidence_level: L5
indication_count: 58
---

# Mogamulizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **58**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mogamulizumab |
| DrugBank ID | [DB12498](https://go.drugbank.com/drugs/DB12498) |
| Brand Names (EU) | Poteligeo |
| Evidence Level | L5 |
| Predicted Indications | 58 |
| Top Prediction Score | 99.44% |

---

## Approved Indication (EMA)

Poteligeo is indicated for the treatment of adult patients with mycosis fungoides (MF) or Sézary syndrome (SS) who have received at least one prior systemic therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | prostatic urethra urothelial carcinoma | 99.44% | DL |
| 2 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.42% | DL |
| 3 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.40% | DL |
| 4 | renal pelvis papillary urothelial carcinoma | 99.37% | DL |
| 5 | human herpesvirus 8-related tumor | 99.24% | DL |
| 6 | ectomesenchymoma | 99.15% | DL |
| 7 | malignant cutaneous granular cell skin tumor | 99.15% | DL |
| 8 | middle ear neuroendocrine tumor | 99.00% | DL |
| 9 | transitional cell carcinoma | 98.98% | DL |
| 10 | Richter syndrome | 98.56% | DL |
| 11 | metastatic neoplasm | 98.33% | DL |
| 12 | malignant spiradenoma | 98.30% | DL |
| 13 | HER2 positive breast carcinoma | 97.67% | DL |
| 14 | cutaneous neuroendocrine carcinoma | 96.95% | DL |
| 15 | normal breast-like subtype of breast carcinoma | 96.77% | DL |
| 16 | progesterone-receptor positive breast cancer | 96.77% | DL |
| 17 | localized pagetoid reticulosis | 96.75% | DL |
| 18 | progesterone-receptor negative breast cancer | 96.71% | DL |
| 19 | breast tumor luminal A or B | 96.59% | DL |
| 20 | liver neuroendocrine carcinoma | 96.22% | DL |

*Showing top 20 of 58 predictions.*

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
