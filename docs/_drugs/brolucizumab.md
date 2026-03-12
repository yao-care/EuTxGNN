---
layout: default
title: Brolucizumab
description: "Brolucizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 97
evidence_level: L5
indication_count: 50
---

# Brolucizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Brolucizumab |
| DrugBank ID | [DB14864](https://go.drugbank.com/drugs/DB14864) |
| Brand Names (EU) | Beovu |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.67% |

---

## Approved Indication (EMA)

Beovu is indicated in adults for the treatment of neovascular (wet) age-related macular degeneration (AMD).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 99.67% | DL |
| 2 | esophageal varices without bleeding | 99.12% | DL |
| 3 | esophageal varices with bleeding | 99.12% | DL |
| 4 | exocrine pancreatic insufficiency | 99.07% | DL |
| 5 | MRCS syndrome | 98.54% | DL |
| 6 | pigmented paravenous retinochoroidal atrophy | 98.33% | DL |
| 7 | familial flecked retinopathy | 97.90% | DL |
| 8 | ectopia lentis-chorioretinal dystrophy-myopia syndrome | 97.82% | DL |
| 9 | retinal dystrophy in systemic or cerebroretinal lipidoses | 97.73% | DL |
| 10 | senile reticular retinal degeneration | 97.71% | DL |
| 11 | Blessig's cysts | 97.71% | DL |
| 12 | pseudoretinitis pigmentosa | 97.71% | DL |
| 13 | cone dystrophy | 97.68% | DL |
| 14 | genetic macular dystrophy | 97.58% | DL |
| 15 | X-linked retinal dysplasia | 97.46% | DL |
| 16 | progressive bifocal chorioretinal atrophy | 97.45% | DL |
| 17 | varicose disease | 97.38% | DL |
| 18 | retinal drusen | 97.36% | DL |
| 19 | macular degeneration | 97.34% | DL |
| 20 | retinoschisis | 97.30% | DL |

*Showing top 20 of 50 predictions.*

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
