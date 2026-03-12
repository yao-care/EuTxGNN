---
layout: default
title: Ozanimod Hydrochloride
description: "Ozanimod Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 431
evidence_level: L5
indication_count: 50
---

# Ozanimod Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ozanimod Hydrochloride |
| DrugBank ID | [DB12612](https://go.drugbank.com/drugs/DB12612) |
| Brand Names (EU) | Zeposia |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.58% |

---

## Approved Indication (EMA)

Multiple sclerosis  Zeposia is indicated for the treatment of adult patients with relapsing remitting multiple sclerosis (RRMS) with active disease as defined by clinical or imaging features.  Ulcerative colitis  Zeposia is indicated for the treatment of adult patients with moderately to severely active ulcerative colitis (UC) who have had an inadequate response, lost response, or were intolerant to either conventional therapy or a biologic agent.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | multiple sclerosis | 99.58% | DL |
| 2 | progressive relapsing multiple sclerosis | 99.34% | DL |
| 3 | transient neonatal thrombocytopenia | 97.90% | DL |
| 4 | thrombocytopenia | 97.83% | DL |
| 5 | marcothrombocytopenia with mitral valve insufficiency | 97.73% | DL |
| 6 | hereditary thrombocytopenia with normal platelets | 97.71% | DL |
| 7 | relapsing-remitting multiple sclerosis | 97.68% | DL |
| 8 | dense granule disease | 97.49% | DL |
| 9 | colonic neoplasm | 96.66% | DL |
| 10 | psoriasis | 96.43% | DL |
| 11 | cecum villous adenoma | 96.17% | DL |
| 12 | rectosigmoid junction neoplasm | 96.13% | DL |
| 13 | lipoma of colon | 96.11% | DL |
| 14 | cecum neuroendocrine tumor G1 | 96.09% | DL |
| 15 | cecal disease | 96.09% | DL |
| 16 | colon leiomyoma | 96.07% | DL |
| 17 | benign neoplasm of cecum | 96.03% | DL |
| 18 | colonic lymphangioma | 96.03% | DL |
| 19 | cavernous hemangioma of colon | 95.78% | DL |
| 20 | pityriasis lichenoides | 94.92% | DL |

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
