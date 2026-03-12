---
layout: default
title: Avelumab
description: "Avelumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 60
evidence_level: L5
indication_count: 50
---

# Avelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Avelumab |
| DrugBank ID | [DB11945](https://go.drugbank.com/drugs/DB11945) |
| Brand Names (EU) | Bavencio |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Bavencio is indicated as monotherapy for the treatment of adult patients with metastatic Merkel cell carcinoma (MCC). Bavencio in combination with axitinib is indicated for the first-line treatment of adult patients with advanced renal cell carcinoma (RCC). Bavencio is indicated as monotherapy for the first?line maintenance treatment of adult patients with locally advanced or metastatic urothelial carcinoma (UC) who are progression-free following platinum?based chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | human herpesvirus 8-related tumor | 99.97% | DL |
| 2 | middle ear neuroendocrine tumor | 99.97% | DL |
| 3 | malignant cutaneous granular cell skin tumor | 99.97% | DL |
| 4 | ectomesenchymoma | 99.97% | DL |
| 5 | adenosine deaminase deficiency | 99.95% | DL |
| 6 | reticular dysgenesis | 99.94% | DL |
| 7 | Immunoerythromyeloid hypoplasia | 99.94% | DL |
| 8 | non-severe combined immunodeficiency | 99.92% | DL |
| 9 | prostatic urethra urothelial carcinoma | 99.92% | DL |
| 10 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.91% | DL |
| 11 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.91% | DL |
| 12 | renal pelvis papillary urothelial carcinoma | 99.91% | DL |
| 13 | lung fibrosis-immunodeficiency-46,XX gonadal dysgenesis syndrome | 99.90% | DL |
| 14 | severe combined immunodeficiency due to LCK deficiency | 99.90% | DL |
| 15 | T-B+ severe combined immunodeficiency due to gamma chain deficiency | 99.89% | DL |
| 16 | T-B+ severe combined immunodeficiency due to CD45 deficiency | 99.88% | DL |
| 17 | severe combined immunodeficiency (disease) | 99.87% | DL |
| 18 | combined immunodeficiency, X-linked | 99.87% | DL |
| 19 | glottis verrucous carcinoma | 99.85% | DL |
| 20 | severe combined immunodeficiency, autosomal recessive, T cell-negative, B cell-negative, NK cell-positive | 99.85% | DL |

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
