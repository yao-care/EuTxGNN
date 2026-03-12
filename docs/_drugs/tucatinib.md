---
layout: default
title: Tucatinib
description: "Tucatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 610
evidence_level: L5
indication_count: 50
---

# Tucatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tucatinib |
| DrugBank ID | [DB11652](https://go.drugbank.com/drugs/DB11652) |
| Brand Names (EU) | Tukysa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.62% |

---

## Approved Indication (EMA)

Tukysa is indicated in combination with trastuzumab and capecitabine for the treatment of adult patients with HER2?positive locally advanced or metastatic breast cancer who have received at least 2 prior anti-HER2 treatment regimens.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 98.62% | DL |
| 2 | multiple endocrine neoplasia | 98.52% | DL |
| 3 | nephrogenic syndrome of inappropriate antidiuresis | 98.45% | DL |
| 4 | migraine with brainstem aura | 98.37% | DL |
| 5 | pulmonary hypertension | 98.36% | DL |
| 6 | homozygous familial hypercholesterolemia | 98.26% | DL |
| 7 | kyphoscoliotic heart disease | 98.20% | DL |
| 8 | migraine with or without aura, susceptibility to | 98.01% | DL |
| 9 | Prinzmetal angina | 97.99% | DL |
| 10 | rheumatoid arthritis | 97.77% | DL |
| 11 | leprosy | 97.25% | DL |
| 12 | brachydactyly-syndactyly syndrome | 97.02% | DL |
| 13 | atrophoderma vermiculata | 96.78% | DL |
| 14 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.43% | DL |
| 15 | hyperthyroidism | 96.30% | DL |
| 16 | ulerythema ophryogenesis | 96.21% | DL |
| 17 | hypoalphalipoproteinemia | 96.14% | DL |
| 18 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 95.84% | DL |
| 19 | cytomegalovirus infection | 95.74% | DL |
| 20 | amyotrophic lateral sclerosis | 95.59% | DL |

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
