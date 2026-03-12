---
layout: default
title: Fluciclovine (18F)
description: "Fluciclovine (18F) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 250
evidence_level: L5
indication_count: 50
---

# Fluciclovine (18F)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fluciclovine (18F) |
| DrugBank ID | [DB13146](https://go.drugbank.com/drugs/DB13146) |
| Brand Names (EU) | Axumin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.86% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only. Axumin is indicated for Positron Emission Tomography (PET) imaging to detect recurrence of prostate cancer in adult men with a suspected recurrence based on elevated blood prostate specific antigen (PSA) levels after primary curative treatment.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | trichotillomania | 97.86% | DL |
| 2 | Tourette syndrome | 97.70% | DL |
| 3 | migraine disorder | 97.25% | DL |
| 4 | migraine with brainstem aura | 96.81% | DL |
| 5 | erectile dysfunction (disease) | 96.31% | DL |
| 6 | postural orthostatic tachycardia syndrome | 96.09% | DL |
| 7 | multifocal atrial tachycardia (disease) | 95.64% | DL |
| 8 | His bundle tachycardia | 95.52% | DL |
| 9 | idiopathic neonatal atrial flutter | 95.19% | DL |
| 10 | hyperthyroidism | 94.55% | DL |
| 11 | multiple endocrine neoplasia | 94.17% | DL |
| 12 | atypical coarctation of aorta | 93.94% | DL |
| 13 | cauda equina syndrome | 93.65% | DL |
| 14 | hyperthyroxinemia | 93.59% | DL |
| 15 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 93.51% | DL |
| 16 | anaphylaxis | 93.25% | DL |
| 17 | atrophoderma vermiculata | 93.17% | DL |
| 18 | thyroid gland disease | 93.10% | DL |
| 19 | open-angle glaucoma | 92.98% | DL |
| 20 | ulerythema ophryogenesis | 92.75% | DL |

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
