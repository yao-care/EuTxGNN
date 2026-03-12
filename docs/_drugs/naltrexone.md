---
layout: default
title: Naltrexone
description: "Naltrexone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 394
evidence_level: L5
indication_count: 50
---

# Naltrexone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Naltrexone |
| DrugBank ID | [DB00704](https://go.drugbank.com/drugs/DB00704) |
| Brand Names (EU) | Naltrexone |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.89% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | obesity disorder | 98.89% | DL |
| 2 | hypervitaminosis | 98.66% | DL |
| 3 | proximal 16p11.2 microdeletion syndrome | 98.13% | DL |
| 4 | obsolete hypertelorism (disease) | 95.64% | DL |
| 5 | frontorhiny | 93.19% | DL |
| 6 | restless legs syndrome | 92.20% | DL |
| 7 | monogenic obesity | 89.74% | DL |
| 8 | progressive encephalopathy with leukodystrophy due to DECR deficiency | 72.94% | DL |
| 9 | substance abuse/dependence | 70.32% | DL |
| 10 | mitral valve prolapse, myxomatous | 62.59% | DL |
| 11 | attention deficit hyperactivity disorder, inattentive type | 62.20% | DL |
| 12 | hypospadias 3, autosomal | 61.77% | DL |
| 13 | sella turcica, bridged | 61.77% | DL |
| 14 | triphalangeal thumb, Nonopposable | 61.77% | DL |
| 15 | musk, inability to smell | 61.47% | DL |
| 16 | polyhydramnios, chronic idiopathic | 61.47% | DL |
| 17 | cornea plana 1, autosomal dominant | 61.47% | DL |
| 18 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 60.85% | DL |
| 19 | specific developmental disorder | 60.24% | DL |
| 20 | cholangiocarcinoma, susceptibility to | 60.10% | DL |

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
