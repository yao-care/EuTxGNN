---
layout: default
title: Apremilast
description: "Apremilast drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 45
evidence_level: L5
indication_count: 51
---

# Apremilast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Apremilast |
| DrugBank ID | [DB05676](https://go.drugbank.com/drugs/DB05676) |
| Brand Names (EU) | Apremilast Accord, Otezla |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 98.66% |

---

## Approved Indication (EMA)

Psoriatic arthritisOtezla, alone or in combination with Disease Modifying Antirheumatic Drugs (DMARDs), is indicated for the treatment of active psoriatic arthritis (PsA) in adult patients who have had an inadequate response or who have been intolerant to a prior DMARD therapy.&nbsp;PsoriasisOtezla is indicated for the treatment of moderate to severe chronic plaque psoriasis (PSOR) in adult patients who failed to respond to or who have a contraindication to, or are intolerant to other systemic t

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 98.66% | DL |
| 2 | migraine with brainstem aura | 98.49% | DL |
| 3 | rheumatoid arthritis | 98.09% | DL |
| 4 | pulmonary hypertension | 98.09% | DL |
| 5 | migraine with or without aura, susceptibility to | 97.81% | DL |
| 6 | kyphoscoliotic heart disease | 97.79% | DL |
| 7 | brachydactyly-syndactyly syndrome | 97.36% | DL |
| 8 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.95% | DL |
| 9 | atrophoderma vermiculata | 96.69% | DL |
| 10 | ulerythema ophryogenesis | 96.17% | DL |
| 11 | Prinzmetal angina | 95.91% | DL |
| 12 | homozygous familial hypercholesterolemia | 95.91% | DL |
| 13 | thrombotic disease | 95.42% | DL |
| 14 | nephrogenic syndrome of inappropriate antidiuresis | 94.65% | DL |
| 15 | non-inflammatory vasculopathy | 94.63% | DL |
| 16 | angiodysplasia | 94.63% | DL |
| 17 | tendinitis | 94.54% | DL |
| 18 | venous thromboembolism | 94.49% | DL |
| 19 | fibrocartilaginous embolism | 94.49% | DL |
| 20 | cor pulmonale | 94.45% | DL |

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
