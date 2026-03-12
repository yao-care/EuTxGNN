---
layout: default
title: Inclisiran
description: "Inclisiran drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 298
evidence_level: L5
indication_count: 50
---

# Inclisiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Inclisiran |
| DrugBank ID | [DB14901](https://go.drugbank.com/drugs/DB14901) |
| Brand Names (EU) | Leqvio |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Leqvio is indicated in adults with primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia, as an adjunct to diet:  in combination with a statin or statin with other lipid-lowering therapies in patients unable to reach LDL-C goals with the maximum tolerated dose of a statin, or alone or in combination with other lipid-lowering therapies in patients who are statin-intolerant, or for whom a statin is contraindicated.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | potassium deficiency disease | 99.93% | DL |
| 2 | esophageal disease | 99.87% | DL |
| 3 | atypical coarctation of aorta | 99.86% | DL |
| 4 | migraine disorder | 99.83% | DL |
| 5 | non-syndromic esophageal malformation | 99.83% | DL |
| 6 | migraine with brainstem aura | 99.78% | DL |
| 7 | migraine with or without aura, susceptibility to | 99.78% | DL |
| 8 | aortic malformation | 99.76% | DL |
| 9 | esophageal ulcer | 99.73% | DL |
| 10 | Raynaud disease | 99.73% | DL |
| 11 | peptic esophagitis | 99.68% | DL |
| 12 | cauda equina syndrome | 99.67% | DL |
| 13 | gastrin secretion abnormality | 99.65% | DL |
| 14 | ulerythema ophryogenesis | 99.64% | DL |
| 15 | irritable bowel syndrome | 99.59% | DL |
| 16 | atrophoderma vermiculata | 99.53% | DL |
| 17 | peptic ulcer disease | 99.48% | DL |
| 18 | esophageal diverticulosis | 99.48% | DL |
| 19 | phaeochromocytoma | 99.48% | DL |
| 20 | dyskinesia of esophagus | 99.47% | DL |

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
