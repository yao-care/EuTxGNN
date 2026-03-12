---
layout: default
title: Baloxavir Marboxil
description: "Baloxavir Marboxil drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 68
evidence_level: L5
indication_count: 50
---

# Baloxavir Marboxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Baloxavir Marboxil |
| DrugBank ID | [DB13997](https://go.drugbank.com/drugs/DB13997) |
| Brand Names (EU) | Xofluza |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.56% |

---

## Approved Indication (EMA)

Treatment of influenza Xofluza is indicated for the treatment of uncomplicated influenza in patients aged 1 year and above. Post exposure prophylaxis of influenza Xofluza is indicated for post-exposure prophylaxis of influenza in individuals aged 1 year and above. Xofluza should be used in accordance with official recommendations.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | influenza, severe, susceptibility to | 99.56% | DL |
| 2 | acquired hemophagocytic lymphohistiocytosis associated with malignant disease | 98.85% | DL |
| 3 | hemophagocytic syndrome associated with an infection | 98.85% | DL |
| 4 | influenza | 98.65% | DL |
| 5 | cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency | 98.55% | DL |
| 6 | Singleton-Merten syndrome | 97.81% | DL |
| 7 | hemophagocytic syndrome | 94.97% | DL |
| 8 | chronic hepatitis C virus infection | 94.95% | DL |
| 9 | hepatitis C virus infection | 93.26% | DL |
| 10 | hepatitis E virus infection | 92.53% | DL |
| 11 | hepatitis A virus infection | 92.42% | DL |
| 12 | Omsk hemorrhagic fever | 92.00% | DL |
| 13 | Kyasanur forest disease | 91.81% | DL |
| 14 | hepatitis, viral, animal | 91.63% | DL |
| 15 | hepatitis B virus infection | 89.74% | DL |
| 16 | pyelonephritis | 87.98% | DL |
| 17 | squamous cell lung carcinoma | 84.97% | DL |
| 18 | mendelian susceptibility to mycobacterial diseases due to complete ISG15 deficiency | 84.13% | DL |
| 19 | A20 haploinsufficiency | 82.74% | DL |
| 20 | immune dysregulation with inflammatory bowel disease | 82.07% | DL |

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
