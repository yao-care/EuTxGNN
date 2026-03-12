---
layout: default
title: Leflunomide
description: "leflunomide drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 337
evidence_level: L5
indication_count: 51
---

# Leflunomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Leflunomide |
| DrugBank ID | [DB01097](https://go.drugbank.com/drugs/DB01097) |
| Brand Names (EU) | Arava, Leflunomide medac |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Leflunomide is indicated for the treatment of adult patients with:  active rheumatoid arthritis as a 'disease-modifying antirheumatic drug' (DMARD); active psoriatic arthritis.  Recent or concurrent treatment with hepatotoxic or haematotoxic DMARDs (e.g. methotrexate) may result in an increased risk of serious adverse reactions; therefore, the initiation of leflunomide treatment has to be carefully considered regarding these benefit / risk aspects. Moreover, switching from leflunomide to another

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.97% | DL |
| 2 | brachydactyly-syndactyly syndrome | 99.93% | DL |
| 3 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.93% | DL |
| 4 | indolent plasma cell myeloma | 95.47% | DL |
| 5 | plasma cell myeloma | 95.16% | DL |
| 6 | myeloid leukemia | 92.99% | DL |
| 7 | Meester-Loeys syndrome | 86.55% | DL |
| 8 | ganglioneuroblastoma (disease) | 76.30% | DL |
| 9 | WHIM syndrome | 75.88% | DL |
| 10 | scalp dermatosis | 73.87% | DL |
| 11 | vertebral anomalies and variable endocrine and T-cell dysfunction | 72.25% | DL |
| 12 | retroperitoneal neoplasm | 71.43% | DL |
| 13 | obsolete susceptibility to ischemic stroke | 70.51% | DL |
| 14 | neuroblastoma | 64.84% | DL |
| 15 | gout | 63.94% | DL |
| 16 | polydipsia | 62.14% | DL |
| 17 | congenital temporomandibular joint ankylosis | 61.70% | DL |
| 18 | cholangiocarcinoma, susceptibility to | 60.31% | DL |
| 19 | anuria | 59.24% | DL |
| 20 | osteoarthritis susceptibility | 57.89% | DL |

*Showing top 20 of 51 predictions.*

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
