---
layout: default
title: Ibuprofen
description: "Ibuprofen drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 285
evidence_level: L5
indication_count: 50
---

# Ibuprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ibuprofen |
| DrugBank ID | [DB01050](https://go.drugbank.com/drugs/DB01050) |
| Brand Names (EU) | Pedea |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.90% |

---

## Approved Indication (EMA)

Treatment of a haemodynamically significant patent ductus arteriosus in preterm newborn infants less than 34 weeks of gestational age.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | osteoarthritis susceptibility | 99.90% | DL |
| 2 | osteoarthritis | 99.82% | DL |
| 3 | rheumatoid arthritis | 99.77% | DL |
| 4 | acromesomelic dysplasia, Hunter-Thompson type | 99.74% | DL |
| 5 | brachyolmia-amelogenesis imperfecta syndrome | 99.71% | DL |
| 6 | myosclerosis | 99.68% | DL |
| 7 | brachyolmia | 99.67% | DL |
| 8 | brachydactyly-syndactyly syndrome | 99.66% | DL |
| 9 | pseudoachondroplasia | 99.66% | DL |
| 10 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.60% | DL |
| 11 | arthropathy | 99.53% | DL |
| 12 | hypotrichosis simplex of the scalp | 98.59% | DL |
| 13 | WHIM syndrome | 98.43% | DL |
| 14 | congenital hypotrichosis milia | 98.31% | DL |
| 15 | diffuse alopecia areata | 98.25% | DL |
| 16 | rheumatoid nodulosis | 96.76% | DL |
| 17 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 96.45% | DL |
| 18 | juvenile idiopathic arthritis | 96.43% | DL |
| 19 | juvenile arthritis due to defect in LACC1 | 96.31% | DL |
| 20 | combined immunodeficiency due to moesin deficiency | 96.30% | DL |

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
