---
layout: default
title: Bimatoprost
description: "bimatoprost drug repurposing predictions from TxGNN. Evidence level L2 with 51 predicted indications."
parent: Phase 2 Evidence (L2)
nav_order: 82
evidence_level: L2
indication_count: 51
---

# Bimatoprost
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bimatoprost |
| DrugBank ID | [DB00905](https://go.drugbank.com/drugs/DB00905) |
| Brand Names (EU) | Lumigan |
| Evidence Level | L2 |
| Predicted Indications | 51 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Reduction of elevated intraocular pressure in chronic open-angle glaucoma and ocular hypertension (as monotherapy or as adjunctive therapy to beta-blockers).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hypertrichosis (disease) | 100.00% | DL |
| 2 | malformation syndrome with odontal and/or periodontal component | 100.00% | DL |
| 3 | syndrome with a Dandy-Walker malformation as major feature | 100.00% | DL |
| 4 | isolated genetic hair shaft abnormality | 100.00% | DL |
| 5 | Ambras type hypertrichosis universalis congenita | 100.00% | DL |
| 6 | hypotrichosis simplex of the scalp | 100.00% | DL |
| 7 | congenital hypotrichosis milia | 99.99% | DL |
| 8 | diffuse alopecia areata | 99.99% | DL |
| 9 | alopecia | 99.99% | DL |
| 10 | genetic alopecia | 99.97% | DL |
| 11 | pulmonary arteriovenous malformation (disease) | 99.95% | DL |
| 12 | pulmonary arterial hypertension | 99.95% | DL |
| 13 | pulmonary arterial hypertension associated with congenital heart disease | 99.95% | DL |
| 14 | pulmonary arterial hypertension associated with connective tissue disease | 99.94% | DL |
| 15 | pulmonary arterial hypertension associated with schistosomiasis | 99.94% | DL |
| 16 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.94% | DL |
| 17 | pulmonary arterial hypertension associated with HIV infection | 99.94% | DL |
| 18 | polycystic kidney disease 3 with or without polycystic liver disease | 99.80% | DL |
| 19 | pseudopelade of Brocq | 99.77% | DL |
| 20 | thoracic malformation | 99.72% | DL |

*Showing top 20 of 51 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| alopecia | L2 | 11 | 20 | 4 Phase 2 trial(s), 1 RCT(s), 1 review(s)/meta-ana |
| hypertrichosis (disease) | L4 | 2 | 0 | AI prediction only |

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
