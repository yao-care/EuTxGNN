---
layout: default
title: Tafamidis
description: "Tafamidis drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 551
evidence_level: L5
indication_count: 52
---

# Tafamidis
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tafamidis |
| DrugBank ID | [DB11644](https://go.drugbank.com/drugs/DB11644) |
| Brand Names (EU) | Vyndaqel |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 89.27% |

---

## Approved Indication (EMA)

Vyndaqel is indicated for the treatment of transthyretin amyloidosis in adult patients with stage-1 symptomatic polyneuropathy to delay peripheral neurologic impairment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 89.27% | DL |
| 2 | thrombocytopenic purpura | 88.73% | DL |
| 3 | pseudo-von Willebrand disease | 87.88% | DL |
| 4 | Glanzmann thrombasthenia | 85.79% | DL |
| 5 | primary amyloidosis | 85.00% | DL |
| 6 | acquired amyloid peripheral neuropathy | 84.77% | DL |
| 7 | primary hyperoxaluria | 84.33% | DL |
| 8 | dermis disease | 83.36% | DL |
| 9 | biotin metabolic disease | 83.32% | DL |
| 10 | mixed-type autoimmune hemolytic anemia | 82.31% | DL |
| 11 | drug-induced autoimmune hemolytic anemia | 81.98% | DL |
| 12 | proteinuria | 81.75% | DL |
| 13 | inherited thrombophilia | 80.98% | DL |
| 14 | amyloidosis cutis dyschromia | 80.80% | DL |
| 15 | nodular cutaneous amyloidosis | 80.80% | DL |
| 16 | macular amyloidosis | 80.80% | DL |
| 17 | neonatal autoimmune hemolytic anemia | 80.72% | DL |
| 18 | Ledderhose disease | 80.42% | DL |
| 19 | familial apolipoprotein C-II deficiency | 78.49% | DL |
| 20 | infantile digital fibromatosis | 78.16% | DL |

*Showing top 20 of 52 predictions.*

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
