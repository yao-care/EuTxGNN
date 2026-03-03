---
layout: default
title: Mometasone Furoate
description: "Mometasone Furoate drug repurposing predictions from TxGNN. Evidence level L5 with 55 predicted indications."
parent: AI Predictions (L5)
nav_order: 390
evidence_level: L5
indication_count: 55
---

# Mometasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **55**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mometasone Furoate |
| DrugBank ID | [DB14512](https://go.drugbank.com/drugs/DB14512) |
| Brand Names (EU) | Atectura Breezhaler, Mometasone furoate, Zimbus Breezhaler |
| Evidence Level | L5 |
| Predicted Indications | 55 |
| Top Prediction Score | 99.72% |

---

## Approved Indication (EMA)

Bemrist Breezhaler is indicated as a maintenance   treatment of asthma in adults and adolescents 12 years of age and older not adequately controlled with inhaled corticosteroids and inhaled short acting beta2-agonists.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | atopic eczema | 99.72% | DL |
| 2 | dermatitis, atopic | 99.33% | DL |
| 3 | 2-hydroxyethyl methacrylate sensitization | 98.62% | DL |
| 4 | seborrheic dermatitis | 98.10% | DL |
| 5 | polyp of vocal cord | 97.67% | DL |
| 6 | polyp of middle ear | 97.65% | DL |
| 7 | polyp of frontal sinus | 97.56% | DL |
| 8 | polyp of external auditory canal | 97.55% | DL |
| 9 | fibroepithelial polyp | 97.55% | DL |
| 10 | polyp of vulva | 97.54% | DL |
| 11 | polyp of ureter | 97.53% | DL |
| 12 | epulis | 97.53% | DL |
| 13 | neoplastic polyp | 97.51% | DL |
| 14 | uterine polyp | 97.50% | DL |
| 15 | primary cutaneous T-cell non-Hodgkin lymphoma | 97.30% | DL |
| 16 | alopecia mucinosa | 97.21% | DL |
| 17 | alopecia areata | 97.09% | DL |
| 18 | telogen effluvium | 97.05% | DL |
| 19 | Quinquaud's folliculitis decalvans | 96.70% | DL |
| 20 | seborrheic keratosis | 96.63% | DL |

*Showing top 20 of 55 predictions.*

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
