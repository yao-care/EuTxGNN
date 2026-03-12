---
layout: default
title: Everolimus
description: "Everolimus drug repurposing predictions from TxGNN. Evidence level L5 with 57 predicted indications."
parent: AI Predictions (L5)
nav_order: 232
evidence_level: L5
indication_count: 57
---

# Everolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **57**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Everolimus |
| DrugBank ID | [DB01590](https://go.drugbank.com/drugs/DB01590) |
| Brand Names (EU) | Afinitor, Votubia |
| Evidence Level | L5 |
| Predicted Indications | 57 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Renal angiomyolipoma associated with tuberous sclerosis complex (TSC) Votubia is indicated for the treatment of adult patients with renal angiomyolipoma associated with tuberous sclerosis complex (TSC) who are at risk of complications (based on factors such as tumour size or presence of aneurysm, or presence of multiple or bilateral tumours) but who do not require immediate surgery. The evidence is based on analysis of change in sum of angiomyolipoma volume. Subependymal giant cell astrocytoma (

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | liposarcoma | 99.88% | DL |
| 2 | ovarian myxoid liposarcoma | 99.84% | DL |
| 3 | dermatofibrosarcoma protuberans | 99.82% | DL |
| 4 | clear cell renal carcinoma | 99.81% | DL |
| 5 | parameningeal embryonal rhabdomyosarcoma | 99.77% | DL |
| 6 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.76% | DL |
| 7 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.75% | DL |
| 8 | rhabdomyosarcoma (disease) | 99.74% | DL |
| 9 | prostate embryonal rhabdomyosarcoma | 99.74% | DL |
| 10 | unclassified renal cell carcinoma | 99.72% | DL |
| 11 | renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions | 99.72% | DL |
| 12 | renal cell carcinoma associated with neuroblastoma | 99.72% | DL |
| 13 | extrahepatic bile duct rhabdomyosarcoma | 99.72% | DL |
| 14 | uterine corpus perivascular epithelioid cell tumor | 99.71% | DL |
| 15 | benign PEComa | 99.71% | DL |
| 16 | lymphangiomyoma | 99.70% | DL |
| 17 | renal cell carcinoma (disease) | 99.69% | DL |
| 18 | liver sarcoma | 99.68% | DL |
| 19 | childhood kidney cell carcinoma | 99.67% | DL |
| 20 | lymphangioleiomyomatosis | 99.63% | DL |

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
