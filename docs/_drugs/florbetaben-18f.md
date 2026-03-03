---
layout: default
title: Florbetaben (18F)
description: "Florbetaben (18F) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 248
evidence_level: L5
indication_count: 50
---

# Florbetaben (18F)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Florbetaben (18F) |
| DrugBank ID | [DB09148](https://go.drugbank.com/drugs/DB09148) |
| Brand Names (EU) | Neuraceq |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.41% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only. Neuraceq is a radiopharmaceutical indicated for Positron Emission Tomography (PET) imaging of ? amyloid neuritic plaque density in the brains of adult patients with cognitive impairment who are being evaluated for Alzheimer’s disease (AD) and other causes of cognitive impairment. Neuraceq should be used in conjunction with a clinical evaluation. A negative scan indicates sparse or no plaques, which is not consistent with a diagnosis of AD.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.41% | DL |
| 2 | rheumatoid arthritis | 99.39% | DL |
| 3 | migraine with brainstem aura | 99.36% | DL |
| 4 | migraine with or without aura, susceptibility to | 99.10% | DL |
| 5 | pulmonary hypertension | 98.97% | DL |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.94% | DL |
| 7 | kyphoscoliotic heart disease | 98.82% | DL |
| 8 | headache disorder | 98.75% | DL |
| 9 | trigeminal autonomic cephalalgia | 98.71% | DL |
| 10 | Raynaud disease | 98.68% | DL |
| 11 | brachydactyly-syndactyly syndrome | 98.67% | DL |
| 12 | ulerythema ophryogenesis | 98.54% | DL |
| 13 | atrophoderma vermiculata | 98.51% | DL |
| 14 | intermittent vascular claudication | 98.33% | DL |
| 15 | peripheral vascular disease | 98.29% | DL |
| 16 | intracranial arteriosclerosis | 98.28% | DL |
| 17 | gastroduodenitis | 98.27% | DL |
| 18 | bronchitis | 98.14% | DL |
| 19 | Monckeberg arteriosclerosis | 97.97% | DL |
| 20 | peptic ulcer disease | 97.86% | DL |

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
