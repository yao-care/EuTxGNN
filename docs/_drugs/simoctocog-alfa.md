---
layout: default
title: Simoctocog Alfa
description: "simoctocog alfa drug repurposing predictions from TxGNN. Evidence level L4 with 50 predicted indications."
parent: Preclinical Evidence (L4)
nav_order: 530
evidence_level: L4
indication_count: 50
---

# Simoctocog Alfa
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Simoctocog Alfa |
| DrugBank ID | [DB09108](https://go.drugbank.com/drugs/DB09108) |
| Brand Names (EU) | Nuwiq |
| Evidence Level | L4 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor VIII deficiency). Nuwiq can be used for all age groups.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pseudo-von Willebrand disease | 100.00% | DL |
| 2 | primary release disorder of platelets | 100.00% | DL |
| 3 | Glanzmann thrombasthenia | 99.99% | DL |
| 4 | hemophilia | 99.98% | DL |
| 5 | Scott syndrome | 99.97% | DL |
| 6 | acquired coagulation factor deficiency | 99.95% | DL |
| 7 | symptomatic form of hemophilia in female carriers | 99.93% | DL |
| 8 | bleeding diathesis due to a collagen receptor defect | 99.92% | DL |
| 9 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.92% | DL |
| 10 | fetal and neonatal alloimmune thrombocytopenia | 99.84% | DL |
| 11 | hemophilia A with vascular abnormality | 99.78% | DL |
| 12 | thrombotic thrombocytopenic purpura | 99.72% | DL |
| 13 | platelet-type bleeding disorder | 99.67% | DL |
| 14 | factor XI deficiency | 99.60% | DL |
| 15 | Ehlers-Danlos syndrome, fibronectinemic type | 99.58% | DL |
| 16 | flood factor deficiency | 99.44% | DL |
| 17 | methylcobalamin deficiency type cblG | 99.40% | DL |
| 18 | familial thrombomodulin anomalies | 99.32% | DL |
| 19 | hereditary thrombocytosis with transverse limb defect | 99.31% | DL |
| 20 | hemorrhagic disorder due to a platelet anomaly | 99.26% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| hemophilia | L4 | 3 | 11 | 1 Phase 3 trial(s), 1 Phase 2 trial(s) |

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
