---
layout: default
title: Elacestrant
description: "Elacestrant drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 196
evidence_level: L5
indication_count: 50
---

# Elacestrant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Elacestrant |
| DrugBank ID | [DB06374](https://go.drugbank.com/drugs/DB06374) |
| Brand Names (EU) | Orserdu |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 92.50% |

---

## Approved Indication (EMA)

Orserdu monotherapy is indicated for the treatment of postmenopausal women, and men, with estrogen receptor (ER) positive, HER2-negative, locally advanced or metastatic breast cancer with an activating ESR1 mutation who have disease progression following at least one line of endocrine therapy including a CDK 4/6 inhibitor.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | amenorrhea (disease) | 92.50% | DL |
| 2 | bone Paget disease | 86.81% | DL |
| 3 | multiple endocrine neoplasia | 85.85% | DL |
| 4 | primary cutaneous T-cell lymphoma | 84.71% | DL |
| 5 | seborrheic dermatitis | 83.32% | DL |
| 6 | familial adrenal hypoplasia with absent pituitary luteinizing hormone | 82.91% | DL |
| 7 | candidiasis | 82.04% | DL |
| 8 | Leydig cell hypoplasia due to LH resistance | 81.79% | DL |
| 9 | hypogonadotropic hypogonadism with or without anosmia | 81.67% | DL |
| 10 | 46,XY disorder of sex development due to impaired androgen production | 81.65% | DL |
| 11 | seborrheic keratosis | 81.53% | DL |
| 12 | adrenocortical insufficiency | 81.34% | DL |
| 13 | PAGOD syndrome | 81.28% | DL |
| 14 | vulvar inverted follicular keratosis | 80.71% | DL |
| 15 | 46,XY disorder of sex development | 80.60% | DL |
| 16 | renin-angiotensin-aldosterone system-blocker-induced angioedema | 80.31% | DL |
| 17 | dermoid cyst of ovary | 78.75% | DL |
| 18 | spinal cord dermoid cyst | 78.63% | DL |
| 19 | cystic teratoma | 78.60% | DL |
| 20 | disease of orbital part of eye adnexa | 78.52% | DL |

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
