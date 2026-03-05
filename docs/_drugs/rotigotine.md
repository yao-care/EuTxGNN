---
layout: default
title: Rotigotine
description: "rotigotine drug repurposing predictions from TxGNN. Evidence level L2 with 50 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 508
evidence_level: L2
indication_count: 50
---

# Rotigotine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rotigotine |
| DrugBank ID | [DB05271](https://go.drugbank.com/drugs/DB05271) |
| Brand Names (EU) | Neupro |
| Evidence Level | L2 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Parkinson's disease: Neupro is indicated for the treatment of the signs and symptoms of early-stage idiopathic Parkinson's disease as monotherapy (i.e. without levodopa) or in combination with levodopa, i.e. over the course of the disease, through to late stages when the effect of levodopa wears off or becomes inconsistent and fluctuations of the therapeutic effect occur (end of dose or 'on-off' fluctuations). Restless-legs syndrome: Neupro is indicated for the symptomatic treatment of moderate 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | attention deficit-hyperactivity disorder | 100.00% | DL |
| 2 | schizophrenia | 100.00% | DL |
| 3 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.99% | DL |
| 4 | faciodigitogenital syndrome | 99.99% | DL |
| 5 | congenital disorder of glycosylation with defective fucosylation | 99.99% | DL |
| 6 | retinal dystrophy with or without extraocular anomalies | 99.99% | DL |
| 7 | myopia X-linked | 99.99% | DL |
| 8 | atypical glycine encephalopathy | 99.99% | DL |
| 9 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.99% | DL |
| 10 | myopia 26, X-linked, female-limited | 99.99% | DL |
| 11 | syndromic myopia | 99.99% | DL |
| 12 | hydranencephaly (disease) | 99.99% | DL |
| 13 | attention deficit hyperactivity disorder, inattentive type | 99.98% | DL |
| 14 | juvenile onset Parkinson disease 19A | 99.96% | DL |
| 15 | chondromyxoid fibroma | 99.95% | DL |
| 16 | specific developmental disorder | 99.94% | DL |
| 17 | hereditary late onset Parkinson disease | 99.91% | DL |
| 18 | atypical juvenile parkinsonism | 99.89% | DL |
| 19 | trichotillomania | 99.89% | DL |
| 20 | PLA2G6-associated neurodegeneration | 99.88% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| schizophrenia | L2 | 0 | 3 | 1 review(s)/meta-analysis |

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
