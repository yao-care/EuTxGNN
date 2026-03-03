---
layout: default
title: Darolutamide
description: "Darolutamide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 157
evidence_level: L5
indication_count: 50
---

# Darolutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Darolutamide |
| DrugBank ID | [DB12941](https://go.drugbank.com/drugs/DB12941) |
| Brand Names (EU) | Nubeqa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.11% |

---

## Approved Indication (EMA)

NUBEQA is indicated for the treatment of adult men with  non‑metastatic castration resistant prostate cancer (nmCRPC) who are at high risk of developing metastatic disease (see section&nbsp;5.1). metastatic hormone‑sensitive prostate cancer (mHSPC) in combination with androgen deprivation therapy (see section&nbsp;5.1). metastatic hormone‑sensitive prostate cancer (mHSPC) in combination with docetaxel and androgen deprivation therapy (see section&nbsp;5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | homozygous familial hypercholesterolemia | 99.11% | DL |
| 2 | multiple endocrine neoplasia | 99.06% | DL |
| 3 | HIV infectious disease | 99.04% | DL |
| 4 | simian immunodeficiency virus infection | 98.70% | DL |
| 5 | feline acquired immunodeficiency syndrome | 98.70% | DL |
| 6 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.56% | DL |
| 7 | cytomegalovirus infection | 98.33% | DL |
| 8 | thrombotic disease | 98.29% | DL |
| 9 | malignant catarrh | 98.18% | DL |
| 10 | infectious bovine rhinotracheitis | 98.18% | DL |
| 11 | rheumatoid arthritis | 97.64% | DL |
| 12 | Prinzmetal angina | 97.57% | DL |
| 13 | hypoalphalipoproteinemia | 97.52% | DL |
| 14 | antithrombin deficiency type 2 | 97.38% | DL |
| 15 | heparin cofactor 2 deficiency | 97.29% | DL |
| 16 | hyperthyroidism | 97.27% | DL |
| 17 | factor 5 excess with spontaneous thrombosis | 97.14% | DL |
| 18 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 97.01% | DL |
| 19 | oral candidiasis | 96.75% | DL |
| 20 | leprosy | 96.70% | DL |

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
