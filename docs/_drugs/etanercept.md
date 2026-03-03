---
layout: default
title: Etanercept
description: "Etanercept drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 229
evidence_level: L5
indication_count: 50
---

# Etanercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Etanercept |
| DrugBank ID | [DB00005](https://go.drugbank.com/drugs/DB00005) |
| Brand Names (EU) | Nepexto |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.74% |

---

## Approved Indication (EMA)

Rheumatoid arthritis Nepexto in combination with methotrexate is indicated for the treatment of moderate to severe active rheumatoid arthritis in adults when the response to disease-modifying antirheumatic drugs, including methotrexate (unless contraindicated), has been inadequate. Nepexto can be given as monotherapy in case of intolerance to methotrexate or when continued treatment with methotrexate is inappropriate.&nbsp; Nepexto is also indicated in the treatment of severe, active and progres

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ankylosing spondylitis | 99.74% | DL |
| 2 | rheumatoid vasculitis | 99.71% | DL |
| 3 | hypermobility of coccyx | 99.63% | DL |
| 4 | inflammatory spondylopathy | 99.57% | DL |
| 5 | spondyloarthropathy, susceptibility to | 99.55% | DL |
| 6 | Kummell disease | 99.55% | DL |
| 7 | polyarticular juvenile rheumatoid arthritis | 99.50% | DL |
| 8 | vertebral disease | 99.16% | DL |
| 9 | juvenile idiopathic arthritis | 98.65% | DL |
| 10 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 98.26% | DL |
| 11 | rheumatoid arthritis | 98.24% | DL |
| 12 | rheumatoid nodulosis | 98.20% | DL |
| 13 | juvenile chronic polyarthritis | 98.08% | DL |
| 14 | juvenile arthritis due to defect in LACC1 | 97.95% | DL |
| 15 | WHIM syndrome | 97.71% | DL |
| 16 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 97.03% | DL |
| 17 | brachydactyly-syndactyly syndrome | 96.76% | DL |
| 18 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.68% | DL |
| 19 | leukoplakia | 95.47% | DL |
| 20 | spondyloarthropathy | 95.16% | DL |

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
