---
layout: default
title: Cemiplimab
description: "Cemiplimab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 125
evidence_level: L5
indication_count: 50
---

# Cemiplimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cemiplimab |
| DrugBank ID | [DB14707](https://go.drugbank.com/drugs/DB14707) |
| Brand Names (EU) | Libtayo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Cutaneous Squamous Cell Carcinoma  Libtayo as monotherapy is indicated for the treatment of adult patients with metastatic or locally advanced cutaneous squamous cell carcinoma (mCSCC or laCSCC) who are not candidates for curative surgery or curative radiation. Libtayo as monotherapy is indicated for the adjuvant treatment of adult patients with CSCC at high risk of recurrence after surgery and radiation (see section 5.1 for selection criteria).&nbsp;  Basal Cell Carcinoma  Libtayo as monotherap

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | gallbladder adenosquamous carcinoma | 99.99% | DL |
| 2 | glottis squamous cell carcinoma | 99.99% | DL |
| 3 | rectal cloacogenic carcinoma | 99.99% | DL |
| 4 | external ear basal cell carcinoma | 99.99% | DL |
| 5 | adenosquamous prostate carcinoma | 99.99% | DL |
| 6 | urethral verrucous carcinoma | 99.99% | DL |
| 7 | lung occult squamous cell carcinoma | 99.99% | DL |
| 8 | pancreatic adenosquamous carcinoma | 99.99% | DL |
| 9 | non-keratinizing sinonasal squamous cell carcinoma | 99.99% | DL |
| 10 | supraglottis squamous cell carcinoma | 99.99% | DL |
| 11 | larynx verrucous carcinoma | 99.99% | DL |
| 12 | spindle cell variant squamous cell breast carcinoma | 99.99% | DL |
| 13 | non-small cell squamous lung carcinoma | 99.99% | DL |
| 14 | cervical adenosquamous carcinoma | 99.99% | DL |
| 15 | adenosquamous breast carcinoma | 99.99% | DL |
| 16 | acantholytic variant squamous cell breast carcinoma | 99.99% | DL |
| 17 | esophagus verrucous carcinoma | 99.99% | DL |
| 18 | maxillary sinus carcinoma | 99.99% | DL |
| 19 | carcinoma of lip | 99.99% | DL |
| 20 | lacrimal gland carcinoma | 99.99% | DL |

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
