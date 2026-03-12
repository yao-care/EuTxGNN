---
layout: default
title: Palbociclib
description: "Palbociclib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 433
evidence_level: L5
indication_count: 50
---

# Palbociclib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Palbociclib |
| DrugBank ID | [DB09073](https://go.drugbank.com/drugs/DB09073) |
| Brand Names (EU) | Ibrance |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.44% |

---

## Approved Indication (EMA)

Ibrance is indicated for the treatment of hormone receptor (HR) positive, human epidermal growth factor receptor 2 (HER2) negative locally advanced or metastatic breast cancer:  in combination with an aromatase inhibitor; in combination with fulvestrant in women who have received prior endocrine therapy.  In pre- or perimenopausal women, the endocrine therapy should be combined with a luteinizing hormone releasing hormone (LHRH) agonist.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hyperthyroidism | 99.44% | DL |
| 2 | rheumatoid arthritis | 99.36% | DL |
| 3 | thrombotic disease | 99.32% | DL |
| 4 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 99.30% | DL |
| 5 | brachydactyly-syndactyly syndrome | 99.00% | DL |
| 6 | myeloid leukemia | 98.94% | DL |
| 7 | multiple endocrine neoplasia | 98.86% | DL |
| 8 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.85% | DL |
| 9 | hyperthyroxinemia | 98.78% | DL |
| 10 | Prinzmetal angina | 98.75% | DL |
| 11 | homozygous familial hypercholesterolemia | 98.70% | DL |
| 12 | vein disease | 98.55% | DL |
| 13 | thrombocytopenia | 98.51% | DL |
| 14 | female breast carcinoma | 98.39% | DL |
| 15 | Graves disease | 98.32% | DL |
| 16 | marcothrombocytopenia with mitral valve insufficiency | 98.31% | DL |
| 17 | hereditary thrombocytopenia with normal platelets | 98.31% | DL |
| 18 | transient neonatal thrombocytopenia | 98.24% | DL |
| 19 | plasma cell myeloma | 98.20% | DL |
| 20 | dense granule disease | 98.14% | DL |

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
