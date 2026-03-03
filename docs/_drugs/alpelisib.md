---
layout: default
title: Alpelisib
description: "Alpelisib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 32
evidence_level: L5
indication_count: 50
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Alpelisib |
| DrugBank ID | [DB12015](https://go.drugbank.com/drugs/DB12015) |
| Brand Names (EU) | Piqray |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.03% |

---

## Approved Indication (EMA)

Piqray is indicated in combination with fulvestrant for the treatment of postmenopausal women, and men, with hormone receptor (HR)-positive, human epidermal growth factor receptor 2 (HER2)-negative, locally advanced or metastatic breast cancer with a PIK3CA mutation after disease progression following endocrine therapy as monotherapy (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary hypertension | 99.03% | DL |
| 2 | migraine with or without aura, susceptibility to | 98.95% | DL |
| 3 | migraine disorder | 98.90% | DL |
| 4 | kyphoscoliotic heart disease | 98.86% | DL |
| 5 | rheumatoid arthritis | 98.75% | DL |
| 6 | leprosy | 98.69% | DL |
| 7 | migraine with brainstem aura | 98.68% | DL |
| 8 | thrombotic disease | 98.56% | DL |
| 9 | amyotrophic lateral sclerosis | 98.40% | DL |
| 10 | multiple endocrine neoplasia | 98.38% | DL |
| 11 | brachydactyly-syndactyly syndrome | 98.34% | DL |
| 12 | amyotrohpic lateral sclerosis type 22 | 98.12% | DL |
| 13 | nephrogenic syndrome of inappropriate antidiuresis | 98.11% | DL |
| 14 | Mills syndrome | 98.08% | DL |
| 15 | amyotrophic lateral sclerosis, susceptibility to | 98.08% | DL |
| 16 | female breast carcinoma | 98.07% | DL |
| 17 | coronary artery disease | 97.97% | DL |
| 18 | Prinzmetal angina | 97.93% | DL |
| 19 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.90% | DL |
| 20 | axial spondylometaphyseal dysplasia | 97.89% | DL |

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
