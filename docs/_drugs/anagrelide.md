---
layout: default
title: Anagrelide
description: "Anagrelide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 37
evidence_level: L5
indication_count: 50
---

# Anagrelide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Anagrelide |
| DrugBank ID | [DB00261](https://go.drugbank.com/drugs/DB00261) |
| Brand Names (EU) | Xagrid |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Xagrid is indicated for the reduction of elevated platelet counts in at-risk essential-thrombocythaemia (ET) patients who are intolerant to their current therapy or whose elevated platelet counts are not reduced to an acceptable level by their current therapy. An at-risk patient An at-risk ET is defined by one or more of the following features:  &gt;60 years of age or; a platelet count &gt;1000 x 109/l or; a history of thrombohaemorrhagic events.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | familial thrombocytosis | 99.89% | DL |
| 2 | reactive thrombocytosis | 99.83% | DL |
| 3 | inverse Klippel-Trenaunay syndrome | 99.59% | DL |
| 4 | thrombocythemia | 99.52% | DL |
| 5 | dermatofibrosarcoma protuberans | 98.91% | DL |
| 6 | rheumatoid arthritis | 98.86% | DL |
| 7 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 98.50% | DL |
| 8 | juvenile idiopathic arthritis | 98.48% | DL |
| 9 | osteoarthritis | 98.45% | DL |
| 10 | pseudoachondroplasia | 98.45% | DL |
| 11 | rheumatoid nodulosis | 98.14% | DL |
| 12 | juvenile chronic polyarthritis | 98.12% | DL |
| 13 | osteoarthritis susceptibility | 97.83% | DL |
| 14 | brachydactyly-syndactyly syndrome | 97.81% | DL |
| 15 | acromesomelic dysplasia, Hunter-Thompson type | 97.50% | DL |
| 16 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.50% | DL |
| 17 | juvenile arthritis due to defect in LACC1 | 97.35% | DL |
| 18 | myosclerosis | 97.25% | DL |
| 19 | brachyolmia-amelogenesis imperfecta syndrome | 97.14% | DL |
| 20 | brachyolmia | 97.05% | DL |

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
