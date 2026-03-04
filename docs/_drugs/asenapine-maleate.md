---
layout: default
title: Asenapine Maleate
description: "asenapine maleate drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 51
evidence_level: L1
indication_count: 50
---

# Asenapine Maleate
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Asenapine Maleate |
| DrugBank ID | [DB06216](https://go.drugbank.com/drugs/DB06216) |
| Brand Names (EU) | Sycrest |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Sycrest is indicated for the treatment of moderate to severe manic episodes associated with bipolar I disorder in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.99% | DL |
| 2 | schizophrenia | 99.90% | DL |
| 3 | bipolar disorder | 99.80% | DL |
| 4 | retinal dystrophy with or without extraocular anomalies | 99.77% | DL |
| 5 | congenital disorder of glycosylation with defective fucosylation | 99.75% | DL |
| 6 | hydranencephaly (disease) | 99.74% | DL |
| 7 | syndromic myopia | 99.70% | DL |
| 8 | myopia X-linked | 99.69% | DL |
| 9 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.68% | DL |
| 10 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.68% | DL |
| 11 | myopia 26, X-linked, female-limited | 99.65% | DL |
| 12 | atypical glycine encephalopathy | 99.58% | DL |
| 13 | major affective disorder | 99.57% | DL |
| 14 | distal 17p13.3 microdeletion syndrome | 99.56% | DL |
| 15 | schizophreniform disorder | 99.24% | DL |
| 16 | hydrops-lactic acidosis-sideroblastic anemia-multisystemic failure syndrome | 99.21% | DL |
| 17 | Malan overgrowth syndrome | 99.12% | DL |
| 18 | trichotillomania | 98.80% | DL |
| 19 | Tourette syndrome | 97.74% | DL |
| 20 | anxiety disorder | 97.12% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| manic bipolar affective disorder | L1 | 13 | 0 | 9 Phase 3 trial(s) |

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
