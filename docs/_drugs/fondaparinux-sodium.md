---
layout: default
title: Fondaparinux Sodium
description: "Fondaparinux Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 254
evidence_level: L5
indication_count: 50
---

# Fondaparinux Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fondaparinux Sodium |
| DrugBank ID | [DB00569](https://go.drugbank.com/drugs/DB00569) |
| Brand Names (EU) | Arixtra |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.44% |

---

## Approved Indication (EMA)

1.5-mg/0.3-ml and 2.5-mg/0.5-ml solution for injection Prevention of venous thromboembolic events (VTE) in adults undergoing major orthopaedic surgery of the lower limbs such as hip fracture, major knee surgery or hip-replacement surgery. Prevention of VTE in adults undergoing abdominal surgery who are judged to be at high risk of thromboembolic complications, such as patients undergoing abdominal cancer surgery. Prevention of VTE in adult medical patients who are judged to be at high risk for V

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary embolism (disease) | 96.44% | DL |
| 2 | primary release disorder of platelets | 93.06% | DL |
| 3 | pseudo-von Willebrand disease | 90.87% | DL |
| 4 | Glanzmann thrombasthenia | 90.62% | DL |
| 5 | Ledderhose disease | 89.28% | DL |
| 6 | vertebral artery occlusion | 87.44% | DL |
| 7 | retinal microaneurysm | 87.42% | DL |
| 8 | arteriosclerotic retinopathy | 87.42% | DL |
| 9 | infantile digital fibromatosis | 86.96% | DL |
| 10 | palmar fibromatosis | 86.53% | DL |
| 11 | retinal telangiectasia | 86.38% | DL |
| 12 | thrombotic thrombocytopenic purpura | 86.31% | DL |
| 13 | retinal artery occlusion | 84.54% | DL |
| 14 | penile fibromatosis | 84.45% | DL |
| 15 | atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 80.69% | DL |
| 16 | purpura fulminans | 78.48% | DL |
| 17 | neuropathy, painful | 78.00% | DL |
| 18 | breast fibrocystic disease | 75.56% | DL |
| 19 | thrombocytopenic purpura | 75.23% | DL |
| 20 | hepatopulmonary syndrome | 75.00% | DL |

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
