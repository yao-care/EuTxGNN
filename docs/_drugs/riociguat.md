---
layout: default
title: Riociguat
description: "Riociguat drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 495
evidence_level: L5
indication_count: 50
---

# Riociguat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Riociguat |
| DrugBank ID | [DB08931](https://go.drugbank.com/drugs/DB08931) |
| Brand Names (EU) | Adempas |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 94.92% |

---

## Approved Indication (EMA)

Chronic thromboembolic pulmonary hypertension (CTEPH) Adempas is indicated for the treatment of adult patients with WHO Functional Class (FC) II to III with  inoperable CTEPH, persistent or recurrent CTEPH after surgical treatment, to improve exercise capacity.  Pulmonary arterial hypertension (PAH) AdultsAdempas, as monotherapy or in combination with endothelin receptor antagonists, is indicated for the treatment of adult patients with pulmonary arterial hypertension (PAH) with WHO Functional C

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ambras type hypertrichosis universalis congenita | 94.92% | DL |
| 2 | malformation syndrome with odontal and/or periodontal component | 94.45% | DL |
| 3 | syndrome with a Dandy-Walker malformation as major feature | 94.27% | DL |
| 4 | isolated genetic hair shaft abnormality | 94.05% | DL |
| 5 | hypertrichosis (disease) | 93.81% | DL |
| 6 | pulmonary arterial hypertension associated with congenital heart disease | 92.58% | DL |
| 7 | pulmonary arteriovenous malformation (disease) | 92.08% | DL |
| 8 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 91.55% | DL |
| 9 | pulmonary arterial hypertension associated with HIV infection | 91.55% | DL |
| 10 | pulmonary arterial hypertension associated with schistosomiasis | 91.55% | DL |
| 11 | pulmonary arterial hypertension associated with connective tissue disease | 91.55% | DL |
| 12 | pulmonary arterial hypertension | 90.64% | DL |
| 13 | hypotrichosis simplex of the scalp | 87.51% | DL |
| 14 | congenital hypotrichosis milia | 85.94% | DL |
| 15 | diffuse alopecia areata | 84.93% | DL |
| 16 | polycystic kidney disease 3 with or without polycystic liver disease | 82.61% | DL |
| 17 | syndrome with limb duplication, polydactyly, syndactyly, and/or hyperphalangy | 81.56% | DL |
| 18 | thoracic malformation | 81.55% | DL |
| 19 | adult familial nephronophthisis-spastic quadriparesia syndrome | 79.91% | DL |
| 20 | renal-hepatic-pancreatic dysplasia | 79.67% | DL |

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
