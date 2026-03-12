---
layout: default
title: Florbetapir (18F)
description: "Florbetapir (18F) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 249
evidence_level: L5
indication_count: 50
---

# Florbetapir (18F)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Florbetapir (18F) |
| DrugBank ID | [DB09149](https://go.drugbank.com/drugs/DB09149) |
| Brand Names (EU) | Amyvid |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.66% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only. Amyvid is a radiopharmaceutical indicated for Positron Emission Tomography (PET) imaging of ?-amyloid neuritic plaque density in the brains of adult patients with cognitive impairment who are being evaluated for Alzheimer’s disease (AD) and other causes of cognitive impairment. Amyvid should be used in conjunction with a clinical evaluation. A negative scan indicates sparse or no plaques, which is not consistent with a diagnosis of AD.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 99.66% | DL |
| 2 | rheumatoid arthritis | 98.24% | DL |
| 3 | bronchial neoplasm (disease) | 96.86% | DL |
| 4 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.85% | DL |
| 5 | brachydactyly-syndactyly syndrome | 95.93% | DL |
| 6 | gout | 95.92% | DL |
| 7 | headache disorder | 95.68% | DL |
| 8 | trigeminal autonomic cephalalgia | 95.64% | DL |
| 9 | laryngotracheitis | 95.54% | DL |
| 10 | osteoarthritis susceptibility | 95.53% | DL |
| 11 | obstructive lung disease | 95.52% | DL |
| 12 | heparin cofactor 2 deficiency | 94.98% | DL |
| 13 | Ledderhose disease | 94.85% | DL |
| 14 | factor 5 excess with spontaneous thrombosis | 94.70% | DL |
| 15 | antithrombin deficiency type 2 | 94.67% | DL |
| 16 | dermatitis | 94.65% | DL |
| 17 | penile fibromatosis | 94.39% | DL |
| 18 | infantile digital fibromatosis | 93.76% | DL |
| 19 | palmar fibromatosis | 93.63% | DL |
| 20 | hydroa vacciniforme, familial | 93.50% | DL |

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
