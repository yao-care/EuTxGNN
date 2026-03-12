---
layout: default
title: Tezepelumab
description: "Tezepelumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 575
evidence_level: L5
indication_count: 50
---

# Tezepelumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tezepelumab |
| DrugBank ID | [DB15090](https://go.drugbank.com/drugs/DB15090) |
| Brand Names (EU) | Tezspire |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.40% |

---

## Approved Indication (EMA)

AsthmaTezspire is indicated as an add-on maintenance treatment in adults and adolescents 12 years and older with severe asthma who are inadequately controlled despite high dose inhaled corticosteroids plus another medicinal product for maintenance treatment. Chronic rhinosinusitis with nasal polyps (CRSwNP)&nbsp;Tezspire is indicated as an add-on therapy with intranasal corticosteroids for the treatment of adult patients with severe CRSwNP for whom therapy with systemic corticosteroids, and/or s

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetic cataract | 98.40% | DL |
| 2 | craniostenosis cataract | 98.31% | DL |
| 3 | mature cataract | 98.31% | DL |
| 4 | tetanic cataract | 98.31% | DL |
| 5 | diabetes mellitus type 2 associated cataract | 98.31% | DL |
| 6 | immature cataract | 98.31% | DL |
| 7 | cortical cataract | 98.29% | DL |
| 8 | nuclear senile cataract | 98.29% | DL |
| 9 | senile cataract | 98.22% | DL |
| 10 | diabetic retinopathy | 98.12% | DL |
| 11 | antithrombin deficiency type 2 | 98.06% | DL |
| 12 | factor 5 excess with spontaneous thrombosis | 98.01% | DL |
| 13 | heparin cofactor 2 deficiency | 97.96% | DL |
| 14 | severe nonproliferative diabetic retinopathy | 97.86% | DL |
| 15 | thrombophilia | 97.70% | DL |
| 16 | diffuse gastric adenocarcinoma | 95.54% | DL |
| 17 | hemorrhagic disease of newborn | 95.16% | DL |
| 18 | gastric carcinoma | 94.97% | DL |
| 19 | gastric adenocarcinoma and proximal polyposis of the stomach | 94.84% | DL |
| 20 | signet ring cell gastric adenocarcinoma | 94.73% | DL |

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
