---
layout: default
title: Entecavir
description: "entecavir drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 213
evidence_level: L1
indication_count: 50
---

# Entecavir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Entecavir |
| DrugBank ID | [DB00442](https://go.drugbank.com/drugs/DB00442) |
| Brand Names (EU) | Entecavir Accord |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Entecavir Accord is indicated for the treatment of chronic hepatitis B virus (HBV) infection in adults with:  compensated liver disease and evidence of active viral replication, persistently elevated serum alanine aminotransferase (ALT) levels and histological evidence of active inflammation and/or fibrosis. decompensated liver disease.  For both compensated and decompensated liver disease, this indication is based on clinical trial data in nucleoside naive patients with HBeAg positive and HBeAg

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | chronic hepatitis C virus infection | 99.98% | DL |
| 2 | hepatitis B virus infection | 99.85% | DL |
| 3 | HIV infectious disease | 99.80% | DL |
| 4 | hepatitis C virus infection | 99.69% | DL |
| 5 | chronic hepatitis B virus infection | 99.67% | DL |
| 6 | simian immunodeficiency virus infection | 99.65% | DL |
| 7 | feline acquired immunodeficiency syndrome | 99.65% | DL |
| 8 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.64% | DL |
| 9 | hepatitis, viral, animal | 99.46% | DL |
| 10 | hepatitis E virus infection | 99.45% | DL |
| 11 | hepatitis A virus infection | 99.44% | DL |
| 12 | Omsk hemorrhagic fever | 99.41% | DL |
| 13 | Kyasanur forest disease | 99.39% | DL |
| 14 | early-onset familial noncirrhotic portal hypertension | 97.94% | DL |
| 15 | hepatoportal sclerosis | 97.94% | DL |
| 16 | hepatopulmonary syndrome | 97.94% | DL |
| 17 | idiopathic copper-associated cirrhosis | 97.94% | DL |
| 18 | primitive portal vein thrombosis | 97.94% | DL |
| 19 | obsolete familial combined hyperlipidemia | 97.64% | DL |
| 20 | hepatic porphyria | 97.39% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| chronic hepatitis C virus infection | L1 | 20 | 2 | 2 Phase 3 trial(s), 6 Phase 2 trial(s) |

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
