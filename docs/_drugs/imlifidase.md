---
layout: default
title: Imlifidase
description: "Imlifidase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 297
evidence_level: L5
indication_count: 50
---

# Imlifidase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Imlifidase |
| DrugBank ID | [DB15258](https://go.drugbank.com/drugs/DB15258) |
| Brand Names (EU) | Idefirix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.75% |

---

## Approved Indication (EMA)

Idefirix is indicated for desensitisation treatment of highly sensitised adult kidney transplant patients with positive crossmatch against an available deceased donor. The use of Idefirix should be reserved for patients unlikely to be transplanted under the available kidney allocation system including prioritisation programmes for highly sensitised patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 98.75% | DL |
| 2 | immature cataract | 98.69% | DL |
| 3 | mature cataract | 98.69% | DL |
| 4 | craniostenosis cataract | 98.69% | DL |
| 5 | tetanic cataract | 98.69% | DL |
| 6 | diabetes mellitus type 2 associated cataract | 98.69% | DL |
| 7 | nuclear senile cataract | 98.67% | DL |
| 8 | cortical cataract | 98.67% | DL |
| 9 | senile cataract | 98.61% | DL |
| 10 | diabetic retinopathy | 98.48% | DL |
| 11 | severe nonproliferative diabetic retinopathy | 98.25% | DL |
| 12 | antithrombin deficiency type 2 | 97.26% | DL |
| 13 | factor 5 excess with spontaneous thrombosis | 97.14% | DL |
| 14 | heparin cofactor 2 deficiency | 97.07% | DL |
| 15 | gastric carcinoma | 96.90% | DL |
| 16 | thrombophilia | 96.80% | DL |
| 17 | diffuse gastric adenocarcinoma | 96.79% | DL |
| 18 | drug-induced osteoporosis | 96.57% | DL |
| 19 | gastric adenocarcinoma and proximal polyposis of the stomach | 96.15% | DL |
| 20 | gastric cardia adenocarcinoma | 96.08% | DL |

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
