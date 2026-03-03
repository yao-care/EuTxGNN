---
layout: default
title: Bedaquiline Fumarate
description: "Bedaquiline Fumarate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 72
evidence_level: L5
indication_count: 50
---

# Bedaquiline Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bedaquiline Fumarate |
| DrugBank ID | [DB08903](https://go.drugbank.com/drugs/DB08903) |
| Brand Names (EU) | Sirturo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

&nbsp;Sirturo is indicated for use as part of an appropriate combination regimen in adult and paediatric patients (2 years to less than 18 years of age and weighing at least 7 kg) with pulmonary tuberculosis (TB) due to Mycobacterium tuberculosis resistant to at least rifampicin and isoniazid. Consideration should be given to official guidance on the appropriate use of antibacterial agents. &nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multidrug-resistant tuberculosis | 99.98% | DL |
| 2 | tuberculosis, bovine | 99.96% | DL |
| 3 | tuberculoma | 99.96% | DL |
| 4 | tuberculous ascites | 99.96% | DL |
| 5 | inactive tuberculosis | 99.96% | DL |
| 6 | tuberculosis, avian | 99.96% | DL |
| 7 | vulvovaginal candidiasis | 99.88% | DL |
| 8 | fascioliasis | 99.88% | DL |
| 9 | urea cycle disorder | 99.78% | DL |
| 10 | cutaneous tuberculosis | 99.70% | DL |
| 11 | esophageal candidiasis | 99.68% | DL |
| 12 | inhalational botulism | 99.66% | DL |
| 13 | helminthiasis, animal | 99.64% | DL |
| 14 | necatoriasis | 99.63% | DL |
| 15 | hymenolepiasis | 99.63% | DL |
| 16 | paragonimiasis | 99.63% | DL |
| 17 | echinostomiasis | 99.63% | DL |
| 18 | fascioloidiasis | 99.63% | DL |
| 19 | monieziasis | 99.63% | DL |
| 20 | fasciolopsiasis | 99.63% | DL |

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
