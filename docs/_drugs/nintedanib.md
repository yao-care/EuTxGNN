---
layout: default
title: Nintedanib
description: "Nintedanib drug repurposing predictions from TxGNN. Evidence level L5 with 55 predicted indications."
parent: AI Predictions (L5)
nav_order: 404
evidence_level: L5
indication_count: 55
---

# Nintedanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **55**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Nintedanib |
| DrugBank ID | [DB09079](https://go.drugbank.com/drugs/DB09079) |
| Brand Names (EU) | Nintedanib Accord, Ofev, Vargatef |
| Evidence Level | L5 |
| Predicted Indications | 55 |
| Top Prediction Score | 99.15% |

---

## Approved Indication (EMA)

Vargatef is indicated in combination with docetaxel for the treatment of adult patients with locally advanced, metastatic or locally recurrent non-small cell lung cancer (NSCLC) of adenocarcinoma tumour histology after first line chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatofibrosarcoma protuberans | 99.15% | DL |
| 2 | liposarcoma | 99.13% | DL |
| 3 | ovarian myxoid liposarcoma | 99.12% | DL |
| 4 | heart fibrosarcoma | 98.88% | DL |
| 5 | axial spondylometaphyseal dysplasia | 98.87% | DL |
| 6 | amyotrohpic lateral sclerosis type 22 | 98.86% | DL |
| 7 | fibroblastic neoplasm | 98.84% | DL |
| 8 | kidney fibrosarcoma | 98.83% | DL |
| 9 | conventional fibrosarcoma | 98.81% | DL |
| 10 | amyotrophic lateral sclerosis, susceptibility to | 98.80% | DL |
| 11 | amyotrophic lateral sclerosis | 98.78% | DL |
| 12 | bilateral parasagittal parieto-occipital polymicrogyria | 98.75% | DL |
| 13 | low grade fibromyxoid sarcoma | 98.74% | DL |
| 14 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 98.66% | DL |
| 15 | Mills syndrome | 98.63% | DL |
| 16 | familial rhabdoid tumor | 98.51% | DL |
| 17 | lower motor neuron syndrome with late-adult onset | 98.47% | DL |
| 18 | extracutaneous mastocytoma | 98.46% | DL |
| 19 | monomelic amyotrophy | 98.31% | DL |
| 20 | autosomal dominant mitochondrial myopathy with exercise intolerance | 98.25% | DL |

*Showing top 20 of 55 predictions.*

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
