---
layout: default
title: Midostaurin
description: "Midostaurin drug repurposing predictions from TxGNN. Evidence level L5 with 56 predicted indications."
parent: AI Predictions (L5)
nav_order: 381
evidence_level: L5
indication_count: 56
---

# Midostaurin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **56**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Midostaurin |
| DrugBank ID | [DB06595](https://go.drugbank.com/drugs/DB06595) |
| Brand Names (EU) | Rydapt |
| Evidence Level | L5 |
| Predicted Indications | 56 |
| Top Prediction Score | 98.92% |

---

## Approved Indication (EMA)

Rydapt is indicated:  in combination with standard daunorubicin and cytarabine induction and high dose cytarabine consolidation chemotherapy, and for patients in complete response followed by Rydapt single agent maintenance therapy, for adult patients with newly diagnosed acute myeloid leukaemia (AML) who are FLT3 mutation positive (see section 4.2); as monotherapy for the treatment of adult patients with aggressive systemic mastocytosis (ASM), systemic mastocytosis with associated haematologica

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | familial thrombocytosis | 98.92% | DL |
| 2 | reactive thrombocytosis | 98.76% | DL |
| 3 | metastatic melanoma | 97.64% | DL |
| 4 | inverse Klippel-Trenaunay syndrome | 97.62% | DL |
| 5 | thrombocythemia | 97.48% | DL |
| 6 | non-cutaneous melanoma | 97.13% | DL |
| 7 | epithelioid cell melanoma | 96.95% | DL |
| 8 | eyelid melanoma | 96.94% | DL |
| 9 | scrotum melanoma | 96.73% | DL |
| 10 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 96.39% | DL |
| 11 | superficial spreading melanoma | 96.39% | DL |
| 12 | lentigo maligna melanoma | 96.39% | DL |
| 13 | CDK4 linked melanoma | 96.39% | DL |
| 14 | acral lentiginous melanoma (disease) | 96.39% | DL |
| 15 | balloon cell malignant melanoma | 96.39% | DL |
| 16 | amelanotic skin melanoma | 96.39% | DL |
| 17 | nodular malignant melanoma | 96.39% | DL |
| 18 | malignant melanoma of the mucosa | 96.39% | DL |
| 19 | choroideremia | 96.38% | DL |
| 20 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 96.37% | DL |

*Showing top 20 of 56 predictions.*

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
