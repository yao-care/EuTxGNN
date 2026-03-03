---
layout: default
title: Tadalafil
description: "Tadalafil drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 550
evidence_level: L5
indication_count: 53
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tadalafil |
| DrugBank ID | [DB00820](https://go.drugbank.com/drugs/DB00820) |
| Brand Names (EU) | Adcirca (previously Tadalafil Lilly), Talmanco (previously Tadalafil Generics) |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Talmanco is indicated in adults for the treatment of pulmonary arterial hypertension (PAH) classified as WHO functional class II and III, to improve exercise capacity. Efficacy has been shown in idiopathic PAH (IPAH) and in PAH related to collagen vascular disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ambras type hypertrichosis universalis congenita | 99.98% | DL |
| 2 | hypertrichosis (disease) | 99.98% | DL |
| 3 | malformation syndrome with odontal and/or periodontal component | 99.97% | DL |
| 4 | syndrome with a Dandy-Walker malformation as major feature | 99.97% | DL |
| 5 | isolated genetic hair shaft abnormality | 99.96% | DL |
| 6 | benign prostatic hyperplasia (disease) | 99.96% | DL |
| 7 | familial isolated trichomegaly | 99.65% | DL |
| 8 | pulmonary hypertension | 99.43% | DL |
| 9 | kyphoscoliotic heart disease | 99.43% | DL |
| 10 | migraine with brainstem aura | 99.08% | DL |
| 11 | migraine disorder | 98.91% | DL |
| 12 | hypotrichosis simplex of the scalp | 98.71% | DL |
| 13 | Raynaud disease | 98.58% | DL |
| 14 | congenital hypotrichosis milia | 98.56% | DL |
| 15 | alopecia | 98.34% | DL |
| 16 | diffuse alopecia areata | 98.06% | DL |
| 17 | genetic alopecia | 98.02% | DL |
| 18 | familial clubfoot due to 17q23.1q23.2 microduplication | 97.73% | DL |
| 19 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 97.63% | DL |
| 20 | pulmonary hypertension, primary, autosomal recessive | 97.61% | DL |

*Showing top 20 of 53 predictions.*

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
