---
layout: default
title: Eflornithine
description: "Eflornithine drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 193
evidence_level: L5
indication_count: 51
---

# Eflornithine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eflornithine |
| DrugBank ID | [DB06243](https://go.drugbank.com/drugs/DB06243) |
| Brand Names (EU) | Vaniqa |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.85% |

---

## Approved Indication (EMA)

Treatment of facial hirsutism in women.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | esotropia | 99.85% | DL |
| 2 | neurotrophic keratopathy | 99.38% | DL |
| 3 | congenital analbuminemia | 98.89% | DL |
| 4 | hyperamylasemia | 98.75% | DL |
| 5 | polyclonal hyperviscosity syndrome | 98.75% | DL |
| 6 | human African trypanosomiasis | 98.63% | DL |
| 7 | trypanosomiasis, bovine | 98.42% | DL |
| 8 | blood group incompatibility | 98.36% | DL |
| 9 | monoclonal gammopathy | 98.18% | DL |
| 10 | premalignant hematological system disease | 98.10% | DL |
| 11 | congenital prothrombin deficiency | 98.02% | DL |
| 12 | metabolic disease associated with ocular features | 98.00% | DL |
| 13 | congenital hematological disorder | 97.91% | DL |
| 14 | nutritional biotin deficiency | 97.87% | DL |
| 15 | bullous impetigo | 97.77% | DL |
| 16 | hematological disease associated with an acquired peripheral neuropathy | 97.72% | DL |
| 17 | reticular dysgenesis | 97.67% | DL |
| 18 | lung fibrosis-immunodeficiency-46,XX gonadal dysgenesis syndrome | 97.38% | DL |
| 19 | Immunoerythromyeloid hypoplasia | 97.24% | DL |
| 20 | adenosine deaminase deficiency | 97.12% | DL |

*Showing top 20 of 51 predictions.*

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
