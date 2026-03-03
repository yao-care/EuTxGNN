---
layout: default
title: Inotersen Sodium
description: "Inotersen Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 302
evidence_level: L5
indication_count: 50
---

# Inotersen Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Inotersen Sodium |
| DrugBank ID | [DB14713](https://go.drugbank.com/drugs/DB14713) |
| Brand Names (EU) | Tegsedi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Treatment of stage 1 or Stage 2 polyneuropathy in adult patients with hereditary transthyretin amyloidosis (hATTR).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute intermittent porphyria | 99.92% | DL |
| 2 | appendicitis | 99.91% | DL |
| 3 | IgG4-related pachymeningitis | 99.90% | DL |
| 4 | IgG4-related retroperitoneal fibrosis | 99.88% | DL |
| 5 | non-infectious meningitis | 99.86% | DL |
| 6 | peritonitis | 99.86% | DL |
| 7 | infectious meningitis | 99.85% | DL |
| 8 | eosinophilic angiocentric fibrosis | 99.80% | DL |
| 9 | IgG4-related mesenteritis | 99.80% | DL |
| 10 | IgG4-related aortitis | 99.80% | DL |
| 11 | IgG4-related mediastinitis | 99.80% | DL |
| 12 | chronic meningitis | 99.80% | DL |
| 13 | type I complement component 8 deficiency | 99.80% | DL |
| 14 | rheumatoid arthritis | 99.79% | DL |
| 15 | endocarditis | 99.79% | DL |
| 16 | IgG4-related hepatopathy | 99.79% | DL |
| 17 | porphyria | 99.72% | DL |
| 18 | endocardial fibroelastosis | 99.71% | DL |
| 19 | meningococcal infection | 99.70% | DL |
| 20 | pneumonia | 99.69% | DL |

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
