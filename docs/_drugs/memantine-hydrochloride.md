---
layout: default
title: Memantine Hydrochloride
description: "Memantine Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 368
evidence_level: L5
indication_count: 50
---

# Memantine Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Memantine Hydrochloride |
| DrugBank ID | [DB01043](https://go.drugbank.com/drugs/DB01043) |
| Brand Names (EU) | Marixino (previously Maruxa) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.54% |

---

## Approved Indication (EMA)

Treatment of patients with moderate to severe Alzheimer’s disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary hypertension | 99.54% | DL |
| 2 | migraine disorder | 99.52% | DL |
| 3 | kyphoscoliotic heart disease | 99.43% | DL |
| 4 | migraine with brainstem aura | 99.41% | DL |
| 5 | rheumatoid arthritis | 98.73% | DL |
| 6 | nephrogenic syndrome of inappropriate antidiuresis | 98.67% | DL |
| 7 | atrophoderma vermiculata | 98.48% | DL |
| 8 | migraine with or without aura, susceptibility to | 98.43% | DL |
| 9 | ulerythema ophryogenesis | 98.21% | DL |
| 10 | brachydactyly-syndactyly syndrome | 98.12% | DL |
| 11 | osteoarthritis susceptibility | 97.75% | DL |
| 12 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.59% | DL |
| 13 | tendinitis | 97.58% | DL |
| 14 | pulmonary hypertension, primary, autosomal recessive | 97.50% | DL |
| 15 | gout | 97.46% | DL |
| 16 | myositis fibrosa | 97.44% | DL |
| 17 | idiopathic granulomatous myositis | 97.44% | DL |
| 18 | fibromyalgia | 97.23% | DL |
| 19 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 97.17% | DL |
| 20 | multiple endocrine neoplasia | 97.17% | DL |

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
