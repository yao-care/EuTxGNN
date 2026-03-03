---
layout: default
title: Tigecycline
description: "Tigecycline drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 580
evidence_level: L5
indication_count: 50
---

# Tigecycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tigecycline |
| DrugBank ID | [DB00560](https://go.drugbank.com/drugs/DB00560) |
| Brand Names (EU) | Tigecycline Accord |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.76% |

---

## Approved Indication (EMA)

Tygecycline Accord is indicated in adults and in children from the age of eight years for the treatment of the following infections (see sections 4.4 and 5.1):  Complicated skin and soft tissue infections (cSSTI), excluding diabetic foot infections (see section 4.4) Complicated intra-abdominal infections (cIAI)  Tygecycline Accord should be used only in situations where other alternative antibiotics are not suitable (see sections 4.4, 4.8 and 5.1). Consideration should be given to official guida

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | disorder of tyrosine metabolism | 95.76% | DL |
| 2 | teratogenic Pierre Robin syndrome | 95.33% | DL |
| 3 | tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria | 94.91% | DL |
| 4 | disorder of phenylalanine metabolism | 93.60% | DL |
| 5 | hyperamylasemia | 93.55% | DL |
| 6 | polyclonal hyperviscosity syndrome | 93.55% | DL |
| 7 | congenital analbuminemia | 92.84% | DL |
| 8 | blood group incompatibility | 91.94% | DL |
| 9 | premalignant hematological system disease | 91.75% | DL |
| 10 | monoclonal gammopathy | 90.87% | DL |
| 11 | hematological disease associated with an acquired peripheral neuropathy | 90.25% | DL |
| 12 | pyelonephritis | 90.05% | DL |
| 13 | congenital hematological disorder | 89.02% | DL |
| 14 | septicemic plague | 88.14% | DL |
| 15 | streptococcal pneumonia | 88.04% | DL |
| 16 | neonatal epileptic encephalopathy due to glutaminase deficiency | 84.90% | DL |
| 17 | semicircular canal dehiscence syndrome | 84.79% | DL |
| 18 | idiopathic bilateral vestibulopathy | 84.79% | DL |
| 19 | genetic otorhinolaryngological malformation | 84.65% | DL |
| 20 | inborn disorder of phenylalanin or tyrosine metabolism | 84.48% | DL |

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
