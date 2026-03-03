---
layout: default
title: Adalimumab
description: "Adalimumab drug repurposing predictions from TxGNN. Evidence level L5 with 61 predicted indications."
parent: AI Predictions (L5)
nav_order: 18
evidence_level: L5
indication_count: 61
---

# Adalimumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **61**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Adalimumab |
| DrugBank ID | [DB00051](https://go.drugbank.com/drugs/DB00051) |
| Brand Names (EU) | Amgevita, Amsparity, Hukyndra, Hulio, Humira, Idacio, Yuflyma |
| Evidence Level | L5 |
| Predicted Indications | 61 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Rheumatoid arthritis  Amgevita in combination with methotrexate, is indicated for:  the treatment of moderate to severe, active rheumatoid arthritis in adult patients when the response to disease-modifying anti-rheumatic drugs including methotrexate has been inadequate. the treatment of severe, active and progressive rheumatoid arthritis in adults not previously treated with methotrexate.   Amgevita can be given as monotherapy in case of intolerance to methotrexate or when continued treatment wi

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ankylosing spondylitis | 99.85% | DL |
| 2 | rheumatoid vasculitis | 99.80% | DL |
| 3 | hypermobility of coccyx | 99.77% | DL |
| 4 | inflammatory spondylopathy | 99.77% | DL |
| 5 | Kummell disease | 99.74% | DL |
| 6 | polyarticular juvenile rheumatoid arthritis | 99.72% | DL |
| 7 | spondyloarthropathy, susceptibility to | 99.59% | DL |
| 8 | vertebral disease | 99.18% | DL |
| 9 | polyp of middle ear | 97.94% | DL |
| 10 | polyp of vocal cord | 97.93% | DL |
| 11 | polyp of ureter | 97.86% | DL |
| 12 | polyp of frontal sinus | 97.85% | DL |
| 13 | epulis | 97.84% | DL |
| 14 | polyp of external auditory canal | 97.83% | DL |
| 15 | polyp of vulva | 97.75% | DL |
| 16 | uterine polyp | 97.75% | DL |
| 17 | fibroepithelial polyp | 97.70% | DL |
| 18 | neoplastic polyp | 97.68% | DL |
| 19 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 97.42% | DL |
| 20 | acne (disease) | 96.83% | DL |

*Showing top 20 of 61 predictions.*

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
