---
layout: default
title: Nitisinone
description: "Nitisinone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 406
evidence_level: L5
indication_count: 50
---

# Nitisinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nitisinone |
| DrugBank ID | [DB00348](https://go.drugbank.com/drugs/DB00348) |
| Brand Names (EU) | Nityr |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Treatment of adult and paediatric patients with confirmed diagnosis of hereditary tyrosinemia type 1 (HT-1) in combination with dietary restriction of tyrosine and phenylalanine.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | renal tubular acidosis | 99.96% | DL |
| 2 | galactosemia | 99.95% | DL |
| 3 | serpinopathy with toxic serpin polymerization | 99.90% | DL |
| 4 | C1 inhibitor deficiency | 99.90% | DL |
| 5 | glycogen storage disease | 99.89% | DL |
| 6 | adult polyglucosan body disease | 99.88% | DL |
| 7 | glycogen storage disease due to glucose-6-phosphatase deficiency | 99.87% | DL |
| 8 | Griscelli syndrome | 99.87% | DL |
| 9 | granulomatous disease, chronic, X-linked | 99.87% | DL |
| 10 | ermine phenotype | 99.87% | DL |
| 11 | ocular albinism (disease) | 99.86% | DL |
| 12 | piebaldism | 99.86% | DL |
| 13 | ocular albinism with sensorineural deafness | 99.86% | DL |
| 14 | anemia, nonspherocytic hemolytic, due to G6PD deficiency | 99.85% | DL |
| 15 | cold agglutinin disease | 99.85% | DL |
| 16 | primary CD59 deficiency | 99.85% | DL |
| 17 | hemolytic anemia due to diphosphoglycerate mutase deficiency | 99.85% | DL |
| 18 | cholelithiasis | 99.84% | DL |
| 19 | albinism | 99.84% | DL |
| 20 | classic galactosemia | 99.84% | DL |

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
