---
layout: default
title: Simvastatin
description: "simvastatin drug repurposing predictions from TxGNN. Evidence level L1 with 52 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 531
evidence_level: L1
indication_count: 52
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Simvastatin |
| DrugBank ID | [DB00641](https://go.drugbank.com/drugs/DB00641) |
| Brand Names (EU) | Cholib, Simvastatin |
| Evidence Level | L1 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Cholib is indicated as adjunctive therapy to diet and exercise in high cardiovascular risk adult patients with mixed dyslipidaemia to reduce triglycerides and increase HDL C levels when LDL C levels are adequately controlled with the corresponding dose of simvastatin monotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | homozygous familial hypercholesterolemia | 99.98% | DL |
| 2 | obsolete familial combined hyperlipidemia | 99.93% | DL |
| 3 | hyperlipidemia, familial combined, LPL related | 99.89% | DL |
| 4 | hyperlipoproteinemia | 99.79% | DL |
| 5 | obsolete susceptibility to ischemic stroke | 99.70% | DL |
| 6 | familial hypercholesterolemia | 99.63% | DL |
| 7 | brain stem infarction | 99.41% | DL |
| 8 | cholesterol-ester transfer protein deficiency | 99.39% | DL |
| 9 | hypercholesterolemia, autosomal dominant | 99.36% | DL |
| 10 | hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.27% | DL |
| 11 | HIV infectious disease | 99.22% | DL |
| 12 | cerebral infarction | 99.19% | DL |
| 13 | hypoalphalipoproteinemia | 99.14% | DL |
| 14 | ABri amyloidosis | 99.13% | DL |
| 15 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.10% | DL |
| 16 | fibroma of prostate | 98.91% | DL |
| 17 | feline acquired immunodeficiency syndrome | 98.79% | DL |
| 18 | simian immunodeficiency virus infection | 98.79% | DL |
| 19 | cerebral artery occlusion | 98.74% | DL |
| 20 | benign reproductive system neoplasm | 98.74% | DL |

*Showing top 20 of 52 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| homozygous familial hypercholesterolemia | L1 | 4 | 20 | 3 Phase 3 trial(s), 1 RCT(s) |

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
