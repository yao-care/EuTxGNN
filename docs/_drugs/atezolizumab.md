---
layout: default
title: Atezolizumab
description: "atezolizumab drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 54
evidence_level: L2
indication_count: 50
---

# Atezolizumab
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Atezolizumab |
| DrugBank ID | [DB11595](https://go.drugbank.com/drugs/DB11595) |
| Brand Names (EU) | Tecentriq |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Urothelial carcinoma&nbsp;Tecentriq as monotherapy is indicated for the treatment of adult patients with locally advanced or metastatic urothelial carcinoma (UC):  after prior platinum containing chemotherapy, or who are considered cisplatin ineligible, and whose tumours have a PD-L1 expression ≥ 5% (see section 5.1).  Early-stage non-small cell lung cancer (NSCLC)&nbsp;Tecentriq as monotherapy is indicated as adjuvant treatment following complete resection and platinum-based chemotherapy for ad

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
| 6 | uterine ligament adenocarcinoma | 99.93% | DL |
| 7 | endocervical carcinoma | 99.92% | DL |
| 8 | adenoid cystic carcinoma of the cervix uteri | 99.92% | DL |
| 9 | uterine ligament serous adenocarcinoma | 99.92% | DL |
| 10 | signet ring cell variant cervical mucinous adenocarcinoma | 99.91% | DL |
| 11 | intestinal variant cervical mucinous adenocarcinoma | 99.91% | DL |
| 12 | uterine ligament mucinous adenocarcinoma | 99.91% | DL |
| 13 | uterine ligament endometrioid adenocarcinoma | 99.91% | DL |
| 14 | cervical adenosquamous carcinoma, glassy cell variant | 99.91% | DL |
| 15 | endocervical type cervical mucinous adenocarcinoma | 99.91% | DL |
| 16 | cervical mucinous adenocarcinoma, minimal deviation variant | 99.91% | DL |
| 17 | uterine ligament clear cell adenocarcinoma | 99.91% | DL |
| 18 | nasopharyngeal teratoma | 99.86% | DL |
| 19 | odontogenic cyst | 99.86% | DL |
| 20 | epiglottis neoplasm | 99.86% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| transitional cell carcinoma | L2 | 20 | 4 | 2 Phase 3 trial(s), 8 Phase 2 trial(s), 1 review(s |
| prostatic urethra urothelial carcinoma | L3 | 2 | 0 | 1 Phase 2 trial(s) |
| renal pelvis papillary urothelial carcinoma | L4 | 1 | 0 | AI prediction only |

---

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
