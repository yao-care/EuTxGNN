---
layout: default
title: Lurasidone
description: "lurasidone drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 356
evidence_level: L1
indication_count: 50
---

# Lurasidone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lurasidone |
| DrugBank ID | [DB08815](https://go.drugbank.com/drugs/DB08815) |
| Brand Names (EU) | Latuda |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Treatment of schizophrenia in adults aged 18 years and over.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.98% | DL |
| 2 | schizophrenia | 99.98% | DL |
| 3 | retinal dystrophy with or without extraocular anomalies | 99.95% | DL |
| 4 | hydranencephaly (disease) | 99.95% | DL |
| 5 | congenital disorder of glycosylation with defective fucosylation | 99.95% | DL |
| 6 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.94% | DL |
| 7 | myopia X-linked | 99.94% | DL |
| 8 | syndromic myopia | 99.94% | DL |
| 9 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.94% | DL |
| 10 | myopia 26, X-linked, female-limited | 99.93% | DL |
| 11 | atypical glycine encephalopathy | 99.92% | DL |
| 12 | bipolar disorder | 99.73% | DL |
| 13 | distal 17p13.3 microdeletion syndrome | 99.71% | DL |
| 14 | major affective disorder | 99.64% | DL |
| 15 | hydrops-lactic acidosis-sideroblastic anemia-multisystemic failure syndrome | 99.53% | DL |
| 16 | Malan overgrowth syndrome | 99.13% | DL |
| 17 | schizophreniform disorder | 98.84% | DL |
| 18 | trichotillomania | 96.06% | DL |
| 19 | anxiety disorder | 95.61% | DL |
| 20 | psychotic disorder | 95.27% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| schizophrenia | L1 | 20 | 18 | 10 Phase 3 trial(s), 2 Phase 2 trial(s), 9 review( |
| manic bipolar affective disorder | L1 | 15 | 0 | 10 Phase 3 trial(s), 1 Phase 2 trial(s) |

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
