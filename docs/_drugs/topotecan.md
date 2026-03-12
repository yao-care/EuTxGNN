---
layout: default
title: Topotecan
description: "Topotecan drug repurposing predictions from TxGNN. Evidence level L5 with 57 predicted indications."
parent: AI Predictions (L5)
nav_order: 596
evidence_level: L5
indication_count: 57
---

# Topotecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **57**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Topotecan |
| DrugBank ID | [DB01030](https://go.drugbank.com/drugs/DB01030) |
| Brand Names (EU) | Hycamtin, Potactasol |
| Evidence Level | L5 |
| Predicted Indications | 57 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Topotecan monotherapy is indicated for the treatment of:- patients with metastatic carcinoma of the ovary after failure of first-line or subsequent therapy- patients with relapsed small cell lung cancer (SCLC) for whom re-treatment with the first-line regimen is not considered appropriate (see section 5.1). Topotecan in combination with cisplatin is indicated for patients with carcinoma of the cervix recurrent after radiotherapy and for patients with Stage IVB disease. Patients with prior exposu

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | female breast carcinoma | 99.92% | DL |
| 2 | primary non-gestational choriocarcinoma of ovary | 99.90% | DL |
| 3 | ovarian clear cell adenocarcinoma | 99.86% | DL |
| 4 | hereditary breast ovarian cancer syndrome | 99.83% | DL |
| 5 | yolk sac tumor | 99.70% | DL |
| 6 | ovarian mucinous adenocarcinoma | 99.67% | DL |
| 7 | maligant granulosa cell tumor of ovary | 99.57% | DL |
| 8 | adult germ cell tumor | 99.57% | DL |
| 9 | ovarian endometrioid adenocarcinoma | 99.53% | DL |
| 10 | malignant non-dysgerminomatous germ cell tumor of ovary | 99.49% | DL |
| 11 | testicular yolk sac tumor, endodermal sinus pattern | 99.49% | DL |
| 12 | testicular yolk sac tumor, solid pattern | 99.49% | DL |
| 13 | testicular yolk sac tumor, papillary pattern | 99.49% | DL |
| 14 | testicular yolk sac tumor, hepatoid pattern | 99.49% | DL |
| 15 | testicular yolk sac tumor, macrocystic pattern | 99.49% | DL |
| 16 | enteric pattern testicular yolk sac tumor | 99.49% | DL |
| 17 | polyvesicular vitelline pattern testicular yolk sac tumor | 99.49% | DL |
| 18 | reticular pattern testicular yolk sac tumor | 99.49% | DL |
| 19 | rectum mucinous adenocarcinoma | 99.49% | DL |
| 20 | mediastinal malignant germ cell tumor | 99.48% | DL |

*Showing top 20 of 57 predictions.*

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
