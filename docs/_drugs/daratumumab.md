---
layout: default
title: Daratumumab
description: "Daratumumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 154
evidence_level: L5
indication_count: 50
---

# Daratumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Daratumumab |
| DrugBank ID | [DB09331](https://go.drugbank.com/drugs/DB09331) |
| Brand Names (EU) | Darzalex |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.13% |

---

## Approved Indication (EMA)

Multiple Myeloma&nbsp; Darzalex&nbsp;is&nbsp;indicated:  in combination with lenalidomide and dexamethasone&nbsp;or&nbsp;with&nbsp;bortezomib,&nbsp;melphalan&nbsp;and prednisone for the treatment of adult patients with newly diagnosed multiple myeloma who are ineligible for autologous stem cell transplant. in&nbsp;combination&nbsp;with&nbsp;bortezomib,&nbsp;lenalidomide&nbsp;and dexamethasone for the treatment of adult patients with newly diagnosed multiple myeloma. in&nbsp;combination&nbsp;with

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | indolent plasma cell myeloma | 98.13% | DL |
| 2 | plasma cell myeloma | 97.44% | DL |
| 3 | cholangiocarcinoma, susceptibility to | 65.06% | DL |
| 4 | placenta disease | 62.82% | DL |
| 5 | minimally invasive lung adenocarcinoma | 62.75% | DL |
| 6 | GCGR-related hyperglucagonemia | 61.81% | DL |
| 7 | hemoglobin C-beta-thalassemia syndrome | 61.49% | DL |
| 8 | giant cell reparative granuloma | 59.40% | DL |
| 9 | colon inflammatory polyp | 58.73% | DL |
| 10 | dental caries | 58.69% | DL |
| 11 | epidural abscess | 58.08% | DL |
| 12 | prostate adenoid cystic carcinoma | 57.95% | DL |
| 13 | cloacogenic carcinoma | 57.57% | DL |
| 14 | acute articular rheumatism | 57.56% | DL |
| 15 | conduct disorder | 57.44% | DL |
| 16 | intraductal tubulopapillary neoplasm of pancreas | 57.37% | DL |
| 17 | renal artery obstruction | 57.25% | DL |
| 18 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 57.22% | DL |
| 19 | Coronavinae infectious disease | 57.21% | DL |
| 20 | mitral valve stenosis | 57.14% | DL |

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
