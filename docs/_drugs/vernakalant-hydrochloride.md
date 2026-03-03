---
layout: default
title: Vernakalant Hydrochloride
description: "Vernakalant Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 629
evidence_level: L5
indication_count: 50
---

# Vernakalant Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vernakalant Hydrochloride |
| DrugBank ID | [DB06217](https://go.drugbank.com/drugs/DB06217) |
| Brand Names (EU) | Brinavess |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.83% |

---

## Approved Indication (EMA)

Rapid conversion of recent onset atrial fibrillation to sinus rhythm in adults:  for non-surgery patients: atrial fibrillation&nbsp;&lt;/= 7 days duration; for post-cardiac surgery patients: atrial fibrillation&nbsp;&lt;/= 3 days duration.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | stroke disorder | 99.83% | DL |
| 2 | atrial fibrillation (disease) | 99.61% | DL |
| 3 | sick sinus syndrome 2, autosomal dominant | 99.55% | DL |
| 4 | obsolete susceptibility to ischemic stroke | 99.43% | DL |
| 5 | sarcoglycanopathy | 99.32% | DL |
| 6 | Wildervanck syndrome | 99.29% | DL |
| 7 | ABri amyloidosis | 99.26% | DL |
| 8 | transient ischemic attack (disease) | 98.99% | DL |
| 9 | macrocephaly, dysmorphic facies, and psychomotor retardation | 98.91% | DL |
| 10 | obesity disorder | 98.81% | DL |
| 11 | hypervitaminosis | 98.76% | DL |
| 12 | cerebrovascular disorder | 98.75% | DL |
| 13 | spinal cord ischemia | 98.54% | DL |
| 14 | manic bipolar affective disorder | 98.48% | DL |
| 15 | proximal 16p11.2 microdeletion syndrome | 97.73% | DL |
| 16 | duodenal obstruction | 97.40% | DL |
| 17 | brain stem infarction | 97.08% | DL |
| 18 | obsolete hypertelorism (disease) | 96.93% | DL |
| 19 | cerebral artery occlusion | 95.99% | DL |
| 20 | frontorhiny | 95.88% | DL |

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
