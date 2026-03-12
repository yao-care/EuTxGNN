---
layout: default
title: Certolizumab Pegol
description: "Certolizumab Pegol drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 129
evidence_level: L5
indication_count: 52
---

# Certolizumab Pegol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Certolizumab Pegol |
| DrugBank ID | [DB08904](https://go.drugbank.com/drugs/DB08904) |
| Brand Names (EU) | Cimzia |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.84% |

---

## Approved Indication (EMA)

Rheumatoid arthritis Cimzia, in combination with methotrexate (MTX), is indicated for:  the treatment of moderate to severe, active rheumatoid arthritis (RA) in adult patients when the response to disease-modifying antirheumatic drugs (DMARDs) including MTX, has been inadequate. Cimzia can be given as monotherapy in case of intolerance to MTX or when continued treatment with MTX is inappropriate the treatment of severe, active and progressive RA in adults not previously treated with MTX or other

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ankylosing spondylitis | 99.84% | DL |
| 2 | rheumatoid vasculitis | 99.78% | DL |
| 3 | hypermobility of coccyx | 99.75% | DL |
| 4 | inflammatory spondylopathy | 99.73% | DL |
| 5 | Kummell disease | 99.70% | DL |
| 6 | polyarticular juvenile rheumatoid arthritis | 99.69% | DL |
| 7 | spondyloarthropathy, susceptibility to | 99.61% | DL |
| 8 | vertebral disease | 99.26% | DL |
| 9 | rheumatoid arthritis | 97.79% | DL |
| 10 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 96.85% | DL |
| 11 | brachydactyly-syndactyly syndrome | 96.01% | DL |
| 12 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 95.72% | DL |
| 13 | inflammatory bowel disease | 95.70% | DL |
| 14 | tenosynovitis | 95.69% | DL |
| 15 | polyp of vocal cord | 95.15% | DL |
| 16 | polyp of middle ear | 95.13% | DL |
| 17 | epulis | 94.93% | DL |
| 18 | polyp of frontal sinus | 94.93% | DL |
| 19 | polyp of ureter | 94.92% | DL |
| 20 | polyp of external auditory canal | 94.88% | DL |

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
