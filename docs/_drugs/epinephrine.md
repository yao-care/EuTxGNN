---
layout: default
title: Epinephrine
description: "epinephrine drug repurposing predictions from TxGNN. Evidence level L1 with 54 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 216
evidence_level: L1
indication_count: 54
---

# Epinephrine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **54**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Epinephrine |
| DrugBank ID | [DB00668](https://go.drugbank.com/drugs/DB00668) |
| Brand Names (EU) | Eurneffy |
| Evidence Level | L1 |
| Predicted Indications | 54 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Emergency treatment of allergic reactions (anaphylaxis) due to insect stings or bites, foods, medicinal products and other allergens as well as idiopathic or exercise induced anaphylaxis. Treatment is indicated for adults and children with a body weight ≥30&nbsp;kg.&nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 99.98% | DL |
| 2 | obstructive lung disease | 99.71% | DL |
| 3 | anaphylaxis | 99.70% | DL |
| 4 | food-dependent exercise-induced anaphylaxis | 99.57% | DL |
| 5 | Rienhoff syndrome | 99.57% | DL |
| 6 | respiratory malformation | 99.56% | DL |
| 7 | pulmonary emphysema | 99.49% | DL |
| 8 | dry eye syndrome | 98.51% | DL |
| 9 | pseudoallergy | 97.32% | DL |
| 10 | laryngotracheitis | 97.31% | DL |
| 11 | headache disorder | 97.07% | DL |
| 12 | anorectal stricture | 97.02% | DL |
| 13 | trigeminal autonomic cephalalgia | 96.90% | DL |
| 14 | primary hereditary glaucoma | 96.80% | DL |
| 15 | anal polyp | 96.66% | DL |
| 16 | open-angle glaucoma | 95.72% | DL |
| 17 | tracheal disease | 95.59% | DL |
| 18 | imperforate anus | 95.50% | DL |
| 19 | bronchial neoplasm (disease) | 95.30% | DL |
| 20 | bronchial disease | 95.20% | DL |

*Showing top 20 of 54 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| bronchitis | L1 | 20 | 19 | 4 Phase 3 trial(s), 2 Phase 2 trial(s), 1 RCT(s) |

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
