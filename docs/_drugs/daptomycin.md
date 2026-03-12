---
layout: default
title: Daptomycin
description: "Daptomycin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 153
evidence_level: L5
indication_count: 50
---

# Daptomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Daptomycin |
| DrugBank ID | [DB00080](https://go.drugbank.com/drugs/DB00080) |
| Brand Names (EU) | Cubicin |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.86% |

---

## Approved Indication (EMA)

Cubicin is indicated for the treatment of the following infections.  Adult and paediatric (1 to 17 years of age) patients with complicated skin and soft-tissue infections (cSSTI). Adult patients with right-sided infective endocarditis (RIE) due to Staphylococcus aureus.  It is recommended that the decision to use daptomycin should take into account the antibacterial susceptibility of the organism and should be based on expert advice.  Adult and paediatric (1 to 17 years of age) patients with Sta

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | osteoarthritis | 99.86% | DL |
| 2 | rheumatoid arthritis | 99.84% | DL |
| 3 | osteoarthritis susceptibility | 99.79% | DL |
| 4 | gout | 99.79% | DL |
| 5 | pseudoachondroplasia | 99.75% | DL |
| 6 | acromesomelic dysplasia, Hunter-Thompson type | 99.68% | DL |
| 7 | brachyolmia | 99.67% | DL |
| 8 | brachydactyly-syndactyly syndrome | 99.62% | DL |
| 9 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.61% | DL |
| 10 | brachyolmia-amelogenesis imperfecta syndrome | 99.61% | DL |
| 11 | myosclerosis | 99.61% | DL |
| 12 | arthropathy | 99.57% | DL |
| 13 | congestive heart failure | 99.49% | DL |
| 14 | acute pulmonary heart disease | 99.36% | DL |
| 15 | chronic pulmonary heart disease | 99.30% | DL |
| 16 | pulmonary hypertension owing to lung disease and/or hypoxia | 99.26% | DL |
| 17 | pulmonary hypertension with unclear multifactorial mechanism | 99.26% | DL |
| 18 | malignant hypertensive renal disease | 99.25% | DL |
| 19 | malignant renovascular hypertension | 99.25% | DL |
| 20 | hypertensive disorder | 99.24% | DL |

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
