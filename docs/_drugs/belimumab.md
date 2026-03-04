---
layout: default
title: Belimumab
description: "belimumab drug repurposing predictions from TxGNN. Evidence level L3 with 52 predicted indications."
parent: Observational Evidence (L3)
nav_order: 74
evidence_level: L3
indication_count: 52
---

# Belimumab
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Belimumab |
| DrugBank ID | [DB08879](https://go.drugbank.com/drugs/DB08879) |
| Brand Names (EU) | Benlysta |
| Evidence Level | L3 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Benlysta is indicated as add-on therapy in patients aged 5 years and older with active, autoantibody-positive systemic lupus erythematosus (SLE) with a high degree of disease activity&nbsp;(e.g., positive anti‑dsDNA and low complement)&nbsp;despite standard therapy. Benlysta is indicated in combination with background immunosuppressive therapies for the treatment of adult patients with active lupus nephritis.Benlysta is indicated as add-on therapy in adult patients with active, autoantibody-posi

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 99.96% | DL |
| 2 | pseudo-von Willebrand disease | 99.96% | DL |
| 3 | Glanzmann thrombasthenia | 99.88% | DL |
| 4 | fetal and neonatal alloimmune thrombocytopenia | 99.59% | DL |
| 5 | severe nonproliferative diabetic retinopathy | 99.05% | DL |
| 6 | autosomal dominant macrothrombocytopenia | 99.04% | DL |
| 7 | granulomatous disease, chronic, autosomal recessive, 5 | 97.91% | DL |
| 8 | anus disease | 97.89% | DL |
| 9 | inflammatory bowel disease | 97.76% | DL |
| 10 | granulomatous disease with defect in neutrophil chemotaxis | 97.71% | DL |
| 11 | Scott syndrome | 97.42% | DL |
| 12 | functional neutrophil defect | 97.15% | DL |
| 13 | congenital hypotrichosis with juvenile macular dystrophy | 97.05% | DL |
| 14 | systemic sclerosis | 96.72% | DL |
| 15 | psoriasis | 96.70% | DL |
| 16 | bleeding diathesis due to a collagen receptor defect | 96.67% | DL |
| 17 | hemorrhagic disorder due to a constitutional thrombocytopenia | 96.63% | DL |
| 18 | Crohn disease of the esophagus | 96.51% | DL |
| 19 | ulcerative colitis (disease) | 96.50% | DL |
| 20 | cyclic hematopoiesis | 96.05% | DL |

*Showing top 20 of 52 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| primary release disorder of platelets | L3 | 1 | 0 | 1 Phase 2 trial(s) |

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
