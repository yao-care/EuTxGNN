---
layout: default
title: Lefamulin Acetate
description: "Lefamulin Acetate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 336
evidence_level: L5
indication_count: 50
---

# Lefamulin Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lefamulin Acetate |
| DrugBank ID | [DB12825](https://go.drugbank.com/drugs/DB12825) |
| Brand Names (EU) | Xenleta |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.24% |

---

## Approved Indication (EMA)

Xenleta is indicated for the treatment of community-acquired pneumonia (CAP) in adults when it is considered inappropriate to use antibacterial agents that are commonly recommended for the initial treatment of CAP or when these have failed. Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | leishmaniasis, diffuse cutaneous | 99.24% | DL |
| 2 | hyperamylasemia | 99.10% | DL |
| 3 | polyclonal hyperviscosity syndrome | 99.10% | DL |
| 4 | congenital analbuminemia | 98.92% | DL |
| 5 | Mycoplasma pneumoniae pneumonia | 98.81% | DL |
| 6 | blood group incompatibility | 98.78% | DL |
| 7 | premalignant hematological system disease | 98.65% | DL |
| 8 | staphylococcus aureus pneumonia | 98.53% | DL |
| 9 | monoclonal gammopathy | 98.52% | DL |
| 10 | hematological disease associated with an acquired peripheral neuropathy | 98.43% | DL |
| 11 | streptococcal pneumonia | 98.41% | DL |
| 12 | Legionnaires' disease | 98.24% | DL |
| 13 | mucocutaneous leishmaniasis | 98.17% | DL |
| 14 | inhalational botulism | 98.14% | DL |
| 15 | septicemic plague | 98.14% | DL |
| 16 | Klebsiella pneumonia | 98.08% | DL |
| 17 | fascioliasis | 98.04% | DL |
| 18 | congenital hematological disorder | 98.00% | DL |
| 19 | endomyometritis | 97.97% | DL |
| 20 | Clostridium infectious disease | 97.92% | DL |

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
