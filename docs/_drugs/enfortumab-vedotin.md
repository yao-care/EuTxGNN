---
layout: default
title: Enfortumab Vedotin
description: "Enfortumab Vedotin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 209
evidence_level: L5
indication_count: 50
---

# Enfortumab Vedotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Enfortumab Vedotin |
| DrugBank ID | [DB13007](https://go.drugbank.com/drugs/DB13007) |
| Brand Names (EU) | Padcev |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.53% |

---

## Approved Indication (EMA)

Padcev, in combination with pembrolizumab, is indicated for the first-line treatment of adult patients with unresectable or metastatic urothelial cancer who are eligible for platinum-containing chemotherapy.&nbsp; Padcev as monotherapy is indicated for the treatment of adult patients with locally advanced or metastatic urothelial cancer who have previously received a platinum-containing chemotherapy and a programmed death receptor 1 or programmed death ligand 1 inhibitor.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | leprosy | 99.53% | DL |
| 2 | multiple endocrine neoplasia | 99.43% | DL |
| 3 | cytomegalovirus infection | 99.36% | DL |
| 4 | candidiasis | 99.30% | DL |
| 5 | cerebral infarction | 99.23% | DL |
| 6 | HIV infectious disease | 99.19% | DL |
| 7 | homozygous familial hypercholesterolemia | 99.18% | DL |
| 8 | malignant catarrh | 99.13% | DL |
| 9 | infectious bovine rhinotracheitis | 99.13% | DL |
| 10 | HER2 positive breast carcinoma | 98.99% | DL |
| 11 | feline acquired immunodeficiency syndrome | 98.93% | DL |
| 12 | simian immunodeficiency virus infection | 98.93% | DL |
| 13 | Prinzmetal angina | 98.91% | DL |
| 14 | oral candidiasis | 98.91% | DL |
| 15 | cerebral arterial disease | 98.90% | DL |
| 16 | coronary artery disease | 98.88% | DL |
| 17 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.71% | DL |
| 18 | breast fibrocystic disease | 98.65% | DL |
| 19 | commissural lip fistula | 98.59% | DL |
| 20 | osteoradionecrosis of the mandible | 98.58% | DL |

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
