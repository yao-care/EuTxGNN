---
layout: default
title: Letermovir
description: "Letermovir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 339
evidence_level: L5
indication_count: 50
---

# Letermovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Letermovir |
| DrugBank ID | [DB12070](https://go.drugbank.com/drugs/DB12070) |
| Brand Names (EU) | Prevymis |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Prevymis is indicated for prophylaxis of cytomegalovirus (CMV) reactivation and disease in adult and paediatric patients weighing at least 5 kg who are CMV-seropositive recipients [R+] of an allogeneic haematopoietic stem cell transplant (HSCT).Prevymis is indicated for prophylaxis of CMV disease in CMV-seronegative adult and paediatric patients weighing at least 40 kg who have received a kidney transplant from a CMV-seropositive donor [D+/R-].Prevymis is indicated for prophylaxis of cytomegalov

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | vulvovaginal candidiasis | 99.88% | DL |
| 2 | fungal infectious disease | 98.93% | DL |
| 3 | tinea nigra | 98.62% | DL |
| 4 | infectious bovine rhinotracheitis | 98.48% | DL |
| 5 | malignant catarrh | 98.48% | DL |
| 6 | anogenital human papillomavirus infection | 97.99% | DL |
| 7 | cytomegalovirus infection | 97.96% | DL |
| 8 | AIDS | 97.86% | DL |
| 9 | dermatophytosis | 97.66% | DL |
| 10 | piedra | 97.16% | DL |
| 11 | varicella zoster infection | 96.87% | DL |
| 12 | congenital human immunodeficiency virus | 96.86% | DL |
| 13 | AIDS related complex | 96.86% | DL |
| 14 | postmenopausal atrophic vaginitis | 96.46% | DL |
| 15 | vulvovaginitis | 96.08% | DL |
| 16 | roseolovirus infectious disease | 95.68% | DL |
| 17 | vulvitis | 95.57% | DL |
| 18 | mycotic corneal ulcer | 95.51% | DL |
| 19 | commissural lip fistula | 95.36% | DL |
| 20 | burning mouth syndrome | 95.30% | DL |

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
