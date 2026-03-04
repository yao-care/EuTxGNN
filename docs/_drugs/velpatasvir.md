---
layout: default
title: Velpatasvir
description: "velpatasvir drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 626
evidence_level: L1
indication_count: 50
---

# Velpatasvir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Velpatasvir |
| DrugBank ID | [DB11613](https://go.drugbank.com/drugs/DB11613) |
| Brand Names (EU) | Velpatasvir |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Epclusa is indicated for the treatment of chronic hepatitis C virus (HCV) infection in patients 3 years of age and older (see sections 4.2, 4.4 and 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic hepatitis C virus infection | 99.97% | DL |
| 2 | hepatitis C virus infection | 99.89% | DL |
| 3 | hepatitis B virus infection | 99.87% | DL |
| 4 | hepatitis E virus infection | 99.80% | DL |
| 5 | hepatitis A virus infection | 99.80% | DL |
| 6 | hepatitis, viral, animal | 99.79% | DL |
| 7 | Omsk hemorrhagic fever | 99.79% | DL |
| 8 | Kyasanur forest disease | 99.79% | DL |
| 9 | HIV infectious disease | 99.77% | DL |
| 10 | feline acquired immunodeficiency syndrome | 99.66% | DL |
| 11 | simian immunodeficiency virus infection | 99.66% | DL |
| 12 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.58% | DL |
| 13 | chronic hepatitis B virus infection | 99.30% | DL |
| 14 | obsolete familial combined hyperlipidemia | 98.68% | DL |
| 15 | fibroma of prostate | 98.64% | DL |
| 16 | benign reproductive system neoplasm | 98.58% | DL |
| 17 | Brenner tumor | 98.57% | DL |
| 18 | benign prostate phyllodes tumor | 98.51% | DL |
| 19 | male reproductive organ cancer | 98.34% | DL |
| 20 | prostate leiomyoma | 98.14% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| chronic hepatitis C virus infection | L1 | 20 | 19 | 6 Phase 3 trial(s), 5 Phase 2 trial(s), 2 review(s |

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
