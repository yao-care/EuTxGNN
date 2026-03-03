---
layout: default
title: Nusinersen Sodium
description: "Nusinersen Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 413
evidence_level: L5
indication_count: 50
---

# Nusinersen Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nusinersen Sodium |
| DrugBank ID | [DB13161](https://go.drugbank.com/drugs/DB13161) |
| Brand Names (EU) | Spinraza |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 50.00% |

---

## Approved Indication (EMA)

Spinraza is indicated for the treatment of 5q Spinal Muscular Atrophy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | PRPS1 deficiency disorder | 50.00% | DL |
| 2 | hypervalinemia and hyperleucine-isoleucinemia | 50.00% | DL |
| 3 | exercise-induced anaphylaxis | 50.00% | DL |
| 4 | acetazolamide-responsive hereditary episodic ataxia | 50.00% | DL |
| 5 | cerebral folate deficiency | 50.00% | DL |
| 6 | adolescent/adult onset autosomal dominant epilepsy with auditory features | 50.00% | DL |
| 7 | antibody mediated epilepsy | 50.00% | DL |
| 8 | febrile seizures plus, genetic epilepsy with febrile seizures plus | 50.00% | DL |
| 9 | food protein-induced allergic proctocolitis | 50.00% | DL |
| 10 | MED12-related intellectual disability syndrome | 50.00% | DL |
| 11 | rod-cone dystrophy, sensorineural deafness, and Fanconi-type renal dysfunction | 50.00% | DL |
| 12 | mixed mineral dust pneumoconiosis | 50.00% | DL |
| 13 | epilepsy of infancy with migrating focal seizures | 50.00% | DL |
| 14 | neonatal/infantile epilepsy syndrome | 50.00% | DL |
| 15 | primary mast cell activation syndrome | 50.00% | DL |
| 16 | adult-onset segmental dystonia | 50.00% | DL |
| 17 | paratenonitis with tendinosis | 50.00% | DL |
| 18 | tendinosis | 50.00% | DL |
| 19 | TH-deficient infantile parkinsonism and motor delay | 50.00% | DL |
| 20 | saccharopinuria | 50.00% | DL |

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
