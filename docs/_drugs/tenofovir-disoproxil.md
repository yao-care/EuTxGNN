---
layout: default
title: Tenofovir Disoproxil
description: "tenofovir disoproxil drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 569
evidence_level: L1
indication_count: 50
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tenofovir Disoproxil |
| DrugBank ID | [DB00300](https://go.drugbank.com/drugs/DB00300) |
| Brand Names (EU) | Tenofovir disoproxil |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

HIV-1 infection Tenofovir disoproxil 245 mg film-coated tablets are indicated in combination with other antiretroviral medicinal products for the treatment of HIV-1 infected adults. In adults, the demonstration of the benefit of tenofovir disoproxil in HIV-1 infection is based on results of one study in treatment-naïve patients, including patients with a high viral load (&gt; 100,000 copies/ml) and studies in which tenofovir disoproxil was added to stable background therapy (mainly tritherapy) i

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.98% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.95% | DL |
| 3 | simian immunodeficiency virus infection | 99.95% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.95% | DL |
| 5 | obsolete familial combined hyperlipidemia | 99.60% | DL |
| 6 | chronic hepatitis C virus infection | 98.02% | DL |
| 7 | AIDS | 97.57% | DL |
| 8 | fibroma of prostate | 95.92% | DL |
| 9 | hepatitis B virus infection | 95.77% | DL |
| 10 | Brenner tumor | 95.53% | DL |
| 11 | benign reproductive system neoplasm | 95.52% | DL |
| 12 | benign prostate phyllodes tumor | 94.98% | DL |
| 13 | hepatitis C virus infection | 94.89% | DL |
| 14 | congenital human immunodeficiency virus | 94.56% | DL |
| 15 | AIDS related complex | 94.56% | DL |
| 16 | male reproductive organ cancer | 94.15% | DL |
| 17 | primitive portal vein thrombosis | 93.91% | DL |
| 18 | hepatopulmonary syndrome | 93.91% | DL |
| 19 | hepatoportal sclerosis | 93.91% | DL |
| 20 | early-onset familial noncirrhotic portal hypertension | 93.91% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 1 Phase 3 trial(s), 7 Phase 2 trial(s) |

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
