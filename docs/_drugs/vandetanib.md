---
layout: default
title: Vandetanib
description: "Vandetanib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 621
evidence_level: L5
indication_count: 50
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vandetanib |
| DrugBank ID | [DB05294](https://go.drugbank.com/drugs/DB05294) |
| Brand Names (EU) | Caprelsa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Caprelsa is indicated for the treatment of aggressive and symptomatic medullary thyroid cancer (MTC) in patients with unresectable locally advanced or metastatic disease. Caprelsa is indicated in adults, children and adolescents aged 5 years and older. For patients in whom re-arranged-during-transfection(RET) mutation is not known or is negative, a possible lower benefit should be taken into account before individual treatment decision.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | renal cell carcinoma (disease) | 99.92% | DL |
| 2 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.90% | DL |
| 3 | unclassified renal cell carcinoma | 99.90% | DL |
| 4 | renal cell carcinoma associated with neuroblastoma | 99.90% | DL |
| 5 | renal pelvis carcinoma | 99.88% | DL |
| 6 | clear cell renal carcinoma | 99.87% | DL |
| 7 | childhood kidney cell carcinoma | 99.86% | DL |
| 8 | renal carcinoma | 99.83% | DL |
| 9 | angiolipoma | 99.82% | DL |
| 10 | familial spontaneous pneumothorax | 99.76% | DL |
| 11 | endocrine-cerebro-osteodysplasia syndrome | 99.73% | DL |
| 12 | nonpapillary renal cell carcinoma | 99.70% | DL |
| 13 | sarcomatoid renal cell carcinoma | 99.68% | DL |
| 14 | chromophobe renal cell carcinoma | 99.68% | DL |
| 15 | collecting duct carcinoma | 99.62% | DL |
| 16 | liposarcoma | 99.49% | DL |
| 17 | ovarian myxoid liposarcoma | 99.38% | DL |
| 18 | acquired cystic disease-associated renal cell carcinoma | 99.29% | DL |
| 19 | cystic renal cell carcinoma | 99.29% | DL |
| 20 | kidney medullary carcinoma | 99.29% | DL |

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
