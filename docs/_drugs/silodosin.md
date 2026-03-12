---
layout: default
title: Silodosin
description: "Silodosin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 528
evidence_level: L5
indication_count: 50
---

# Silodosin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Silodosin |
| DrugBank ID | [DB06207](https://go.drugbank.com/drugs/DB06207) |
| Brand Names (EU) | Silodosin Recordati |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment of the signs and symptoms of benign prostatic hyperplasia (BPH) in adult men.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ambras type hypertrichosis universalis congenita | 99.99% | DL |
| 2 | hypertrichosis (disease) | 99.99% | DL |
| 3 | malformation syndrome with odontal and/or periodontal component | 99.99% | DL |
| 4 | syndrome with a Dandy-Walker malformation as major feature | 99.98% | DL |
| 5 | isolated genetic hair shaft abnormality | 99.98% | DL |
| 6 | benign prostatic hyperplasia (disease) | 99.91% | DL |
| 7 | familial isolated trichomegaly | 99.23% | DL |
| 8 | persistent fetal circulation syndrome | 96.36% | DL |
| 9 | hypotrichosis simplex of the scalp | 94.89% | DL |
| 10 | congenital hypotrichosis milia | 94.67% | DL |
| 11 | chronic thromboembolic pulmonary hypertension | 94.64% | DL |
| 12 | allergic urticaria | 94.08% | DL |
| 13 | diffuse alopecia areata | 92.76% | DL |
| 14 | kyphoscoliotic heart disease | 92.28% | DL |
| 15 | migraine with brainstem aura | 91.54% | DL |
| 16 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 90.02% | DL |
| 17 | familial clubfoot due to 17q23.1q23.2 microduplication | 89.67% | DL |
| 18 | alopecia | 89.46% | DL |
| 19 | pulmonary hypertension | 89.34% | DL |
| 20 | pulmonary hypertension, primary, autosomal recessive | 88.69% | DL |

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
