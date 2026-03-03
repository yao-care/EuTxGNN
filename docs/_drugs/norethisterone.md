---
layout: default
title: Norethisterone
description: "Norethisterone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 412
evidence_level: L5
indication_count: 50
---

# Norethisterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Norethisterone |
| DrugBank ID | [DB00717](https://go.drugbank.com/drugs/DB00717) |
| Brand Names (EU) | Norethisterone |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

See EMA product information

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acne (disease) | 99.96% | DL |
| 2 | amenorrhea (disease) | 99.60% | DL |
| 3 | symptomatic form of fragile X syndrome in female carrier | 96.95% | DL |
| 4 | zinc, elevated plasma | 96.93% | DL |
| 5 | anovulation | 96.63% | DL |
| 6 | ovarian remnant syndrome | 96.63% | DL |
| 7 | primary ovarian failure | 96.54% | DL |
| 8 | partial trisomy/tetrasomy of the short arm of chromosome 18 | 96.49% | DL |
| 9 | partial trisomy/tetrasomy of the short arm of chromosome 12 | 96.45% | DL |
| 10 | luteoma of pregnancy | 96.43% | DL |
| 11 | blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome | 96.38% | DL |
| 12 | partial trisomy/tetrasomy of the short arm of chromosome 5 | 96.34% | DL |
| 13 | partial autosomal trisomy/tetrasomy | 96.31% | DL |
| 14 | ovarian ectopic pregnancy | 96.20% | DL |
| 15 | ovarian dysfunction | 96.07% | DL |
| 16 | stapes ankylosis with broad thumbs and toes | 96.07% | DL |
| 17 | blepharophimosis-epicanthus inversus-ptosis | 95.99% | DL |
| 18 | telecanthus | 95.43% | DL |
| 19 | urethral obstruction sequence | 94.80% | DL |
| 20 | ovarian hyperstimulation syndrome | 94.52% | DL |

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
