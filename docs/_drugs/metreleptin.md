---
layout: default
title: Metreleptin
description: "Metreleptin drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 377
evidence_level: L5
indication_count: 53
---

# Metreleptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Metreleptin |
| DrugBank ID | [DB09046](https://go.drugbank.com/drugs/DB09046) |
| Brand Names (EU) | Myalepta |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Myalepta is indicated as an adjunct to diet as a replacement therapy to treat the complications of leptin deficiency in lipodystrophy (LD) patients:  with confirmed congenital generalised LD (Berardinelli-Seip syndrome) or acquired generalised LD (Lawrence syndrome) in adults and children 2 years of age and above with confirmed familial partial LD or acquired partial LD (Barraquer-Simons syndrome), in adults and children 12 years of age and above for whom standard treatments have failed to achie

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | familial generalized lentiginosis | 99.71% | DL |
| 2 | gastrocutaneous syndrome | 99.70% | DL |
| 3 | Moynahan syndrome | 99.67% | DL |
| 4 | rhabdoid tumor | 99.62% | DL |
| 5 | osteopathia striata-pigmentary dermopathy-white forelock syndrome | 99.62% | DL |
| 6 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 99.61% | DL |
| 7 | acromelanosis | 99.61% | DL |
| 8 | leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome | 99.58% | DL |
| 9 | benign neoplasm of adrenal gland | 99.52% | DL |
| 10 | peripheral nerve schwannoma | 99.50% | DL |
| 11 | schwannoma of twelfth cranial nerve | 99.48% | DL |
| 12 | sympathetic neurilemmoma | 99.46% | DL |
| 13 | trigeminal schwannoma | 99.45% | DL |
| 14 | microcystic/reticular schwannoma | 99.45% | DL |
| 15 | glaucoma | 99.13% | DL |
| 16 | lipoatrophic diabetes | 99.06% | DL |
| 17 | Gaucher disease | 99.04% | DL |
| 18 | proximal myopathy with extrapyramidal signs | 99.04% | DL |
| 19 | autosomal ichthyosis syndrome with fatal disease course | 98.97% | DL |
| 20 | pseudo-von Willebrand disease | 98.96% | DL |

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
