---
layout: default
title: Mirvetuximab Soravtansine
description: "Mirvetuximab Soravtansine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 386
evidence_level: L5
indication_count: 50
---

# Mirvetuximab Soravtansine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mirvetuximab Soravtansine |
| DrugBank ID | [DB12489](https://go.drugbank.com/drugs/DB12489) |
| Brand Names (EU) | Elahere |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.95% |

---

## Approved Indication (EMA)

Elahere as monotherapy is indicated for the treatment of adult patients with folate receptor-alpha (FRα) positive, platinum-resistant high grade serous epithelial ovarian, fallopian tube, or primary peritoneal cancer who have received one to three prior systemic treatment regimens.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | antithrombin deficiency type 2 | 97.95% | DL |
| 2 | heparin cofactor 2 deficiency | 97.83% | DL |
| 3 | factor 5 excess with spontaneous thrombosis | 97.81% | DL |
| 4 | candidiasis | 97.69% | DL |
| 5 | plasma cell myeloma | 97.61% | DL |
| 6 | indolent plasma cell myeloma | 97.41% | DL |
| 7 | tinea corporis | 96.84% | DL |
| 8 | thrombophilia | 96.70% | DL |
| 9 | uterine polyp | 96.56% | DL |
| 10 | pediatric systemic lupus erythematosus | 96.55% | DL |
| 11 | polyp of vocal cord | 96.49% | DL |
| 12 | polyp of middle ear | 96.48% | DL |
| 13 | polyp of frontal sinus | 96.44% | DL |
| 14 | polyp of external auditory canal | 96.43% | DL |
| 15 | polyp of ureter | 96.42% | DL |
| 16 | polyp of vulva | 96.41% | DL |
| 17 | fibroepithelial polyp | 96.38% | DL |
| 18 | neoplastic polyp | 96.33% | DL |
| 19 | epulis | 96.33% | DL |
| 20 | mantle cell lymphoma | 96.14% | DL |

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
