---
layout: default
title: Paclitaxel
description: "paclitaxel drug repurposing predictions from TxGNN. Evidence level L2 with 71 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 432
evidence_level: L2
indication_count: 71
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **71**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Paclitaxel |
| DrugBank ID | [DB01229](https://go.drugbank.com/drugs/DB01229) |
| Brand Names (EU) | Abraxane, Apexelsin, Naveruclif, Pazenir |
| Evidence Level | L2 |
| Predicted Indications | 71 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Apexelsin monotherapy is indicated for the treatment of metastatic breast cancer in adult patients who have failed first-line treatment for metastatic disease and for whom standard, anthracycline containing therapy is not indicated. Apexelsin in combination with gemcitabine is indicated for the first-line treatment of adult patients with metastatic adenocarcinoma of the pancreas. Apexelsin in combination with carboplatin is indicated for the first-line treatment of non-small cell lung cancer in 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | female breast carcinoma | 100.00% | DL |
| 2 | hereditary breast ovarian cancer syndrome | 99.95% | DL |
| 3 | estrogen-receptor negative breast cancer | 99.91% | DL |
| 4 | Ehrlich tumor carcinoma | 99.91% | DL |
| 5 | hormone-resistant breast carcinoma | 99.91% | DL |
| 6 | estrogen-receptor positive breast cancer | 99.91% | DL |
| 7 | bilateral breast carcinoma | 99.89% | DL |
| 8 | breast carcinoma by gene expression profile | 99.89% | DL |
| 9 | nipple carcinoma | 99.89% | DL |
| 10 | ovarian clear cell adenocarcinoma | 99.88% | DL |
| 11 | parameningeal embryonal rhabdomyosarcoma | 99.73% | DL |
| 12 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.73% | DL |
| 13 | borderline epithelial tumor of ovary | 99.72% | DL |
| 14 | rhabdomyosarcoma (disease) | 99.72% | DL |
| 15 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.71% | DL |
| 16 | prostate embryonal rhabdomyosarcoma | 99.69% | DL |
| 17 | maligant granulosa cell tumor of ovary | 99.66% | DL |
| 18 | Ewing sarcoma | 99.66% | DL |
| 19 | extrahepatic bile duct rhabdomyosarcoma | 99.66% | DL |
| 20 | ovarian endometrioid adenocarcinoma | 99.65% | DL |

*Showing top 20 of 71 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| female breast carcinoma | L2 | 20 | 0 | 2 Phase 3 trial(s), 8 Phase 2 trial(s) |

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
