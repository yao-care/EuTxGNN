---
layout: default
title: Golimumab
description: "Golimumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 275
evidence_level: L5
indication_count: 50
---

# Golimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Golimumab |
| DrugBank ID | [DB06674](https://go.drugbank.com/drugs/DB06674) |
| Brand Names (EU) | Gobivaz |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.79% |

---

## Approved Indication (EMA)

Rheumatoid arthritis (RA) Gobivaz, in combination with methotrexate (MTX), is indicated for:  the treatment of moderate to severe, active rheumatoid arthritis in adults when the response to disease-modifying anti-rheumatic drug (DMARD) therapy including MTX has been inadequate. the treatment of severe, active and progressive rheumatoid arthritis in adults not previously treated with MTX.  Golimumab, in combination with MTX, has been shown to reduce the rate of progression of joint damage as meas

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ankylosing spondylitis | 99.79% | DL |
| 2 | rheumatoid vasculitis | 99.73% | DL |
| 3 | hypermobility of coccyx | 99.67% | DL |
| 4 | inflammatory spondylopathy | 99.66% | DL |
| 5 | Kummell disease | 99.61% | DL |
| 6 | polyarticular juvenile rheumatoid arthritis | 99.59% | DL |
| 7 | spondyloarthropathy, susceptibility to | 99.53% | DL |
| 8 | vertebral disease | 98.76% | DL |
| 9 | ulcerative colitis (disease) | 96.62% | DL |
| 10 | congenital hypotrichosis with juvenile macular dystrophy | 96.16% | DL |
| 11 | polyp of vocal cord | 95.83% | DL |
| 12 | polyp of middle ear | 95.83% | DL |
| 13 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 95.74% | DL |
| 14 | polyp of ureter | 95.67% | DL |
| 15 | polyp of frontal sinus | 95.65% | DL |
| 16 | epulis | 95.58% | DL |
| 17 | polyp of external auditory canal | 95.58% | DL |
| 18 | uterine polyp | 95.48% | DL |
| 19 | polyp of vulva | 95.46% | DL |
| 20 | heparin cofactor 2 deficiency | 95.38% | DL |

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
