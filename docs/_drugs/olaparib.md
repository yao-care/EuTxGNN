---
layout: default
title: Olaparib
description: "Olaparib drug repurposing predictions from TxGNN. Evidence level L5 with 54 predicted indications."
parent: AI Predictions (L5)
nav_order: 419
evidence_level: L5
indication_count: 54
---

# Olaparib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **54**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Olaparib |
| DrugBank ID | [DB09074](https://go.drugbank.com/drugs/DB09074) |
| Brand Names (EU) | Lynparza |
| Evidence Level | L5 |
| Predicted Indications | 54 |
| Top Prediction Score | 99.66% |

---

## Approved Indication (EMA)

Ovarian cancer Lynparza is indicated as monotherapy for the:  maintenance treatment of adult patients with advanced (FIGO stages III and IV) BRCA1/2-mutated (germline and/or somatic) high-grade epithelial ovarian, fallopian tube or primary peritoneal cancer who are in response (complete or partial) following completion of first-line platinum-based chemotherapy. maintenance treatment of adult patients with platinum sensitive relapsed high grade epithelial ovarian, fallopian tube, or primary perit

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | borderline epithelial tumor of ovary | 99.66% | DL |
| 2 | ovarian clear cell adenocarcinoma | 99.28% | DL |
| 3 | malignant dysgerminomatous germ cell tumor of ovary | 99.22% | DL |
| 4 | hereditary site-specific ovarian cancer syndrome | 99.12% | DL |
| 5 | female breast carcinoma | 99.09% | DL |
| 6 | gonadal germ cell tumor | 98.95% | DL |
| 7 | ovarian primitive germ cell tumor | 98.95% | DL |
| 8 | choriocarcinoma of ovary | 98.91% | DL |
| 9 | malignant sex cord stromal tumor of ovary | 98.79% | DL |
| 10 | ovarian neoplasm | 98.75% | DL |
| 11 | familial ovarian cancer | 98.74% | DL |
| 12 | hereditary breast ovarian cancer syndrome | 98.67% | DL |
| 13 | ovarian adenocarcinoma | 98.67% | DL |
| 14 | yolk sac tumor | 98.62% | DL |
| 15 | maligant granulosa cell tumor of ovary | 98.52% | DL |
| 16 | ovarian malignant mesothelioma | 98.36% | DL |
| 17 | malignant non-epithelial tumor of ovary | 98.28% | DL |
| 18 | ovarian cancer, susceptibility to, 1 | 98.27% | DL |
| 19 | ovarian adenosarcoma | 98.27% | DL |
| 20 | theca steroid-producing cell malignant tumor of ovary, not further specified | 98.24% | DL |

*Showing top 20 of 54 predictions.*

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
