---
layout: default
title: Hydrocortisone
description: "Hydrocortisone drug repurposing predictions from TxGNN. Evidence level L5 with 171 predicted indications."
parent: AI Predictions (L5)
nav_order: 282
evidence_level: L5
indication_count: 171
---

# Hydrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **171**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Hydrocortisone |
| DrugBank ID | [DB00741](https://go.drugbank.com/drugs/DB00741) |
| Brand Names (EU) | Alkindi, Efmody, Plenadren |
| Evidence Level | L5 |
| Predicted Indications | 171 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Treatment of adrenal insufficiency in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | alopecia areata | 99.97% | DL |
| 2 | alopecia mucinosa | 99.97% | DL |
| 3 | telogen effluvium | 99.97% | DL |
| 4 | Quinquaud's folliculitis decalvans | 99.97% | DL |
| 5 | alopecia antibody deficiency | 99.96% | DL |
| 6 | hereditary hypotrichosis with recurrent skin vesicles | 99.96% | DL |
| 7 | alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 99.96% | DL |
| 8 | atrichia with papular lesions | 99.86% | DL |
| 9 | acquired thrombocytopenia | 99.67% | DL |
| 10 | alopecia universalis onychodystrophy vitiligo | 99.61% | DL |
| 11 | nephrotic syndrome | 99.61% | DL |
| 12 | tenosynovitis | 99.51% | DL |
| 13 | idiopathic steroid-sensitive nephrotic syndrome | 99.46% | DL |
| 14 | sporadic idiopathic steroid-resistant nephrotic syndrome | 99.43% | DL |
| 15 | fetal erythroblastosis | 99.38% | DL |
| 16 | miliary tuberculosis | 99.36% | DL |
| 17 | Trichinellosis | 99.26% | DL |
| 18 | granulomatous slack skin disease | 99.21% | DL |
| 19 | autoimmune hemolytic anemia | 99.04% | DL |
| 20 | rheumatic heart disease | 99.02% | DL |

*Showing top 20 of 171 predictions.*

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
