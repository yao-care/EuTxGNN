---
layout: default
title: Enoxaparin Sodium
description: "Enoxaparin Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 211
evidence_level: L5
indication_count: 50
---

# Enoxaparin Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Enoxaparin Sodium |
| DrugBank ID | [DB01225](https://go.drugbank.com/drugs/DB01225) |
| Brand Names (EU) | Inhixa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.81% |

---

## Approved Indication (EMA)

Inhixa is indicated for adults for:  Prophylaxis of venous thromboembolism, particularly in patients undergoing orthopaedic, general or oncological surgery. Prophylaxis of venous thromboembolism in patients bedridden due to acute illnesses including acute heart failure, acute respiratory failure, severe infections, as well as exacerbation of rheumatic diseases causing immobilisation of the patient (applies to strengths of 40 mg/0.4 mL). Treatment of deep vein thrombosis (DVT), complicated or unc

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | purpura fulminans | 99.81% | DL |
| 2 | pulmonary embolism (disease) | 99.61% | DL |
| 3 | thrombophilia due to protein C deficiency, autosomal recessive | 99.58% | DL |
| 4 | acquired purpura fulminans | 98.99% | DL |
| 5 | primary release disorder of platelets | 98.91% | DL |
| 6 | atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 98.63% | DL |
| 7 | pseudo-von Willebrand disease | 98.50% | DL |
| 8 | Glanzmann thrombasthenia | 98.31% | DL |
| 9 | neuropathy, painful | 98.30% | DL |
| 10 | disseminated intravascular coagulation | 97.54% | DL |
| 11 | thrombotic thrombocytopenic purpura | 96.73% | DL |
| 12 | retinal telangiectasia | 90.68% | DL |
| 13 | arteriosclerotic retinopathy | 89.82% | DL |
| 14 | retinal microaneurysm | 89.82% | DL |
| 15 | vertebral artery occlusion | 89.40% | DL |
| 16 | fetal and neonatal alloimmune thrombocytopenia | 87.31% | DL |
| 17 | retinal artery occlusion | 87.14% | DL |
| 18 | Ledderhose disease | 87.14% | DL |
| 19 | hemorrhagic disorder due to a constitutional thrombocytopenia | 86.62% | DL |
| 20 | bleeding diathesis due to a collagen receptor defect | 86.38% | DL |

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
