---
layout: default
title: Oseltamivir
description: "Oseltamivir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 426
evidence_level: L5
indication_count: 50
---

# Oseltamivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Oseltamivir |
| DrugBank ID | [DB00198](https://go.drugbank.com/drugs/DB00198) |
| Brand Names (EU) | Tamiflu |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.72% |

---

## Approved Indication (EMA)

Treatment of influenza Tamiflu is indicated in adults and children including full term neonates who present with symptoms typical of influenza, when influenza virus is circulating in the community. Efficacy has been demonstrated when treatment is initiated within two days of first onset of symptoms.Prevention of influenza  Post-exposure prevention in individuals one year of age or older following contact with a clinically diagnosed influenza case when influenza virus is circulating in the commun

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | influenza, severe, susceptibility to | 98.72% | DL |
| 2 | pyelonephritis | 97.85% | DL |
| 3 | disorder of tyrosine metabolism | 96.69% | DL |
| 4 | teratogenic Pierre Robin syndrome | 96.12% | DL |
| 5 | disorder of phenylalanine metabolism | 95.74% | DL |
| 6 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 95.10% | DL |
| 7 | staphylococcus aureus infection | 95.05% | DL |
| 8 | cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency | 93.93% | DL |
| 9 | pneumonia | 92.14% | DL |
| 10 | influenza | 90.74% | DL |
| 11 | streptococcal pneumonia | 90.46% | DL |
| 12 | aspergillosis, susceptibility to | 89.78% | DL |
| 13 | dengue virus, susceptibility to | 89.78% | DL |
| 14 | susceptibility to HIV infection | 89.78% | DL |
| 15 | legionnaire disease, susceptibility to | 89.78% | DL |
| 16 | Schistosoma mansoni infection, susceptibility | 89.50% | DL |
| 17 | primitive portal vein thrombosis | 88.90% | DL |
| 18 | early-onset familial noncirrhotic portal hypertension | 88.90% | DL |
| 19 | hepatopulmonary syndrome | 88.90% | DL |
| 20 | idiopathic copper-associated cirrhosis | 88.90% | DL |

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
