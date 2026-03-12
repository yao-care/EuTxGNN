---
layout: default
title: Enfuvirtide
description: "Enfuvirtide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 210
evidence_level: L5
indication_count: 51
---

# Enfuvirtide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Enfuvirtide |
| DrugBank ID | [DB00109](https://go.drugbank.com/drugs/DB00109) |
| Brand Names (EU) | Fuzeon |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.68% |

---

## Approved Indication (EMA)

Fuzeon is indicated in combination with other antiretroviral medicinal products for the treatment of HIV-1-infected patients who have received treatment with and failed on regimens containing at least one medicinal product from each of the following antiretroviral classes: protease inhibitors, non-nucleoside reverse-transcriptase inhibitors and nucleoside reverse-transcriptase inhibitors, or who have intolerance to previous antiretroviral regimens. In deciding on a new regimen for patients who h

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 98.68% | DL |
| 2 | simian immunodeficiency virus infection | 98.18% | DL |
| 3 | feline acquired immunodeficiency syndrome | 98.18% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 97.37% | DL |
| 5 | ulceration of vulva | 89.60% | DL |
| 6 | vulvar neoplasm | 88.74% | DL |
| 7 | vulvitis | 88.56% | DL |
| 8 | commissural lip fistula | 77.79% | DL |
| 9 | osteoradionecrosis of the mandible | 77.43% | DL |
| 10 | burning mouth syndrome | 77.36% | DL |
| 11 | oral leukoedema | 77.36% | DL |
| 12 | postmenopausal atrophic vaginitis | 73.45% | DL |
| 13 | vulvovaginitis | 73.32% | DL |
| 14 | ocular tuberculosis | 70.68% | DL |
| 15 | oral candidiasis | 70.54% | DL |
| 16 | corneal pigmentation | 70.18% | DL |
| 17 | myringitis bullosa hemorrhagica | 69.69% | DL |
| 18 | mycotic corneal ulcer | 68.43% | DL |
| 19 | guttate psoriasis | 68.09% | DL |
| 20 | anogenital human papillomavirus infection | 67.92% | DL |

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
