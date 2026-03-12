---
layout: default
title: Cholic Acid
description: "Cholic Acid drug repurposing predictions from TxGNN. Evidence level L5 with 56 predicted indications."
parent: AI Predictions (L5)
nav_order: 133
evidence_level: L5
indication_count: 56
---

# Cholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **56**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cholic Acid |
| DrugBank ID | [DB02659](https://go.drugbank.com/drugs/DB02659) |
| Brand Names (EU) | Orphacol |
| Evidence Level | L5 |
| Predicted Indications | 56 |
| Top Prediction Score | 99.89% |

---

## Approved Indication (EMA)

Orphacol is indicated for the treatment of inborn errors in primary bile acid synthesis due to3β-Hydroxy-Δ5-C27-steroid oxidoreductase deficiency or Δ4-3-Oxosteroid-5β-reductase deficiency ininfants, children and adolescents aged 1 month to 18 years and adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | cholelithiasis | 99.89% | DL |
| 2 | HIV infectious disease | 99.79% | DL |
| 3 | obsolete familial combined hyperlipidemia | 99.78% | DL |
| 4 | homozygous familial hypercholesterolemia | 99.75% | DL |
| 5 | biotin metabolic disease | 99.74% | DL |
| 6 | vitamin deficiency disorder | 99.71% | DL |
| 7 | hereditary hemochromatosis | 99.69% | DL |
| 8 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.66% | DL |
| 9 | hemosiderosis | 99.65% | DL |
| 10 | disorder of phenylalanine metabolism | 99.61% | DL |
| 11 | bone Paget disease | 99.60% | DL |
| 12 | inborn error of biotin metabolism | 99.56% | DL |
| 13 | feline acquired immunodeficiency syndrome | 99.56% | DL |
| 14 | simian immunodeficiency virus infection | 99.56% | DL |
| 15 | obsolete rare hereditary hemochromatosis | 99.52% | DL |
| 16 | hyperphenylalaninemia due to tetrahydrobiopterin deficiency | 99.51% | DL |
| 17 | inborn disorder of pyridoxine metabolism | 99.46% | DL |
| 18 | Wilson disease | 99.44% | DL |
| 19 | constitutional megaloblastic anemia due to folate metabolism disorder | 99.43% | DL |
| 20 | cerebral folate deficiency | 99.42% | DL |

*Showing top 20 of 56 predictions.*

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
