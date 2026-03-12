---
layout: default
title: Gilteritinib Fumarate
description: "Gilteritinib Fumarate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 265
evidence_level: L5
indication_count: 50
---

# Gilteritinib Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Gilteritinib Fumarate |
| DrugBank ID | [DB12141](https://go.drugbank.com/drugs/DB12141) |
| Brand Names (EU) | Xospata |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.45% |

---

## Approved Indication (EMA)

Xospata is indicated as monotherapy for the treatment of adult patients who have relapsed or refractory acute myeloid leukaemia (AML) with a FLT3 mutation.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 99.45% | DL |
| 2 | acute myeloid leukemia with CEBPA somatic mutations | 99.43% | DL |
| 3 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 99.39% | DL |
| 4 | acute myeloid leukemia and myelodysplastic syndromes related to topoisomerase type 2 inhibitor | 99.30% | DL |
| 5 | bulbar polio | 99.10% | DL |
| 6 | acute myeloid leukemia and myelodysplastic syndromes related to alkylating agent | 98.99% | DL |
| 7 | acute myeloid leukemia and myelodysplastic syndromes related to radiation | 98.99% | DL |
| 8 | 5q35 microduplication syndrome | 98.89% | DL |
| 9 | myeloid leukemia | 98.58% | DL |
| 10 | therapy related acute myeloid leukemia and myelodysplastic syndrome | 98.54% | DL |
| 11 | acute myeloid leukemia with t(8;16)(p11;p13) translocation | 98.46% | DL |
| 12 | acute myeloid leukemia with t(9;11)(p22;q23) | 98.27% | DL |
| 13 | unclassified acute myeloid leukemia | 98.20% | DL |
| 14 | acute myeloblastic leukemia with maturation | 98.19% | DL |
| 15 | acute myeloblastic leukemia without maturation | 98.11% | DL |
| 16 | acute myeloid leukemia with t(6;9)(p23;q34) | 98.10% | DL |
| 17 | neuralgic amyotrophy | 98.10% | DL |
| 18 | acute myeloid leukemia with minimal differentiation | 98.09% | DL |
| 19 | amyotrophic neuralgia | 97.96% | DL |
| 20 | inherited acute myeloid leukemia | 97.86% | DL |

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
