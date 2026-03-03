---
layout: default
title: Estradiol
description: "Estradiol drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 228
evidence_level: L5
indication_count: 53
---

# Estradiol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Estradiol |
| DrugBank ID | [DB00783](https://go.drugbank.com/drugs/DB00783) |
| Brand Names (EU) | Estradiol, Zoely |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Oral contraception

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acne (disease) | 99.96% | DL |
| 2 | symptomatic form of fragile X syndrome in female carrier | 98.76% | DL |
| 3 | ovarian remnant syndrome | 98.58% | DL |
| 4 | anovulation | 98.58% | DL |
| 5 | partial trisomy/tetrasomy of the short arm of chromosome 18 | 98.56% | DL |
| 6 | partial trisomy/tetrasomy of the short arm of chromosome 12 | 98.56% | DL |
| 7 | partial trisomy/tetrasomy of the short arm of chromosome 5 | 98.54% | DL |
| 8 | blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | 98.52% | DL |
| 9 | luteoma of pregnancy | 98.47% | DL |
| 10 | partial autosomal trisomy/tetrasomy | 98.45% | DL |
| 11 | ovarian ectopic pregnancy | 98.44% | DL |
| 12 | primary ovarian failure | 98.44% | DL |
| 13 | blepharophimosis-epicanthus inversus-ptosis | 98.41% | DL |
| 14 | ovarian dysfunction | 98.36% | DL |
| 15 | zinc, elevated plasma | 98.23% | DL |
| 16 | stapes ankylosis with broad thumbs and toes | 98.15% | DL |
| 17 | telecanthus | 98.15% | DL |
| 18 | ovarian hyperstimulation syndrome | 97.48% | DL |
| 19 | sebaceous gland anomaly | 94.61% | DL |
| 20 | pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 93.17% | DL |

*Showing top 20 of 53 predictions.*

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
