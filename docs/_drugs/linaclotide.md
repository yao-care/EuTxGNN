---
layout: default
title: Linaclotide
description: "Linaclotide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 344
evidence_level: L5
indication_count: 50
---

# Linaclotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Linaclotide |
| DrugBank ID | [DB08890](https://go.drugbank.com/drugs/DB08890) |
| Brand Names (EU) | Constella |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Constella is indicated for the symptomatic treatment of moderate to severe irritable-bowel syndrome with constipation (IBS-C) in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | cauda equina syndrome | 99.96% | DL |
| 2 | irritable bowel syndrome | 99.91% | DL |
| 3 | obsolete neurogenic bladder (disease) | 99.89% | DL |
| 4 | insomnia (disease) | 99.51% | DL |
| 5 | neurocirculatory asthenia | 99.23% | DL |
| 6 | autonomic nervous system disease | 98.85% | DL |
| 7 | familial mitral valve prolapse | 97.84% | DL |
| 8 | mitral valve prolapse (disease) | 97.45% | DL |
| 9 | MVP1 | 96.90% | DL |
| 10 | gastroduodenitis | 96.51% | DL |
| 11 | large intestine disease | 95.14% | DL |
| 12 | rhinitis | 94.67% | DL |
| 13 | small intestine disease | 94.47% | DL |
| 14 | peptic ulcer disease | 94.04% | DL |
| 15 | dysautonomia | 94.00% | DL |
| 16 | gastroenteritis | 92.87% | DL |
| 17 | active vestibular Meniere disease | 89.83% | DL |
| 18 | active cochlear Meniere disease | 89.83% | DL |
| 19 | active cochleovestibular Meniere disease | 89.83% | DL |
| 20 | vertigo, benign recurrent, 2 | 89.46% | DL |

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
