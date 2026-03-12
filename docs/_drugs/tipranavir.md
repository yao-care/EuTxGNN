---
layout: default
title: Tipranavir
description: "tipranavir drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 584
evidence_level: L1
indication_count: 50
---

# Tipranavir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tipranavir |
| DrugBank ID | [DB00932](https://go.drugbank.com/drugs/DB00932) |
| Brand Names (EU) | Aptivus |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Aptivus, co-administered with low-dose ritonavir, is indicated for combination antiretroviral treatment of HIV-1 infection in highly pretreated adults and adolescents 12 years of age or older with virus resistant to multiple protease inhibitors. Aptivus should only be used as part of an active combination antiretroviral regimen in patients with no other therapeutic options. This indication is based on the results of two phase-III studies, performed in highly pretreated adult patients (median num

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.99% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.99% | DL |
| 3 | simian immunodeficiency virus infection | 99.99% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.99% | DL |
| 5 | AIDS | 99.94% | DL |
| 6 | obsolete familial combined hyperlipidemia | 99.93% | DL |
| 7 | AIDS related complex | 99.83% | DL |
| 8 | congenital human immunodeficiency virus | 99.83% | DL |
| 9 | fibroma of prostate | 99.44% | DL |
| 10 | Brenner tumor | 99.39% | DL |
| 11 | benign reproductive system neoplasm | 99.39% | DL |
| 12 | benign prostate phyllodes tumor | 99.31% | DL |
| 13 | male reproductive organ cancer | 99.24% | DL |
| 14 | prostate leiomyoma | 99.11% | DL |
| 15 | prostate cancer/brain cancer susceptibility | 99.10% | DL |
| 16 | breast fibrocystic disease | 98.87% | DL |
| 17 | homozygous familial hypercholesterolemia | 98.68% | DL |
| 18 | benign mammary dysplasia | 98.36% | DL |
| 19 | blunt duct adenosis of breast | 98.34% | DL |
| 20 | apocrine adenosis of breast | 98.34% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 3 Phase 3 trial(s), 8 Phase 2 trial(s) |

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
