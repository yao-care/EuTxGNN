---
layout: default
title: Olanzapine
description: "Olanzapine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 418
evidence_level: L5
indication_count: 50
---

# Olanzapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Olanzapine |
| DrugBank ID | [DB00334](https://go.drugbank.com/drugs/DB00334) |
| Brand Names (EU) | Olazax Disperzi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Adults Olanzapine is indicated for the treatment of schizophrenia. Olanzapine is effective in maintaining the clinical improvement during continuation therapy in patients who have shown an initial treatment response. Olanzapine is indicated for the treatment of moderate to severe manic episode. In patients whose manic episode has responded to olanzapine treatment, olanzapine is indicated for the prevention of recurrence in patients with bipolar disorder.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.93% | DL |
| 2 | anxiety disorder | 99.75% | DL |
| 3 | bipolar disorder | 99.55% | DL |
| 4 | benign paroxysmal torticollis of infancy | 99.54% | DL |
| 5 | agoraphobia | 99.47% | DL |
| 6 | major affective disorder | 99.41% | DL |
| 7 | schizophrenia | 99.38% | DL |
| 8 | endogenous depression | 99.28% | DL |
| 9 | dysthymic disorder | 99.28% | DL |
| 10 | major depressive disorder | 99.06% | DL |
| 11 | distal 17p13.3 microdeletion syndrome | 98.97% | DL |
| 12 | neurotic disorder | 98.93% | DL |
| 13 | neurotic depression | 98.77% | DL |
| 14 | melancholia | 98.77% | DL |
| 15 | retinal dystrophy with or without extraocular anomalies | 98.74% | DL |
| 16 | Ohdo syndrome and variants | 98.63% | DL |
| 17 | childhood apraxia of speech | 98.63% | DL |
| 18 | unipolar depression | 98.62% | DL |
| 19 | congenital disorder of glycosylation with defective fucosylation | 98.55% | DL |
| 20 | hydranencephaly (disease) | 98.53% | DL |

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
