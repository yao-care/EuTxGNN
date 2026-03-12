---
layout: default
title: Lutropin Alfa
description: "Lutropin Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 359
evidence_level: L5
indication_count: 50
---

# Lutropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lutropin Alfa |
| DrugBank ID | [DB00044](https://go.drugbank.com/drugs/DB00044) |
| Brand Names (EU) | Luveris |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.04% |

---

## Approved Indication (EMA)

Luveris in association with a follicle-stimulating-hormone (FSH) preparation is recommended for the stimulation of follicular development in women with severe luteinising-hormone (LH) and FSH deficiency. In clinical trials, these patients were defined by an endogenous serum LH level &lt;1.2 IU/l.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | postural orthostatic tachycardia syndrome | 97.04% | DL |
| 2 | peptic esophagitis | 97.02% | DL |
| 3 | trichotillomania | 96.31% | DL |
| 4 | Raynaud disease | 95.65% | DL |
| 5 | duodenal ulcer (disease) | 95.58% | DL |
| 6 | Tourette syndrome | 95.18% | DL |
| 7 | esophageal disease | 94.93% | DL |
| 8 | sinoatrial block | 94.91% | DL |
| 9 | multiple endocrine neoplasia | 94.87% | DL |
| 10 | duodenogastric reflux | 94.58% | DL |
| 11 | duodenal obstruction | 94.44% | DL |
| 12 | sinoatrial node disease | 94.20% | DL |
| 13 | non-syndromic esophageal malformation | 93.46% | DL |
| 14 | amenorrhea (disease) | 93.07% | DL |
| 15 | active peptic ulcer disease | 92.75% | DL |
| 16 | esophageal ulcer | 92.70% | DL |
| 17 | progressive familial heart block | 92.58% | DL |
| 18 | adrenal gland hyperfunction | 92.42% | DL |
| 19 | gastrojejunal ulcer | 92.42% | DL |
| 20 | peptic ulcer perforation | 92.42% | DL |

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
