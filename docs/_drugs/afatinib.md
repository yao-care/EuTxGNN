---
layout: default
title: Afatinib
description: "Afatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 20
evidence_level: L5
indication_count: 50
---

# Afatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Afatinib |
| DrugBank ID | [DB08916](https://go.drugbank.com/drugs/DB08916) |
| Brand Names (EU) | Giotrif |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.65% |

---

## Approved Indication (EMA)

Giotrif as monotherapy is indicated for the treatment of  Epidermal Growth Factor Receptor (EGFR) TKI-naïve adult patients with locally advanced or metastatic non-small cell lung cancer (NSCLC) with activating EGFR mutation(s); locally advanced or metastatic NSCLC of squamous histology progressing on or after platinum-based chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HER2 positive breast carcinoma | 98.65% | DL |
| 2 | multiple endocrine neoplasia | 98.48% | DL |
| 3 | progesterone-receptor negative breast cancer | 97.93% | DL |
| 4 | normal breast-like subtype of breast carcinoma | 97.89% | DL |
| 5 | progesterone-receptor positive breast cancer | 97.89% | DL |
| 6 | breast tumor luminal A or B | 97.87% | DL |
| 7 | thrombocytopenia | 97.58% | DL |
| 8 | marcothrombocytopenia with mitral valve insufficiency | 97.42% | DL |
| 9 | hereditary thrombocytopenia with normal platelets | 97.39% | DL |
| 10 | dense granule disease | 97.28% | DL |
| 11 | transient neonatal thrombocytopenia | 97.23% | DL |
| 12 | malignant catarrh | 96.84% | DL |
| 13 | infectious bovine rhinotracheitis | 96.84% | DL |
| 14 | cytomegalovirus infection | 96.67% | DL |
| 15 | amenorrhea (disease) | 96.45% | DL |
| 16 | platelet storage pool deficiency | 96.18% | DL |
| 17 | myeloid leukemia | 95.15% | DL |
| 18 | amyotrophic lateral sclerosis | 94.92% | DL |
| 19 | glaucoma | 94.88% | DL |
| 20 | amyotrohpic lateral sclerosis type 22 | 94.54% | DL |

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
