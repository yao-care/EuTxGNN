---
layout: default
title: Ribociclib Succinate
description: "Ribociclib Succinate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 491
evidence_level: L5
indication_count: 50
---

# Ribociclib Succinate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ribociclib Succinate |
| DrugBank ID | [DB11730](https://go.drugbank.com/drugs/DB11730) |
| Brand Names (EU) | Kisqali |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.35% |

---

## Approved Indication (EMA)

Early breast cancerKisqali in combination with an aromatase inhibitor is indicated for the adjuvant treatment of patients with hormone receptor (HR)-positive, human epidermal growth factor receptor 2 (HER2)-negative early breast cancer at high risk of recurrence (see section 5.1 for selection criteria).In pre- or perimenopausal women, or in men, the aromatase inhibitor should be combined with a luteinising hormone-releasing hormone (LHRH) agonist.Advanced or metastatic breast cancerKisqali is in

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | myeloid leukemia | 99.35% | DL |
| 2 | thrombocytopenia | 99.27% | DL |
| 3 | marcothrombocytopenia with mitral valve insufficiency | 99.08% | DL |
| 4 | hereditary thrombocytopenia with normal platelets | 99.07% | DL |
| 5 | transient neonatal thrombocytopenia | 98.98% | DL |
| 6 | dense granule disease | 98.90% | DL |
| 7 | female breast carcinoma | 98.47% | DL |
| 8 | multiple endocrine neoplasia | 98.10% | DL |
| 9 | HIV infectious disease | 98.09% | DL |
| 10 | heart neoplasm | 98.07% | DL |
| 11 | platelet storage pool deficiency | 97.94% | DL |
| 12 | plasma cell myeloma | 97.72% | DL |
| 13 | collagenopathy | 97.69% | DL |
| 14 | lymphocytic hypereosinophilic syndrome | 97.66% | DL |
| 15 | cardiovascular disease | 97.57% | DL |
| 16 | heart valve disease | 97.56% | DL |
| 17 | simian immunodeficiency virus infection | 97.55% | DL |
| 18 | feline acquired immunodeficiency syndrome | 97.55% | DL |
| 19 | heart conduction disease | 97.50% | DL |
| 20 | melanoma | 97.47% | DL |

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
