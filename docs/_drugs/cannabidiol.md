---
layout: default
title: Cannabidiol
description: "Cannabidiol drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 111
evidence_level: L5
indication_count: 53
---

# Cannabidiol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cannabidiol |
| DrugBank ID | [DB09061](https://go.drugbank.com/drugs/DB09061) |
| Brand Names (EU) | Epidyolex |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 96.17% |

---

## Approved Indication (EMA)

Epidyolex is indicated for use as adjunctive therapy of seizures associated with Lennox Gastaut syndrome (LGS) or Dravet syndrome (DS), in conjunction with clobazam, for patients 2 years of age and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | restless legs syndrome | 96.17% | DL |
| 2 | bilateral parasagittal parieto-occipital polymicrogyria | 95.99% | DL |
| 3 | axial spondylometaphyseal dysplasia | 94.22% | DL |
| 4 | amyotrophic lateral sclerosis | 94.15% | DL |
| 5 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 93.83% | DL |
| 6 | episodic kinesigenic dyskinesia | 93.73% | DL |
| 7 | Mills syndrome | 93.41% | DL |
| 8 | amyotrophic lateral sclerosis, susceptibility to | 93.40% | DL |
| 9 | lower motor neuron syndrome with late-adult onset | 93.21% | DL |
| 10 | lethal arthrogryposis-anterior horn cell disease syndrome | 93.18% | DL |
| 11 | monomelic amyotrophy | 93.07% | DL |
| 12 | amyotrohpic lateral sclerosis type 22 | 92.89% | DL |
| 13 | PURA-related severe neonatal hypotonia-seizures-encephalopathy syndrome due to a point mutation | 92.39% | DL |
| 14 | neonatal period electroclinical syndrome | 92.30% | DL |
| 15 | 1q44 microdeletion syndrome | 92.22% | DL |
| 16 | myoclonic epilepsy, Hartung type | 92.01% | DL |
| 17 | developmental and epileptic encephalopathy | 91.99% | DL |
| 18 | genetic lethal multiple congenital anomalies/dysmorphic syndrome | 91.92% | DL |
| 19 | autosomal dominant mitochondrial myopathy with exercise intolerance | 91.88% | DL |
| 20 | infancy electroclinical syndrome | 91.85% | DL |

*Showing top 20 of 53 predictions.*

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
