---
layout: default
title: Denosumab
description: "Denosumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 167
evidence_level: L5
indication_count: 52
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Denosumab |
| DrugBank ID | [DB06643](https://go.drugbank.com/drugs/DB06643) |
| Brand Names (EU) | Degevma, Vevzuo, Xbryk |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.63% |

---

## Approved Indication (EMA)

Prevention of skeletal related events (pathological fracture, radiation to bone, spinal cord compression or surgery to bone) in adults with advanced malignancies involving bone (see section 5.1). Treatment of adults and skeletally mature adolescents with giant cell tumour of bone that is unresectable or where surgical resection is likely to result in severe morbidity.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | severe nonproliferative diabetic retinopathy | 99.63% | DL |
| 2 | drug-induced osteoporosis | 99.36% | DL |
| 3 | diabetic retinopathy | 99.23% | DL |
| 4 | dermatitis | 97.25% | DL |
| 5 | diabetic cataract | 96.66% | DL |
| 6 | acrodermatitis chronica atrophicans | 96.23% | DL |
| 7 | neonatal dermatomyositis | 95.81% | DL |
| 8 | hydroa vacciniforme, familial | 95.20% | DL |
| 9 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 94.97% | DL |
| 10 | acne keloid | 94.78% | DL |
| 11 | amyopathic dermatomyositis | 94.67% | DL |
| 12 | nuclear senile cataract | 93.96% | DL |
| 13 | cortical cataract | 93.96% | DL |
| 14 | senile cataract | 93.78% | DL |
| 15 | craniostenosis cataract | 93.11% | DL |
| 16 | mature cataract | 93.11% | DL |
| 17 | tetanic cataract | 93.11% | DL |
| 18 | diabetes mellitus type 2 associated cataract | 93.11% | DL |
| 19 | immature cataract | 93.11% | DL |
| 20 | primary release disorder of platelets | 92.24% | DL |

*Showing top 20 of 52 predictions.*

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
