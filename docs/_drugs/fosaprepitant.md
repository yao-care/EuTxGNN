---
layout: default
title: Fosaprepitant
description: "Fosaprepitant drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 255
evidence_level: L5
indication_count: 50
---

# Fosaprepitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fosaprepitant |
| DrugBank ID | [DB06717](https://go.drugbank.com/drugs/DB06717) |
| Brand Names (EU) | Ivemend |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Prevention of nausea and vomiting associated with highly and moderately emetogenic cancer chemotherapy in adults and paediatric patients aged 6 months and older. Ivemend 150 mg is given as part of a combination therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.92% | DL |
| 2 | pneumocystosis | 99.87% | DL |
| 3 | leprosy | 99.82% | DL |
| 4 | Cryptococcal meningitis | 99.79% | DL |
| 5 | multiple endocrine neoplasia | 99.76% | DL |
| 6 | intracranial abscess | 99.75% | DL |
| 7 | retinitis | 99.68% | DL |
| 8 | Plasmodium falciparum malaria | 99.64% | DL |
| 9 | echinococcus granulosus infectious disease | 99.50% | DL |
| 10 | hyperargininemia | 99.41% | DL |
| 11 | hypertrichosis (disease) | 99.41% | DL |
| 12 | cysticercosis | 99.41% | DL |
| 13 | acute neonatal citrullinemia type I | 99.30% | DL |
| 14 | adult-onset citrullinemia type I | 99.30% | DL |
| 15 | malaria | 99.25% | DL |
| 16 | persistent Mullerian duct syndrome | 99.25% | DL |
| 17 | HIV infectious disease | 99.19% | DL |
| 18 | syndrome with a Dandy-Walker malformation as major feature | 99.16% | DL |
| 19 | motor nerve neuritis | 99.15% | DL |
| 20 | malformation syndrome with odontal and/or periodontal component | 99.15% | DL |

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
