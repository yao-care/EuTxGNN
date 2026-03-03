---
layout: default
title: Anakinra
description: "Anakinra drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 38
evidence_level: L5
indication_count: 52
---

# Anakinra
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Anakinra |
| DrugBank ID | [DB00026](https://go.drugbank.com/drugs/DB00026) |
| Brand Names (EU) | Kineret |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Rheumatoid Arthritis (RA) Kineret is indicated in adults for the treatment of the signs and symptoms of RA in combination with methotrexate, with an inadequate response to methotrexate alone. COVID-19 Kineret is indicated for the treatment of coronavirus disease 2019 (COVID-19) in adult patients with pneumonia requiring supplemental oxygen (low- or high-flow oxygen) who are at risk of progressing to severe respiratory failure determined by plasma concentration of soluble urokinase plasminogen ac

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | extracutaneous mastocytoma | 99.93% | DL |
| 2 | hepatic infarction | 99.89% | DL |
| 3 | autosomal recessive familial Mediterranean fever | 99.89% | DL |
| 4 | aggressive systemic mastocytosis | 99.88% | DL |
| 5 | hepatic veno-occlusive disease | 99.88% | DL |
| 6 | peliosis hepatis | 99.85% | DL |
| 7 | oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies | 99.85% | DL |
| 8 | oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies | 99.85% | DL |
| 9 | pyogenic autoinflammatory syndrome | 99.83% | DL |
| 10 | unclassified autoinflammatory syndrome | 99.81% | DL |
| 11 | granulomatous autoinflammatory syndrome | 99.78% | DL |
| 12 | syndrome with combined immunodeficiency | 99.71% | DL |
| 13 | liver angiosarcoma | 99.64% | DL |
| 14 | mastocytosis | 99.63% | DL |
| 15 | Kimura disease | 99.62% | DL |
| 16 | indolent systemic mastocytosis | 99.61% | DL |
| 17 | bilateral parasagittal parieto-occipital polymicrogyria | 99.59% | DL |
| 18 | familial Mediterranean fever, autosomal dominant | 99.54% | DL |
| 19 | hepatic veno-occlusive disease-immunodeficiency syndrome | 99.53% | DL |
| 20 | amyotrophic lateral sclerosis | 99.53% | DL |

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
