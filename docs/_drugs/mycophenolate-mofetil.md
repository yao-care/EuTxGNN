---
layout: default
title: Mycophenolate Mofetil
description: "Mycophenolate Mofetil drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 392
evidence_level: L5
indication_count: 50
---

# Mycophenolate Mofetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mycophenolate Mofetil |
| DrugBank ID | [DB00688](https://go.drugbank.com/drugs/DB00688) |
| Brand Names (EU) | Myclausen |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Myclausen is indicated in combination with ciclosporin and corticosteroids for the prophylaxis of acute transplant rejection in patients receiving allogeneic renal, cardiac or hepatic transplants.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.86% | DL |
| 2 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.76% | DL |
| 3 | bone Paget disease | 99.74% | DL |
| 4 | feline acquired immunodeficiency syndrome | 99.72% | DL |
| 5 | simian immunodeficiency virus infection | 99.72% | DL |
| 6 | multiple sclerosis | 99.54% | DL |
| 7 | hemosiderosis | 99.52% | DL |
| 8 | Heiner syndrome | 99.46% | DL |
| 9 | African iron overload | 99.36% | DL |
| 10 | neonatal hemochromatosis | 99.36% | DL |
| 11 | obsolete familial combined hyperlipidemia | 99.35% | DL |
| 12 | chronic hepatitis C virus infection | 99.32% | DL |
| 13 | hemosiderosis, pulmonary, with deficiency of gamma-a globulin | 99.32% | DL |
| 14 | hereditary hemochromatosis | 99.29% | DL |
| 15 | progressive relapsing multiple sclerosis | 99.28% | DL |
| 16 | AIDS | 99.25% | DL |
| 17 | gout | 99.16% | DL |
| 18 | skin disease | 98.89% | DL |
| 19 | psoriasis | 98.80% | DL |
| 20 | obsolete rare hereditary hemochromatosis | 98.79% | DL |

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
