---
layout: default
title: Loxapine
description: "Loxapine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 354
evidence_level: L5
indication_count: 50
---

# Loxapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Loxapine |
| DrugBank ID | [DB00408](https://go.drugbank.com/drugs/DB00408) |
| Brand Names (EU) | Adasuve |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Adasuve is indicated for the rapid control of mild-to-moderate agitation in adult patients with schizophrenia or bipolar disorder. Patients should receive regular treatment immediately after control of acute agitation symptoms.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.99% | DL |
| 2 | schizophrenia | 99.97% | DL |
| 3 | retinal dystrophy with or without extraocular anomalies | 99.95% | DL |
| 4 | hydranencephaly (disease) | 99.93% | DL |
| 5 | myopia X-linked | 99.93% | DL |
| 6 | congenital disorder of glycosylation with defective fucosylation | 99.92% | DL |
| 7 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.92% | DL |
| 8 | myopia 26, X-linked, female-limited | 99.92% | DL |
| 9 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.92% | DL |
| 10 | syndromic myopia | 99.92% | DL |
| 11 | atypical glycine encephalopathy | 99.90% | DL |
| 12 | bipolar disorder | 99.84% | DL |
| 13 | major affective disorder | 99.82% | DL |
| 14 | distal 17p13.3 microdeletion syndrome | 99.78% | DL |
| 15 | attention deficit hyperactivity disorder, inattentive type | 99.61% | DL |
| 16 | hydrops-lactic acidosis-sideroblastic anemia-multisystemic failure syndrome | 99.61% | DL |
| 17 | anxiety disorder | 99.56% | DL |
| 18 | attention deficit-hyperactivity disorder | 99.49% | DL |
| 19 | Malan overgrowth syndrome | 99.45% | DL |
| 20 | benign paroxysmal torticollis of infancy | 99.42% | DL |

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
