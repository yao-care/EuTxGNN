---
layout: default
title: Luspatercept
description: "Luspatercept drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 357
evidence_level: L5
indication_count: 52
---

# Luspatercept
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Luspatercept |
| DrugBank ID | [DB12281](https://go.drugbank.com/drugs/DB12281) |
| Brand Names (EU) | Reblozyl |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 96.32% |

---

## Approved Indication (EMA)

Reblozyl is indicated in adults for the treatment of transfusion-dependent anaemia due to very low, low and intermediate-risk myelodysplastic syndromes (MDS).Reblozyl is indicated in adults for the treatment of anaemia associated with transfusion dependent and non transfusion dependent beta thalassaemia.&nbsp; Reblozyl is indicated in adults for the treatment of transfusion-dependent anaemia due to very low, low and intermediate-risk myelodysplastic syndromes (MDS).Reblozyl is indicated in adult

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dominant beta-thalassemia | 96.32% | DL |
| 2 | monosomy X | 96.00% | DL |
| 3 | hepatic infarction | 95.70% | DL |
| 4 | hepatic veno-occlusive disease | 94.91% | DL |
| 5 | peliosis hepatis | 94.75% | DL |
| 6 | syndrome with combined immunodeficiency | 94.28% | DL |
| 7 | pyruvate kinase deficiency of red cells | 93.84% | DL |
| 8 | thalassemia, beta+, silent allele | 93.32% | DL |
| 9 | familial apolipoprotein C-II deficiency | 93.05% | DL |
| 10 | adenosine deaminase deficiency | 92.86% | DL |
| 11 | Hb Bart's hydrops fetalis | 92.75% | DL |
| 12 | beta-thalassemia with other manifestations | 92.61% | DL |
| 13 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 92.34% | DL |
| 14 | partial deletion of the short arm of chromosome 16 | 92.14% | DL |
| 15 | hemolytic anemia due to glucophosphate isomerase deficiency | 91.92% | DL |
| 16 | liver angiosarcoma | 91.84% | DL |
| 17 | pyropoikilocytosis, hereditary | 91.80% | DL |
| 18 | reticular dysgenesis | 91.66% | DL |
| 19 | beta thalassemia | 91.57% | DL |
| 20 | severe combined immunodeficiency due to LCK deficiency | 91.50% | DL |

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
