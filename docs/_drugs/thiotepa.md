---
layout: default
title: Thiotepa
description: "Thiotepa drug repurposing predictions from TxGNN. Evidence level L5 with 75 predicted indications."
parent: AI Predictions (L5)
nav_order: 577
evidence_level: L5
indication_count: 75
---

# Thiotepa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **75**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Thiotepa |
| DrugBank ID | [DB04572](https://go.drugbank.com/drugs/DB04572) |
| Brand Names (EU) | Tepadina, Thiotepa Riemser |
| Evidence Level | L5 |
| Predicted Indications | 75 |
| Top Prediction Score | 99.53% |

---

## Approved Indication (EMA)

Thiotepa Riemser is indicated, in combination with other chemotherapy medicinal products:  with or without total body irradiation (TBI), as conditioning treatment prior to allogeneic or autologous haematopoietic progenitor cell transplantation (HPCT) in haematological diseases in adult and paediatric patients; when high dose chemotherapy with HPCT support is appropriate for the treatment of solid tumours in adult and paediatric patients.  Thiotepa Riemser is indicated, in combination with other 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary non-gestational choriocarcinoma of ovary | 99.53% | DL |
| 2 | ovarian clear cell adenocarcinoma | 99.21% | DL |
| 3 | female breast carcinoma | 98.97% | DL |
| 4 | yolk sac tumor | 98.88% | DL |
| 5 | adult germ cell tumor | 98.51% | DL |
| 6 | ovarian mucinous adenocarcinoma | 98.51% | DL |
| 7 | hereditary breast ovarian cancer syndrome | 98.47% | DL |
| 8 | maligant granulosa cell tumor of ovary | 98.41% | DL |
| 9 | testicular yolk sac tumor, papillary pattern | 98.36% | DL |
| 10 | enteric pattern testicular yolk sac tumor | 98.36% | DL |
| 11 | reticular pattern testicular yolk sac tumor | 98.36% | DL |
| 12 | testicular yolk sac tumor, hepatoid pattern | 98.36% | DL |
| 13 | polyvesicular vitelline pattern testicular yolk sac tumor | 98.36% | DL |
| 14 | testicular yolk sac tumor, macrocystic pattern | 98.36% | DL |
| 15 | testicular yolk sac tumor, endodermal sinus pattern | 98.36% | DL |
| 16 | testicular yolk sac tumor, solid pattern | 98.36% | DL |
| 17 | childhood ovarian yolk sac tumor | 98.30% | DL |
| 18 | ovarian yolk sac tumor, hepatoid pattern | 98.29% | DL |
| 19 | ovarian yolk sac tumor, polyvesicular vitelline pattern | 98.29% | DL |
| 20 | ovarian yolk sac tumor, glandular pattern | 98.29% | DL |

*Showing top 20 of 75 predictions.*

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
