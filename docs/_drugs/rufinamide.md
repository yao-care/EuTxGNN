---
layout: default
title: Rufinamide
description: "Rufinamide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 511
evidence_level: L5
indication_count: 50
---

# Rufinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rufinamide |
| DrugBank ID | [DB06201](https://go.drugbank.com/drugs/DB06201) |
| Brand Names (EU) | Inovelon |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.59% |

---

## Approved Indication (EMA)

Inovelon is indicated as adjunctive therapy in the treatment of seizures associated with Lennox Gastaut syndrome in patients 4 years of age and older.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Lennox-Gastaut syndrome | 99.59% | DL |
| 2 | febrile infection-related epilepsy syndrome | 99.57% | DL |
| 3 | perioral myoclonia with absences | 99.51% | DL |
| 4 | photosensitive occipital lobe epilepsy | 99.44% | DL |
| 5 | cryptogenic late-onset epileptic spasms | 99.44% | DL |
| 6 | atypical childhood epilepsy with centrotemporal spikes | 99.44% | DL |
| 7 | cutis verticis gyrata | 98.66% | DL |
| 8 | trigeminal nerve neoplasm | 97.91% | DL |
| 9 | benign occipital epilepsy | 97.75% | DL |
| 10 | childhood onset epileptic encephalopathy | 97.71% | DL |
| 11 | early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation | 96.37% | DL |
| 12 | renal-hepatic-pancreatic dysplasia | 96.26% | DL |
| 13 | polycystic kidney disease 3 with or without polycystic liver disease | 95.53% | DL |
| 14 | Joubert syndrome with renal defect | 95.37% | DL |
| 15 | karyomegalic interstitial nephritis | 95.22% | DL |
| 16 | thoracic malformation | 95.15% | DL |
| 17 | adult familial nephronophthisis-spastic quadriparesia syndrome | 94.98% | DL |
| 18 | early onset absence epilepsy | 94.89% | DL |
| 19 | acute encephalopathy with biphasic seizures and late reduced diffusion | 94.86% | DL |
| 20 | trigeminal neuralgia | 93.46% | DL |

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
