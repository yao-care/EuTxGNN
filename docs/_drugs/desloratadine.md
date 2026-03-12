---
layout: default
title: Desloratadine
description: "desloratadine drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 168
evidence_level: L5
indication_count: 53
---

# Desloratadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Desloratadine |
| DrugBank ID | [DB00967](https://go.drugbank.com/drugs/DB00967) |
| Brand Names (EU) | Aerinaze, Dasselta, Desloratadine ratiopharm |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Dasselta is indicated for the relief of symptoms associated with:  allergic rhinitis; urticaria.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | allergic urticaria | 99.99% | DL |
| 2 | papillary conjunctivitis | 99.97% | DL |
| 3 | cold urticaria | 99.94% | DL |
| 4 | pharyngitis | 99.87% | DL |
| 5 | nasal cavity disease | 99.87% | DL |
| 6 | acute laryngopharyngitis | 99.85% | DL |
| 7 | atopic conjunctivitis | 99.84% | DL |
| 8 | vernal conjunctivitis | 99.78% | DL |
| 9 | recalcitrant atopic dermatitis | 99.75% | DL |
| 10 | nasopharyngitis | 99.66% | DL |
| 11 | IgE responsiveness, atopic | 99.64% | DL |
| 12 | rosacea conjunctivitis | 99.40% | DL |
| 13 | common cold | 99.02% | DL |
| 14 | headache disorder | 98.44% | DL |
| 15 | trigeminal autonomic cephalalgia | 98.33% | DL |
| 16 | punctate epithelial keratoconjunctivitis | 97.68% | DL |
| 17 | Angelucci syndrome | 97.64% | DL |
| 18 | chronic follicular conjunctivitis | 97.62% | DL |
| 19 | parasitic conjunctivitis | 97.62% | DL |
| 20 | serous conjunctivitis except viral | 97.62% | DL |

*Showing top 20 of 53 predictions.*

---


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
