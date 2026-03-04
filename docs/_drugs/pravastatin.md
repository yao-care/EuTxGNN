---
layout: default
title: Pravastatin
description: "pravastatin drug repurposing predictions from TxGNN. Evidence level L2 with 52 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 469
evidence_level: L2
indication_count: 52
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pravastatin |
| DrugBank ID | [DB00175](https://go.drugbank.com/drugs/DB00175) |
| Brand Names (EU) | Pravafenix, Pravastatin |
| Evidence Level | L2 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.95% |

---

## Approved Indication (EMA)

Pravafenix is indicated as an adjunct to diet and other non-pharmacological treatment (e.g. exercise, weight reduction) for the treatment of mixed hyperlipidaemia in adult patients at high cardiovascular risk to reduce triglycerides and increase HDL C when LDL C levels are adequately controlled while on a treatment with pravastatin 40 mg monotherapy or on another moderate-intensity statin regimen.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | homozygous familial hypercholesterolemia | 99.95% | DL |
| 2 | obsolete familial combined hyperlipidemia | 99.82% | DL |
| 3 | HIV infectious disease | 99.74% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.62% | DL |
| 5 | feline acquired immunodeficiency syndrome | 99.55% | DL |
| 6 | simian immunodeficiency virus infection | 99.55% | DL |
| 7 | hyperlipoproteinemia | 99.43% | DL |
| 8 | familial hypercholesterolemia | 99.34% | DL |
| 9 | hypoalphalipoproteinemia | 99.21% | DL |
| 10 | hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.07% | DL |
| 11 | cholesterol-ester transfer protein deficiency | 99.04% | DL |
| 12 | hyperlipidemia, familial combined, LPL related | 98.87% | DL |
| 13 | obsolete susceptibility to ischemic stroke | 98.76% | DL |
| 14 | hypercholesterolemia, autosomal dominant | 98.69% | DL |
| 15 | familial hyperlipidemia | 98.54% | DL |
| 16 | brain stem infarction | 98.42% | DL |
| 17 | hyperlipidemia due to hepatic triglyceride lipase deficiency | 98.17% | DL |
| 18 | hypolipoproteinemia (disease) | 98.12% | DL |
| 19 | hyperlipidemia | 98.05% | DL |
| 20 | cerebral infarction | 97.92% | DL |

*Showing top 20 of 52 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| homozygous familial hypercholesterolemia | L2 | 1 | 5 | 1 Phase 3 trial(s) |

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
