---
layout: default
title: Siltuximab
description: "Siltuximab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 529
evidence_level: L5
indication_count: 50
---

# Siltuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Siltuximab |
| DrugBank ID | [DB09036](https://go.drugbank.com/drugs/DB09036) |
| Brand Names (EU) | Sylvant |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

Sylvant is indicated for the treatment of adult patients with multicentric Castleman’s disease (MCD who are human immunodeficiency virus (HIV) negative and human herpesvirus-8 (HHV-8) negative.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Kimura disease | 99.82% | DL |
| 2 | extracutaneous mastocytoma | 99.64% | DL |
| 3 | hepatic infarction | 99.44% | DL |
| 4 | hepatic veno-occlusive disease | 99.40% | DL |
| 5 | Castleman disease | 99.39% | DL |
| 6 | peliosis hepatis | 99.29% | DL |
| 7 | Kaposi's sarcoma (disease) | 99.28% | DL |
| 8 | autosomal recessive familial Mediterranean fever | 99.22% | DL |
| 9 | aggressive systemic mastocytosis | 99.16% | DL |
| 10 | autosomal dominant familial periodic fever | 99.05% | DL |
| 11 | syndrome with combined immunodeficiency | 98.85% | DL |
| 12 | TAFRO syndrome | 98.79% | DL |
| 13 | dermatofibrosarcoma protuberans | 98.76% | DL |
| 14 | lymphangiomyoma | 98.67% | DL |
| 15 | benign PEComa | 98.66% | DL |
| 16 | uterine corpus perivascular epithelioid cell tumor | 98.64% | DL |
| 17 | primary release disorder of platelets | 98.56% | DL |
| 18 | hepatic veno-occlusive disease-immunodeficiency syndrome | 98.48% | DL |
| 19 | pancytopenia due to IKZF1 mutations | 98.40% | DL |
| 20 | periodic fever-infantile enterocolitis-autoinflammatory syndrome | 98.40% | DL |

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
