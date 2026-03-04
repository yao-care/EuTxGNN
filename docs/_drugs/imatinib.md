---
layout: default
title: Imatinib
description: "imatinib drug repurposing predictions from TxGNN. Evidence level L2 with 56 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 293
evidence_level: L2
indication_count: 56
---

# Imatinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **56**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Imatinib |
| DrugBank ID | [DB00619](https://go.drugbank.com/drugs/DB00619) |
| Brand Names (EU) | Glivec, Imatinib Accord, Imatinib Teva |
| Evidence Level | L2 |
| Predicted Indications | 56 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Imatinib Teva is indicated for the treatment of  Adult and paediatric patients with newly diagnosed Philadelphia chromosome (bcr?abl) positive (Ph+) chronic myeloid leukaemia (CML) for whom bone marrow transplantation is not considered as the first line of treatment. Adult and paediatric patients with Ph+ CML in chronic phase after failure of interferon?alpha therapy, or in accelerated phase or blast crisis. Adult and paediatric patients with newly diagnosed Philadelphia chromosome positive acut

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatofibrosarcoma protuberans | 99.99% | DL |
| 2 | heart fibrosarcoma | 99.94% | DL |
| 3 | fibroblastic neoplasm | 99.94% | DL |
| 4 | conventional fibrosarcoma | 99.93% | DL |
| 5 | kidney fibrosarcoma | 99.93% | DL |
| 6 | low grade fibromyxoid sarcoma | 99.93% | DL |
| 7 | liposarcoma | 99.88% | DL |
| 8 | liver fibrosarcoma | 99.86% | DL |
| 9 | autosomal recessive familial Mediterranean fever | 99.86% | DL |
| 10 | ovarian myxoid liposarcoma | 99.85% | DL |
| 11 | familial rhabdoid tumor | 99.83% | DL |
| 12 | benign PEComa | 99.81% | DL |
| 13 | uterine corpus perivascular epithelioid cell tumor | 99.81% | DL |
| 14 | lymphangiomyoma | 99.80% | DL |
| 15 | lymphangioleiomyomatosis | 99.77% | DL |
| 16 | bone fibrosarcoma | 99.75% | DL |
| 17 | cutaneous undifferentiated pleomorphic sarcoma | 99.74% | DL |
| 18 | cutaneous leiomyosarcoma (disease) | 99.73% | DL |
| 19 | central nervous system fibrosarcoma | 99.72% | DL |
| 20 | vulva sarcoma | 99.67% | DL |

*Showing top 20 of 56 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| dermatofibrosarcoma protuberans | L2 | 9 | 20 | 7 Phase 2 trial(s), 2 review(s)/meta-analysis |

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
