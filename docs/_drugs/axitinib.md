---
layout: default
title: Axitinib
description: "axitinib drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 63
evidence_level: L2
indication_count: 50
---

# Axitinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Axitinib |
| DrugBank ID | [DB06626](https://go.drugbank.com/drugs/DB06626) |
| Brand Names (EU) | Inlyta |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Inlyta is indicated for the treatment of adult patients with advanced renal cell carcinoma (RCC) after failure of prior treatment with sunitinib or a cytokine.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | clear cell renal carcinoma | 99.94% | DL |
| 2 | renal cell carcinoma associated with neuroblastoma | 99.90% | DL |
| 3 | unclassified renal cell carcinoma | 99.90% | DL |
| 4 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.90% | DL |
| 5 | childhood kidney cell carcinoma | 99.87% | DL |
| 6 | liposarcoma | 99.87% | DL |
| 7 | renal carcinoma | 99.85% | DL |
| 8 | ovarian myxoid liposarcoma | 99.84% | DL |
| 9 | renal cell carcinoma (disease) | 99.83% | DL |
| 10 | angiolipoma | 99.83% | DL |
| 11 | collecting duct carcinoma | 99.81% | DL |
| 12 | familial spontaneous pneumothorax | 99.78% | DL |
| 13 | endocrine-cerebro-osteodysplasia syndrome | 99.77% | DL |
| 14 | renal pelvis carcinoma | 99.74% | DL |
| 15 | chromophobe renal cell carcinoma | 99.70% | DL |
| 16 | nonpapillary renal cell carcinoma | 99.69% | DL |
| 17 | sarcomatoid renal cell carcinoma | 99.69% | DL |
| 18 | adenocarcinoma of liver and intrahepatic biliary tract | 99.68% | DL |
| 19 | spindle cell liposarcoma | 99.62% | DL |
| 20 | undifferentiated carcinoma of liver and intrahepatic biliary tract | 99.60% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| clear cell renal carcinoma | L2 | 20 | 13 | 1 Phase 3 trial(s), 12 Phase 2 trial(s), 1 review( |

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
