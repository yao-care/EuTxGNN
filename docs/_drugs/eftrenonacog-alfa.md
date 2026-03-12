---
layout: default
title: Eftrenonacog Alfa
description: "Eftrenonacog Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 195
evidence_level: L5
indication_count: 50
---

# Eftrenonacog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eftrenonacog Alfa |
| DrugBank ID | [DB11608](https://go.drugbank.com/drugs/DB11608) |
| Brand Names (EU) | Alprolix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.48% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of bleeding in patients with haemophilia B (congenital factor IX deficiency).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pseudo-von Willebrand disease | 99.48% | DL |
| 2 | primary release disorder of platelets | 99.42% | DL |
| 3 | hemophilia | 99.29% | DL |
| 4 | Glanzmann thrombasthenia | 99.28% | DL |
| 5 | acquired coagulation factor deficiency | 98.97% | DL |
| 6 | symptomatic form of hemophilia in female carriers | 98.84% | DL |
| 7 | Scott syndrome | 98.62% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 97.58% | DL |
| 9 | hemorrhagic disorder due to a constitutional thrombocytopenia | 97.45% | DL |
| 10 | hemophilia A with vascular abnormality | 96.93% | DL |
| 11 | factor XI deficiency | 96.42% | DL |
| 12 | familial apolipoprotein C-II deficiency | 96.38% | DL |
| 13 | thrombotic thrombocytopenic purpura | 95.59% | DL |
| 14 | flood factor deficiency | 95.09% | DL |
| 15 | hemorrhagic disorder due to a platelet anomaly | 95.00% | DL |
| 16 | inherited thrombophilia | 94.96% | DL |
| 17 | congenital factor XIII deficiency | 94.78% | DL |
| 18 | factor XIII, A subunit, deficiency | 94.77% | DL |
| 19 | hereditary thrombocytosis with transverse limb defect | 94.02% | DL |
| 20 | familial thrombomodulin anomalies | 94.01% | DL |

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
