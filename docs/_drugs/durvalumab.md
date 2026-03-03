---
layout: default
title: Durvalumab
description: "Durvalumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 189
evidence_level: L5
indication_count: 50
---

# Durvalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Durvalumab |
| DrugBank ID | [DB11714](https://go.drugbank.com/drugs/DB11714) |
| Brand Names (EU) | Imfinzi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Non-Small Cell Lung Cancer (NSCLC)IMFINZI in combination with platinum-based chemotherapy as neoadjuvant treatment, followed by IMFINZI as monotherapy as adjuvant treatment, is indicated for the treatment of adults with resectable NSCLC at high risk of recurrence and no EGFR mutations or ALK rearrangements (for selection criteria, see section 5.1). IMFINZI as monotherapy is indicated for the treatment of locally advanced, unresectable non small cell lung cancer (NSCLC) in adults whose tumours ex

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | prostatic urethra urothelial carcinoma | 99.98% | DL |
| 2 | kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | DL |
| 3 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 99.98% | DL |
| 4 | renal pelvis papillary urothelial carcinoma | 99.98% | DL |
| 5 | transitional cell carcinoma | 99.97% | DL |
| 6 | uterine ligament adenocarcinoma | 99.92% | DL |
| 7 | endocervical carcinoma | 99.91% | DL |
| 8 | adenoid cystic carcinoma of the cervix uteri | 99.91% | DL |
| 9 | uterine ligament serous adenocarcinoma | 99.91% | DL |
| 10 | signet ring cell variant cervical mucinous adenocarcinoma | 99.90% | DL |
| 11 | intestinal variant cervical mucinous adenocarcinoma | 99.90% | DL |
| 12 | uterine ligament mucinous adenocarcinoma | 99.90% | DL |
| 13 | uterine ligament endometrioid adenocarcinoma | 99.90% | DL |
| 14 | cervical adenosquamous carcinoma, glassy cell variant | 99.90% | DL |
| 15 | endocervical type cervical mucinous adenocarcinoma | 99.90% | DL |
| 16 | cervical mucinous adenocarcinoma, minimal deviation variant | 99.90% | DL |
| 17 | uterine ligament clear cell adenocarcinoma | 99.89% | DL |
| 18 | nasopharyngeal teratoma | 99.84% | DL |
| 19 | odontogenic cyst | 99.84% | DL |
| 20 | epiglottis neoplasm | 99.84% | DL |

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
