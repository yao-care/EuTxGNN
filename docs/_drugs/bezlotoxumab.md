---
layout: default
title: Bezlotoxumab
description: "Bezlotoxumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 80
evidence_level: L5
indication_count: 50
---

# Bezlotoxumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bezlotoxumab |
| DrugBank ID | [DB13140](https://go.drugbank.com/drugs/DB13140) |
| Brand Names (EU) | Zinplava |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Zinplava is indicated for the prevention of recurrence of Clostridium difficile infection (CDI) in adults at high risk for recurrence of CDI.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute female pelvic peritonitis | 99.89% | DL |
| 2 | embryonic cyst of fallopian tube | 99.89% | DL |
| 3 | tubal pregnancy | 99.89% | DL |
| 4 | salpingitis isthmica nodosa | 99.88% | DL |
| 5 | disease of uterine broad ligament | 99.87% | DL |
| 6 | lumbar spinal stenosis | 99.87% | DL |
| 7 | celiac trunk compression syndrome | 99.87% | DL |
| 8 | abdominal cystic lymphangioma | 99.87% | DL |
| 9 | abdominal ectopic pregnancy | 99.87% | DL |
| 10 | pelvic varices | 99.87% | DL |
| 11 | lymph node palisaded myofibroblastoma | 99.87% | DL |
| 12 | disease of retroperitoneum | 99.87% | DL |
| 13 | sacrum chordoma | 99.87% | DL |
| 14 | disease of peritoneum | 99.87% | DL |
| 15 | urethral disease | 99.87% | DL |
| 16 | pudendal neuralgia | 99.83% | DL |
| 17 | bronchial adenomas/carcinoids childhood | 99.80% | DL |
| 18 | non-seminomatous lesion | 99.80% | DL |
| 19 | ductal or ductular proliferation | 99.80% | DL |
| 20 | chondroid hamartoma | 99.80% | DL |

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
