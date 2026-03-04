---
layout: default
title: Acetylsalicylic Acid
description: "acetylsalicylic acid drug repurposing predictions from TxGNN. Evidence level L1 with 54 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 16
evidence_level: L1
indication_count: 54
---

# Acetylsalicylic Acid
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **54**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Acetylsalicylic Acid |
| DrugBank ID | [DB00945](https://go.drugbank.com/drugs/DB00945) |
| Brand Names (EU) | Acetylsalicylic acid, Clopidogrel / Acetylsalicylic acid Viatris (previously Clopidogrel / Acetylsalicylic acid Mylan), Clopidogrel/Acetylsalicylic acid Zentiva (previously DuoCover), DuoPlavin |
| Evidence Level | L1 |
| Predicted Indications | 54 |
| Top Prediction Score | 99.94% |

---

## Approved Indication (EMA)

Acute Coronary Syndrome Myocardial Infarction

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.94% | DL |
| 2 | migraine with brainstem aura | 99.94% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.78% | DL |
| 4 | atrophoderma vermiculata | 99.59% | DL |
| 5 | ulerythema ophryogenesis | 99.45% | DL |
| 6 | headache disorder | 99.44% | DL |
| 7 | heparin cofactor 2 deficiency | 99.41% | DL |
| 8 | factor 5 excess with spontaneous thrombosis | 99.40% | DL |
| 9 | antithrombin deficiency type 2 | 99.40% | DL |
| 10 | trigeminal autonomic cephalalgia | 99.40% | DL |
| 11 | thrombotic disease | 99.14% | DL |
| 12 | thrombophilia | 99.04% | DL |
| 13 | rheumatoid arthritis | 98.84% | DL |
| 14 | Raynaud disease | 98.67% | DL |
| 15 | non-inflammatory vasculopathy | 98.51% | DL |
| 16 | angiodysplasia | 98.42% | DL |
| 17 | fibrocartilaginous embolism | 98.34% | DL |
| 18 | venous thromboembolism | 98.34% | DL |
| 19 | vein disease | 98.34% | DL |
| 20 | brachydactyly-syndactyly syndrome | 98.27% | DL |

*Showing top 20 of 54 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| migraine disorder | L1 | 20 | 0 | 7 Phase 3 trial(s), 2 Phase 2 trial(s) |

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
