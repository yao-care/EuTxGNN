---
layout: default
title: Tobramycin
description: "Tobramycin drug repurposing predictions from TxGNN. Evidence level L5 with 67 predicted indications."
parent: AI Predictions (L5)
nav_order: 590
evidence_level: L5
indication_count: 67
---

# Tobramycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **67**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tobramycin |
| DrugBank ID | [DB00684](https://go.drugbank.com/drugs/DB00684) |
| Brand Names (EU) | Tobi Podhaler, Vantobra (previously Tobramycin PARI) |
| Evidence Level | L5 |
| Predicted Indications | 67 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Vantobra&nbsp;is indicated for the management of chronic pulmonary infection due to Pseudomonas aeruginosa in patients aged 6 years and older with cystic fibrosis (CF). Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | punctate epithelial keratoconjunctivitis | 99.99% | DL |
| 2 | exposure keratitis | 99.93% | DL |
| 3 | non-human animal disease | 99.83% | DL |
| 4 | otitis externa | 99.81% | DL |
| 5 | postinfectious vasculitis | 99.80% | DL |
| 6 | post-bacterial disorder | 99.79% | DL |
| 7 | post-infectious syndrome | 99.79% | DL |
| 8 | infective urethral stricture | 99.78% | DL |
| 9 | Chagas cardiomyopathy | 99.78% | DL |
| 10 | infection-related hemolytic uremic syndrome | 99.78% | DL |
| 11 | neurotrophic keratopathy | 99.77% | DL |
| 12 | acute contagious conjunctivitis | 99.66% | DL |
| 13 | superior limbic keratoconjunctivitis | 99.48% | DL |
| 14 | conjunctivitis | 99.43% | DL |
| 15 | epidemic keratoconjunctivitis | 99.38% | DL |
| 16 | eye infectious disease | 99.38% | DL |
| 17 | globe disease | 99.35% | DL |
| 18 | papillary conjunctivitis | 99.33% | DL |
| 19 | bronchitis | 99.14% | DL |
| 20 | blepharoconjunctivitis | 99.12% | DL |

*Showing top 20 of 67 predictions.*

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
