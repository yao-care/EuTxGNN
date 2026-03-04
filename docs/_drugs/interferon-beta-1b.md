---
layout: default
title: Interferon Beta-1B
description: "interferon beta-1b drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 312
evidence_level: L1
indication_count: 50
---

# Interferon Beta-1B
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Interferon Beta-1B |
| DrugBank ID | [DB00068](https://go.drugbank.com/drugs/DB00068) |
| Brand Names (EU) | Betaferon |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Betaferon is indicated for the treatment of  patients with a single demyelinating event with an active inflammatory process, if it is severe enough to warrant treatment with intravenous corticosteroids, if alternative diagnoses have been excluded, and if they are determined to be at high risk of developing clinically definite multiple sclerosis; patients with relapsing-remitting multiple sclerosis and two or more relapses within the last two years; patients with secondary progressive multiple sc

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 99.99% | DL |
| 2 | hairy cell leukemia | 99.16% | DL |
| 3 | autoimmune disease of central nervous system | 99.02% | DL |
| 4 | CNS demyelinating autoimmune disease | 98.94% | DL |
| 5 | multiple sclerosis, susceptibility to | 98.85% | DL |
| 6 | fetal methylmercury syndrome | 98.52% | DL |
| 7 | hepatic infarction | 98.19% | DL |
| 8 | progressive multiple sclerosis | 97.97% | DL |
| 9 | hairy cell leukemia variant | 97.90% | DL |
| 10 | extramammary Paget disease | 97.86% | DL |
| 11 | peliosis hepatis | 97.67% | DL |
| 12 | hepatic veno-occlusive disease | 97.43% | DL |
| 13 | rete ovarii cystadenoma | 97.23% | DL |
| 14 | borderline ovarian serous tumor | 97.21% | DL |
| 15 | ovarian benign neoplasm | 97.13% | DL |
| 16 | ovarian papillary cystadenoma | 97.11% | DL |
| 17 | ovarian mucinous cystadenofibroma | 97.09% | DL |
| 18 | syndrome with combined immunodeficiency | 97.06% | DL |
| 19 | serous neoplasm | 97.01% | DL |
| 20 | malignant ovarian Brenner tumor | 96.99% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| relapsing-remitting multiple sclerosis | L1 | 20 | 20 | 1 Phase 3 trial(s), 3 Phase 2 trial(s), 3 RCT(s),  |

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
