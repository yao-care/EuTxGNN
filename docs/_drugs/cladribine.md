---
layout: default
title: Cladribine
description: "Cladribine drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 137
evidence_level: L5
indication_count: 51
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cladribine |
| DrugBank ID | [DB00242](https://go.drugbank.com/drugs/DB00242) |
| Brand Names (EU) | Litak, Mavenclad |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.77% |

---

## Approved Indication (EMA)

Litak is indicated for the treatment of hairy-cell leukaemia.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | parameningeal embryonal rhabdomyosarcoma | 99.77% | DL |
| 2 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.77% | DL |
| 3 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.76% | DL |
| 4 | prostate embryonal rhabdomyosarcoma | 99.75% | DL |
| 5 | extrahepatic bile duct rhabdomyosarcoma | 99.75% | DL |
| 6 | rhabdomyosarcoma (disease) | 99.74% | DL |
| 7 | liver sarcoma | 99.70% | DL |
| 8 | relapsing-remitting multiple sclerosis | 99.52% | DL |
| 9 | skeletal muscle neoplasm | 98.96% | DL |
| 10 | gestational trophoblastic neoplasm | 98.37% | DL |
| 11 | pleural adenomatoid tumor | 98.07% | DL |
| 12 | ovarian myxoid liposarcoma | 98.03% | DL |
| 13 | partial hydatidiform mole | 98.03% | DL |
| 14 | gestational uterine corpus choriocarcinoma | 97.92% | DL |
| 15 | liposarcoma | 97.89% | DL |
| 16 | pleural biphasic mesothelioma | 97.78% | DL |
| 17 | malignant peritoneal mesothelioma | 97.78% | DL |
| 18 | hydatidiform mole, recurrent | 97.72% | DL |
| 19 | fallopian tube gestational choriocarcinoma | 97.66% | DL |
| 20 | pleural epithelioid mesothelioma | 97.64% | DL |

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
