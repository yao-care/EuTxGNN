---
layout: default
title: Emicizumab
description: "Emicizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 204
evidence_level: L5
indication_count: 50
---

# Emicizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Emicizumab |
| DrugBank ID | [DB13923](https://go.drugbank.com/drugs/DB13923) |
| Brand Names (EU) | Hemlibra |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Hemlibra is indicated for routine prophylaxis of bleeding episodes in patients with haemophilia A (congenital factor VIII deficiency):  with factor VIII inhibitors without factor VIII inhibitors who have:  severe disease (FVIII &lt; 1%) moderate disease (FVIII ? 1% and ? 5%) with severe bleeding phenotype.    Hemlibra can be used in all age groups.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pseudo-von Willebrand disease | 99.99% | DL |
| 2 | primary release disorder of platelets | 99.99% | DL |
| 3 | Glanzmann thrombasthenia | 99.98% | DL |
| 4 | hemophilia | 99.94% | DL |
| 5 | Scott syndrome | 99.92% | DL |
| 6 | acquired coagulation factor deficiency | 99.90% | DL |
| 7 | bleeding diathesis due to a collagen receptor defect | 99.86% | DL |
| 8 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.85% | DL |
| 9 | symptomatic form of hemophilia in female carriers | 99.79% | DL |
| 10 | thrombotic thrombocytopenic purpura | 99.61% | DL |
| 11 | fetal and neonatal alloimmune thrombocytopenia | 99.52% | DL |
| 12 | flood factor deficiency | 99.40% | DL |
| 13 | hereditary thrombocytosis with transverse limb defect | 99.27% | DL |
| 14 | familial thrombomodulin anomalies | 99.27% | DL |
| 15 | inherited thrombophilia | 99.25% | DL |
| 16 | platelet-type bleeding disorder | 99.22% | DL |
| 17 | hemophilia A with vascular abnormality | 99.02% | DL |
| 18 | methylcobalamin deficiency type cblG | 98.95% | DL |
| 19 | Ehlers-Danlos syndrome, fibronectinemic type | 98.82% | DL |
| 20 | factor XI deficiency | 98.73% | DL |

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
