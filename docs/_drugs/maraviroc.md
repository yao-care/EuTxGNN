---
layout: default
title: Maraviroc
description: "Maraviroc drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 363
evidence_level: L5
indication_count: 50
---

# Maraviroc
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Maraviroc |
| DrugBank ID | [DB04835](https://go.drugbank.com/drugs/DB04835) |
| Brand Names (EU) | Celsentri |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

Celsentri, in combination with other antiretroviral medicinal products, is indicated for treatment experienced adults, adolescents and children of 2 years of age and older and weighing at least 10 kg infected with only CCR5-tropic HIV-1 detectable

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 99.82% | DL |
| 2 | acne (disease) | 99.76% | DL |
| 3 | primary cutaneous T-cell lymphoma | 99.72% | DL |
| 4 | pediatric systemic lupus erythematosus | 99.71% | DL |
| 5 | primary cutaneous T-cell non-Hodgkin lymphoma | 99.50% | DL |
| 6 | primary cutaneous B-cell lymphoma | 99.38% | DL |
| 7 | candidiasis | 99.28% | DL |
| 8 | complement component 4a deficiency | 99.24% | DL |
| 9 | cytomegalovirus infection | 99.23% | DL |
| 10 | HER2 positive breast carcinoma | 99.22% | DL |
| 11 | hereditary neuroendocrine tumor of small intestine | 99.16% | DL |
| 12 | psoriasis | 99.09% | DL |
| 13 | Sezary syndrome | 99.02% | DL |
| 14 | infectious bovine rhinotracheitis | 99.01% | DL |
| 15 | malignant catarrh | 99.01% | DL |
| 16 | nephrotic syndrome | 99.01% | DL |
| 17 | Ewing sarcoma | 98.95% | DL |
| 18 | eye disease | 98.91% | DL |
| 19 | amenorrhea (disease) | 98.90% | DL |
| 20 | gestational trophoblastic neoplasm | 98.88% | DL |

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
