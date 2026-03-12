---
layout: default
title: Vismodegib
description: "vismodegib drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 636
evidence_level: L2
indication_count: 50
---

# Vismodegib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vismodegib |
| DrugBank ID | [DB08828](https://go.drugbank.com/drugs/DB08828) |
| Brand Names (EU) | Erivedge |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Erivedge is indicated for the treatment of adult patients with:- symptomatic metastatic basal cell carcinoma- locally advanced basal cell carcinoma inappropriate for surgery or radiotherapy

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | basal cell carcinoma | 99.98% | DL |
| 2 | medulloblastoma with extensive nodularity | 99.93% | DL |
| 3 | sebaceous adenocarcinoma | 99.93% | DL |
| 4 | sweat gland cancer | 99.91% | DL |
| 5 | xeroderma pigmentosum | 99.91% | DL |
| 6 | skin carcinoma | 99.88% | DL |
| 7 | annular epidermolytic ichthyosis | 99.87% | DL |
| 8 | epidermolysis bullosa simplex with mottled pigmentation | 99.86% | DL |
| 9 | prostate cancer/brain cancer susceptibility | 99.85% | DL |
| 10 | Brenner tumor | 99.83% | DL |
| 11 | cutaneous adenocystic carcinoma | 99.83% | DL |
| 12 | prostate leiomyoma | 99.83% | DL |
| 13 | skin cancer | 99.82% | DL |
| 14 | benign neoplasm of sweat gland | 99.82% | DL |
| 15 | fibroma of prostate | 99.81% | DL |
| 16 | benign reproductive system neoplasm | 99.81% | DL |
| 17 | male reproductive organ cancer | 99.81% | DL |
| 18 | trichothiodystrophy photosensitive | 99.81% | DL |
| 19 | eccrine carcinoma | 99.81% | DL |
| 20 | benign prostate phyllodes tumor | 99.79% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| basal cell carcinoma | L2 | 20 | 18 | 14 Phase 2 trial(s) |

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
