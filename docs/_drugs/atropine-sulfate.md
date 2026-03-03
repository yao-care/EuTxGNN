---
layout: default
title: Atropine Sulfate
description: "Atropine Sulfate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 56
evidence_level: L5
indication_count: 50
---

# Atropine Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Atropine Sulfate |
| DrugBank ID | [DB00572](https://go.drugbank.com/drugs/DB00572) |
| Brand Names (EU) | Ryjunea |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.56% |

---

## Approved Indication (EMA)

Ryjunea is indicated for slowing the progression of myopia in paediatric patients. Treatment may be initiated in children aged 3-14 years with a progression rate of 0.5 D or more per year and a severity of -0.5 D to -6.0 D.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.56% | DL |
| 2 | migraine with brainstem aura | 99.42% | DL |
| 3 | migraine with or without aura, susceptibility to | 98.15% | DL |
| 4 | atrophoderma vermiculata | 98.15% | DL |
| 5 | open-angle glaucoma | 98.03% | DL |
| 6 | primary hereditary glaucoma | 97.78% | DL |
| 7 | ulerythema ophryogenesis | 97.76% | DL |
| 8 | headache disorder | 97.24% | DL |
| 9 | trigeminal autonomic cephalalgia | 96.46% | DL |
| 10 | nephrogenic syndrome of inappropriate antidiuresis | 96.34% | DL |
| 11 | diffuse alopecia areata | 95.28% | DL |
| 12 | hypertrichosis (disease) | 95.27% | DL |
| 13 | congenital hypotrichosis milia | 95.23% | DL |
| 14 | alopecia | 95.14% | DL |
| 15 | Ambras type hypertrichosis universalis congenita | 95.13% | DL |
| 16 | common cold | 95.10% | DL |
| 17 | hypotrichosis simplex of the scalp | 94.99% | DL |
| 18 | sciatic neuropathy | 94.73% | DL |
| 19 | malformation syndrome with odontal and/or periodontal component | 94.63% | DL |
| 20 | syndrome with a Dandy-Walker malformation as major feature | 94.56% | DL |

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
