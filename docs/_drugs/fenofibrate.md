---
layout: default
title: Fenofibrate
description: "Fenofibrate drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 240
evidence_level: L5
indication_count: 51
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fenofibrate |
| DrugBank ID | [DB01039](https://go.drugbank.com/drugs/DB01039) |
| Brand Names (EU) | Fenofibrate, Pravafenix |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.91% |

---

## Approved Indication (EMA)

Pravafenix is indicated as an adjunct to diet and other non-pharmacological treatment (e.g. exercise, weight reduction) for the treatment of mixed hyperlipidaemia in adult patients at high cardiovascular risk to reduce triglycerides and increase HDL C when LDL C levels are adequately controlled while on a treatment with pravastatin 40 mg monotherapy or on another moderate-intensity statin regimen.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | homozygous familial hypercholesterolemia | 99.91% | DL |
| 2 | obsolete familial combined hyperlipidemia | 99.81% | DL |
| 3 | hyperlipoproteinemia | 99.65% | DL |
| 4 | familial hypercholesterolemia | 99.62% | DL |
| 5 | cholesterol-ester transfer protein deficiency | 99.61% | DL |
| 6 | hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.52% | DL |
| 7 | hyperlipidemia | 99.48% | DL |
| 8 | hyperlipidemia due to hepatic triglyceride lipase deficiency | 99.42% | DL |
| 9 | familial hyperlipidemia | 99.40% | DL |
| 10 | hyperlipidemia, familial combined, LPL related | 99.39% | DL |
| 11 | hypoalphalipoproteinemia | 99.38% | DL |
| 12 | hypercholesterolemia, autosomal dominant | 99.05% | DL |
| 13 | hypolipoproteinemia (disease) | 98.69% | DL |
| 14 | hyperalphalipoproteinemia | 97.57% | DL |
| 15 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 97.00% | DL |
| 16 | HIV infectious disease | 96.96% | DL |
| 17 | sitosterolemia | 96.92% | DL |
| 18 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 96.84% | DL |
| 19 | obsolete susceptibility to ischemic stroke | 96.68% | DL |
| 20 | brain small vessel disease 1 with or without ocular anomalies | 96.65% | DL |

*Showing top 20 of 51 predictions.*

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
