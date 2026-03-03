---
layout: default
title: Velaglucerase Alfa
description: "Velaglucerase Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 625
evidence_level: L5
indication_count: 50
---

# Velaglucerase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Velaglucerase Alfa |
| DrugBank ID | [DB06720](https://go.drugbank.com/drugs/DB06720) |
| Brand Names (EU) | Vpriv |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.99% |

---

## Approved Indication (EMA)

Vpriv is indicated for long-term enzyme-replacement therapy (ERT) in patients with type-1 Gaucher disease.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Steel syndrome | 96.99% | DL |
| 2 | esophageal varices with bleeding | 96.20% | DL |
| 3 | esophageal varices without bleeding | 96.20% | DL |
| 4 | hypophosphatasia | 95.04% | DL |
| 5 | Gaucher disease | 94.16% | DL |
| 6 | Wolman disease with hypolipoproteinemia and acanthocytosis | 93.99% | DL |
| 7 | autosomal ichthyosis syndrome with fatal disease course | 93.74% | DL |
| 8 | cholesteryl ester storage disease | 92.90% | DL |
| 9 | varicose disease | 92.70% | DL |
| 10 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 92.08% | DL |
| 11 | proximal myopathy with extrapyramidal signs | 92.06% | DL |
| 12 | reticular dysgenesis | 91.64% | DL |
| 13 | familial apolipoprotein C-II deficiency | 91.05% | DL |
| 14 | Charcot-Marie-Tooth disease | 90.61% | DL |
| 15 | skeletal muscle disease | 90.29% | DL |
| 16 | Wolman disease | 89.83% | DL |
| 17 | congenital Horner syndrome (disease) | 89.63% | DL |
| 18 | ptosis-vocal cord paralysis syndrome | 89.34% | DL |
| 19 | ptosis-strabismus-ectopic pupils syndrome | 89.07% | DL |
| 20 | congenital entropion | 88.71% | DL |

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
