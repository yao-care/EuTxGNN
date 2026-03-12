---
layout: default
title: Tocilizumab
description: "tocilizumab drug repurposing predictions from TxGNN. Evidence level L1 with 53 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 591
evidence_level: L1
indication_count: 53
---

# Tocilizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tocilizumab |
| DrugBank ID | [DB06273](https://go.drugbank.com/drugs/DB06273) |
| Brand Names (EU) | Avtozma, RoActemra, Tocilizumab STADA (previously Tofidence), Tyenne |
| Evidence Level | L1 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

RoActemra, in combination with methotrexate (MTX), is indicated for  the treatment of severe, active and progressive rheumatoid arthritis (RA) in adults not previously treated with MTX. the treatment of moderate to severe active RA in adult patients who have either responded inadequately to, or who were intolerant to, previous therapy with one or more disease-modifying anti-rheumatic drugs (DMARDs) or tumour necrosis factor (TNF) antagonists. 	In these patients, RoActemra can be given as monothe

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ankylosing spondylitis | 99.99% | DL |
| 2 | rheumatoid vasculitis | 99.98% | DL |
| 3 | hypermobility of coccyx | 99.98% | DL |
| 4 | spondyloarthropathy, susceptibility to | 99.98% | DL |
| 5 | inflammatory spondylopathy | 99.98% | DL |
| 6 | Kummell disease | 99.98% | DL |
| 7 | polyarticular juvenile rheumatoid arthritis | 99.98% | DL |
| 8 | vertebral disease | 99.93% | DL |
| 9 | juvenile idiopathic arthritis | 99.90% | DL |
| 10 | mendelian susceptibility to mycobacterial diseases due to complete IL12B deficiency | 99.87% | DL |
| 11 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 99.87% | DL |
| 12 | rheumatoid nodulosis | 99.85% | DL |
| 13 | juvenile chronic polyarthritis | 99.83% | DL |
| 14 | juvenile arthritis due to defect in LACC1 | 99.71% | DL |
| 15 | autosomal recessive familial Mediterranean fever | 99.48% | DL |
| 16 | anti-glomerular basement membrane disease | 99.24% | DL |
| 17 | WHIM syndrome | 99.18% | DL |
| 18 | systemic mastocytosis | 99.10% | DL |
| 19 | familial Mediterranean fever, autosomal dominant | 99.07% | DL |
| 20 | psoriasis-related juvenile idiopathic arthritis | 99.02% | DL |

*Showing top 20 of 53 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| ankylosing spondylitis | L1 | 8 | 19 | 2 Phase 3 trial(s), 1 Phase 2 trial(s), 1 RCT(s),  |
| inflammatory spondylopathy | L4 | 11 | 0 | 2 Phase 3 trial(s), 1 Phase 2 trial(s) |

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
