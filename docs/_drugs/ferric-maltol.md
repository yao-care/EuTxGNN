---
layout: default
title: Ferric Maltol
description: "ferric maltol drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 242
evidence_level: L1
indication_count: 50
---

# Ferric Maltol
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ferric Maltol |
| DrugBank ID | [DB15598](https://go.drugbank.com/drugs/DB15598) |
| Brand Names (EU) | Feraccru |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Feraccru is indicated in adults for the treatment of iron deficiency.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | iron deficiency anemia | 100.00% | DL |
| 2 | deficiency anemia | 100.00% | DL |
| 3 | Plummer-Vinson syndrome | 99.98% | DL |
| 4 | vitamin B12- and folate-independent constitutional megaloblastic anemia | 99.98% | DL |
| 5 | microcytic anemia | 99.93% | DL |
| 6 | IRIDA syndrome | 99.33% | DL |
| 7 | biotin metabolic disease | 98.25% | DL |
| 8 | severe nonproliferative diabetic retinopathy | 98.08% | DL |
| 9 | ariboflavinosis | 97.72% | DL |
| 10 | Keshan disease | 97.22% | DL |
| 11 | non-syndromic esophageal malformation | 97.22% | DL |
| 12 | folic acid deficiency anemia | 97.21% | DL |
| 13 | protein-energy malnutrition | 97.19% | DL |
| 14 | choline deficiency disease | 97.13% | DL |
| 15 | swayback | 97.13% | DL |
| 16 | potassium deficiency | 97.13% | DL |
| 17 | magnesium deficiency | 97.06% | DL |
| 18 | steatitis | 97.04% | DL |
| 19 | vitamin deficiency disorder | 96.92% | DL |
| 20 | hypochromic anemia | 96.85% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| iron deficiency anemia | L1 | 16 | 15 | 7 Phase 3 trial(s), 4 RCT(s) |
| deficiency anemia | L1 | 16 | 15 | 7 Phase 3 trial(s), 4 RCT(s) |

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
