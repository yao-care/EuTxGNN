---
layout: default
title: Natalizumab
description: "Natalizumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 395
evidence_level: L5
indication_count: 52
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Natalizumab |
| DrugBank ID | [DB00108](https://go.drugbank.com/drugs/DB00108) |
| Brand Names (EU) | Tyruko |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

Tyruko is indicated as single disease modifying therapy in adults with highly active relapsing remitting multiple sclerosis (RRMS) for the following patient groups: Patients with highly active disease despite a full and adequate course of treatment with at least one disease modifying therapy (DMT) (for exceptions and information about washout periods see sections 4.4 and 5.1) or Patients with rapidly evolving severe RRMS defined by 2 or more disabling relapses in one year, and with 1 or more Gad

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 99.46% | DL |
| 2 | parapsoriasis | 99.37% | DL |
| 3 | psoriasis | 99.19% | DL |
| 4 | severe nonproliferative diabetic retinopathy | 99.18% | DL |
| 5 | acute lichenoid pityriasis | 99.04% | DL |
| 6 | pityriasis lichenoides | 98.65% | DL |
| 7 | penile fibromatosis | 98.42% | DL |
| 8 | pustulosis palmaris et plantaris | 98.30% | DL |
| 9 | dermatitis | 98.25% | DL |
| 10 | neonatal dermatomyositis | 97.71% | DL |
| 11 | palmar fibromatosis | 97.70% | DL |
| 12 | Ledderhose disease | 97.67% | DL |
| 13 | acrodermatitis chronica atrophicans | 97.65% | DL |
| 14 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 97.61% | DL |
| 15 | amyopathic dermatomyositis | 97.58% | DL |
| 16 | acne keloid | 97.57% | DL |
| 17 | infantile digital fibromatosis | 97.56% | DL |
| 18 | psoriasis 14, pustular | 97.56% | DL |
| 19 | hydroa vacciniforme, familial | 97.24% | DL |
| 20 | inflammatory bowel disease | 96.99% | DL |

*Showing top 20 of 52 predictions.*

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
