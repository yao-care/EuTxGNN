---
layout: default
title: Tedizolid
description: "Tedizolid drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 560
evidence_level: L5
indication_count: 50
---

# Tedizolid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tedizolid |
| DrugBank ID | [DB14569](https://go.drugbank.com/drugs/DB14569) |
| Brand Names (EU) | Sivextro |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.94% |

---

## Approved Indication (EMA)

Sivextro tablets are indicated for the treatment of acute bacterial skin and skin structure infections (ABSSSI) in adults, adolescents and children weighing at least 35 kg.Consideration should be given to official guidance on the appropriate use of antibacterial agents. Sivextro powder for concentrate for solution for infusion is indicated for the treatment of acute bacterial skin and skin structure infections (ABSSSI) from birth. Consideration should be given to official guidance on the appropr

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | orofacial clefting syndrome | 93.94% | DL |
| 2 | interventricular septum aneurysm | 93.87% | DL |
| 3 | bronchitis | 93.87% | DL |
| 4 | Jeune syndrome situs inversus | 93.72% | DL |
| 5 | Pierre Robin syndrome associated with a chromosomal anomaly | 93.63% | DL |
| 6 | Laubry-Pezzi syndrome | 93.57% | DL |
| 7 | genetic syndromic Pierre Robin syndrome | 93.54% | DL |
| 8 | disorder of fucoglycosan synthesis | 93.50% | DL |
| 9 | partial deletion of the long arm of chromosome 7 | 93.49% | DL |
| 10 | partial deletion of the long arm of chromosome 22 | 93.32% | DL |
| 11 | pulmonary valve disease | 93.29% | DL |
| 12 | mitral valve disease | 92.61% | DL |
| 13 | heart disease | 91.21% | DL |
| 14 | heart neoplasm | 83.57% | DL |
| 15 | epiglottitis | 82.78% | DL |
| 16 | conjunctivitis | 81.74% | DL |
| 17 | heart conduction disease | 81.38% | DL |
| 18 | congenital anomaly of ventricular septum | 80.96% | DL |
| 19 | bronchial neoplasm (disease) | 80.96% | DL |
| 20 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 78.96% | DL |

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
