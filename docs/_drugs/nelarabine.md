---
layout: default
title: Nelarabine
description: "Nelarabine drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 396
evidence_level: L5
indication_count: 51
---

# Nelarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nelarabine |
| DrugBank ID | [DB01280](https://go.drugbank.com/drugs/DB01280) |
| Brand Names (EU) | Atriance |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.43% |

---

## Approved Indication (EMA)

Nelarabine is indicated for the treatment of patients with T-cell acute lymphoblastic leukaemia (T-ALL) and T-cell lymphoblastic lymphoma (T-LBL) whose disease has not responded to or has relapsed following treatment with at least two chemotherapy regimens. Due to the small patient populations in these disease settings, the information to support these indications is based on limited data.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 99.43% | DL |
| 2 | acute lymphoblastic/lymphocytic leukemia | 99.03% | DL |
| 3 | T-cell leukemia | 98.86% | DL |
| 4 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 98.65% | DL |
| 5 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 98.65% | DL |
| 6 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 98.27% | DL |
| 7 | Hodgkins lymphoma | 98.23% | DL |
| 8 | rhabdomyosarcoma (disease) | 98.17% | DL |
| 9 | extrahepatic bile duct rhabdomyosarcoma | 98.13% | DL |
| 10 | pancreatic adenocarcinoma | 98.07% | DL |
| 11 | embryonal extrahepatic bile duct rhabdomyosarcoma | 98.06% | DL |
| 12 | parameningeal embryonal rhabdomyosarcoma | 98.01% | DL |
| 13 | pancreatic carcinoma with mixed differentiation | 98.00% | DL |
| 14 | solid pseudopapillary carcinoma of pancreas | 97.99% | DL |
| 15 | osteoclastic giant cell tumor of pancreas | 97.99% | DL |
| 16 | Ewing sarcoma | 97.99% | DL |
| 17 | prostate embryonal rhabdomyosarcoma | 97.98% | DL |
| 18 | upper aerodigestive tract neoplasm | 97.90% | DL |
| 19 | pancreatic intraductal papillary-mucinous carcinoma | 97.90% | DL |
| 20 | mixed ductal-endocrine carcinoma of pancreas | 97.81% | DL |

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
