---
layout: default
title: Dexamethasone
description: "dexamethasone drug repurposing predictions from TxGNN. Evidence level L1 with 174 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 170
evidence_level: L1
indication_count: 174
---

# Dexamethasone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **174**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dexamethasone |
| DrugBank ID | [DB01234](https://go.drugbank.com/drugs/DB01234) |
| Brand Names (EU) | Neofordex, Ozurdex |
| Evidence Level | L1 |
| Predicted Indications | 174 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment of multiple myeloma.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | alopecia areata | 99.99% | DL |
| 2 | alopecia mucinosa | 99.99% | DL |
| 3 | telogen effluvium | 99.99% | DL |
| 4 | Quinquaud's folliculitis decalvans | 99.99% | DL |
| 5 | alopecia antibody deficiency | 99.99% | DL |
| 6 | hereditary hypotrichosis with recurrent skin vesicles | 99.99% | DL |
| 7 | alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 99.99% | DL |
| 8 | atrichia with papular lesions | 99.95% | DL |
| 9 | tenosynovitis | 99.83% | DL |
| 10 | granulomatous slack skin disease | 99.78% | DL |
| 11 | familial adrenal hypoplasia with absent pituitary luteinizing hormone | 99.78% | DL |
| 12 | adrenocortical insufficiency | 99.76% | DL |
| 13 | alopecia universalis onychodystrophy vitiligo | 99.76% | DL |
| 14 | acquired thrombocytopenia | 99.75% | DL |
| 15 | nephrotic syndrome | 99.73% | DL |
| 16 | Addison disease | 99.70% | DL |
| 17 | prolapse of lacrimal gland | 99.65% | DL |
| 18 | miliary tuberculosis | 99.62% | DL |
| 19 | idiopathic steroid-sensitive nephrotic syndrome | 99.58% | DL |
| 20 | sporadic idiopathic steroid-resistant nephrotic syndrome | 99.57% | DL |

*Showing top 20 of 174 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| alopecia areata | L1 | 13 | 20 | 3 Phase 2 trial(s), 2 RCT(s), 2 review(s)/meta-ana |

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
