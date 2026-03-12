---
layout: default
title: Eltrombopag
description: "Eltrombopag drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 202
evidence_level: L5
indication_count: 51
---

# Eltrombopag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eltrombopag |
| DrugBank ID | [DB06210](https://go.drugbank.com/drugs/DB06210) |
| Brand Names (EU) | Revolade |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.26% |

---

## Approved Indication (EMA)

Revolade is indicated for the treatment of adult patients with primary immune thrombocytopenia (ITP) who are refractory to other treatments (e.g. corticosteroids, immunoglobulins) (see sections 4.2 and 5.1). Revolade is indicated for the treatment of paediatric patients aged 1 year and above with primary immune thrombocytopenia (ITP) lasting 6 months or longer from diagnosis and who are refractory to other treatments (e.g. corticosteroids, immunoglobulins) (see sections 4.2 and 5.1). Revolade is

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.26% | DL |
| 2 | feline acquired immunodeficiency syndrome | 98.81% | DL |
| 3 | simian immunodeficiency virus infection | 98.81% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.76% | DL |
| 5 | female breast carcinoma | 98.59% | DL |
| 6 | obsolete familial combined hyperlipidemia | 98.04% | DL |
| 7 | homozygous familial hypercholesterolemia | 97.57% | DL |
| 8 | AIDS | 97.09% | DL |
| 9 | rheumatoid arthritis | 96.79% | DL |
| 10 | cholecystolithiasis | 96.08% | DL |
| 11 | conjunctivitis | 95.88% | DL |
| 12 | oral candidiasis | 95.60% | DL |
| 13 | commissural lip fistula | 95.32% | DL |
| 14 | osteoradionecrosis of the mandible | 95.30% | DL |
| 15 | oral leukoedema | 95.24% | DL |
| 16 | burning mouth syndrome | 95.24% | DL |
| 17 | conjunctivitis (disease) | 95.18% | DL |
| 18 | thrombotic disease | 94.73% | DL |
| 19 | congenital human immunodeficiency virus | 94.66% | DL |
| 20 | AIDS related complex | 94.66% | DL |

*Showing top 20 of 51 predictions.*

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
