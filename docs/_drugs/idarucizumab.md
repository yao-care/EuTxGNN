---
layout: default
title: Idarucizumab
description: "Idarucizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 288
evidence_level: L5
indication_count: 50
---

# Idarucizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Idarucizumab |
| DrugBank ID | [DB09264](https://go.drugbank.com/drugs/DB09264) |
| Brand Names (EU) | Praxbind |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.66% |

---

## Approved Indication (EMA)

Praxbind is a specific reversal agent for dabigatran and is indicated in adult patients treated with Pradaxa (dabigatran etexilate) when rapid reversal of its anticoagulant effects is required:  for emergency surgery/urgent procedures; in life-threatening or uncontrolled bleeding.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hemoglobinopathy | 95.66% | DL |
| 2 | rheumatoid arthritis | 95.52% | DL |
| 3 | partial deletion of the short arm of chromosome 16 | 95.00% | DL |
| 4 | beta-thalassemia with other manifestations | 94.98% | DL |
| 5 | pyruvate kinase deficiency of red cells | 94.82% | DL |
| 6 | hemolytic anemia due to glucophosphate isomerase deficiency | 94.56% | DL |
| 7 | pyropoikilocytosis, hereditary | 94.26% | DL |
| 8 | bronchitis | 94.09% | DL |
| 9 | gout | 93.75% | DL |
| 10 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 93.62% | DL |
| 11 | osteoarthritis | 93.49% | DL |
| 12 | antithrombin deficiency type 2 | 92.76% | DL |
| 13 | osteoarthritis susceptibility | 92.71% | DL |
| 14 | heparin cofactor 2 deficiency | 92.67% | DL |
| 15 | factor 5 excess with spontaneous thrombosis | 92.55% | DL |
| 16 | brachydactyly-syndactyly syndrome | 92.21% | DL |
| 17 | pseudoachondroplasia | 91.53% | DL |
| 18 | thrombophilia | 91.36% | DL |
| 19 | hepatic porphyria | 90.95% | DL |
| 20 | myocardial infarction | 90.84% | DL |

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
