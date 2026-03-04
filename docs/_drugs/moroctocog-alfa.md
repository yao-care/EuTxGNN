---
layout: default
title: Moroctocog Alfa
description: "moroctocog alfa drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 391
evidence_level: L1
indication_count: 50
---

# Moroctocog Alfa
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Moroctocog Alfa |
| DrugBank ID | [DB13999](https://go.drugbank.com/drugs/DB13999) |
| Brand Names (EU) | ReFacto AF |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor-VIII deficiency). ReFacto AF is appropriate for use in adults and children of all ages, including newborns. ReFacto AF does not contain von-Willebrand factor, and hence is not indicated in von-Willebrand's disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.97% | DL |
| 2 | pseudo-von Willebrand disease | 99.97% | DL |
| 3 | Glanzmann thrombasthenia | 99.96% | DL |
| 4 | hemophilia | 99.93% | DL |
| 5 | acquired coagulation factor deficiency | 99.88% | DL |
| 6 | Scott syndrome | 99.86% | DL |
| 7 | bleeding diathesis due to a collagen receptor defect | 99.73% | DL |
| 8 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.72% | DL |
| 9 | symptomatic form of hemophilia in female carriers | 99.40% | DL |
| 10 | flood factor deficiency | 99.11% | DL |
| 11 | hereditary thrombocytosis with transverse limb defect | 98.92% | DL |
| 12 | familial thrombomodulin anomalies | 98.91% | DL |
| 13 | inherited thrombophilia | 98.72% | DL |
| 14 | thrombotic thrombocytopenic purpura | 98.61% | DL |
| 15 | fetal and neonatal alloimmune thrombocytopenia | 98.46% | DL |
| 16 | methylcobalamin deficiency type cblG | 98.45% | DL |
| 17 | platelet-type bleeding disorder | 98.12% | DL |
| 18 | hemophilia A with vascular abnormality | 97.91% | DL |
| 19 | factor XI deficiency | 97.54% | DL |
| 20 | Ehlers-Danlos syndrome, fibronectinemic type | 97.29% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| primary release disorder of platelets | L1 | 7 | 0 | 3 Phase 3 trial(s) |

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
