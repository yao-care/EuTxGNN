---
layout: default
title: Lapatinib
description: "Lapatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 328
evidence_level: L5
indication_count: 50
---

# Lapatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lapatinib |
| DrugBank ID | [DB01259](https://go.drugbank.com/drugs/DB01259) |
| Brand Names (EU) | Tyverb |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.30% |

---

## Approved Indication (EMA)

Tyverb is indicated for the treatment of patients with breast cancer, whose tumours overexpress HER2 (ErbB2):  in combination with capecitabine for patients with advanced or metastatic disease with progression following prior therapy, which must have included anthracyclines and taxanes and therapy with trastuzumab in the metastatic setting; in combination with trastuzumab for patients with hormone-receptor-negative metastatic disease that has progressed on prior trastuzumab therapy or therapies 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatofibrosarcoma protuberans | 99.30% | DL |
| 2 | fibroblastic neoplasm | 98.43% | DL |
| 3 | conventional fibrosarcoma | 98.36% | DL |
| 4 | kidney fibrosarcoma | 98.35% | DL |
| 5 | cysticercosis | 98.34% | DL |
| 6 | heart fibrosarcoma | 98.25% | DL |
| 7 | low grade fibromyxoid sarcoma | 98.23% | DL |
| 8 | Plasmodium falciparum malaria | 98.02% | DL |
| 9 | coenurosis | 97.46% | DL |
| 10 | HER2 positive breast carcinoma | 97.36% | DL |
| 11 | lymphangiomyoma | 97.29% | DL |
| 12 | benign PEComa | 97.29% | DL |
| 13 | uterine corpus perivascular epithelioid cell tumor | 97.26% | DL |
| 14 | autosomal recessive familial Mediterranean fever | 97.04% | DL |
| 15 | liver fibrosarcoma | 96.89% | DL |
| 16 | cutaneous undifferentiated pleomorphic sarcoma | 96.73% | DL |
| 17 | central nervous system fibrosarcoma | 96.38% | DL |
| 18 | progesterone-receptor positive breast cancer | 96.34% | DL |
| 19 | normal breast-like subtype of breast carcinoma | 96.34% | DL |
| 20 | progesterone-receptor negative breast cancer | 96.28% | DL |

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
