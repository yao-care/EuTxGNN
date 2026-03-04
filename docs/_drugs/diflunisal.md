---
layout: default
title: Diflunisal
description: "diflunisal drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 174
evidence_level: L1
indication_count: 50
---

# Diflunisal
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Diflunisal |
| DrugBank ID | [DB00861](https://go.drugbank.com/drugs/DB00861) |
| Brand Names (EU) | Attrogy |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Attrogy is indicated for the treatment of hereditary transthyretin-mediated amyloidosis (ATTRv) in adult patients with stage 1 or stage 2 polyneuropathy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | osteoarthritis susceptibility | 100.00% | DL |
| 2 | acromesomelic dysplasia, Hunter-Thompson type | 99.99% | DL |
| 3 | brachyolmia-amelogenesis imperfecta syndrome | 99.99% | DL |
| 4 | spondyloarthropathy, susceptibility to | 99.99% | DL |
| 5 | rheumatoid arthritis | 99.99% | DL |
| 6 | myosclerosis | 99.99% | DL |
| 7 | osteoarthritis | 99.99% | DL |
| 8 | ankylosing spondylitis | 99.98% | DL |
| 9 | brachyolmia | 99.98% | DL |
| 10 | arthropathy | 99.98% | DL |
| 11 | hypermobility of coccyx | 99.97% | DL |
| 12 | rheumatoid vasculitis | 99.97% | DL |
| 13 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.97% | DL |
| 14 | inflammatory spondylopathy | 99.97% | DL |
| 15 | brachydactyly-syndactyly syndrome | 99.97% | DL |
| 16 | polyarticular juvenile rheumatoid arthritis | 99.97% | DL |
| 17 | Kummell disease | 99.97% | DL |
| 18 | pseudoachondroplasia | 99.96% | DL |
| 19 | vertebral disease | 99.94% | DL |
| 20 | WHIM syndrome | 99.92% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| rheumatoid arthritis | L1 | 0 | 20 | 11 RCT(s) |
| osteoarthritis | L1 | 0 | 20 | 9 RCT(s), 1 review(s)/meta-analysis |
| ankylosing spondylitis | L2 | 0 | 7 | 2 RCT(s) |

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
