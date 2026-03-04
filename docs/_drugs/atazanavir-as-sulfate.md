---
layout: default
title: Atazanavir (As Sulfate)
description: "atazanavir (as sulfate) drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 53
evidence_level: L1
indication_count: 50
---

# Atazanavir (As Sulfate)
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Atazanavir (As Sulfate) |
| DrugBank ID | [DB01072](https://go.drugbank.com/drugs/DB01072) |
| Brand Names (EU) | Reyataz |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Reyataz capsules, co-administered with low dose ritonavir, are indicated for the treatment of HIV-1 infected adults and paediatric patients 6 years of age and older in combination with other antiretroviral medicinal products (see section 4.2). Based on available virological and clinical data from adult patients, no benefit is expected in patients with strains resistant to multiple protease inhibitors (? 4 PI mutations). The choice of Reyataz in treatment experienced adult and paediatric patients

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.99% | DL |
| 2 | feline acquired immunodeficiency syndrome | 99.98% | DL |
| 3 | simian immunodeficiency virus infection | 99.98% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.98% | DL |
| 5 | AIDS | 99.90% | DL |
| 6 | obsolete familial combined hyperlipidemia | 99.82% | DL |
| 7 | congenital human immunodeficiency virus | 99.71% | DL |
| 8 | AIDS related complex | 99.71% | DL |
| 9 | fibroma of prostate | 98.78% | DL |
| 10 | Brenner tumor | 98.68% | DL |
| 11 | benign reproductive system neoplasm | 98.67% | DL |
| 12 | benign prostate phyllodes tumor | 98.51% | DL |
| 13 | male reproductive organ cancer | 98.32% | DL |
| 14 | prostate cancer/brain cancer susceptibility | 98.12% | DL |
| 15 | prostate leiomyoma | 98.03% | DL |
| 16 | homozygous familial hypercholesterolemia | 97.02% | DL |
| 17 | breast fibrocystic disease | 96.44% | DL |
| 18 | chronic hepatitis C virus infection | 95.93% | DL |
| 19 | hypercholesterolemia, autosomal dominant | 95.89% | DL |
| 20 | apocrine adenosis of breast | 95.36% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| HIV infectious disease | L1 | 20 | 0 | 3 Phase 3 trial(s), 5 Phase 2 trial(s) |

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
