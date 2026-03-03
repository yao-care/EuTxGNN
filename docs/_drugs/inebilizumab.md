---
layout: default
title: Inebilizumab
description: "Inebilizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 300
evidence_level: L5
indication_count: 50
---

# Inebilizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Inebilizumab |
| DrugBank ID | [DB12530](https://go.drugbank.com/drugs/DB12530) |
| Brand Names (EU) | Uplizna |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.44% |

---

## Approved Indication (EMA)

Uplizna is indicated as monotherapy for the treatment of adult patients with neuromyelitis optica spectrum disorders (NMOSD) who are anti-aquaporin 4 immunoglobulin G (AQP4-IgG) seropositive (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 96.44% | DL |
| 2 | psoriasis | 95.75% | DL |
| 3 | pityriasis lichenoides | 94.03% | DL |
| 4 | plasma cell myeloma | 92.75% | DL |
| 5 | indolent plasma cell myeloma | 92.65% | DL |
| 6 | ulcerative colitis (disease) | 92.38% | DL |
| 7 | congenital hypotrichosis with juvenile macular dystrophy | 91.59% | DL |
| 8 | HER2 positive breast carcinoma | 91.55% | DL |
| 9 | parapsoriasis | 91.49% | DL |
| 10 | severe nonproliferative diabetic retinopathy | 90.60% | DL |
| 11 | acute lichenoid pityriasis | 90.26% | DL |
| 12 | primary release disorder of platelets | 89.69% | DL |
| 13 | progesterone-receptor positive breast cancer | 89.51% | DL |
| 14 | normal breast-like subtype of breast carcinoma | 89.51% | DL |
| 15 | breast tumor luminal A or B | 89.36% | DL |
| 16 | rheumatoid arthritis | 89.21% | DL |
| 17 | pustulosis palmaris et plantaris | 89.21% | DL |
| 18 | progesterone-receptor negative breast cancer | 89.13% | DL |
| 19 | inflammatory bowel disease | 89.07% | DL |
| 20 | psoriasis 14, pustular | 88.60% | DL |

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
