---
layout: default
title: Idebenone
description: "Idebenone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 289
evidence_level: L5
indication_count: 50
---

# Idebenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Idebenone |
| DrugBank ID | [DB09081](https://go.drugbank.com/drugs/DB09081) |
| Brand Names (EU) | Raxone |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Raxone is indicated for the treatment of visual impairment in adolescent and adult patients with Leber’s Hereditary Optic Neuropathy (LHON).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hepatic porphyria | 99.92% | DL |
| 2 | hepatoportal sclerosis | 99.92% | DL |
| 3 | idiopathic copper-associated cirrhosis | 99.92% | DL |
| 4 | hepatopulmonary syndrome | 99.92% | DL |
| 5 | early-onset familial noncirrhotic portal hypertension | 99.92% | DL |
| 6 | primitive portal vein thrombosis | 99.92% | DL |
| 7 | immune-mediated necrotizing myopathy | 99.76% | DL |
| 8 | osteogenesis imperfecta-retinopathy-seizures-intellectual disability syndrome | 99.75% | DL |
| 9 | antisynthetase syndrome | 99.75% | DL |
| 10 | focal myositis | 99.74% | DL |
| 11 | maternally-inherited mitochondrial myopathy | 99.73% | DL |
| 12 | primary optic atrophy | 99.72% | DL |
| 13 | idiopathic eosinophilic myositis | 99.70% | DL |
| 14 | inflammatory myopathy with abundant macrophages | 99.70% | DL |
| 15 | maternally-inherited mitochondrial dystonia | 99.70% | DL |
| 16 | maternally-inherited Leigh syndrome | 99.63% | DL |
| 17 | Leber hereditary optic neuropathy | 99.54% | DL |
| 18 | juvenile nasopharyngeal angiofibroma (disease) | 99.47% | DL |
| 19 | familial nasal acilia | 99.47% | DL |
| 20 | silent sinus syndrome | 99.45% | DL |

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
