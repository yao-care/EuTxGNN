---
layout: default
title: Voretigene Neparvovec
description: "Voretigene Neparvovec drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 640
evidence_level: L5
indication_count: 50
---

# Voretigene Neparvovec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Voretigene Neparvovec |
| DrugBank ID | [DB13932](https://go.drugbank.com/drugs/DB13932) |
| Brand Names (EU) | Luxturna |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 56.42% |

---

## Approved Indication (EMA)

Luxturna is indicated for the treatment of adult and paediatric patients with vision loss due to inherited retinal dystrophy caused by confirmed biallelic RPE65 mutations and who have sufficient viable retinal cells.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | mitral valve prolapse, myxomatous | 56.42% | DL |
| 2 | pituitary dwarfism | 56.27% | DL |
| 3 | cystic hygroma | 55.80% | DL |
| 4 | conductive hearing loss disorder | 55.79% | DL |
| 5 | susceptibility to mononeuropathy of the median nerve, mild | 54.30% | DL |
| 6 | Wiskott-Aldrich syndrome 2 | 54.05% | DL |
| 7 | non-syndromic esophageal malformation | 53.99% | DL |
| 8 | hypermobility syndrome | 53.97% | DL |
| 9 | woolly hair, autosomal recessive 3 | 53.78% | DL |
| 10 | obsolete hypertension, diastolic, resistance to | 53.77% | DL |
| 11 | obsolete rare tumor of gallbladder and extrahepatic biliary tract | 53.70% | DL |
| 12 | isolated sedoheptulokinase deficiency | 53.55% | DL |
| 13 | ocular tuberculosis | 53.45% | DL |
| 14 | cornea plana 1, autosomal dominant | 53.37% | DL |
| 15 | musk, inability to smell | 53.37% | DL |
| 16 | polyhydramnios, chronic idiopathic | 53.37% | DL |
| 17 | childhood encephalopathy due to thiamine pyrophosphokinase deficiency | 53.24% | DL |
| 18 | hemifacial microsomia | 52.70% | DL |
| 19 | congenital insensitivity to pain-hypohidrosis syndrome | 52.65% | DL |
| 20 | corneal degeneration, band-shaped spheroid | 52.61% | DL |

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
