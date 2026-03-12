---
layout: default
title: Melphalan Hydrochloride
description: "Melphalan Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 367
evidence_level: L5
indication_count: 50
---

# Melphalan Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Melphalan Hydrochloride |
| DrugBank ID | [DB01042](https://go.drugbank.com/drugs/DB01042) |
| Brand Names (EU) | Phelinun |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

High-dose of Phelinun used alone or in combination with other cytotoxic medicinal products and/or total body irradiation is indicated in the treatment of:  multiple myeloma, malignant lymphoma (Hodgkin, non-Hodgkin lymphoma), acute lymphoblastic and myeloblastic leukemia, childhood neuroblastoma, ovarian cancer, mammary adenocarcinoma.  Phelinun in combination with other cytotoxic medicinal products is indicated as reduced intensity conditioning (RIC) treatment prior to allogeneic haematopoietic

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hereditary breast ovarian cancer syndrome | 99.94% | DL |
| 2 | malignant dysgerminomatous germ cell tumor of ovary | 99.87% | DL |
| 3 | ovarian clear cell adenocarcinoma | 99.84% | DL |
| 4 | primary non-gestational choriocarcinoma of ovary | 99.84% | DL |
| 5 | maligant granulosa cell tumor of ovary | 99.81% | DL |
| 6 | hereditary site-specific ovarian cancer syndrome | 99.78% | DL |
| 7 | borderline epithelial tumor of ovary | 99.77% | DL |
| 8 | gonadal germ cell tumor | 99.77% | DL |
| 9 | ovarian primitive germ cell tumor | 99.75% | DL |
| 10 | choriocarcinoma of ovary | 99.74% | DL |
| 11 | female breast carcinoma | 99.67% | DL |
| 12 | ovarian mucinous adenocarcinoma | 99.61% | DL |
| 13 | malignant sex cord stromal tumor of ovary | 99.58% | DL |
| 14 | malignant non-epithelial tumor of ovary | 99.55% | DL |
| 15 | malignant germ cell tumor of ovary | 99.49% | DL |
| 16 | familial ovarian cancer | 99.44% | DL |
| 17 | ovarian endometrioid adenocarcinoma | 99.44% | DL |
| 18 | ovarian small cell carcinoma | 99.41% | DL |
| 19 | rectum mucinous adenocarcinoma | 99.38% | DL |
| 20 | theca steroid-producing cell malignant tumor of ovary, not further specified | 99.38% | DL |

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
