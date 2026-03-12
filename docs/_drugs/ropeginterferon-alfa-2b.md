---
layout: default
title: Ropeginterferon Alfa-2B
description: "Ropeginterferon Alfa-2B drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 507
evidence_level: L5
indication_count: 50
---

# Ropeginterferon Alfa-2B
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ropeginterferon Alfa-2B |
| DrugBank ID | [DB15119](https://go.drugbank.com/drugs/DB15119) |
| Brand Names (EU) | Besremi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Besremi is indicated as monotherapy in adults for the treatment of polycythaemia vera without symptomatic splenomegaly.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Laubry-Pezzi syndrome | 99.93% | DL |
| 2 | interventricular septum aneurysm | 99.92% | DL |
| 3 | genetic syndromic Pierre Robin syndrome | 99.92% | DL |
| 4 | Pierre Robin syndrome associated with a chromosomal anomaly | 99.92% | DL |
| 5 | partial deletion of the long arm of chromosome 7 | 99.92% | DL |
| 6 | disorder of fucoglycosan synthesis | 99.92% | DL |
| 7 | Jeune syndrome situs inversus | 99.92% | DL |
| 8 | partial deletion of the long arm of chromosome 22 | 99.92% | DL |
| 9 | orofacial clefting syndrome | 99.91% | DL |
| 10 | pulmonary valve disease | 99.91% | DL |
| 11 | mitral valve disease | 99.91% | DL |
| 12 | heart disease | 99.90% | DL |
| 13 | plasmacytoma | 99.89% | DL |
| 14 | neurolymphomatosis | 99.79% | DL |
| 15 | polycythemia (disease) | 99.28% | DL |
| 16 | acquired secondary polycythemia | 99.22% | DL |
| 17 | congenital secondary polycythemia | 99.13% | DL |
| 18 | plasma cell myeloma | 98.82% | DL |
| 19 | indolent plasma cell myeloma | 98.81% | DL |
| 20 | heart conduction disease | 98.39% | DL |

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
