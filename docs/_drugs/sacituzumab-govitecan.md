---
layout: default
title: Sacituzumab Govitecan
description: "Sacituzumab Govitecan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 513
evidence_level: L5
indication_count: 50
---

# Sacituzumab Govitecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sacituzumab Govitecan |
| DrugBank ID | [DB12893](https://go.drugbank.com/drugs/DB12893) |
| Brand Names (EU) | Trodelvy |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.78% |

---

## Approved Indication (EMA)

Trodelvy as monotherapy is indicated for the treatment of adult patients with unresectable or metastatic triple-negative breast cancer (mTNBC) who have received two or more prior systemic therapies, including at least one of them for advanced disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 99.78% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 99.69% | DL |
| 3 | diabetic retinopathy | 99.60% | DL |
| 4 | diabetic cataract | 99.12% | DL |
| 5 | cortical cataract | 98.55% | DL |
| 6 | nuclear senile cataract | 98.55% | DL |
| 7 | senile cataract | 98.52% | DL |
| 8 | diabetes mellitus type 2 associated cataract | 98.40% | DL |
| 9 | immature cataract | 98.40% | DL |
| 10 | tetanic cataract | 98.40% | DL |
| 11 | craniostenosis cataract | 98.40% | DL |
| 12 | mature cataract | 98.40% | DL |
| 13 | respiratory syncytial virus infectious disease | 97.82% | DL |
| 14 | dry eye syndrome | 97.49% | DL |
| 15 | hemorrhagic disease of newborn | 97.45% | DL |
| 16 | non-syndromic visceral malformation | 97.39% | DL |
| 17 | non-seminomatous lesion | 97.33% | DL |
| 18 | ductal or ductular proliferation | 97.33% | DL |
| 19 | bronchial adenomas/carcinoids childhood | 97.33% | DL |
| 20 | chondroid hamartoma | 97.33% | DL |

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
