---
layout: default
title: Ospemifene
description: "Ospemifene drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 428
evidence_level: L5
indication_count: 51
---

# Ospemifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ospemifene |
| DrugBank ID | [DB04938](https://go.drugbank.com/drugs/DB04938) |
| Brand Names (EU) | Senshio |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.98% |

---

## Approved Indication (EMA)

Senshio is indicated for the treatment of moderate to severe symptomatic vulvar and vaginal atrophy (VVA) in post-menopausal women.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | leprosy | 98.98% | DL |
| 2 | pulmonary hypertension | 98.95% | DL |
| 3 | kyphoscoliotic heart disease | 98.78% | DL |
| 4 | migraine with or without aura, susceptibility to | 98.69% | DL |
| 5 | migraine disorder | 98.53% | DL |
| 6 | migraine with brainstem aura | 98.27% | DL |
| 7 | nephrogenic syndrome of inappropriate antidiuresis | 97.99% | DL |
| 8 | rheumatoid arthritis | 97.43% | DL |
| 9 | atrophoderma vermiculata | 97.21% | DL |
| 10 | ulerythema ophryogenesis | 96.78% | DL |
| 11 | brachydactyly-syndactyly syndrome | 96.56% | DL |
| 12 | coronary artery disease | 96.46% | DL |
| 13 | pulmonary hypertension, primary, autosomal recessive | 96.36% | DL |
| 14 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.21% | DL |
| 15 | hypertrichosis (disease) | 96.09% | DL |
| 16 | persistent Mullerian duct syndrome | 95.80% | DL |
| 17 | anomalous left coronary artery from the pulmonary artery | 95.78% | DL |
| 18 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 95.60% | DL |
| 19 | Ambras type hypertrichosis universalis congenita | 95.52% | DL |
| 20 | malformation syndrome with odontal and/or periodontal component | 95.49% | DL |

*Showing top 20 of 51 predictions.*

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
