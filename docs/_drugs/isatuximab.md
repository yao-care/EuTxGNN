---
layout: default
title: Isatuximab
description: "Isatuximab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 315
evidence_level: L5
indication_count: 50
---

# Isatuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Isatuximab |
| DrugBank ID | [DB14811](https://go.drugbank.com/drugs/DB14811) |
| Brand Names (EU) | Sarclisa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.23% |

---

## Approved Indication (EMA)

SARCLISA is indicated:&nbsp;  In combination with pomalidomide and dexamethasone, for the treatment of adult patients with relapsed and refractory multiple myeloma who have received at least two prior therapies including lenalidomide and a proteasome inhibitor and have demonstrated disease progression on the last therapy. In combination with carfilzomib and dexamethasone, for the treatment of adult patients with multiple myeloma who have received at least one prior therapy. In combination with b

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | indolent plasma cell myeloma | 98.23% | DL |
| 2 | plasma cell myeloma | 97.58% | DL |
| 3 | cholangiocarcinoma, susceptibility to | 65.08% | DL |
| 4 | minimally invasive lung adenocarcinoma | 63.55% | DL |
| 5 | placenta disease | 62.84% | DL |
| 6 | GCGR-related hyperglucagonemia | 61.80% | DL |
| 7 | hemoglobin C-beta-thalassemia syndrome | 61.50% | DL |
| 8 | giant cell reparative granuloma | 59.41% | DL |
| 9 | dental caries | 58.71% | DL |
| 10 | colon inflammatory polyp | 58.71% | DL |
| 11 | epidural abscess | 58.05% | DL |
| 12 | prostate adenoid cystic carcinoma | 57.92% | DL |
| 13 | acute articular rheumatism | 57.55% | DL |
| 14 | cloacogenic carcinoma | 57.53% | DL |
| 15 | conduct disorder | 57.46% | DL |
| 16 | intraductal tubulopapillary neoplasm of pancreas | 57.36% | DL |
| 17 | renal artery obstruction | 57.22% | DL |
| 18 | mitral valve stenosis | 57.18% | DL |
| 19 | Coronavinae infectious disease | 57.13% | DL |
| 20 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 57.13% | DL |

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
