---
layout: default
title: Nomegestrol Acetate
description: "Nomegestrol Acetate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 409
evidence_level: L5
indication_count: 50
---

# Nomegestrol Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nomegestrol Acetate |
| DrugBank ID | [DB13981](https://go.drugbank.com/drugs/DB13981) |
| Brand Names (EU) | Nomegestrol acetate |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.78% |

---

## Approved Indication (EMA)

Oral contraception

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | candidiasis | 98.78% | DL |
| 2 | antithrombin deficiency type 2 | 98.53% | DL |
| 3 | heparin cofactor 2 deficiency | 98.49% | DL |
| 4 | factor 5 excess with spontaneous thrombosis | 98.45% | DL |
| 5 | plasma cell myeloma | 97.75% | DL |
| 6 | gout | 97.60% | DL |
| 7 | indolent plasma cell myeloma | 97.53% | DL |
| 8 | heart neoplasm | 97.37% | DL |
| 9 | thrombotic disease | 97.37% | DL |
| 10 | rheumatoid arthritis | 97.36% | DL |
| 11 | thrombophilia | 97.35% | DL |
| 12 | cardiovascular disease | 97.20% | DL |
| 13 | oral candidiasis | 97.18% | DL |
| 14 | conjunctivitis | 97.12% | DL |
| 15 | polyp of vocal cord | 97.09% | DL |
| 16 | polyp of middle ear | 97.08% | DL |
| 17 | Bacteroidaceae infectious disease | 97.08% | DL |
| 18 | uterine polyp | 97.06% | DL |
| 19 | leprosy | 97.06% | DL |
| 20 | polyp of frontal sinus | 97.04% | DL |

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
