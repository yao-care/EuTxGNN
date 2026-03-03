---
layout: default
title: Ezetimibe
description: "Ezetimibe drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 236
evidence_level: L5
indication_count: 50
---

# Ezetimibe
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ezetimibe |
| DrugBank ID | [DB00973](https://go.drugbank.com/drugs/DB00973) |
| Brand Names (EU) | Ezetimibe |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Hypercholesterolaemia and mixed dyslipidaemiaNustendi is indicated in adults with primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia, as an adjunct to diet:• in combination with a statin in patients unable to reach LDL-C goals with the maximum tolerated dose of a statin in addition to ezetimibe&nbsp;• alone in patients who are either statin-intolerant or for whom a statin is contraindicated, and are unable to reach LDL-C goals with ezetimibe alone,• in 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | homozygous familial hypercholesterolemia | 99.86% | DL |
| 2 | obsolete familial combined hyperlipidemia | 99.68% | DL |
| 3 | hyperlipoproteinemia | 99.63% | DL |
| 4 | familial hypercholesterolemia | 99.38% | DL |
| 5 | hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.25% | DL |
| 6 | cholesterol-ester transfer protein deficiency | 99.09% | DL |
| 7 | hyperlipidemia, familial combined, LPL related | 98.83% | DL |
| 8 | HIV infectious disease | 98.80% | DL |
| 9 | hypercholesterolemia, autosomal dominant | 98.76% | DL |
| 10 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.69% | DL |
| 11 | hyperlipidemia due to hepatic triglyceride lipase deficiency | 98.57% | DL |
| 12 | familial hyperlipidemia | 98.44% | DL |
| 13 | feline acquired immunodeficiency syndrome | 98.11% | DL |
| 14 | simian immunodeficiency virus infection | 98.11% | DL |
| 15 | hyperlipidemia | 97.34% | DL |
| 16 | hyperalphalipoproteinemia | 97.17% | DL |
| 17 | sitosterolemia | 96.77% | DL |
| 18 | familial chylomicronemia syndrome | 95.51% | DL |
| 19 | hypertriglyceridemia, familial | 94.94% | DL |
| 20 | hypolipoproteinemia (disease) | 93.96% | DL |

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
