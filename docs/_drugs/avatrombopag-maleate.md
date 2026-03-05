---
layout: default
title: Avatrombopag Maleate
description: "avatrombopag maleate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 59
evidence_level: L5
indication_count: 50
---

# Avatrombopag Maleate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Avatrombopag Maleate |
| DrugBank ID | [DB11995](https://go.drugbank.com/drugs/DB11995) |
| Brand Names (EU) | Doptelet |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Doptelet is indicated for the treatment of severe thrombocytopenia in adult patients with chronic liver disease who are scheduled to undergo an invasive procedure. Doptelet is indicated for the treatment of primary chronic immune thrombocytopenia (ITP) in adult patients who are refractory to other treatments (e.g. corticosteroids, immunoglobulins).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | marcothrombocytopenia with mitral valve insufficiency | 100.00% | DL |
| 2 | hereditary thrombocytopenia with normal platelets | 100.00% | DL |
| 3 | transient neonatal thrombocytopenia | 100.00% | DL |
| 4 | dense granule disease | 99.99% | DL |
| 5 | thrombocytopenia | 99.99% | DL |
| 6 | amyotrophic lateral sclerosis | 99.99% | DL |
| 7 | bilateral parasagittal parieto-occipital polymicrogyria | 99.99% | DL |
| 8 | lower motor neuron syndrome with late-adult onset | 99.99% | DL |
| 9 | amyotrophic lateral sclerosis, susceptibility to | 99.99% | DL |
| 10 | Mills syndrome | 99.99% | DL |
| 11 | monomelic amyotrophy | 99.99% | DL |
| 12 | axial spondylometaphyseal dysplasia | 99.99% | DL |
| 13 | amyotrohpic lateral sclerosis type 22 | 99.99% | DL |
| 14 | autosomal dominant mitochondrial myopathy with exercise intolerance | 99.99% | DL |
| 15 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.99% | DL |
| 16 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.99% | DL |
| 17 | platelet storage pool deficiency | 99.95% | DL |
| 18 | neuronopathy, distal hereditary motor | 99.36% | DL |
| 19 | melanoma | 98.55% | DL |
| 20 | CMM7 | 98.53% | DL |

*Showing top 20 of 50 predictions.*

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
