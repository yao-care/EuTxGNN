---
layout: default
title: Ritonavir
description: "ritonavir drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 500
evidence_level: L1
indication_count: 50
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ritonavir |
| DrugBank ID | [DB00503](https://go.drugbank.com/drugs/DB00503) |
| Brand Names (EU) | Ritonavir Viatris (previously Ritonavir Mylan) |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Ritonavir is indicated in combination with other antiretroviral agents for the treatment of HIV 1 infected patients (adults and children of 2 years of age and older).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.96% | DL |
| 2 | simian immunodeficiency virus infection | 99.92% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.92% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.92% | DL |
| 5 | obsolete familial combined hyperlipidemia | 99.76% | DL |
| 6 | chronic hepatitis C virus infection | 99.46% | DL |
| 7 | AIDS | 98.44% | DL |
| 8 | hepatitis B virus infection | 98.09% | DL |
| 9 | hepatitis C virus infection | 96.91% | DL |
| 10 | AIDS related complex | 96.68% | DL |
| 11 | congenital human immunodeficiency virus | 96.68% | DL |
| 12 | chronic hepatitis B virus infection | 96.37% | DL |
| 13 | fibroma of prostate | 95.79% | DL |
| 14 | hepatitis E virus infection | 95.54% | DL |
| 15 | hepatitis, viral, animal | 95.53% | DL |
| 16 | hepatitis A virus infection | 95.42% | DL |
| 17 | Omsk hemorrhagic fever | 95.40% | DL |
| 18 | benign reproductive system neoplasm | 95.37% | DL |
| 19 | Brenner tumor | 95.33% | DL |
| 20 | Kyasanur forest disease | 95.22% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 6 Phase 3 trial(s), 6 Phase 2 trial(s) |

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
