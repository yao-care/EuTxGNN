---
layout: default
title: Nevirapine
description: "Nevirapine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 402
evidence_level: L5
indication_count: 50
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nevirapine |
| DrugBank ID | [DB00238](https://go.drugbank.com/drugs/DB00238) |
| Brand Names (EU) | Viramune |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.91% |

---

## Approved Indication (EMA)

Viramune 50 mg/5 mL oral suspension and 200 mg tablets Viramune is indicated in combination with other anti-retroviral medicinal products for the treatment of HIV-1 infected adults, adolescents, and children of any age.Most of the experience with Viramune is in combination with nucleoside reverse transcriptase inhibitors (NRTIs). The choice of a subsequent therapy after Viramune should be based on clinical experience and resistance testing. Viramune 400 mg prolonged-release tablets Viramune is i

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.91% | DL |
| 2 | simian immunodeficiency virus infection | 99.85% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.85% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.82% | DL |
| 5 | AIDS | 99.38% | DL |
| 6 | fibroma of prostate | 98.99% | DL |
| 7 | Brenner tumor | 98.92% | DL |
| 8 | benign reproductive system neoplasm | 98.90% | DL |
| 9 | benign prostate phyllodes tumor | 98.77% | DL |
| 10 | male reproductive organ cancer | 98.62% | DL |
| 11 | AIDS related complex | 98.52% | DL |
| 12 | congenital human immunodeficiency virus | 98.52% | DL |
| 13 | prostate leiomyoma | 98.45% | DL |
| 14 | prostate cancer/brain cancer susceptibility | 98.40% | DL |
| 15 | obsolete familial combined hyperlipidemia | 97.66% | DL |
| 16 | breast fibrocystic disease | 97.06% | DL |
| 17 | apocrine adenosis of breast | 96.23% | DL |
| 18 | blunt duct adenosis of breast | 96.23% | DL |
| 19 | benign mammary dysplasia | 95.66% | DL |
| 20 | mycotic corneal ulcer | 94.04% | DL |

*Showing top 20 of 50 predictions.*

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
