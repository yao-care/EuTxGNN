---
layout: default
title: Remdesivir
description: "Remdesivir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 487
evidence_level: L5
indication_count: 50
---

# Remdesivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Remdesivir |
| DrugBank ID | [DB14761](https://go.drugbank.com/drugs/DB14761) |
| Brand Names (EU) | Veklury |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.50% |

---

## Approved Indication (EMA)

Veklury is indicated for the treatment of coronavirus disease 2019 (COVID 19) in&nbsp;adults and paediatric patients (at least 4 weeks of age and weighing at least 3 kg):&nbsp;  with pneumonia requiring supplemental oxygen (low- or high-flow oxygen or other non-invasive ventilation at start of treatment) who do not require supplemental oxygen and who are at increased risk of progressing to severe COVID-19 (see section 5.1)

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 99.50% | DL |
| 2 | HIV infectious disease | 99.32% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.07% | DL |
| 4 | simian immunodeficiency virus infection | 99.07% | DL |
| 5 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.03% | DL |
| 6 | homozygous familial hypercholesterolemia | 99.03% | DL |
| 7 | Prinzmetal angina | 98.34% | DL |
| 8 | leprosy | 97.37% | DL |
| 9 | antithrombin deficiency type 2 | 97.25% | DL |
| 10 | cytomegalovirus infection | 97.08% | DL |
| 11 | factor 5 excess with spontaneous thrombosis | 96.99% | DL |
| 12 | heparin cofactor 2 deficiency | 96.95% | DL |
| 13 | infectious bovine rhinotracheitis | 96.89% | DL |
| 14 | malignant catarrh | 96.89% | DL |
| 15 | oral candidiasis | 96.83% | DL |
| 16 | hyperthyroidism | 96.79% | DL |
| 17 | hypoalphalipoproteinemia | 96.70% | DL |
| 18 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 96.62% | DL |
| 19 | conjunctivitis | 96.57% | DL |
| 20 | commissural lip fistula | 96.56% | DL |

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
