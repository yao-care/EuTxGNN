---
layout: default
title: Decitabine
description: "Decitabine drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 161
evidence_level: L5
indication_count: 52
---

# Decitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Decitabine |
| DrugBank ID | [DB01262](https://go.drugbank.com/drugs/DB01262) |
| Brand Names (EU) | Dacogen, Inaqovi |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.56% |

---

## Approved Indication (EMA)

Inaqovi is indicated as monotherapy for the treatment of adult patients with newly diagnosed acute myeloid leukaemia (AML) who are ineligible for standard induction chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myeloid leukemia | 99.56% | DL |
| 2 | refractory cytopenia of childhood | 99.03% | DL |
| 3 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 99.02% | DL |
| 4 | unclassified myelodysplastic syndrome | 98.95% | DL |
| 5 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 98.95% | DL |
| 6 | acute myeloid leukemia with CEBPA somatic mutations | 98.93% | DL |
| 7 | partial deletion of the long arm of chromosome 5 | 98.86% | DL |
| 8 | myelodysplastic syndrome | 98.81% | DL |
| 9 | aregenerative anemia | 98.77% | DL |
| 10 | bulbar polio | 98.76% | DL |
| 11 | severe congenital hypochromic anemia with ringed sideroblasts | 98.63% | DL |
| 12 | 5q35 microduplication syndrome | 98.19% | DL |
| 13 | upper aerodigestive tract neoplasm | 97.69% | DL |
| 14 | neuralgic amyotrophy | 95.94% | DL |
| 15 | amyotrophic neuralgia | 95.46% | DL |
| 16 | Richter syndrome | 93.73% | DL |
| 17 | acute myeloid leukemia with t(8;16)(p11;p13) translocation | 93.26% | DL |
| 18 | acute lymphoblastic/lymphocytic leukemia | 92.74% | DL |
| 19 | acute myeloid leukemia with minimal differentiation | 92.54% | DL |
| 20 | acute myeloid leukemia with t(9;11)(p22;q23) | 92.06% | DL |

*Showing top 20 of 52 predictions.*

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
