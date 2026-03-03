---
layout: default
title: Efavirenz
description: "Efavirenz drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 192
evidence_level: L5
indication_count: 50
---

# Efavirenz
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Efavirenz |
| DrugBank ID | [DB00625](https://go.drugbank.com/drugs/DB00625) |
| Brand Names (EU) | Efavirenz Teva |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Efavirenz is indicated in antiviral combination treatment of human-immunodeficiency-virus-1 (HIV-1)-infected adults, adolescents and children 3 years of age and older. Efavirenz has not been adequately studied in patients with advanced HIV disease, namely in patients with CD4 counts &lt; 50 cells/mm3, or after failure of protease inhibitor (PI)-containing regimens. Although cross-resistance of efavirenz with protease inhibitors (PIs) has not been documented, there are at present insufficient dat

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.88% | DL |
| 2 | simian immunodeficiency virus infection | 99.80% | DL |
| 3 | feline acquired immunodeficiency syndrome | 99.80% | DL |
| 4 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.77% | DL |
| 5 | AIDS | 98.64% | DL |
| 6 | obsolete familial combined hyperlipidemia | 97.72% | DL |
| 7 | congenital human immunodeficiency virus | 96.90% | DL |
| 8 | AIDS related complex | 96.90% | DL |
| 9 | fibroma of prostate | 95.38% | DL |
| 10 | Brenner tumor | 95.07% | DL |
| 11 | benign reproductive system neoplasm | 95.02% | DL |
| 12 | benign prostate phyllodes tumor | 94.64% | DL |
| 13 | male reproductive organ cancer | 93.74% | DL |
| 14 | prostate leiomyoma | 92.95% | DL |
| 15 | prostate cancer/brain cancer susceptibility | 92.87% | DL |
| 16 | breast fibrocystic disease | 88.33% | DL |
| 17 | blunt duct adenosis of breast | 87.01% | DL |
| 18 | apocrine adenosis of breast | 87.01% | DL |
| 19 | benign mammary dysplasia | 83.99% | DL |
| 20 | mycotic corneal ulcer | 81.81% | DL |

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
