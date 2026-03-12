---
layout: default
title: Evolocumab
description: "Evolocumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 234
evidence_level: L5
indication_count: 51
---

# Evolocumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Evolocumab |
| DrugBank ID | [DB09303](https://go.drugbank.com/drugs/DB09303) |
| Brand Names (EU) | Repatha |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

Hypercholesterolaemia and mixed dyslipidaemia Repatha is indicated in adults with primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia, as an adjunct to diet:  in combination with a statin or statin with other lipid lowering therapies in patients unable to reach LDL-C goals with the maximum tolerated dose of a statin or, alone or in combination with other lipid-lowering therapies in patients who are statin-intolerant, or for whom a statin is contraindicat

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | symptomatic form of hemophilia in female carriers | 99.82% | DL |
| 2 | familial apolipoprotein C-II deficiency | 99.50% | DL |
| 3 | thrombocytopenic purpura | 99.42% | DL |
| 4 | factor XI deficiency | 99.29% | DL |
| 5 | hemophilia A with vascular abnormality | 99.22% | DL |
| 6 | disease of catalytic activity | 99.08% | DL |
| 7 | hemorrhagic disease of newborn | 98.89% | DL |
| 8 | ichthyosis, X-linked, without steroid sulfatase deficiency | 98.84% | DL |
| 9 | inherited thrombophilia | 98.82% | DL |
| 10 | disorder of other vitamins and cofactors metabolism and transport | 98.80% | DL |
| 11 | adenosine deaminase deficiency | 98.80% | DL |
| 12 | xanthomatosis (disease) | 98.78% | DL |
| 13 | esophageal varices without bleeding | 98.75% | DL |
| 14 | esophageal varices with bleeding | 98.75% | DL |
| 15 | 46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | 98.73% | DL |
| 16 | 3-hydroxyacyl-CoA dehydrogenase deficiency | 98.70% | DL |
| 17 | cholesterol catabolic process disease | 98.66% | DL |
| 18 | coagulation protein disease | 98.66% | DL |
| 19 | 46,XY disorder of sex development due to a cholesterol synthesis defect | 98.64% | DL |
| 20 | neutral lipid storage disease | 98.56% | DL |

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
