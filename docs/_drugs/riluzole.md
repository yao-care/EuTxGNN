---
layout: default
title: Riluzole
description: "Riluzole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 493
evidence_level: L5
indication_count: 50
---

# Riluzole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Riluzole |
| DrugBank ID | [DB00740](https://go.drugbank.com/drugs/DB00740) |
| Brand Names (EU) | Rilutek |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Rilutek is indicated to extend life or the time to mechanical ventilation for patients with amyotrophic lateral sclerosis (ALS). Clinical trials have demonstrated that Rilutek extends survival for patients with ALS. Survival was defined as patients who were alive, not intubated for mechanical ventilation and tracheotomy-free. There is no evidence that Rilutek exerts a therapeutic effect on motor function, lung function, fasciculations, muscle strength and motor symptoms. Rilutek has not been sho

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bilateral parasagittal parieto-occipital polymicrogyria | 99.99% | DL |
| 2 | amyotrophic lateral sclerosis | 99.99% | DL |
| 3 | axial spondylometaphyseal dysplasia | 99.99% | DL |
| 4 | lower motor neuron syndrome with late-adult onset | 99.99% | DL |
| 5 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.99% | DL |
| 6 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.99% | DL |
| 7 | monomelic amyotrophy | 99.99% | DL |
| 8 | Mills syndrome | 99.98% | DL |
| 9 | amyotrophic lateral sclerosis, susceptibility to | 99.98% | DL |
| 10 | autosomal dominant mitochondrial myopathy with exercise intolerance | 99.98% | DL |
| 11 | amyotrohpic lateral sclerosis type 22 | 99.98% | DL |
| 12 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.70% | DL |
| 13 | hydranencephaly (disease) | 99.67% | DL |
| 14 | congenital disorder of glycosylation with defective fucosylation | 99.67% | DL |
| 15 | schizophrenia | 99.66% | DL |
| 16 | retinal dystrophy with or without extraocular anomalies | 99.64% | DL |
| 17 | atypical glycine encephalopathy | 99.62% | DL |
| 18 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.59% | DL |
| 19 | myopia 26, X-linked, female-limited | 99.55% | DL |
| 20 | syndromic myopia | 99.54% | DL |

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
