---
layout: default
title: Imipenem
description: "Imipenem drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 295
evidence_level: L5
indication_count: 50
---

# Imipenem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Imipenem |
| DrugBank ID | [DB01598](https://go.drugbank.com/drugs/DB01598) |
| Brand Names (EU) | Imipenem |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diffuse scleroderma | 99.99% | DL |
| 2 | paratyphoid fever | 99.99% | DL |
| 3 | bacterial arthritis | 99.99% | DL |
| 4 | salmonellosis | 99.99% | DL |
| 5 | sinusitis | 99.99% | DL |
| 6 | chronic rhinosinusitis | 99.98% | DL |
| 7 | typhoid fever | 99.98% | DL |
| 8 | chronic ethmoidal sinusitis | 99.98% | DL |
| 9 | paranasal sinus neoplasm (disease) | 99.98% | DL |
| 10 | staphylococcus aureus infection | 99.95% | DL |
| 11 | peritonitis | 99.90% | DL |
| 12 | bacterial pneumonia | 99.88% | DL |
| 13 | eosinophilia-myalgia syndrome | 99.85% | DL |
| 14 | infectious otitis media | 99.83% | DL |
| 15 | epiglottitis | 99.83% | DL |
| 16 | streptococcal pneumonia | 99.81% | DL |
| 17 | conjunctivitis | 99.80% | DL |
| 18 | scleroderma, familial progressive | 99.76% | DL |
| 19 | suppurative otitis media | 99.75% | DL |
| 20 | chronic otitis media | 99.75% | DL |

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
