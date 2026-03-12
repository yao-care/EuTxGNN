---
layout: default
title: Azathioprine
description: "azathioprine drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 65
evidence_level: L1
indication_count: 50
---

# Azathioprine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Azathioprine |
| DrugBank ID | [DB00993](https://go.drugbank.com/drugs/DB00993) |
| Brand Names (EU) | Jayempi |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Jayempi is indicated in combination with other immunosuppressive agents for the prophylaxis of transplant rejection in patients receiving allogenic kidney, liver, heart, lung or pancreas transplants. Azathioprine is indicated in immunosuppressive regimens as an adjunct to immunosuppressive agents that form the mainstay of treatment (basis immunosuppression). Jayempi is used as an immunosuppressant antimetabolite either alone or, more commonly, in combination with other agents (usually corticoste

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 100.00% | DL |
| 2 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 100.00% | DL |
| 3 | brachydactyly-syndactyly syndrome | 100.00% | DL |
| 4 | osteoarthritis susceptibility | 99.70% | DL |
| 5 | WHIM syndrome | 99.68% | DL |
| 6 | inflammatory bowel disease | 99.52% | DL |
| 7 | granulomatous disease, chronic, autosomal recessive, 5 | 99.41% | DL |
| 8 | osteoarthritis | 99.40% | DL |
| 9 | granulomatous disease with defect in neutrophil chemotaxis | 99.37% | DL |
| 10 | ulcerative colitis (disease) | 99.33% | DL |
| 11 | acromesomelic dysplasia, Hunter-Thompson type | 99.27% | DL |
| 12 | functional neutrophil defect | 99.27% | DL |
| 13 | Crohn disease of the esophagus | 99.27% | DL |
| 14 | anus disease | 99.25% | DL |
| 15 | plasma cell myeloma | 99.19% | DL |
| 16 | indolent plasma cell myeloma | 99.17% | DL |
| 17 | brachyolmia-amelogenesis imperfecta syndrome | 99.06% | DL |
| 18 | brachyolmia | 98.96% | DL |
| 19 | myosclerosis | 98.84% | DL |
| 20 | congenital hypotrichosis with juvenile macular dystrophy | 98.71% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| rheumatoid arthritis | L1 | 20 | 18 | 2 Phase 3 trial(s), 3 Phase 2 trial(s), 3 review(s |

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
