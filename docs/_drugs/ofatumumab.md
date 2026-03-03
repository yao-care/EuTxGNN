---
layout: default
title: Ofatumumab
description: "Ofatumumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 417
evidence_level: L5
indication_count: 50
---

# Ofatumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ofatumumab |
| DrugBank ID | [DB06650](https://go.drugbank.com/drugs/DB06650) |
| Brand Names (EU) | Kesimpta |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Kesimpta is indicated for the treatment of adult patients with relapsing forms of multiple sclerosis (RMS) with active disease defined by clinical or imaging features (see section&nbsp;5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute lymphoblastic/lymphocytic leukemia | 99.88% | DL |
| 2 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.77% | DL |
| 3 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.77% | DL |
| 4 | Richter syndrome | 99.74% | DL |
| 5 | follicular lymphoma | 99.70% | DL |
| 6 | leukemia, lymphocytic, susceptibility to | 99.59% | DL |
| 7 | chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.55% | DL |
| 8 | metastatic neoplasm | 99.50% | DL |
| 9 | malignant spiradenoma | 99.48% | DL |
| 10 | Langerhans cell histiocytosis | 99.34% | DL |
| 11 | histiocytic and dendritic cell neoplasm | 98.99% | DL |
| 12 | childhood mediastinal neurogenic neoplasm | 98.94% | DL |
| 13 | childhood germ cell tumor | 98.94% | DL |
| 14 | childhood carcinoid tumor | 98.94% | DL |
| 15 | Hodgkins lymphoma | 98.93% | DL |
| 16 | optic nerve glioma | 98.93% | DL |
| 17 | childhood ependymoma | 98.93% | DL |
| 18 | childhood choroid plexus neoplasm | 98.92% | DL |
| 19 | mantle cell lymphoma | 98.91% | DL |
| 20 | neoplasm of mature B-cells | 98.89% | DL |

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
