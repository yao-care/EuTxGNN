---
layout: default
title: Eribulin
description: "Eribulin drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 222
evidence_level: L5
indication_count: 50
---

# Eribulin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eribulin |
| DrugBank ID | [DB08871](https://go.drugbank.com/drugs/DB08871) |
| Brand Names (EU) | Halaven |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.82% |

---

## Approved Indication (EMA)

Halaven monotherapy is indicated for the treatment of patients with locally advanced or metastatic breast cancer who have progressed after at least one chemotherapeutic regimens for advanced disease (see section 5.1). Prior therapy should have included an anthracycline and a taxane unless patients were not suitable for these treatments. Halaven is indicated for the treatment of adult patients with unresectable liposarcoma who have received prior anthracycline containing therapy (unless unsuitabl

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | autosomal recessive familial Mediterranean fever | 99.82% | DL |
| 2 | dermatofibrosarcoma protuberans | 99.66% | DL |
| 3 | pleural mesothelioma | 99.51% | DL |
| 4 | liposarcoma | 99.49% | DL |
| 5 | malignant peritoneal mesothelioma | 99.47% | DL |
| 6 | ovarian myxoid liposarcoma | 99.47% | DL |
| 7 | pleural adenomatoid tumor | 99.46% | DL |
| 8 | pleural biphasic mesothelioma | 99.37% | DL |
| 9 | fibroblastic neoplasm | 99.36% | DL |
| 10 | pleural epithelioid mesothelioma | 99.35% | DL |
| 11 | heart fibrosarcoma | 99.35% | DL |
| 12 | well differentiated papillary mesothelioma | 99.33% | DL |
| 13 | conventional fibrosarcoma | 99.32% | DL |
| 14 | pericardium cancer | 99.31% | DL |
| 15 | pleural sarcomatoid mesothelioma | 99.31% | DL |
| 16 | kidney fibrosarcoma | 99.29% | DL |
| 17 | lymphohistiocytoid mesothelioma | 99.29% | DL |
| 18 | low grade fibromyxoid sarcoma | 99.23% | DL |
| 19 | benign PEComa | 99.00% | DL |
| 20 | uterine corpus perivascular epithelioid cell tumor | 98.98% | DL |

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
