---
layout: default
title: Reslizumab
description: "Reslizumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 489
evidence_level: L5
indication_count: 51
---

# Reslizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Reslizumab |
| DrugBank ID | [DB06602](https://go.drugbank.com/drugs/DB06602) |
| Brand Names (EU) | Cinqaero |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.53% |

---

## Approved Indication (EMA)

Cinqaero is indicated as add-on therapy in adult patients with severe eosinophilic asthma inadequately controlled despite high dose inhaled corticosteroids plus another medicinal product for maintenance treatment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | thrombocytopenia due to immune destruction | 99.53% | DL |
| 2 | primary release disorder of platelets | 99.25% | DL |
| 3 | pseudo-von Willebrand disease | 98.98% | DL |
| 4 | autoimmune thrombocytopenic | 98.89% | DL |
| 5 | Glanzmann thrombasthenia | 98.62% | DL |
| 6 | neonatal thrombocytopenia | 98.07% | DL |
| 7 | autosomal thrombocytopenia with normal platelets | 97.96% | DL |
| 8 | Evans syndrome | 97.89% | DL |
| 9 | filariasis | 96.22% | DL |
| 10 | acne keloid | 95.29% | DL |
| 11 | neonatal dermatomyositis | 94.89% | DL |
| 12 | dermatitis | 94.79% | DL |
| 13 | amyopathic dermatomyositis | 94.65% | DL |
| 14 | acrodermatitis chronica atrophicans | 94.26% | DL |
| 15 | mixed-type autoimmune hemolytic anemia | 94.14% | DL |
| 16 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 94.09% | DL |
| 17 | hydroa vacciniforme, familial | 94.00% | DL |
| 18 | drug-induced autoimmune hemolytic anemia | 93.83% | DL |
| 19 | syndromic constitutional thrombocytopenia | 93.57% | DL |
| 20 | neonatal autoimmune hemolytic anemia | 92.93% | DL |

*Showing top 20 of 51 predictions.*

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
