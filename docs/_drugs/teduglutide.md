---
layout: default
title: Teduglutide
description: "Teduglutide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 561
evidence_level: L5
indication_count: 50
---

# Teduglutide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Teduglutide |
| DrugBank ID | [DB08900](https://go.drugbank.com/drugs/DB08900) |
| Brand Names (EU) | Revestive |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.08% |

---

## Approved Indication (EMA)

Revestive is indicated for the treatment of patients aged 1 year and above with Short Bowel Syndrome (SBS). Patients should be stable following a period of intestinal adaptation after surgery. Revestive is indicated for the treatment of patients aged 1 year and above with Short Bowel Syndrome. Patients should be stable following a period of intestinal adaptation after surgery.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | short bowel syndrome | 99.08% | DL |
| 2 | papillary conjunctivitis | 98.53% | DL |
| 3 | gastroduodenitis | 98.22% | DL |
| 4 | peptic ulcer disease | 96.58% | DL |
| 5 | nasal cavity disease | 96.22% | DL |
| 6 | acute laryngopharyngitis | 95.22% | DL |
| 7 | allergic urticaria | 95.17% | DL |
| 8 | pharyngitis | 94.68% | DL |
| 9 | chronic intestinal vascular insufficiency | 92.22% | DL |
| 10 | isolated mesenteric vein thrombosis | 91.99% | DL |
| 11 | atopic conjunctivitis | 88.73% | DL |
| 12 | cold urticaria | 87.89% | DL |
| 13 | rosacea conjunctivitis | 87.48% | DL |
| 14 | ischemic bowel disease | 87.48% | DL |
| 15 | NK-cell enteropathy | 86.49% | DL |
| 16 | eosinophilic gastrointestinal disease | 86.46% | DL |
| 17 | intestinal atresia (disease) | 86.43% | DL |
| 18 | solitary rectal ulcer syndrome | 86.30% | DL |
| 19 | neurogenic bowel | 86.30% | DL |
| 20 | mucocele of appendix | 86.30% | DL |

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
