---
layout: default
title: Treprostinil Sodium
description: "Treprostinil Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 608
evidence_level: L5
indication_count: 50
---

# Treprostinil Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Treprostinil Sodium |
| DrugBank ID | [DB00374](https://go.drugbank.com/drugs/DB00374) |
| Brand Names (EU) | Trepulmix |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.70% |

---

## Approved Indication (EMA)

Treatment of adult patients with WHO Functional Class (FC) III or IV and:  inoperable chronic thromboembolic pulmonary hypertension (CTEPH), or persistent or recurrent CTEPH after surgical treatment  to improve exercise capacity.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary arteriovenous malformation (disease) | 99.70% | DL |
| 2 | pulmonary arterial hypertension | 99.62% | DL |
| 3 | pulmonary arterial hypertension associated with congenital heart disease | 99.60% | DL |
| 4 | pulmonary arterial hypertension associated with HIV infection | 99.55% | DL |
| 5 | pulmonary arterial hypertension associated with connective tissue disease | 99.55% | DL |
| 6 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.55% | DL |
| 7 | pulmonary arterial hypertension associated with schistosomiasis | 99.55% | DL |
| 8 | hypotrichosis simplex of the scalp | 99.48% | DL |
| 9 | congenital hypotrichosis milia | 99.30% | DL |
| 10 | malformation syndrome with odontal and/or periodontal component | 99.21% | DL |
| 11 | Ambras type hypertrichosis universalis congenita | 99.17% | DL |
| 12 | diffuse alopecia areata | 99.17% | DL |
| 13 | hypertrichosis (disease) | 99.16% | DL |
| 14 | syndrome with a Dandy-Walker malformation as major feature | 99.12% | DL |
| 15 | isolated genetic hair shaft abnormality | 99.08% | DL |
| 16 | alopecia | 98.54% | DL |
| 17 | pulmonary hypertension, primary, autosomal recessive | 97.80% | DL |
| 18 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 97.79% | DL |
| 19 | telangiectasia, hereditary hemorrhagic, | 97.50% | DL |
| 20 | familial clubfoot due to 17q23.1q23.2 microduplication | 97.33% | DL |

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
