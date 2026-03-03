---
layout: default
title: Benralizumab
description: "Benralizumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 76
evidence_level: L5
indication_count: 52
---

# Benralizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Benralizumab |
| DrugBank ID | [DB12023](https://go.drugbank.com/drugs/DB12023) |
| Brand Names (EU) | Fasenra |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.34% |

---

## Approved Indication (EMA)

AsthmaFasenra is indicated as an add on maintenance treatment in adult patients with severe eosinophilic asthma inadequately controlled despite high-dose inhaled corticosteroids plus long acting β agonists (see section 5.1).Eosinophilic granulomatosis with polyangiitis (EGPA)Fasenra is indicated as an add-on treatment for adult patients with relapsing or refractory eosinophilic granulomatosis with polyangiitis (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | thrombocytopenia due to immune destruction | 99.34% | DL |
| 2 | dermatitis | 99.16% | DL |
| 3 | acne keloid | 99.13% | DL |
| 4 | neonatal dermatomyositis | 99.05% | DL |
| 5 | amyopathic dermatomyositis | 99.03% | DL |
| 6 | acrodermatitis chronica atrophicans | 98.92% | DL |
| 7 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 98.90% | DL |
| 8 | hydroa vacciniforme, familial | 98.90% | DL |
| 9 | autoimmune thrombocytopenic | 98.37% | DL |
| 10 | Evans syndrome | 98.24% | DL |
| 11 | autosomal thrombocytopenia with normal platelets | 97.80% | DL |
| 12 | primary release disorder of platelets | 97.79% | DL |
| 13 | neonatal thrombocytopenia | 97.28% | DL |
| 14 | pseudo-von Willebrand disease | 97.10% | DL |
| 15 | mixed-type autoimmune hemolytic anemia | 96.78% | DL |
| 16 | drug-induced autoimmune hemolytic anemia | 96.60% | DL |
| 17 | Glanzmann thrombasthenia | 96.24% | DL |
| 18 | neonatal autoimmune hemolytic anemia | 95.90% | DL |
| 19 | proteinuria | 95.81% | DL |
| 20 | filariasis | 95.56% | DL |

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
