---
layout: default
title: Zonisamide
description: "Zonisamide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 651
evidence_level: L5
indication_count: 50
---

# Zonisamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Zonisamide |
| DrugBank ID | [DB00909](https://go.drugbank.com/drugs/DB00909) |
| Brand Names (EU) | Zonegran |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Zonegran is indicated as:  monotherapy in the treatment of partial seizures, with or without secondary generalisation, in adults with newly diagnosed epilepsy; adjunctive therapy in the treatment of partial seizures, with or without secondary generalisation, in adults, adolescents, and children aged six years and above.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Tourette syndrome | 99.85% | DL |
| 2 | trichotillomania | 99.78% | DL |
| 3 | methemoglobinemia, alpha type | 99.64% | DL |
| 4 | methemoglobinemia | 99.63% | DL |
| 5 | Prinzmetal angina | 99.55% | DL |
| 6 | methemoglobin reductase deficiency | 99.53% | DL |
| 7 | manic bipolar affective disorder | 99.35% | DL |
| 8 | absence epilepsy | 99.24% | DL |
| 9 | fibromyalgia | 99.20% | DL |
| 10 | conjunctivitis | 99.16% | DL |
| 11 | trigeminal nerve neoplasm | 99.15% | DL |
| 12 | multifocal atrial tachycardia (disease) | 99.14% | DL |
| 13 | tendinitis | 99.12% | DL |
| 14 | myositis fibrosa | 99.12% | DL |
| 15 | idiopathic granulomatous myositis | 99.12% | DL |
| 16 | nephrogenic syndrome of inappropriate antidiuresis | 99.05% | DL |
| 17 | migraine disorder | 99.05% | DL |
| 18 | visual epilepsy | 99.04% | DL |
| 19 | idiopathic neonatal atrial flutter | 98.90% | DL |
| 20 | inclusion body myositis | 98.87% | DL |

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
