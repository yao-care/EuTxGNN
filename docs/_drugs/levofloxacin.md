---
layout: default
title: Levofloxacin
description: "Levofloxacin drug repurposing predictions from TxGNN. Evidence level L5 with 60 predicted indications."
parent: AI Predictions (L5)
nav_order: 342
evidence_level: L5
indication_count: 60
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **60**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Levofloxacin |
| DrugBank ID | [DB01137](https://go.drugbank.com/drugs/DB01137) |
| Brand Names (EU) | Quinsair |
| Evidence Level | L5 |
| Predicted Indications | 60 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Quinsair is indicated for the management of chronic pulmonary infections due to Pseudomonas aeruginosa in adult patients with cystic fibrosis. Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | punctate epithelial keratoconjunctivitis | 99.92% | DL |
| 2 | polyclonal hyperviscosity syndrome | 99.90% | DL |
| 3 | hyperamylasemia | 99.90% | DL |
| 4 | congenital analbuminemia | 99.89% | DL |
| 5 | blood group incompatibility | 99.85% | DL |
| 6 | premalignant hematological system disease | 99.83% | DL |
| 7 | monoclonal gammopathy | 99.81% | DL |
| 8 | hematological disease associated with an acquired peripheral neuropathy | 99.80% | DL |
| 9 | septicemic plague | 99.80% | DL |
| 10 | congenital hematological disorder | 99.72% | DL |
| 11 | conjunctivitis | 99.71% | DL |
| 12 | post-infectious syndrome | 99.69% | DL |
| 13 | postinfectious vasculitis | 99.68% | DL |
| 14 | otitis externa | 99.68% | DL |
| 15 | post-bacterial disorder | 99.68% | DL |
| 16 | infective urethral stricture | 99.66% | DL |
| 17 | infection-related hemolytic uremic syndrome | 99.65% | DL |
| 18 | Chagas cardiomyopathy | 99.65% | DL |
| 19 | exposure keratitis | 99.62% | DL |
| 20 | bronchitis | 99.42% | DL |

*Showing top 20 of 60 predictions.*

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
