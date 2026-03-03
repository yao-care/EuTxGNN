---
layout: default
title: Degarelix
description: "Degarelix drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 165
evidence_level: L5
indication_count: 50
---

# Degarelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Degarelix |
| DrugBank ID | [DB06699](https://go.drugbank.com/drugs/DB06699) |
| Brand Names (EU) | Firmagon |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

FIRMAGON is a gonadotrophin releasing hormone (GnRH) antagonist indicated: - for treatment of adult male patients with advanced hormone-dependent prostate cancer. - for treatment of high-risk localised and locally advanced hormone dependent prostate cancer in combination with radiotherapy. - as neo-adjuvant treatment prior to radiotherapy in patients with high-risk localised or locally advanced hormone dependent prostate cancer.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypertrichosis (disease) | 99.99% | DL |
| 2 | Ambras type hypertrichosis universalis congenita | 99.98% | DL |
| 3 | syndrome with a Dandy-Walker malformation as major feature | 99.98% | DL |
| 4 | malformation syndrome with odontal and/or periodontal component | 99.98% | DL |
| 5 | isolated genetic hair shaft abnormality | 99.98% | DL |
| 6 | allergic urticaria | 99.97% | DL |
| 7 | cold urticaria | 99.86% | DL |
| 8 | familial male-limited precocious puberty | 99.84% | DL |
| 9 | centra precocious puberty 1 | 99.67% | DL |
| 10 | familial isolated trichomegaly | 99.65% | DL |
| 11 | precocious puberty | 99.63% | DL |
| 12 | Plasmodium falciparum malaria | 99.52% | DL |
| 13 | nephrogenic syndrome of inappropriate antidiuresis | 99.48% | DL |
| 14 | aromatase excess syndrome | 99.47% | DL |
| 15 | IgE responsiveness, atopic | 99.29% | DL |
| 16 | recalcitrant atopic dermatitis | 99.12% | DL |
| 17 | subarachnoid hemorrhage (disease) | 99.09% | DL |
| 18 | renal-hepatic-pancreatic dysplasia | 99.04% | DL |
| 19 | thoracic malformation | 98.98% | DL |
| 20 | adult familial nephronophthisis-spastic quadriparesia syndrome | 98.98% | DL |

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
