---
layout: default
title: Zanamivir
description: "Zanamivir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 643
evidence_level: L5
indication_count: 50
---

# Zanamivir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Zanamivir |
| DrugBank ID | [DB00558](https://go.drugbank.com/drugs/DB00558) |
| Brand Names (EU) | Dectova |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.84% |

---

## Approved Indication (EMA)

Dectova is indicated for the treatment of complicated and potentially life-threatening influenza A or B virus infection in adult and paediatric patients (aged ?6 months) when:  The patient’s influenza virus is known or suspected to be resistant to anti-influenza medicinal products other than zanamivir, and/or Other anti-viral medicinal products for treatment of influenza, including inhaled zanamivir, are not suitable for the individual patient.  Dectova should be used in accordance with official

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pyelonephritis | 99.84% | DL |
| 2 | influenza, severe, susceptibility to | 99.42% | DL |
| 3 | disorder of tyrosine metabolism | 99.02% | DL |
| 4 | teratogenic Pierre Robin syndrome | 98.94% | DL |
| 5 | disorder of phenylalanine metabolism | 98.86% | DL |
| 6 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 98.41% | DL |
| 7 | susceptibility to HIV infection | 98.40% | DL |
| 8 | dengue virus, susceptibility to | 98.40% | DL |
| 9 | legionnaire disease, susceptibility to | 98.40% | DL |
| 10 | aspergillosis, susceptibility to | 98.40% | DL |
| 11 | Schistosoma mansoni infection, susceptibility | 98.35% | DL |
| 12 | influenza | 98.17% | DL |
| 13 | cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency | 98.13% | DL |
| 14 | staphylococcus aureus infection | 97.91% | DL |
| 15 | pyogenic bacterial infections due to MyD88 deficiency | 97.83% | DL |
| 16 | acute hemorrhagic encephalitis | 97.78% | DL |
| 17 | acute necrotizing encephalitis | 97.76% | DL |
| 18 | HHV-6 encephalitis | 97.76% | DL |
| 19 | Hendra virus infection | 97.76% | DL |
| 20 | equine encephalitis | 97.64% | DL |

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
