---
layout: default
title: Setmelanotide
description: "Setmelanotide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 525
evidence_level: L5
indication_count: 50
---

# Setmelanotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Setmelanotide |
| DrugBank ID | [DB11700](https://go.drugbank.com/drugs/DB11700) |
| Brand Names (EU) | Imcivree |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 92.25% |

---

## Approved Indication (EMA)

IMCIVREE is indicated for the treatment of obesity and the control of hunger associated with genetically confirmed Bardet Biedl syndrome (BBS), loss-of-function biallelic pro-opiomelanocortin (POMC), including PCSK1, deficiency or biallelic leptin receptor (LEPR) deficiency in adults and children 2 years of age and above.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 92.25% | DL |
| 2 | migraine with brainstem aura | 91.68% | DL |
| 3 | non-syndromic esophageal malformation | 89.60% | DL |
| 4 | esophageal disease | 88.38% | DL |
| 5 | amenorrhea (disease) | 86.01% | DL |
| 6 | cauda equina syndrome | 83.00% | DL |
| 7 | obsolete neurogenic bladder (disease) | 82.21% | DL |
| 8 | esophageal ulcer | 81.44% | DL |
| 9 | Ambras type hypertrichosis universalis congenita | 81.23% | DL |
| 10 | pituitary dwarfism | 81.07% | DL |
| 11 | migraine with or without aura, susceptibility to | 80.37% | DL |
| 12 | atrophoderma vermiculata | 79.98% | DL |
| 13 | malformation syndrome with odontal and/or periodontal component | 78.91% | DL |
| 14 | syndrome with a Dandy-Walker malformation as major feature | 78.38% | DL |
| 15 | isolated genetic hair shaft abnormality | 78.00% | DL |
| 16 | erectile dysfunction (disease) | 77.93% | DL |
| 17 | hypertrichosis (disease) | 77.89% | DL |
| 18 | ulerythema ophryogenesis | 76.67% | DL |
| 19 | acne (disease) | 74.14% | DL |
| 20 | adrenal gland hyperfunction | 72.82% | DL |

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
