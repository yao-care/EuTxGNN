---
layout: default
title: Tafasitamab
description: "Tafasitamab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 552
evidence_level: L5
indication_count: 50
---

# Tafasitamab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tafasitamab |
| DrugBank ID | [DB15044](https://go.drugbank.com/drugs/DB15044) |
| Brand Names (EU) | Minjuvi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.71% |

---

## Approved Indication (EMA)

Minjuvi is indicated in combination with lenalidomide followed by Minjuvi monotherapy for the treatment of adult patients with relapsed or refractory diffuse large B-cell lymphoma (DLBCL) who are not eligible for autologous stem cell transplant (ASCT).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | drug-induced osteoporosis | 98.71% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 97.34% | DL |
| 3 | diabetic retinopathy | 95.40% | DL |
| 4 | HER2 positive breast carcinoma | 94.51% | DL |
| 5 | psoriasis | 94.03% | DL |
| 6 | progesterone-receptor positive breast cancer | 93.00% | DL |
| 7 | normal breast-like subtype of breast carcinoma | 93.00% | DL |
| 8 | breast tumor luminal A or B | 92.91% | DL |
| 9 | progesterone-receptor negative breast cancer | 92.67% | DL |
| 10 | pityriasis lichenoides | 92.29% | DL |
| 11 | acne (disease) | 89.57% | DL |
| 12 | dermatitis | 89.32% | DL |
| 13 | ulcerative colitis (disease) | 88.74% | DL |
| 14 | congenital hypotrichosis with juvenile macular dystrophy | 88.57% | DL |
| 15 | neonatal dermatomyositis | 88.10% | DL |
| 16 | parapsoriasis | 87.99% | DL |
| 17 | amyopathic dermatomyositis | 87.58% | DL |
| 18 | acrodermatitis chronica atrophicans | 87.46% | DL |
| 19 | acne keloid | 87.36% | DL |
| 20 | diabetic cataract | 87.30% | DL |

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
