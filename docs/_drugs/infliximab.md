---
layout: default
title: Infliximab
description: "Infliximab drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 301
evidence_level: L5
indication_count: 53
---

# Infliximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Infliximab |
| DrugBank ID | [DB00065](https://go.drugbank.com/drugs/DB00065) |
| Brand Names (EU) | Flixabi, Zessly |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 93.42% |

---

## Approved Indication (EMA)

Treatment of rheumatoid arthritis, Crohn’s disease, ulcerative colitis, ankylosing spondylitis, psoriatic arthritis and psoriasis.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 93.42% | DL |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 90.22% | DL |
| 3 | brachydactyly-syndactyly syndrome | 89.88% | DL |
| 4 | rheumatoid vasculitis | 85.32% | DL |
| 5 | ankylosing spondylitis | 82.92% | DL |
| 6 | hypermobility of coccyx | 82.49% | DL |
| 7 | anus disease | 81.21% | DL |
| 8 | Kummell disease | 81.15% | DL |
| 9 | inflammatory spondylopathy | 80.92% | DL |
| 10 | polyarticular juvenile rheumatoid arthritis | 80.14% | DL |
| 11 | bronchitis | 77.87% | DL |
| 12 | spondyloarthropathy, susceptibility to | 77.73% | DL |
| 13 | Crohn disease of the esophagus | 77.58% | DL |
| 14 | functional neutrophil defect | 77.53% | DL |
| 15 | granulomatous disease, chronic, autosomal recessive, 5 | 77.20% | DL |
| 16 | granulomatous disease with defect in neutrophil chemotaxis | 76.88% | DL |
| 17 | inflammatory bowel disease | 76.85% | DL |
| 18 | vertebral disease | 75.14% | DL |
| 19 | WHIM syndrome | 73.11% | DL |
| 20 | osteoarthritis susceptibility | 72.62% | DL |

*Showing top 20 of 53 predictions.*

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
