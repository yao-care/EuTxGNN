---
layout: default
title: Pasireotide
description: "Pasireotide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 441
evidence_level: L5
indication_count: 50
---

# Pasireotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pasireotide |
| DrugBank ID | [DB06663](https://go.drugbank.com/drugs/DB06663) |
| Brand Names (EU) | Signifor |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 96.83% |

---

## Approved Indication (EMA)

Signifor is indicated for the treatment of adult patients with Cushing’s disease for whom surgery is not an option or for whom surgery has failed. Signifor is indicated for the treatment of adult patients with acromegaly for whom surgery is not an option or has not been curative and who are inadequately controlled on treatment with another somatostatin analogue.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | adrenal gland hyperfunction | 96.83% | DL |
| 2 | nephrogenic syndrome of inappropriate antidiuresis | 96.12% | DL |
| 3 | Ambras type hypertrichosis universalis congenita | 93.83% | DL |
| 4 | malformation syndrome with odontal and/or periodontal component | 93.62% | DL |
| 5 | syndrome with a Dandy-Walker malformation as major feature | 93.25% | DL |
| 6 | hypertrichosis (disease) | 93.22% | DL |
| 7 | carbamoyl phosphate synthetase I deficiency disease | 92.92% | DL |
| 8 | isolated genetic hair shaft abnormality | 92.82% | DL |
| 9 | hyperargininemia | 89.75% | DL |
| 10 | tinea nigra | 89.74% | DL |
| 11 | duodenal obstruction | 89.03% | DL |
| 12 | duodenogastric reflux | 86.42% | DL |
| 13 | duodenal ulcer (disease) | 84.27% | DL |
| 14 | cranioectodermal dysplasia | 79.17% | DL |
| 15 | RHYNS syndrome | 78.93% | DL |
| 16 | renal tubule disease | 77.21% | DL |
| 17 | Senior-Boichis syndrome | 77.21% | DL |
| 18 | candidiasis | 76.18% | DL |
| 19 | nephrogenic diabetes insipidus | 75.65% | DL |
| 20 | epulis | 75.59% | DL |

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
