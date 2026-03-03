---
layout: default
title: Dacomitinib Monohydrate
description: "Dacomitinib Monohydrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 149
evidence_level: L5
indication_count: 50
---

# Dacomitinib Monohydrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dacomitinib Monohydrate |
| DrugBank ID | [DB11963](https://go.drugbank.com/drugs/DB11963) |
| Brand Names (EU) | Vizimpro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.79% |

---

## Approved Indication (EMA)

Vizimpro, as monotherapy, is indicated for the first-line treatment of adult patients with locally advanced or metastatic non small cell lung cancer (NSCLC) with epidermal growth factor receptor (EGFR) activating mutations.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 97.79% | DL |
| 2 | homozygous familial hypercholesterolemia | 96.92% | DL |
| 3 | brachydactyly-syndactyly syndrome | 96.78% | DL |
| 4 | pulmonary hypertension | 96.51% | DL |
| 5 | nephrogenic syndrome of inappropriate antidiuresis | 96.44% | DL |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.44% | DL |
| 7 | kyphoscoliotic heart disease | 96.18% | DL |
| 8 | multiple endocrine neoplasia | 96.18% | DL |
| 9 | amyotrophic lateral sclerosis | 95.12% | DL |
| 10 | leprosy | 94.95% | DL |
| 11 | Prinzmetal angina | 94.92% | DL |
| 12 | migraine disorder | 94.81% | DL |
| 13 | hyperthyroidism | 94.70% | DL |
| 14 | female breast carcinoma | 94.51% | DL |
| 15 | Mills syndrome | 94.50% | DL |
| 16 | amyotrophic lateral sclerosis, susceptibility to | 94.48% | DL |
| 17 | amyotrohpic lateral sclerosis type 22 | 94.46% | DL |
| 18 | migraine with brainstem aura | 94.39% | DL |
| 19 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 94.28% | DL |
| 20 | migraine with or without aura, susceptibility to | 94.24% | DL |

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
