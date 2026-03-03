---
layout: default
title: Deferasirox
description: "Deferasirox drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 162
evidence_level: L5
indication_count: 53
---

# Deferasirox
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Deferasirox |
| DrugBank ID | [DB01609](https://go.drugbank.com/drugs/DB01609) |
| Brand Names (EU) | Deferasirox Accord, Deferasirox Mylan |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.40% |

---

## Approved Indication (EMA)

Deferasirox Mylan is indicated for  the treatment of chronic iron overload due to frequent blood transfusions (?7 ml/kg/month of packed red blood cells) in patients with beta thalassaemia major aged 6 years and older the treatment of chronic iron overload due to blood transfusions when deferoxamine therapy is contraindicated or inadequate in the following patient groups:  in paediatric patients with beta thalassaemia major with iron overload due to frequent blood transfusions (?7 ml/kg/month of 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 99.40% | DL |
| 2 | chronic hepatitis C virus infection | 99.39% | DL |
| 3 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.23% | DL |
| 4 | obsolete familial combined hyperlipidemia | 99.20% | DL |
| 5 | dermatofibrosarcoma protuberans | 99.11% | DL |
| 6 | feline acquired immunodeficiency syndrome | 98.96% | DL |
| 7 | simian immunodeficiency virus infection | 98.96% | DL |
| 8 | beta-thalassemia with other manifestations | 98.59% | DL |
| 9 | pyropoikilocytosis, hereditary | 98.55% | DL |
| 10 | pyruvate kinase deficiency of red cells | 98.50% | DL |
| 11 | hemoglobinopathy | 98.50% | DL |
| 12 | sitosterolemia | 98.48% | DL |
| 13 | Plasmodium falciparum malaria | 98.47% | DL |
| 14 | homozygous familial hypercholesterolemia | 98.33% | DL |
| 15 | partial deletion of the short arm of chromosome 16 | 98.26% | DL |
| 16 | hemolytic anemia due to glucophosphate isomerase deficiency | 98.24% | DL |
| 17 | gout | 97.16% | DL |
| 18 | fibroblastic neoplasm | 97.10% | DL |
| 19 | hepatitis B virus infection | 97.09% | DL |
| 20 | conventional fibrosarcoma | 96.98% | DL |

*Showing top 20 of 53 predictions.*

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
