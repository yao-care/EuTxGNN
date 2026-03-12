---
layout: default
title: Tezacaftor
description: "Tezacaftor drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 574
evidence_level: L5
indication_count: 50
---

# Tezacaftor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tezacaftor |
| DrugBank ID | [DB11712](https://go.drugbank.com/drugs/DB11712) |
| Brand Names (EU) | Tezacaftor |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.24% |

---

## Approved Indication (EMA)

Kaftrio tablets are indicated in a combination regimen with ivacaftor for the treatment of cystic fibrosis (CF) in patients aged 6 years and older who have at least one non-Class I mutation in the cystic fibrosis transmembrane conductance regulator (CFTR) gene. Kaftrio granules are indicated in a combination regimen with ivacaftor for the treatment of cystic fibrosis (CF) in paediatric patients aged 2 to less than 6 years who have at least one non-Class I mutation in the cystic fibrosis transmem

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.24% | DL |
| 2 | leprosy | 99.14% | DL |
| 3 | multiple endocrine neoplasia | 99.06% | DL |
| 4 | simian immunodeficiency virus infection | 98.96% | DL |
| 5 | feline acquired immunodeficiency syndrome | 98.96% | DL |
| 6 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.85% | DL |
| 7 | rheumatoid arthritis | 98.65% | DL |
| 8 | female breast carcinoma | 98.39% | DL |
| 9 | homozygous familial hypercholesterolemia | 98.37% | DL |
| 10 | amyotrophic lateral sclerosis | 98.35% | DL |
| 11 | thrombocytopenia | 98.35% | DL |
| 12 | hereditary thrombocytopenia with normal platelets | 98.08% | DL |
| 13 | marcothrombocytopenia with mitral valve insufficiency | 98.07% | DL |
| 14 | brachydactyly-syndactyly syndrome | 98.05% | DL |
| 15 | transient neonatal thrombocytopenia | 98.02% | DL |
| 16 | oral candidiasis | 97.92% | DL |
| 17 | collagenopathy | 97.90% | DL |
| 18 | dense granule disease | 97.88% | DL |
| 19 | Mills syndrome | 97.88% | DL |
| 20 | amyotrohpic lateral sclerosis type 22 | 97.87% | DL |

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
