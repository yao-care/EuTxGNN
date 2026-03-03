---
layout: default
title: Micafungin
description: "Micafungin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 379
evidence_level: L5
indication_count: 50
---

# Micafungin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Micafungin |
| DrugBank ID | [DB01141](https://go.drugbank.com/drugs/DB01141) |
| Brand Names (EU) | Mycamine |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.03% |

---

## Approved Indication (EMA)

Mycamine is indicated for: Adults, adolescents ≥ 16 years of age and elderly  treatment of invasive candidiasis; treatment of oesophageal candidiasis in patients for whom intravenous therapy is appropriate; prophylaxis of Candida infection in patients undergoing allogeneic haematopoietic stem-cell transplantation or patients who are expected to have neutropenia (absolute neutrophil count &lt; 500 cells/µl) for 10 or more days.  Children (including neonates) and adolescents &lt; 16 years of age  

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | urinary tract infection (disease) | 99.03% | DL |
| 2 | gonococcal urethritis | 98.98% | DL |
| 3 | Ureaplasma urethritis | 98.98% | DL |
| 4 | uterine inflammatory disease | 98.70% | DL |
| 5 | xanthogranulomatous pyelonephritis | 98.67% | DL |
| 6 | malignant pleural mesothelioma | 98.09% | DL |
| 7 | malignant epithelioid mesothelioma | 97.23% | DL |
| 8 | malignant visceral pleura tumor | 97.08% | DL |
| 9 | sarcomatoid mesothelioma | 97.08% | DL |
| 10 | urogenital tuberculosis | 96.79% | DL |
| 11 | impetigo | 94.77% | DL |
| 12 | cysticercosis | 93.38% | DL |
| 13 | hordeolum | 93.37% | DL |
| 14 | staphylococcal scalded skin syndrome | 92.63% | DL |
| 15 | coenurosis | 92.61% | DL |
| 16 | pleural neoplasm | 92.00% | DL |
| 17 | candidemia | 90.52% | DL |
| 18 | bullous impetigo | 90.35% | DL |
| 19 | Clostridium infectious disease | 88.78% | DL |
| 20 | herpes zoster | 88.03% | DL |

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
