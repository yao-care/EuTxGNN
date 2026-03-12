---
layout: default
title: Caplacizumab
description: "caplacizumab drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 113
evidence_level: L2
indication_count: 50
---

# Caplacizumab
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Caplacizumab |
| DrugBank ID | [DB06081](https://go.drugbank.com/drugs/DB06081) |
| Brand Names (EU) | Cablivi |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Cablivi is indicated for the treatment of adults experiencing an episode of acquired thrombotic thrombocytopenic purpura (aTTP), in conjunction with plasma exchange and immunosuppression.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 100.00% | DL |
| 2 | pseudo-von Willebrand disease | 100.00% | DL |
| 3 | Glanzmann thrombasthenia | 100.00% | DL |
| 4 | Scott syndrome | 100.00% | DL |
| 5 | thrombotic thrombocytopenic purpura | 100.00% | DL |
| 6 | bleeding diathesis due to a collagen receptor defect | 100.00% | DL |
| 7 | hemorrhagic disorder due to a constitutional thrombocytopenia | 100.00% | DL |
| 8 | fetal and neonatal alloimmune thrombocytopenia | 99.99% | DL |
| 9 | hemophilia | 99.99% | DL |
| 10 | platelet-type bleeding disorder | 99.99% | DL |
| 11 | acquired coagulation factor deficiency | 99.99% | DL |
| 12 | thrombocytopenic purpura | 99.98% | DL |
| 13 | Ehlers-Danlos syndrome, fibronectinemic type | 99.98% | DL |
| 14 | inherited thrombophilia | 99.97% | DL |
| 15 | flood factor deficiency | 99.97% | DL |
| 16 | symptomatic form of hemophilia in female carriers | 99.97% | DL |
| 17 | congenital factor V deficiency | 99.97% | DL |
| 18 | hereditary thrombocytosis with transverse limb defect | 99.96% | DL |
| 19 | familial thrombomodulin anomalies | 99.96% | DL |
| 20 | methylcobalamin deficiency type cblG | 99.96% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| platelet-type bleeding disorder | L2 | 3 | 0 | 1 Phase 3 trial(s) |

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
