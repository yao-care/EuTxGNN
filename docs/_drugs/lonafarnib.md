---
layout: default
title: Lonafarnib
description: "Lonafarnib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 350
evidence_level: L5
indication_count: 50
---

# Lonafarnib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lonafarnib |
| DrugBank ID | [DB06448](https://go.drugbank.com/drugs/DB06448) |
| Brand Names (EU) | Zokinvy |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.14% |

---

## Approved Indication (EMA)

Zokinvy is indicated for the treatment of patients 12 months of age and older with a genetically confirmed diagnosis of Hutchinson-Gilford progeria syndrome or a processing-deficient progeroid laminopathy associated with either a heterozygous LMNA mutation with progerin-like protein accumulation or a homozygous or compound heterozygous ZMPSTE24 mutation.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | leprosy | 99.14% | DL |
| 2 | rheumatoid arthritis | 98.82% | DL |
| 3 | Prinzmetal angina | 98.57% | DL |
| 4 | homozygous familial hypercholesterolemia | 98.32% | DL |
| 5 | hyperthyroidism | 98.17% | DL |
| 6 | pulmonary hypertension | 98.16% | DL |
| 7 | brachydactyly-syndactyly syndrome | 98.10% | DL |
| 8 | nephrogenic syndrome of inappropriate antidiuresis | 97.97% | DL |
| 9 | kyphoscoliotic heart disease | 97.96% | DL |
| 10 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.95% | DL |
| 11 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 97.85% | DL |
| 12 | heart disease | 97.80% | DL |
| 13 | multiple endocrine neoplasia | 97.66% | DL |
| 14 | Laubry-Pezzi syndrome | 97.65% | DL |
| 15 | Pierre Robin syndrome associated with a chromosomal anomaly | 97.63% | DL |
| 16 | Jeune syndrome situs inversus | 97.62% | DL |
| 17 | genetic syndromic Pierre Robin syndrome | 97.59% | DL |
| 18 | orofacial clefting syndrome | 97.56% | DL |
| 19 | partial deletion of the long arm of chromosome 7 | 97.55% | DL |
| 20 | disorder of fucoglycosan synthesis | 97.54% | DL |

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
