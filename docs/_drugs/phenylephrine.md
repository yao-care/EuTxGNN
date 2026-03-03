---
layout: default
title: Phenylephrine
description: "Phenylephrine drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 457
evidence_level: L5
indication_count: 52
---

# Phenylephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Phenylephrine |
| DrugBank ID | [DB00388](https://go.drugbank.com/drugs/DB00388) |
| Brand Names (EU) | Omidria, Phenylephrine |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Omidria is indicated in adults for maintenance of intraoperative mydriasis, prevention of intraoperative miosis and reduction of acute postoperative ocular pain in intraocular lens replacement surgery.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pharyngitis | 99.98% | DL |
| 2 | nasal cavity disease | 99.97% | DL |
| 3 | acute laryngopharyngitis | 99.97% | DL |
| 4 | common cold | 99.87% | DL |
| 5 | papillary conjunctivitis | 99.71% | DL |
| 6 | headache disorder | 99.44% | DL |
| 7 | trigeminal autonomic cephalalgia | 99.30% | DL |
| 8 | faucial diphtheria | 98.67% | DL |
| 9 | cervical disc degenerative disorder | 98.58% | DL |
| 10 | nasopharyngitis | 97.82% | DL |
| 11 | tracheal disease | 97.74% | DL |
| 12 | atopic conjunctivitis | 96.01% | DL |
| 13 | rosacea conjunctivitis | 95.68% | DL |
| 14 | allergic urticaria | 95.47% | DL |
| 15 | rhinitis | 95.36% | DL |
| 16 | bronchial disease | 93.86% | DL |
| 17 | endobronchial leiomyoma | 93.18% | DL |
| 18 | glossodynia | 93.01% | DL |
| 19 | endobronchial lipoma | 92.73% | DL |
| 20 | coccygodynia | 92.73% | DL |

*Showing top 20 of 52 predictions.*

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
