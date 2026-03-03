---
layout: default
title: Corifollitropin Alfa
description: "Corifollitropin Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 146
evidence_level: L5
indication_count: 50
---

# Corifollitropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Corifollitropin Alfa |
| DrugBank ID | [DB09066](https://go.drugbank.com/drugs/DB09066) |
| Brand Names (EU) | Elonva |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.65% |

---

## Approved Indication (EMA)

Controlled Ovarian Stimulation (COS) in combination with a GnRH antagonist for the development of multiple follicles in women participating in an Assisted Reproductive Technology (ART) program. Elonva is indicated for the treatment of adolescent males (14 to less than 18 years and older) with hypogonadotropic hypogonadism, in combination with human Chorionic Gonadotropin (hCG).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | gastroduodenitis | 99.65% | DL |
| 2 | migraine disorder | 99.63% | DL |
| 3 | peptic ulcer disease | 99.61% | DL |
| 4 | migraine with brainstem aura | 99.59% | DL |
| 5 | Raynaud disease | 99.59% | DL |
| 6 | pulmonary hypertension | 99.44% | DL |
| 7 | kyphoscoliotic heart disease | 99.36% | DL |
| 8 | migraine with or without aura, susceptibility to | 99.11% | DL |
| 9 | atrophoderma vermiculata | 98.81% | DL |
| 10 | peptic esophagitis | 98.68% | DL |
| 11 | ulerythema ophryogenesis | 98.67% | DL |
| 12 | hypotrichosis simplex of the scalp | 98.61% | DL |
| 13 | congenital hypotrichosis milia | 98.34% | DL |
| 14 | alopecia | 98.29% | DL |
| 15 | pulmonary hypertension, primary, autosomal recessive | 98.27% | DL |
| 16 | diffuse alopecia areata | 98.23% | DL |
| 17 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 97.61% | DL |
| 18 | chromosome 17q23.1-q23.2 deletion syndrome | 97.53% | DL |
| 19 | familial clubfoot due to 17q23.1q23.2 microduplication | 97.52% | DL |
| 20 | coxopodopatellar syndrome | 97.15% | DL |

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
