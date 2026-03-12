---
layout: default
title: Ketorolac
description: "Ketorolac drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 323
evidence_level: L5
indication_count: 50
---

# Ketorolac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ketorolac |
| DrugBank ID | [DB00465](https://go.drugbank.com/drugs/DB00465) |
| Brand Names (EU) | Ketorolac |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Omidria is indicated in adults for maintenance of intraoperative mydriasis, prevention of intraoperative miosis and reduction of acute postoperative ocular pain in intraocular lens replacement surgery.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | papillary conjunctivitis | 99.93% | DL |
| 2 | headache disorder | 99.43% | DL |
| 3 | atopic conjunctivitis | 99.41% | DL |
| 4 | rosacea conjunctivitis | 99.40% | DL |
| 5 | trigeminal autonomic cephalalgia | 99.39% | DL |
| 6 | ulcerative proctosigmoiditis | 98.98% | DL |
| 7 | nasopharyngitis | 97.94% | DL |
| 8 | cap polyposis | 97.88% | DL |
| 9 | cutaneous photosensitivity-lethal colitis syndrome | 97.82% | DL |
| 10 | undetermined colitis | 97.74% | DL |
| 11 | allergic urticaria | 97.14% | DL |
| 12 | viral conjunctivitis | 96.14% | DL |
| 13 | vernal conjunctivitis | 95.93% | DL |
| 14 | frozen shoulder | 95.86% | DL |
| 15 | systemic inflammatory disease associated with an acquired peripheral neuropathy | 95.35% | DL |
| 16 | fasciitis (disease) | 95.32% | DL |
| 17 | glossodynia | 95.14% | DL |
| 18 | osteoarthritis susceptibility | 95.12% | DL |
| 19 | coccygodynia | 94.95% | DL |
| 20 | punctate epithelial keratoconjunctivitis | 94.90% | DL |

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
