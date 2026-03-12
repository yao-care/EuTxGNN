---
layout: default
title: Filgrastim
description: "filgrastim drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 246
evidence_level: L2
indication_count: 50
---

# Filgrastim
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Filgrastim |
| DrugBank ID | [DB00099](https://go.drugbank.com/drugs/DB00099) |
| Brand Names (EU) | Ratiograstim |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Ratiograstim is indicated for the reduction in the duration of neutropenia and the incidence of febrile neutropenia in patients treated with established cytotoxic chemotherapy for malignancy (with the exception of chronic myeloid leukaemia and myelodysplastic syndromes) and for the reduction in the duration of neutropenia in patients undergoing myeloablative therapy followed by bone-marrow transplantation considered to be at increased risk of prolonged severe neutropenia. The safety and efficacy

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary release disorder of platelets | 100.00% | DL |
| 2 | pseudo-von Willebrand disease | 100.00% | DL |
| 3 | Glanzmann thrombasthenia | 100.00% | DL |
| 4 | Scott syndrome | 99.96% | DL |
| 5 | hemorrhagic disorder due to a constitutional thrombocytopenia | 99.91% | DL |
| 6 | bleeding diathesis due to a collagen receptor defect | 99.91% | DL |
| 7 | C1 inhibitor deficiency | 99.84% | DL |
| 8 | serpinopathy with toxic serpin polymerization | 99.81% | DL |
| 9 | fetal and neonatal alloimmune thrombocytopenia | 99.77% | DL |
| 10 | platelet-type bleeding disorder | 99.69% | DL |
| 11 | hereditary angioedema with C1Inh deficiency | 99.68% | DL |
| 12 | Ehlers-Danlos syndrome, fibronectinemic type | 99.61% | DL |
| 13 | severe congenital neutropenia | 99.60% | DL |
| 14 | Peyronie disease | 99.58% | DL |
| 15 | primary immunodeficiency syndrome due to p14 deficiency | 99.57% | DL |
| 16 | cyclic hematopoiesis | 99.50% | DL |
| 17 | mixed-type autoimmune hemolytic anemia | 99.44% | DL |
| 18 | proteinuria | 99.43% | DL |
| 19 | primary CD59 deficiency | 99.42% | DL |
| 20 | drug-induced autoimmune hemolytic anemia | 99.42% | DL |

*Showing top 20 of 50 predictions.*

---


---

---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| primary release disorder of platelets | L2 | 14 | 0 | 1 Phase 3 trial(s), 10 Phase 2 trial(s) |

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
