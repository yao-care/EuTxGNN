---
layout: default
title: Linagliptin
description: "Linagliptin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 345
evidence_level: L5
indication_count: 51
---

# Linagliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Linagliptin |
| DrugBank ID | [DB08882](https://go.drugbank.com/drugs/DB08882) |
| Brand Names (EU) | Jentadueto, Trajenta |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 94.90% |

---

## Approved Indication (EMA)

Trajenta is indicated in the treatment of type 2 diabetes mellitus to improve glycaemic control in adults: as monotherapy  in patients inadequately controlled by diet and exercise alone and for whom metformin is inappropriate due to intolerance, or contraindicated due to renal impairment.  as combination therapy  in combination with metformin when diet and exercise plus metformin alone do not provide adequate glycaemic control. in combination with a sulphonylurea and metformin when diet and exer

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opsismodysplasia | 94.90% | DL |
| 2 | thiamine-responsive dysfunction syndrome | 94.47% | DL |
| 3 | focal stiff limb syndrome | 94.23% | DL |
| 4 | classic stiff person syndrome | 94.23% | DL |
| 5 | diabetes mellitus (disease) | 94.09% | DL |
| 6 | drug-induced localized lipodystrophy | 91.75% | DL |
| 7 | centrifugal lipodystrophy | 91.45% | DL |
| 8 | pressure-induced localized lipoatrophy | 91.21% | DL |
| 9 | pancreatic agenesis | 91.18% | DL |
| 10 | idiopathic localized lipodystrophy | 90.84% | DL |
| 11 | homozygous familial hypercholesterolemia | 89.99% | DL |
| 12 | autoimmune oophoritis | 82.75% | DL |
| 13 | type 1 diabetes mellitus | 79.77% | DL |
| 14 | atrial flutter (disease) | 67.27% | DL |
| 15 | congenital temporomandibular joint ankylosis | 63.24% | DL |
| 16 | cholangiocarcinoma, susceptibility to | 62.78% | DL |
| 17 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 61.78% | DL |
| 18 | mitral valve prolapse, myxomatous | 60.80% | DL |
| 19 | hemoglobin C-beta-thalassemia syndrome | 60.41% | DL |
| 20 | polydipsia | 59.67% | DL |

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
