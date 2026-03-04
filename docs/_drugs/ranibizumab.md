---
layout: default
title: Ranibizumab
description: "ranibizumab drug repurposing predictions from TxGNN. Evidence level L1 with 52 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 478
evidence_level: L1
indication_count: 52
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ranibizumab |
| DrugBank ID | [DB01270](https://go.drugbank.com/drugs/DB01270) |
| Brand Names (EU) | Lucentis, Rimmyrah, Ximluci |
| Evidence Level | L1 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Ximluci is indicated in adults for:  The treatment of neovascular (wet) age-related macular degeneration (AMD) The treatment of visual impairment due to diabetic macular oedema (DME) The treatment of proliferative diabetic retinopathy (PDR) The treatment of visual impairment due to macular oedema secondary to retinal vein occlusion (branch RVO or central RVO) The treatment of visual impairment due to choroidal neovascularisation (CNV)

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 99.99% | DL |
| 2 | diabetic retinopathy | 99.99% | DL |
| 3 | diabetic cataract | 99.99% | DL |
| 4 | craniostenosis cataract | 99.99% | DL |
| 5 | mature cataract | 99.99% | DL |
| 6 | diabetes mellitus type 2 associated cataract | 99.99% | DL |
| 7 | immature cataract | 99.99% | DL |
| 8 | tetanic cataract | 99.99% | DL |
| 9 | nuclear senile cataract | 99.99% | DL |
| 10 | cortical cataract | 99.99% | DL |
| 11 | senile cataract | 99.99% | DL |
| 12 | hemorrhagic disease of newborn | 99.87% | DL |
| 13 | esotropia | 99.79% | DL |
| 14 | primary release disorder of platelets | 99.76% | DL |
| 15 | pseudo-von Willebrand disease | 99.76% | DL |
| 16 | esophageal varices with bleeding | 99.63% | DL |
| 17 | esophageal varices without bleeding | 99.63% | DL |
| 18 | varicose disease | 99.42% | DL |
| 19 | retinopathy of prematurity | 99.38% | DL |
| 20 | Glanzmann thrombasthenia | 99.25% | DL |

*Showing top 20 of 52 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| diabetic retinopathy | L1 | 20 | 19 | 8 Phase 3 trial(s), 4 Phase 2 trial(s), 6 RCT(s),  |
| diabetic cataract | L1 | 20 | 1 | 4 Phase 3 trial(s), 3 Phase 2 trial(s) |
| severe nonproliferative diabetic retinopathy | L1 | 6 | 2 | 4 Phase 3 trial(s), 2 RCT(s) |

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
