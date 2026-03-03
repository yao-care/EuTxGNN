---
layout: default
title: Pemigatinib
description: "Pemigatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 452
evidence_level: L5
indication_count: 50
---

# Pemigatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pemigatinib |
| DrugBank ID | [DB15102](https://go.drugbank.com/drugs/DB15102) |
| Brand Names (EU) | Pemazyre |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Pemazyre monotherapy is indicated for the treatment of adults with locally advanced or metastatic cholangiocarcinoma with a fibroblast growth factor receptor 2 (FGFR2) fusion or rearrangement that have progressed &nbsp;after at least one prior line of systemic therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple endocrine neoplasia | 99.71% | DL |
| 2 | amenorrhea (disease) | 99.54% | DL |
| 3 | HER2 positive breast carcinoma | 99.49% | DL |
| 4 | cytomegalovirus infection | 99.46% | DL |
| 5 | malignant catarrh | 99.43% | DL |
| 6 | infectious bovine rhinotracheitis | 99.43% | DL |
| 7 | amyotrophic lateral sclerosis | 99.41% | DL |
| 8 | amyotrohpic lateral sclerosis type 22 | 99.27% | DL |
| 9 | amyotrophic lateral sclerosis, susceptibility to | 99.25% | DL |
| 10 | axial spondylometaphyseal dysplasia | 99.25% | DL |
| 11 | Mills syndrome | 99.22% | DL |
| 12 | progesterone-receptor negative breast cancer | 99.18% | DL |
| 13 | progesterone-receptor positive breast cancer | 99.17% | DL |
| 14 | normal breast-like subtype of breast carcinoma | 99.17% | DL |
| 15 | trichomegaly-retina pigmentary degeneration-dwarfism syndrome | 99.17% | DL |
| 16 | breast tumor luminal A or B | 99.15% | DL |
| 17 | lethal arthrogryposis-anterior horn cell disease syndrome | 99.12% | DL |
| 18 | bilateral parasagittal parieto-occipital polymicrogyria | 99.09% | DL |
| 19 | lower motor neuron syndrome with late-adult onset | 99.08% | DL |
| 20 | monomelic amyotrophy | 99.03% | DL |

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
