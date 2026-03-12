---
layout: default
title: Dronedarone
description: "dronedarone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 183
evidence_level: L5
indication_count: 50
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dronedarone |
| DrugBank ID | [DB04855](https://go.drugbank.com/drugs/DB04855) |
| Brand Names (EU) | Multaq |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Multaq is indicated for the maintenance of sinus rhythm after successful cardioversion in adult clinically stable patients with paroxysmal or persistent atrial fibrillation (AF). Due to its safety profile, Multaq should only be prescribed after alternative treatment options have been considered. Multaq should not be given to patients with left ventricular systolic dysfunction or to patients with current or previous episodes of heart failure.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | stroke disorder | 99.97% | DL |
| 2 | obsolete susceptibility to ischemic stroke | 99.96% | DL |
| 3 | ABri amyloidosis | 99.92% | DL |
| 4 | cerebrovascular disorder | 99.71% | DL |
| 5 | brain stem infarction | 99.71% | DL |
| 6 | atrial fibrillation (disease) | 99.70% | DL |
| 7 | sick sinus syndrome 2, autosomal dominant | 99.63% | DL |
| 8 | duodenal obstruction | 99.56% | DL |
| 9 | cerebral artery occlusion | 99.44% | DL |
| 10 | sarcoglycanopathy | 99.43% | DL |
| 11 | Wildervanck syndrome | 99.37% | DL |
| 12 | manic bipolar affective disorder | 99.27% | DL |
| 13 | duodenal ulcer (disease) | 99.16% | DL |
| 14 | duodenogastric reflux | 99.16% | DL |
| 15 | spinal cord ischemia | 99.13% | DL |
| 16 | macrocephaly, dysmorphic facies, and psychomotor retardation | 98.99% | DL |
| 17 | nephrogenic syndrome of inappropriate antidiuresis | 98.97% | DL |
| 18 | transient ischemic attack (disease) | 98.61% | DL |
| 19 | Prinzmetal angina | 98.55% | DL |
| 20 | MRI defined brain infarct | 98.36% | DL |

*Showing top 20 of 50 predictions.*

---


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
