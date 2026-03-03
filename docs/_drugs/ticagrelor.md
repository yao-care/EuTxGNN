---
layout: default
title: Ticagrelor
description: "Ticagrelor drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 579
evidence_level: L5
indication_count: 51
---

# Ticagrelor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ticagrelor |
| DrugBank ID | [DB08816](https://go.drugbank.com/drugs/DB08816) |
| Brand Names (EU) | Brilique |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Brilique, co administered with acetylsalicylic acid (ASA), is indicated for the prevention of atherothrombotic events in adult patients with  acute coronary syndromes (ACS) or a history of myocardial infarction (MI) and a high risk of developing an atherothrombotic event  Brilique, co-administered with acetyl salicylic acid (ASA), is indicated for the prevention of atherothrombotic events in adult patients with a history of myocardial infarction (MI occurred at least one year ago) and a high ris

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | intracranial arteriosclerosis | 99.97% | DL |
| 2 | intermittent vascular claudication | 99.96% | DL |
| 3 | Monckeberg arteriosclerosis | 99.94% | DL |
| 4 | peripheral arterial disease | 99.91% | DL |
| 5 | peripheral vascular disease | 99.90% | DL |
| 6 | priapism | 99.75% | DL |
| 7 | ischemic disease | 99.64% | DL |
| 8 | May-Thurner syndrome | 99.55% | DL |
| 9 | livedo reticularis | 99.53% | DL |
| 10 | mesenteric vascular occlusion | 99.50% | DL |
| 11 | vascular ectasia | 99.47% | DL |
| 12 | angiodysplasia | 99.28% | DL |
| 13 | venous thromboembolism | 99.27% | DL |
| 14 | fibrocartilaginous embolism | 99.27% | DL |
| 15 | non-inflammatory vasculopathy | 99.13% | DL |
| 16 | erythromelalgia | 99.10% | DL |
| 17 | kyphoscoliotic heart disease | 99.04% | DL |
| 18 | congenital renal artery stenosis | 99.04% | DL |
| 19 | Prinzmetal angina | 98.75% | DL |
| 20 | vascular insufficiency disorder | 98.60% | DL |

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
