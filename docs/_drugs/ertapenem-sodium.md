---
layout: default
title: Ertapenem Sodium
description: "Ertapenem Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 224
evidence_level: L5
indication_count: 50
---

# Ertapenem Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ertapenem Sodium |
| DrugBank ID | [DB00303](https://go.drugbank.com/drugs/DB00303) |
| Brand Names (EU) | Ertapenem SUN |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.72% |

---

## Approved Indication (EMA)

Treatment Ertapenem SUN is indicated in paediatric patients (3 months to 17 years of age) and in adults for the treatment of the following infections when caused by bacteria known or very likely to be susceptible to ertapenem and when parenteral therapy is required (see sections 4.4 and 5.1):  Intra-abdominal infections Community acquired pneumonia Acute gynaecological infections Diabetic foot infections of the skin and soft tissue (see section 4.4)  Prevention Ertapenem SUN is indicated in adul

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bacterial arthritis | 99.72% | DL |
| 2 | staphylococcus aureus infection | 99.28% | DL |
| 3 | Peptostreptococcus infectious disease | 99.23% | DL |
| 4 | streptococcal pneumonia | 99.00% | DL |
| 5 | hyperamylasemia | 98.75% | DL |
| 6 | polyclonal hyperviscosity syndrome | 98.75% | DL |
| 7 | congenital analbuminemia | 98.54% | DL |
| 8 | toxocariasis | 98.44% | DL |
| 9 | urinary tract infection (disease) | 98.34% | DL |
| 10 | blood group incompatibility | 98.26% | DL |
| 11 | gonococcal urethritis | 98.13% | DL |
| 12 | Ureaplasma urethritis | 98.13% | DL |
| 13 | Lyme disease | 98.12% | DL |
| 14 | premalignant hematological system disease | 98.08% | DL |
| 15 | infectious otitis media | 97.92% | DL |
| 16 | toxascariasis | 97.89% | DL |
| 17 | anisakiasis | 97.88% | DL |
| 18 | monoclonal gammopathy | 97.84% | DL |
| 19 | hematological disease associated with an acquired peripheral neuropathy | 97.76% | DL |
| 20 | chronic otitis media | 97.67% | DL |

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
