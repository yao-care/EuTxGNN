---
layout: default
title: Ustekinumab
description: "Ustekinumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 618
evidence_level: L5
indication_count: 51
---

# Ustekinumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ustekinumab |
| DrugBank ID | [DB05679](https://go.drugbank.com/drugs/DB05679) |
| Brand Names (EU) | Stelara |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Adult Crohn’s DiseaseSTELARA is indicated for the treatment of adult patients with moderately to severely active Crohn’s disease who have had an inadequate response with, lost response to, or were intolerant to either conventional therapy or a TNFα antagonist.Paediatric Crohn's DiseaseSTELARA is indicated for the treatment of moderately to severely active Crohn’s disease in paediatric patients weighing at least 40 kg, who have had an inadequate response to, or were intolerant to either conventio

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatitis | 99.99% | DL |
| 2 | neonatal dermatomyositis | 99.98% | DL |
| 3 | acne keloid | 99.97% | DL |
| 4 | acrodermatitis chronica atrophicans | 99.97% | DL |
| 5 | amyopathic dermatomyositis | 99.97% | DL |
| 6 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.97% | DL |
| 7 | hydroa vacciniforme, familial | 99.97% | DL |
| 8 | severe nonproliferative diabetic retinopathy | 99.96% | DL |
| 9 | psoriasis | 99.95% | DL |
| 10 | parapsoriasis | 99.93% | DL |
| 11 | pityriasis lichenoides | 99.89% | DL |
| 12 | acute lichenoid pityriasis | 99.86% | DL |
| 13 | diabetic retinopathy | 99.83% | DL |
| 14 | pustulosis palmaris et plantaris | 99.73% | DL |
| 15 | psoriasis 14, pustular | 99.63% | DL |
| 16 | seborrheic dermatitis | 99.36% | DL |
| 17 | polyp of middle ear | 98.90% | DL |
| 18 | polyp of vocal cord | 98.90% | DL |
| 19 | polyp of ureter | 98.87% | DL |
| 20 | polyp of frontal sinus | 98.87% | DL |

*Showing top 20 of 51 predictions.*

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
