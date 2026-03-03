---
layout: default
title: Avapritinib
description: "Avapritinib drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 58
evidence_level: L5
indication_count: 51
---

# Avapritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Avapritinib |
| DrugBank ID | [DB15233](https://go.drugbank.com/drugs/DB15233) |
| Brand Names (EU) | Ayvakyt |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Unresectable or metastatic gastrointestinal stromal tumour (GIST) AYVAKYT is indicated as monotherapy for the treatment of adult patients with unresectable or metastatic gastrointestinal stromal tumours (GIST) harbouring the platelet-derived growth factor receptor alpha (PDGFRA) D842V mutation. Advanced systemic mastocytosis (AdvSM) AYVAKYT is indicated as monotherapy for the treatment of adult patients with aggressive systemic mastocytosis (ASM), systemic mastocytosis with an associated haemato

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | axial spondylometaphyseal dysplasia | 99.92% | DL |
| 2 | bilateral parasagittal parieto-occipital polymicrogyria | 99.92% | DL |
| 3 | amyotrophic lateral sclerosis | 99.92% | DL |
| 4 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.92% | DL |
| 5 | amyotrophic lateral sclerosis, susceptibility to | 99.91% | DL |
| 6 | amyotrohpic lateral sclerosis type 22 | 99.91% | DL |
| 7 | lower motor neuron syndrome with late-adult onset | 99.91% | DL |
| 8 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.90% | DL |
| 9 | monomelic amyotrophy | 99.89% | DL |
| 10 | Mills syndrome | 99.89% | DL |
| 11 | autosomal dominant mitochondrial myopathy with exercise intolerance | 99.89% | DL |
| 12 | familial generalized lentiginosis | 99.87% | DL |
| 13 | rhabdoid tumor | 99.86% | DL |
| 14 | gastrocutaneous syndrome | 99.86% | DL |
| 15 | acromelanosis | 99.84% | DL |
| 16 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 99.84% | DL |
| 17 | Moynahan syndrome | 99.84% | DL |
| 18 | osteopathia striata-pigmentary dermopathy-white forelock syndrome | 99.83% | DL |
| 19 | leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome | 99.82% | DL |
| 20 | peripheral nerve schwannoma | 99.80% | DL |

*Showing top 20 of 51 predictions.*

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
