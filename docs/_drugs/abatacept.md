---
layout: default
title: Abatacept
description: "Abatacept drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 12
evidence_level: L5
indication_count: 50
---

# Abatacept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Abatacept |
| DrugBank ID | [DB01281](https://go.drugbank.com/drugs/DB01281) |
| Brand Names (EU) | Orencia |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.91% |

---

## Approved Indication (EMA)

Rheumatoid arthritisOrencia, in combination with methotrexate, is indicated for:  the treatment of moderate to severe active rheumatoid arthritis (RA) in adult patients who responded inadequately to previous therapy with one or more disease-modifying anti-rheumatic drugs (DMARDs) including methotrexate (MTX) or a tumour necrosis factor (TNF)-alpha inhibitor. the treatment of highly active and progressive disease in adult patients with rheumatoid arthritis not previously treated with methotrexate

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid vasculitis | 99.91% | DL |
| 2 | ankylosing spondylitis | 99.91% | DL |
| 3 | hypermobility of coccyx | 99.87% | DL |
| 4 | inflammatory spondylopathy | 99.84% | DL |
| 5 | Kummell disease | 99.84% | DL |
| 6 | polyarticular juvenile rheumatoid arthritis | 99.83% | DL |
| 7 | rheumatoid arthritis | 99.77% | DL |
| 8 | vertebral disease | 99.68% | DL |
| 9 | spondyloarthropathy, susceptibility to | 99.65% | DL |
| 10 | brachydactyly-syndactyly syndrome | 99.50% | DL |
| 11 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.48% | DL |
| 12 | WHIM syndrome | 99.34% | DL |
| 13 | juvenile idiopathic arthritis | 99.31% | DL |
| 14 | rheumatoid nodulosis | 99.08% | DL |
| 15 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 99.07% | DL |
| 16 | juvenile chronic polyarthritis | 99.02% | DL |
| 17 | juvenile arthritis due to defect in LACC1 | 98.93% | DL |
| 18 | spondyloarthropathy | 98.18% | DL |
| 19 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 97.07% | DL |
| 20 | leukoplakia | 97.00% | DL |

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
