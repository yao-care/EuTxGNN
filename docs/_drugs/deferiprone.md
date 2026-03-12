---
layout: default
title: Deferiprone
description: "Deferiprone drug repurposing predictions from TxGNN. Evidence level L5 with 56 predicted indications."
parent: AI Predictions (L5)
nav_order: 163
evidence_level: L5
indication_count: 56
---

# Deferiprone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **56**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Deferiprone |
| DrugBank ID | [DB08826](https://go.drugbank.com/drugs/DB08826) |
| Brand Names (EU) | Deferiprone Lipomed, Ferriprox |
| Evidence Level | L5 |
| Predicted Indications | 56 |
| Top Prediction Score | 99.20% |

---

## Approved Indication (EMA)

Deferiprone Lipomed monotherapy is indicated for the treatment of iron overload in patients with thalassaemia major when current chelation therapy is contraindicated or inadequate. Deferiprone Lipomed in combination with another chelator is indicated in patients with thalassaemia major when monotherapy with any iron chelator is ineffective, or when prevention or treatment of life-threatening consequences of iron overload justifies rapid or intensive correction.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hepatic porphyria | 99.20% | DL |
| 2 | hepatopulmonary syndrome | 99.20% | DL |
| 3 | primitive portal vein thrombosis | 99.20% | DL |
| 4 | early-onset familial noncirrhotic portal hypertension | 99.20% | DL |
| 5 | hepatoportal sclerosis | 99.20% | DL |
| 6 | idiopathic copper-associated cirrhosis | 99.20% | DL |
| 7 | hemoglobinopathy | 99.16% | DL |
| 8 | pyruvate kinase deficiency of red cells | 99.15% | DL |
| 9 | beta-thalassemia with other manifestations | 99.03% | DL |
| 10 | pyropoikilocytosis, hereditary | 99.02% | DL |
| 11 | partial deletion of the short arm of chromosome 16 | 98.92% | DL |
| 12 | hemolytic anemia due to glucophosphate isomerase deficiency | 98.79% | DL |
| 13 | chronic hepatitis C virus infection | 98.44% | DL |
| 14 | obsolete familial combined hyperlipidemia | 97.16% | DL |
| 15 | HIV infectious disease | 96.66% | DL |
| 16 | familial hyperlipidemia | 96.50% | DL |
| 17 | homozygous familial hypercholesterolemia | 96.42% | DL |
| 18 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 96.20% | DL |
| 19 | paratenonitis | 96.03% | DL |
| 20 | calcific tendinitis | 95.95% | DL |

*Showing top 20 of 56 predictions.*

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
