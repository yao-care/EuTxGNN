---
layout: default
title: Selumetinib Sulfate
description: "Selumetinib Sulfate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 523
evidence_level: L5
indication_count: 50
---

# Selumetinib Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Selumetinib Sulfate |
| DrugBank ID | [DB11689](https://go.drugbank.com/drugs/DB11689) |
| Brand Names (EU) | Koselugo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Koselugo as monotherapy is indicated for the treatment of symptomatic, inoperable plexiform neurofibromas (PN) in paediatric patients with neurofibromatosis type 1 (NF1) aged 3 years and above

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | familial generalized lentiginosis | 99.96% | DL |
| 2 | gastrocutaneous syndrome | 99.96% | DL |
| 3 | rhabdoid tumor | 99.96% | DL |
| 4 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 99.96% | DL |
| 5 | acromelanosis | 99.96% | DL |
| 6 | Moynahan syndrome | 99.96% | DL |
| 7 | leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome | 99.95% | DL |
| 8 | osteopathia striata-pigmentary dermopathy-white forelock syndrome | 99.95% | DL |
| 9 | peripheral nerve schwannoma | 99.95% | DL |
| 10 | trigeminal schwannoma | 99.95% | DL |
| 11 | microcystic/reticular schwannoma | 99.95% | DL |
| 12 | schwannoma of twelfth cranial nerve | 99.94% | DL |
| 13 | sympathetic neurilemmoma | 99.94% | DL |
| 14 | bilateral parasagittal parieto-occipital polymicrogyria | 99.92% | DL |
| 15 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.91% | DL |
| 16 | axial spondylometaphyseal dysplasia | 99.91% | DL |
| 17 | amyotrophic lateral sclerosis | 99.91% | DL |
| 18 | lower motor neuron syndrome with late-adult onset | 99.91% | DL |
| 19 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.89% | DL |
| 20 | neurofibromatosis | 99.88% | DL |

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
