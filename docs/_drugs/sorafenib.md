---
layout: default
title: Sorafenib
description: "Sorafenib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 540
evidence_level: L5
indication_count: 51
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sorafenib |
| DrugBank ID | [DB00398](https://go.drugbank.com/drugs/DB00398) |
| Brand Names (EU) | Nexavar |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

Hepatocellular carcinoma Nexavar is indicated for the treatment of hepatocellular carcinoma. Renal cell carcinoma Nexavar is indicated for the treatment of patients with advanced renal cell carcinoma who have failed prior interferon-alpha or interleukin-2 based therapy or are considered unsuitable for such therapy. Differentiated thyroid carcinoma Nexavar is indicated for the treatment of patients with progressive, locally advanced or metastatic, differentiated (papillary/follicular/Hürthle cell

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | liposarcoma | 99.82% | DL |
| 2 | ovarian myxoid liposarcoma | 99.76% | DL |
| 3 | clear cell renal carcinoma | 99.73% | DL |
| 4 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.65% | DL |
| 5 | unclassified renal cell carcinoma | 99.65% | DL |
| 6 | renal cell carcinoma associated with neuroblastoma | 99.65% | DL |
| 7 | childhood kidney cell carcinoma | 99.57% | DL |
| 8 | renal cell carcinoma (disease) | 99.57% | DL |
| 9 | female breast carcinoma | 99.53% | DL |
| 10 | renal pelvis carcinoma | 99.40% | DL |
| 11 | vulva sarcoma | 99.37% | DL |
| 12 | dermatofibrosarcoma protuberans | 99.35% | DL |
| 13 | angiolipoma | 99.29% | DL |
| 14 | renal carcinoma | 99.28% | DL |
| 15 | spindle cell liposarcoma | 99.25% | DL |
| 16 | heart fibrosarcoma | 99.19% | DL |
| 17 | fibroblastic neoplasm | 99.16% | DL |
| 18 | kidney fibrosarcoma | 99.14% | DL |
| 19 | childhood malignant neoplasm | 99.12% | DL |
| 20 | conventional fibrosarcoma | 99.09% | DL |

*Showing top 20 of 51 predictions.*

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
