---
layout: default
title: Umeclidinium Bromide
description: "Umeclidinium Bromide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 615
evidence_level: L5
indication_count: 50
---

# Umeclidinium Bromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Umeclidinium Bromide |
| DrugBank ID | [DB09076](https://go.drugbank.com/drugs/DB09076) |
| Brand Names (EU) | Rolufta Ellipta (previously Rolufta) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.36% |

---

## Approved Indication (EMA)

Rolufta is indicated as a maintenance bronchodilator treatment to relieve symptoms in adult patients with chronic obstructive pulmonary disease (COPD).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 96.36% | DL |
| 2 | migraine with brainstem aura | 95.83% | DL |
| 3 | open-angle glaucoma | 93.28% | DL |
| 4 | primary hereditary glaucoma | 92.91% | DL |
| 5 | nephrogenic syndrome of inappropriate antidiuresis | 92.03% | DL |
| 6 | gastroduodenitis | 91.91% | DL |
| 7 | common cold | 91.74% | DL |
| 8 | atrophoderma vermiculata | 91.24% | DL |
| 9 | peptic ulcer disease | 91.05% | DL |
| 10 | allergic urticaria | 90.66% | DL |
| 11 | migraine with or without aura, susceptibility to | 90.62% | DL |
| 12 | ulerythema ophryogenesis | 89.84% | DL |
| 13 | schizophrenia | 89.81% | DL |
| 14 | Ambras type hypertrichosis universalis congenita | 89.80% | DL |
| 15 | hypertrichosis (disease) | 89.55% | DL |
| 16 | insomnia (disease) | 89.47% | DL |
| 17 | headache disorder | 89.44% | DL |
| 18 | acute intermittent porphyria | 89.37% | DL |
| 19 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 89.13% | DL |
| 20 | malformation syndrome with odontal and/or periodontal component | 89.11% | DL |

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
