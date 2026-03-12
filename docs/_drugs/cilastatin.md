---
layout: default
title: Cilastatin
description: "cilastatin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 135
evidence_level: L5
indication_count: 50
---

# Cilastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cilastatin |
| DrugBank ID | [DB01597](https://go.drugbank.com/drugs/DB01597) |
| Brand Names (EU) | Cilastatin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bacterial arthritis | 99.98% | DL |
| 2 | staphylococcus aureus infection | 99.94% | DL |
| 3 | chronic rhinosinusitis | 99.90% | DL |
| 4 | chronic ethmoidal sinusitis | 99.89% | DL |
| 5 | sinusitis | 99.88% | DL |
| 6 | paranasal sinus neoplasm (disease) | 99.86% | DL |
| 7 | pneumonia | 99.81% | DL |
| 8 | paratyphoid fever | 99.65% | DL |
| 9 | bronchitis | 99.65% | DL |
| 10 | streptococcal pneumonia | 99.64% | DL |
| 11 | diffuse scleroderma | 99.55% | DL |
| 12 | salmonellosis | 99.43% | DL |
| 13 | meningococcal infection | 99.40% | DL |
| 14 | urinary tract infection (disease) | 99.36% | DL |
| 15 | bacterial pneumonia | 99.33% | DL |
| 16 | staphylococcal toxemia | 99.31% | DL |
| 17 | Ureaplasma urethritis | 99.24% | DL |
| 18 | gonococcal urethritis | 99.24% | DL |
| 19 | gingivitis | 99.22% | DL |
| 20 | staphylococcal infection | 99.15% | DL |

*Showing top 20 of 50 predictions.*

---


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
