---
layout: default
title: Regorafenib
description: "Regorafenib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 484
evidence_level: L5
indication_count: 51
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Regorafenib |
| DrugBank ID | [DB08896](https://go.drugbank.com/drugs/DB08896) |
| Brand Names (EU) | Stivarga |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.76% |

---

## Approved Indication (EMA)

Stivarga is indicated as monotherapy for the treatment of adult patients with:  metastatic colorectal cancer (CRC) who have been previously treated with, or are not considered candidates for, available therapies - these include fluoropyrimidine-based chemotherapy, an anti-VEGF therapy and an anti-EGFR therapy; unresectable or metastatic gastrointestinal stromal tumors (GIST) who progressed on or are intolerant to prior treatment with imatinib and sunitinib; hepatocellular carcinoma (HCC) who hav

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | liposarcoma | 99.76% | DL |
| 2 | ovarian myxoid liposarcoma | 99.68% | DL |
| 3 | clear cell renal carcinoma | 99.47% | DL |
| 4 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.24% | DL |
| 5 | unclassified renal cell carcinoma | 99.24% | DL |
| 6 | renal cell carcinoma associated with neuroblastoma | 99.24% | DL |
| 7 | childhood kidney cell carcinoma | 99.07% | DL |
| 8 | vulva sarcoma | 99.06% | DL |
| 9 | spindle cell liposarcoma | 98.85% | DL |
| 10 | adenocarcinoma of liver and intrahepatic biliary tract | 98.76% | DL |
| 11 | undifferentiated carcinoma of liver and intrahepatic biliary tract | 98.74% | DL |
| 12 | renal cell carcinoma (disease) | 98.67% | DL |
| 13 | renal carcinoma | 98.61% | DL |
| 14 | angiolipoma | 98.60% | DL |
| 15 | amyotrophic lateral sclerosis | 98.52% | DL |
| 16 | extrahepatic bile duct adenocarcinoma | 98.45% | DL |
| 17 | amyotrohpic lateral sclerosis type 22 | 98.40% | DL |
| 18 | breast fibroadenoma | 98.38% | DL |
| 19 | amyotrophic lateral sclerosis, susceptibility to | 98.37% | DL |
| 20 | pleomorphic adenoma | 98.35% | DL |

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
