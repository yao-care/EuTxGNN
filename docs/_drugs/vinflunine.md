---
layout: default
title: Vinflunine
description: "Vinflunine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 635
evidence_level: L5
indication_count: 50
---

# Vinflunine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vinflunine |
| DrugBank ID | [DB11641](https://go.drugbank.com/drugs/DB11641) |
| Brand Names (EU) | Javlor |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.00% |

---

## Approved Indication (EMA)

Javlor is indicated in monotherapy for the treatment of adult patients with advanced or metastatic transitional-cell carcinoma of the urothelial tract after failure of a prior platinum-containing regimen. Efficacy and safety of vinflunine have not been studied in patients with performance status ? 2.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | amyotrophic lateral sclerosis | 99.00% | DL |
| 2 | bilateral parasagittal parieto-occipital polymicrogyria | 98.73% | DL |
| 3 | Mills syndrome | 98.67% | DL |
| 4 | amyotrohpic lateral sclerosis type 22 | 98.58% | DL |
| 5 | amyotrophic lateral sclerosis, susceptibility to | 98.57% | DL |
| 6 | axial spondylometaphyseal dysplasia | 98.56% | DL |
| 7 | lower motor neuron syndrome with late-adult onset | 98.48% | DL |
| 8 | autosomal dominant mitochondrial myopathy with exercise intolerance | 98.41% | DL |
| 9 | monomelic amyotrophy | 98.41% | DL |
| 10 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 98.25% | DL |
| 11 | lethal arthrogryposis-anterior horn cell disease syndrome | 98.11% | DL |
| 12 | kidney pelvis sarcomatoid transitional cell carcinoma | 95.63% | DL |
| 13 | prostatic urethra urothelial carcinoma | 95.46% | DL |
| 14 | infiltrating bladder urothelial carcinoma sarcomatoid variant | 95.43% | DL |
| 15 | renal pelvis papillary urothelial carcinoma | 95.39% | DL |
| 16 | transitional cell carcinoma | 93.65% | DL |
| 17 | immunodeficiency without anhidrotic ectodermal dysplasia | 91.01% | DL |
| 18 | SMARCA4-deficient sarcoma of thorax | 91.00% | DL |
| 19 | liposarcoma | 90.94% | DL |
| 20 | ovarian myxoid liposarcoma | 90.37% | DL |

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
