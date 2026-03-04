---
layout: default
title: Pegaspargase
description: "pegaspargase drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 444
evidence_level: L1
indication_count: 50
---

# Pegaspargase
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pegaspargase |
| DrugBank ID | [DB00059](https://go.drugbank.com/drugs/DB00059) |
| Brand Names (EU) | Oncaspar |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Oncaspar is indicated as a component of antineoplastic combination therapy in acute lymphoblastic leukaemia (ALL) in paediatric patients from birth to 18 years, and adult patients.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute lymphoblastic leukemia (disease) | 99.99% | DL |
| 2 | leukemia, lymphocytic, susceptibility to | 99.98% | DL |
| 3 | acute lymphoblastic/lymphocytic leukemia | 99.97% | DL |
| 4 | precursor lymphoblastic lymphoma/leukemia | 99.96% | DL |
| 5 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.95% | DL |
| 6 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.95% | DL |
| 7 | follicular lymphoma | 99.90% | DL |
| 8 | acute lymphoblastic leukemia | 99.89% | DL |
| 9 | precursor T-cell acute lymphoblastic leukemia | 99.76% | DL |
| 10 | methylcobalamin deficiency type cblE | 99.74% | DL |
| 11 | lymphoid neoplasm | 99.71% | DL |
| 12 | Hodgkins lymphoma | 99.71% | DL |
| 13 | chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.68% | DL |
| 14 | blast phase chronic myelogenous leukemia, BCR-ABL1 positive | 99.61% | DL |
| 15 | myeloid leukemia | 99.60% | DL |
| 16 | bladder transitional cell carcinoma | 99.41% | DL |
| 17 | Quinquaud's folliculitis decalvans | 98.80% | DL |
| 18 | alopecia mucinosa | 98.76% | DL |
| 19 | telogen effluvium | 98.69% | DL |
| 20 | hereditary hypotrichosis with recurrent skin vesicles | 98.68% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| acute lymphoblastic leukemia (disease) | L1 | 20 | 0 | 6 Phase 3 trial(s), 5 Phase 2 trial(s) |

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
