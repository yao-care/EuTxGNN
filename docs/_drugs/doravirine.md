---
layout: default
title: Doravirine
description: "doravirine drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 180
evidence_level: L1
indication_count: 50
---

# Doravirine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Doravirine |
| DrugBank ID | [DB12301](https://go.drugbank.com/drugs/DB12301) |
| Brand Names (EU) | Pifeltro |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.95% |

---

## Approved Indication (EMA)

Delstrigo is indicated for the treatment of adults infected with HIV 1 without past or present evidence of resistance to the NNRTI class, lamivudine, or tenofovir. Delstrigo is also indicated for the treatment of adolescents aged 12 years and older weighing at least 35 kg who are infected with HIV-1 without past or present evidence of resistance to the NNRTI class, lamivudine, or tenofovir and who have experienced toxicities which preclude the use of other regimens that do not contain tenofovir 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.95% | DL |
| 2 | simian immunodeficiency virus infection | 99.93% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.93% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.91% | DL |
| 5 | AIDS | 99.44% | DL |
| 6 | fibroma of prostate | 98.76% | DL |
| 7 | congenital human immunodeficiency virus | 98.75% | DL |
| 8 | AIDS related complex | 98.75% | DL |
| 9 | Brenner tumor | 98.75% | DL |
| 10 | benign reproductive system neoplasm | 98.70% | DL |
| 11 | benign prostate phyllodes tumor | 98.63% | DL |
| 12 | male reproductive organ cancer | 98.46% | DL |
| 13 | prostate leiomyoma | 98.29% | DL |
| 14 | prostate cancer/brain cancer susceptibility | 98.20% | DL |
| 15 | chronic hepatitis C virus infection | 97.94% | DL |
| 16 | breast fibrocystic disease | 97.43% | DL |
| 17 | blunt duct adenosis of breast | 96.81% | DL |
| 18 | apocrine adenosis of breast | 96.81% | DL |
| 19 | mycotic corneal ulcer | 96.52% | DL |
| 20 | hepatitis C virus infection | 96.18% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 6 Phase 3 trial(s), 3 Phase 2 trial(s) |

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
