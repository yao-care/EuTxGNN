---
layout: default
title: Aztreonam
description: "Aztreonam drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 67
evidence_level: L5
indication_count: 52
---

# Aztreonam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aztreonam |
| DrugBank ID | [DB00355](https://go.drugbank.com/drugs/DB00355) |
| Brand Names (EU) | Aztreonam, Emblaveo |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.73% |

---

## Approved Indication (EMA)

Emblaveo is indicated for the treatment of the following infections in adult patients (see sections 4.4 and 5.1):• Complicated intra-abdominal infection (cIAI)• Hospital-acquired pneumonia (HAP), including ventilator-associated pneumonia (VAP)&nbsp;• Complicated urinary tract infection (cUTI), including pyelonephritisEmblaveo is also indicated for the treatment of infections due to aerobic Gram-negative organisms in adult patients with limited treatment options (see sections 4.2, 4.4, and 5.1).C

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | polyclonal hyperviscosity syndrome | 99.73% | DL |
| 2 | hyperamylasemia | 99.73% | DL |
| 3 | urinary tract infection (disease) | 99.69% | DL |
| 4 | congenital analbuminemia | 99.69% | DL |
| 5 | Ureaplasma urethritis | 99.59% | DL |
| 6 | gonococcal urethritis | 99.59% | DL |
| 7 | blood group incompatibility | 99.59% | DL |
| 8 | premalignant hematological system disease | 99.54% | DL |
| 9 | epiglottitis | 99.53% | DL |
| 10 | monoclonal gammopathy | 99.50% | DL |
| 11 | xanthogranulomatous pyelonephritis | 99.49% | DL |
| 12 | uterine inflammatory disease | 99.47% | DL |
| 13 | hematological disease associated with an acquired peripheral neuropathy | 99.46% | DL |
| 14 | septicemic plague | 99.38% | DL |
| 15 | congenital hematological disorder | 99.32% | DL |
| 16 | Peptostreptococcus infectious disease | 99.28% | DL |
| 17 | staphylococcus aureus infection | 99.19% | DL |
| 18 | toxocariasis | 99.13% | DL |
| 19 | streptococcal pneumonia | 98.90% | DL |
| 20 | urogenital tuberculosis | 98.84% | DL |

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
