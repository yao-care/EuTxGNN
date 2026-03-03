---
layout: default
title: Mepolizumab
description: "Mepolizumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 369
evidence_level: L5
indication_count: 51
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mepolizumab |
| DrugBank ID | [DB06612](https://go.drugbank.com/drugs/DB06612) |
| Brand Names (EU) | Nucala |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.66% |

---

## Approved Indication (EMA)

Severe eosinophilic asthmaNucala is indicated as an add-on treatment for severe refractory eosinophilic asthma in adults, adolescents and children aged 6 years and older . Chronic rhinosinusitis with nasal polyps (CRSwNP)Nucala is indicated as an add-on therapy with intranasal corticosteroids for the treatment of adult patients with severe CRSwNP for whom therapy with systemic corticosteroids and/or surgery do not provide adequate control. Eosinophilic granulomatosis with polyangiitis (EGPA)Nuca

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | thrombocytopenia due to immune destruction | 99.66% | DL |
| 2 | primary release disorder of platelets | 99.61% | DL |
| 3 | pseudo-von Willebrand disease | 99.44% | DL |
| 4 | autoimmune thrombocytopenic | 99.33% | DL |
| 5 | Glanzmann thrombasthenia | 99.28% | DL |
| 6 | Evans syndrome | 98.62% | DL |
| 7 | neonatal thrombocytopenia | 98.60% | DL |
| 8 | autosomal thrombocytopenia with normal platelets | 98.37% | DL |
| 9 | filariasis | 97.67% | DL |
| 10 | mixed-type autoimmune hemolytic anemia | 96.57% | DL |
| 11 | drug-induced autoimmune hemolytic anemia | 96.38% | DL |
| 12 | cyclic hematopoiesis | 96.29% | DL |
| 13 | proteinuria | 95.91% | DL |
| 14 | syndromic constitutional thrombocytopenia | 95.86% | DL |
| 15 | neonatal autoimmune hemolytic anemia | 95.81% | DL |
| 16 | paroxysmal nocturnal hemoglobinuria | 95.48% | DL |
| 17 | fetal and neonatal alloimmune thrombocytopenia | 95.28% | DL |
| 18 | hemorrhagic disorder due to a constitutional thrombocytopenia | 94.59% | DL |
| 19 | bleeding diathesis due to a collagen receptor defect | 94.41% | DL |
| 20 | Scott syndrome | 94.36% | DL |

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
