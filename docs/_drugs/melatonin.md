---
layout: default
title: Melatonin
description: "Melatonin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 366
evidence_level: L5
indication_count: 50
---

# Melatonin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Melatonin |
| DrugBank ID | [DB01065](https://go.drugbank.com/drugs/DB01065) |
| Brand Names (EU) | Melatonin Neurim |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.80% |

---

## Approved Indication (EMA)

Melatonin Neurim is indicated as monotherapy for the short-term treatment of primary insomnia characterised by poor quality of sleep in patients who are aged 55 or over.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | insomnia (disease) | 99.80% | DL |
| 2 | sleep disorder, initiating and maintaining sleep | 96.11% | DL |
| 3 | migraine with brainstem aura | 87.90% | DL |
| 4 | obesity disorder | 85.77% | DL |
| 5 | restless legs syndrome | 85.65% | DL |
| 6 | migraine disorder | 85.52% | DL |
| 7 | hypervitaminosis | 84.39% | DL |
| 8 | obsolete hypertelorism (disease) | 83.11% | DL |
| 9 | monogenic obesity | 81.24% | DL |
| 10 | frontorhiny | 79.42% | DL |
| 11 | proximal 16p11.2 microdeletion syndrome | 78.45% | DL |
| 12 | acute encephalopathy with biphasic seizures and late reduced diffusion | 78.33% | DL |
| 13 | fibrosis of extraocular muscles, congenital, with synergistic divergence | 69.86% | DL |
| 14 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 69.10% | DL |
| 15 | hyperparathyroidism, primary, caused by water clear cell hyperplasia | 67.85% | DL |
| 16 | retinal aplasia | 66.11% | DL |
| 17 | melanoma, malignant familial intraocular | 64.98% | DL |
| 18 | atrophoderma vermiculata | 64.46% | DL |
| 19 | triphalangeal thumb, Nonopposable | 64.13% | DL |
| 20 | sella turcica, bridged | 64.13% | DL |

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
