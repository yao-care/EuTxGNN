---
layout: default
title: Lanadelumab
description: "lanadelumab drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 327
evidence_level: L1
indication_count: 50
---

# Lanadelumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lanadelumab |
| DrugBank ID | [DB14597](https://go.drugbank.com/drugs/DB14597) |
| Brand Names (EU) | Takhzyro |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Takhzyro is indicated for routine prevention of recurrent attacks of hereditary angioedema (HAE) in patients aged 2 years and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | C1 inhibitor deficiency | 100.00% | DL |
| 2 | hereditary angioedema with C1Inh deficiency | 99.99% | DL |
| 3 | serpinopathy with toxic serpin polymerization | 99.99% | DL |
| 4 | pancreatitis | 99.87% | DL |
| 5 | hereditary angioedema | 99.61% | DL |
| 6 | pseudo-von Willebrand disease | 99.52% | DL |
| 7 | primary release disorder of platelets | 99.46% | DL |
| 8 | immune-mediated necrotizing myopathy | 99.33% | DL |
| 9 | Glanzmann thrombasthenia | 99.31% | DL |
| 10 | antisynthetase syndrome | 99.30% | DL |
| 11 | focal myositis | 99.27% | DL |
| 12 | Scott syndrome | 99.12% | DL |
| 13 | idiopathic eosinophilic myositis | 99.12% | DL |
| 14 | inflammatory myopathy with abundant macrophages | 99.12% | DL |
| 15 | Peyronie disease | 98.99% | DL |
| 16 | alcoholic cardiomyopathy | 98.82% | DL |
| 17 | symptomatic form of hemophilia in female carriers | 98.70% | DL |
| 18 | familial apolipoprotein C-II deficiency | 98.57% | DL |
| 19 | bleeding diathesis due to a collagen receptor defect | 98.35% | DL |
| 20 | hemorrhagic disorder due to a constitutional thrombocytopenia | 98.30% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| C1 inhibitor deficiency | L1 | 20 | 20 | 7 Phase 3 trial(s), 1 RCT(s) |

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
