---
layout: default
title: Isavuconazole
description: "Isavuconazole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 316
evidence_level: L5
indication_count: 50
---

# Isavuconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Isavuconazole |
| DrugBank ID | [DB11633](https://go.drugbank.com/drugs/DB11633) |
| Brand Names (EU) | Cresemba |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.99% |

---

## Approved Indication (EMA)

Powder for concentrate for solution for infusion: Cresemba is indicated in patients from 1 year of age and older for the treatment of  invasive aspergillosis mucormycosis in patients for whom amphotericin B is inappropriate (see sections 4.4 and 5.1)  Consideration should be given to official guidance on the appropriate use of antifungal agents. Hard capsules: Cresemba hard capsules are indicated in adults and in paediatric patients from 6 years of age for the treatment of  invasive aspergillosi

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 98.99% | DL |
| 2 | migraine with brainstem aura | 98.79% | DL |
| 3 | migraine with or without aura, susceptibility to | 98.31% | DL |
| 4 | pulmonary hypertension | 98.13% | DL |
| 5 | kyphoscoliotic heart disease | 97.98% | DL |
| 6 | rheumatoid arthritis | 97.57% | DL |
| 7 | atrophoderma vermiculata | 97.39% | DL |
| 8 | nephrogenic syndrome of inappropriate antidiuresis | 97.29% | DL |
| 9 | Prinzmetal angina | 97.08% | DL |
| 10 | ulerythema ophryogenesis | 97.01% | DL |
| 11 | brachydactyly-syndactyly syndrome | 96.49% | DL |
| 12 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.03% | DL |
| 13 | tendinitis | 95.04% | DL |
| 14 | homozygous familial hypercholesterolemia | 94.97% | DL |
| 15 | thrombotic disease | 94.89% | DL |
| 16 | idiopathic granulomatous myositis | 94.83% | DL |
| 17 | myositis fibrosa | 94.83% | DL |
| 18 | multiple endocrine neoplasia | 94.73% | DL |
| 19 | hyperthyroidism | 94.57% | DL |
| 20 | cor pulmonale | 94.49% | DL |

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
