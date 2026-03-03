---
layout: default
title: Budesonide
description: "Budesonide drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 98
evidence_level: L5
indication_count: 52
---

# Budesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Budesonide |
| DrugBank ID | [DB01222](https://go.drugbank.com/drugs/DB01222) |
| Brand Names (EU) | GoResp Digihaler (previously Budesonide/Formoterol Teva Pharma B.V.), Jorveza |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Jorveza is indicated for the treatment of eosinophilic esophagitis (EoE) in adults (older than 18 years of age).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | atopic eczema | 99.96% | DL |
| 2 | allergic asthma | 99.89% | DL |
| 3 | intrinsic asthma | 99.87% | DL |
| 4 | bronchitis | 99.81% | DL |
| 5 | dermatitis, atopic | 99.81% | DL |
| 6 | polyp of vocal cord | 99.71% | DL |
| 7 | polyp of middle ear | 99.71% | DL |
| 8 | epulis | 99.70% | DL |
| 9 | fibroepithelial polyp | 99.69% | DL |
| 10 | uterine polyp | 99.69% | DL |
| 11 | polyp of frontal sinus | 99.69% | DL |
| 12 | polyp of external auditory canal | 99.69% | DL |
| 13 | polyp of vulva | 99.69% | DL |
| 14 | polyp of ureter | 99.69% | DL |
| 15 | neoplastic polyp | 99.69% | DL |
| 16 | 2-hydroxyethyl methacrylate sensitization | 99.60% | DL |
| 17 | asthma | 99.53% | DL |
| 18 | Crohn's colitis | 99.29% | DL |
| 19 | inflammatory bowel disease | 99.19% | DL |
| 20 | anus disease | 98.99% | DL |

*Showing top 20 of 52 predictions.*

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
