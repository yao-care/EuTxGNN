---
layout: default
title: Abiraterone Acetate
description: "Abiraterone Acetate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 14
evidence_level: L5
indication_count: 50
---

# Abiraterone Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Abiraterone Acetate |
| DrugBank ID | [DB05812](https://go.drugbank.com/drugs/DB05812) |
| Brand Names (EU) | Zytiga |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.81% |

---

## Approved Indication (EMA)

Treatment of adult patients with prostate cancer.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 98.81% | DL |
| 2 | migraine with or without aura, susceptibility to | 98.75% | DL |
| 3 | migraine with brainstem aura | 98.61% | DL |
| 4 | leprosy | 98.58% | DL |
| 5 | pulmonary hypertension | 98.36% | DL |
| 6 | nephrogenic syndrome of inappropriate antidiuresis | 98.23% | DL |
| 7 | rheumatoid arthritis | 98.13% | DL |
| 8 | kyphoscoliotic heart disease | 98.11% | DL |
| 9 | atrophoderma vermiculata | 97.66% | DL |
| 10 | ulerythema ophryogenesis | 97.53% | DL |
| 11 | brachydactyly-syndactyly syndrome | 97.08% | DL |
| 12 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.03% | DL |
| 13 | hyperthyroidism | 95.74% | DL |
| 14 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 95.42% | DL |
| 15 | allergic asthma | 95.34% | DL |
| 16 | pulmonary hypertension, primary, autosomal recessive | 95.34% | DL |
| 17 | headache disorder | 95.34% | DL |
| 18 | trigeminal autonomic cephalalgia | 95.05% | DL |
| 19 | genetic multiple congenital anomalies/dysmorphic syndrome without intellectual disability | 94.97% | DL |
| 20 | homozygous familial hypercholesterolemia | 94.96% | DL |

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
