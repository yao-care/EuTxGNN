---
layout: default
title: Mometasone
description: "Mometasone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 389
evidence_level: L5
indication_count: 50
---

# Mometasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mometasone |
| DrugBank ID | [DB00764](https://go.drugbank.com/drugs/DB00764) |
| Brand Names (EU) | Mometasone |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.36% |

---

## Approved Indication (EMA)

Enerzair Breezhaler is indicated as a maintenance treatment of asthma in adult patients not adequately controlled with a maintenance combination of a long acting beta2 agonist and a high dose of an inhaled corticosteroid who experienced one or more asthma exacerbations in the previous year.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | primary cutaneous T-cell lymphoma | 99.36% | DL |
| 2 | Crohn's colitis | 98.81% | DL |
| 3 | myelodysplastic syndrome | 98.34% | DL |
| 4 | refractory cytopenia of childhood | 98.06% | DL |
| 5 | unclassified myelodysplastic syndrome | 97.94% | DL |
| 6 | partial deletion of the long arm of chromosome 5 | 97.86% | DL |
| 7 | cystic teratoma | 97.79% | DL |
| 8 | spinal cord dermoid cyst | 97.75% | DL |
| 9 | aregenerative anemia | 97.75% | DL |
| 10 | disease of orbital part of eye adnexa | 97.73% | DL |
| 11 | severe congenital hypochromic anemia with ringed sideroblasts | 97.71% | DL |
| 12 | renin-angiotensin-aldosterone system-blocker-induced angioedema | 97.69% | DL |
| 13 | dermoid cyst of ovary | 97.62% | DL |
| 14 | disease of orbital region | 97.41% | DL |
| 15 | nephrotic syndrome | 97.22% | DL |
| 16 | granulomatous slack skin disease | 97.21% | DL |
| 17 | Sezary syndrome | 97.13% | DL |
| 18 | primary cutaneous B-cell lymphoma | 96.98% | DL |
| 19 | folliculotropic mycosis fungoides | 96.69% | DL |
| 20 | mycotic corneal ulcer | 96.39% | DL |

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
