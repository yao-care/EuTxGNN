---
layout: default
title: Dalbavancin Hydrochloride
description: "Dalbavancin Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 150
evidence_level: L5
indication_count: 50
---

# Dalbavancin Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dalbavancin Hydrochloride |
| DrugBank ID | [DB06219](https://go.drugbank.com/drugs/DB06219) |
| Brand Names (EU) | Xydalba |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.76% |

---

## Approved Indication (EMA)

Xydalba is indicated for the treatment of acute bacterial skin and skin structure infections (ABSSSI) in adults and paediatric patients from birth (see sections 4.4 and 5.1).Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | postinfectious vasculitis | 99.76% | DL |
| 2 | post-bacterial disorder | 99.76% | DL |
| 3 | post-infectious syndrome | 99.76% | DL |
| 4 | infective urethral stricture | 99.74% | DL |
| 5 | Chagas cardiomyopathy | 99.72% | DL |
| 6 | infection-related hemolytic uremic syndrome | 99.72% | DL |
| 7 | otitis externa | 99.70% | DL |
| 8 | ophthalmic herpes zoster | 99.25% | DL |
| 9 | skin disease caused by infection | 99.20% | DL |
| 10 | infectious mononucleosis | 99.16% | DL |
| 11 | orbital cellulitis | 99.02% | DL |
| 12 | tinea corporis | 98.87% | DL |
| 13 | drug-induced osteoporosis | 98.68% | DL |
| 14 | infectious otitis interna | 97.24% | DL |
| 15 | ulcerative blepharitis | 97.18% | DL |
| 16 | parasitic eyelid infestation | 97.17% | DL |
| 17 | abdominal ectopic pregnancy | 96.82% | DL |
| 18 | celiac trunk compression syndrome | 96.82% | DL |
| 19 | abdominal cystic lymphangioma | 96.82% | DL |
| 20 | lymph node palisaded myofibroblastoma | 96.78% | DL |

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
