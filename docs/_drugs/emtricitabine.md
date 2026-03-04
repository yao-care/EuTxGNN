---
layout: default
title: Emtricitabine
description: "emtricitabine drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 206
evidence_level: L1
indication_count: 50
---

# Emtricitabine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Emtricitabine |
| DrugBank ID | [DB00879](https://go.drugbank.com/drugs/DB00879) |
| Brand Names (EU) | Emtriva |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Treatment of adults and adolescents (aged 12 years and older with body weight at least 35 kg) infected with human immunodeficiency virus 1 (HIV 1) without known mutations associated with resistance to the non nucleoside reverse transcriptase inhibitor (NNRTI) class, tenofovir or emtricitabine and with a viral load ? 100,000 HIV 1 RNA copies/mL.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.96% | DL |
| 2 | simian immunodeficiency virus infection | 99.92% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.92% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.92% | DL |
| 5 | obsolete familial combined hyperlipidemia | 98.21% | DL |
| 6 | AIDS | 97.11% | DL |
| 7 | AIDS related complex | 93.46% | DL |
| 8 | congenital human immunodeficiency virus | 93.46% | DL |
| 9 | chronic hepatitis C virus infection | 85.87% | DL |
| 10 | fibroma of prostate | 81.41% | DL |
| 11 | Brenner tumor | 80.54% | DL |
| 12 | benign reproductive system neoplasm | 80.20% | DL |
| 13 | benign prostate phyllodes tumor | 78.49% | DL |
| 14 | homozygous familial hypercholesterolemia | 76.72% | DL |
| 15 | hepatitis B virus infection | 76.46% | DL |
| 16 | breast fibrocystic disease | 75.45% | DL |
| 17 | male reproductive organ cancer | 74.99% | DL |
| 18 | apocrine adenosis of breast | 74.15% | DL |
| 19 | blunt duct adenosis of breast | 74.15% | DL |
| 20 | hypercholesterolemia, autosomal dominant | 71.53% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 5 Phase 3 trial(s), 4 Phase 2 trial(s) |

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
