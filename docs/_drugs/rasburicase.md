---
layout: default
title: Rasburicase
description: "Rasburicase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 481
evidence_level: L5
indication_count: 50
---

# Rasburicase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rasburicase |
| DrugBank ID | [DB00049](https://go.drugbank.com/drugs/DB00049) |
| Brand Names (EU) | Fasturtec |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment and prophylaxis of acute hyperuricaemia, in order to prevent acute renal failure, in adults, children and adolescents (aged 0 to 17 years) with haematological malignancy with a high tumour burden and at risk of a rapid tumour lysis or shrinkage at initiation of chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | obsolete hyperuricemia (disease) | 99.99% | DL |
| 2 | hypouricemia, renal | 99.99% | DL |
| 3 | hypoxanthine guanine phosphoribosyltransferase partial deficiency | 99.97% | DL |
| 4 | hepatic porphyria | 99.97% | DL |
| 5 | primitive portal vein thrombosis | 99.97% | DL |
| 6 | hepatoportal sclerosis | 99.97% | DL |
| 7 | hepatopulmonary syndrome | 99.97% | DL |
| 8 | early-onset familial noncirrhotic portal hypertension | 99.97% | DL |
| 9 | idiopathic copper-associated cirrhosis | 99.97% | DL |
| 10 | renal tubular acidosis | 99.85% | DL |
| 11 | disorder of phenylalanine metabolism | 99.83% | DL |
| 12 | disorder of tyrosine metabolism | 99.69% | DL |
| 13 | teratogenic Pierre Robin syndrome | 99.68% | DL |
| 14 | glycogen storage disease due to hepatic glycogen synthase deficiency | 99.58% | DL |
| 15 | Lesch-Nyhan syndrome | 99.58% | DL |
| 16 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 99.47% | DL |
| 17 | G6PD deficiency | 99.00% | DL |
| 18 | inborn disorder of gamma-aminobutyric acid metabolism | 97.73% | DL |
| 19 | inborn disorder of ornithine metabolism | 97.68% | DL |
| 20 | inborn disorder of amino acid and other organic acid metabolism | 97.66% | DL |

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
