---
layout: default
title: Upadacitinib
description: "Upadacitinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 616
evidence_level: L5
indication_count: 50
---

# Upadacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Upadacitinib |
| DrugBank ID | [DB15091](https://go.drugbank.com/drugs/DB15091) |
| Brand Names (EU) | Rinvoq |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Rheumatoid arthritisRINVOQ is indicated for the treatment of moderate to severe active rheumatoid arthritis in adult patients who have responded inadequately to, or who are intolerant to one or more disease-modifying anti-rheumatic drugs (DMARDs). RINVOQ may be used as monotherapy or in combination with methotrexate. Psoriatic arthritisRINVOQ is indicated for the treatment of active psoriatic arthritis in adult patients who have responded inadequately to, or who are intolerant to one or more DMA

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.71% | DL |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.61% | DL |
| 3 | brachydactyly-syndactyly syndrome | 99.58% | DL |
| 4 | indolent plasma cell myeloma | 94.40% | DL |
| 5 | amyotrohpic lateral sclerosis type 22 | 93.19% | DL |
| 6 | heparin cofactor 2 deficiency | 92.84% | DL |
| 7 | amyotrophic lateral sclerosis, susceptibility to | 92.79% | DL |
| 8 | plasma cell myeloma | 92.58% | DL |
| 9 | Mills syndrome | 91.91% | DL |
| 10 | amyotrophic lateral sclerosis | 91.88% | DL |
| 11 | axial spondylometaphyseal dysplasia | 91.28% | DL |
| 12 | factor 5 excess with spontaneous thrombosis | 90.50% | DL |
| 13 | antithrombin deficiency type 2 | 90.31% | DL |
| 14 | bilateral parasagittal parieto-occipital polymicrogyria | 89.61% | DL |
| 15 | monomelic amyotrophy | 88.91% | DL |
| 16 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 88.54% | DL |
| 17 | lower motor neuron syndrome with late-adult onset | 87.16% | DL |
| 18 | lethal arthrogryposis-anterior horn cell disease syndrome | 86.71% | DL |
| 19 | autosomal dominant mitochondrial myopathy with exercise intolerance | 86.37% | DL |
| 20 | myeloid leukemia | 84.86% | DL |

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
