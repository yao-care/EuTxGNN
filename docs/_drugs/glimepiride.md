---
layout: default
title: Glimepiride
description: "Glimepiride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 270
evidence_level: L5
indication_count: 50
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glimepiride |
| DrugBank ID | [DB00222](https://go.drugbank.com/drugs/DB00222) |
| Brand Names (EU) | Glimepiride |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.77% |

---

## Approved Indication (EMA)

Tandemact is indicated for the treatment of patients with type-2 diabetes mellitus who show intolerance to metformin or for whom metformin is contraindicated and who are already treated with a combination of pioglitazone and glimepiride.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | diabetes mellitus (disease) | 99.77% | DL |
| 2 | classic stiff person syndrome | 99.75% | DL |
| 3 | focal stiff limb syndrome | 99.75% | DL |
| 4 | opsismodysplasia | 99.74% | DL |
| 5 | thiamine-responsive dysfunction syndrome | 99.73% | DL |
| 6 | drug-induced localized lipodystrophy | 99.62% | DL |
| 7 | centrifugal lipodystrophy | 99.60% | DL |
| 8 | pressure-induced localized lipoatrophy | 99.59% | DL |
| 9 | idiopathic localized lipodystrophy | 99.56% | DL |
| 10 | pancreatic agenesis | 99.55% | DL |
| 11 | type 1 diabetes mellitus | 98.86% | DL |
| 12 | autoimmune oophoritis | 98.80% | DL |
| 13 | diabetes mellitus, insulin-dependent, X-linked, susceptibility to | 92.43% | DL |
| 14 | homozygous familial hypercholesterolemia | 92.26% | DL |
| 15 | permanent neonatal diabetes mellitus | 82.39% | DL |
| 16 | type 2 diabetes mellitus | 79.07% | DL |
| 17 | IDDM 1 | 77.93% | DL |
| 18 | hypotrichosis simplex of the scalp | 71.43% | DL |
| 19 | congenital hypotrichosis milia | 64.99% | DL |
| 20 | cholangiocarcinoma, susceptibility to | 63.33% | DL |

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
