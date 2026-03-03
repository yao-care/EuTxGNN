---
layout: default
title: Zoledronic Acid Monohydrate
description: "Zoledronic Acid Monohydrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 650
evidence_level: L5
indication_count: 50
---

# Zoledronic Acid Monohydrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Zoledronic Acid Monohydrate |
| DrugBank ID | [DB00399](https://go.drugbank.com/drugs/DB00399) |
| Brand Names (EU) | Zoledronic acid medac |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.56% |

---

## Approved Indication (EMA)

Prevention of skeletal related events (pathological fractures, spinal compression, radiation or surgery to bone, or tumour-induced hypercalcaemia) in adult patients with advanced malignancies involving bone. Treatment of adult patients with tumour-induced hypercalcaemia (TIH).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bone Paget disease | 99.56% | DL |
| 2 | HIV infectious disease | 93.95% | DL |
| 3 | obsolete familial combined hyperlipidemia | 93.51% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 93.08% | DL |
| 5 | biotin metabolic disease | 92.88% | DL |
| 6 | feline acquired immunodeficiency syndrome | 91.04% | DL |
| 7 | simian immunodeficiency virus infection | 91.04% | DL |
| 8 | vitamin deficiency disorder | 90.31% | DL |
| 9 | postmenopausal osteoporosis | 90.13% | DL |
| 10 | Worth syndrome | 89.89% | DL |
| 11 | succinyl-CoA:3-ketoacid CoA transferase deficiency | 89.84% | DL |
| 12 | autosomal dominant neovascular inflammatory vitreoretinopathy | 89.35% | DL |
| 13 | hypoglycemia | 89.23% | DL |
| 14 | pregnancy associated osteoporosis | 88.17% | DL |
| 15 | juvenile Paget disease | 87.66% | DL |
| 16 | cholelithiasis | 85.58% | DL |
| 17 | osteomesopyknosis | 83.58% | DL |
| 18 | Paget disease of bone | 83.35% | DL |
| 19 | palmar fibromatosis | 79.75% | DL |
| 20 | homozygous familial hypercholesterolemia | 79.49% | DL |

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
