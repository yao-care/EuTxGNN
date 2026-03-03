---
layout: default
title: Selpercatinib
description: "Selpercatinib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 522
evidence_level: L5
indication_count: 50
---

# Selpercatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Selpercatinib |
| DrugBank ID | [DB15685](https://go.drugbank.com/drugs/DB15685) |
| Brand Names (EU) | Retsevmo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.18% |

---

## Approved Indication (EMA)

Retsevmo as monotherapy is indicated for the treatment of adults with:&nbsp;– advanced RET fusion positive non small cell lung cancer (NSCLC) not previously treated with a RET inhibitor– advanced RET fusion positive solid tumours, when treatment options not targeting RET provide limited clinical benefit, or have been exhausted (see sections 4.4 and 5.1)Retsevmo as monotherapy is indicated for the treatment of adults and adolescents 12 years and older with:– advanced RET fusion positive thyroid c

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary hypertension | 99.18% | DL |
| 2 | migraine disorder | 99.17% | DL |
| 3 | migraine with brainstem aura | 99.05% | DL |
| 4 | kyphoscoliotic heart disease | 98.96% | DL |
| 5 | migraine with or without aura, susceptibility to | 97.99% | DL |
| 6 | pulmonary hypertension, primary, autosomal recessive | 97.74% | DL |
| 7 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 97.32% | DL |
| 8 | idiopathic pulmonary arterial hypertension | 97.03% | DL |
| 9 | atrophoderma vermiculata | 97.02% | DL |
| 10 | coxopodopatellar syndrome | 96.94% | DL |
| 11 | familial clubfoot due to 17q23.1q23.2 microduplication | 96.93% | DL |
| 12 | chromosome 17q23.1-q23.2 deletion syndrome | 96.89% | DL |
| 13 | pulmonary hypertension, primary | 96.84% | DL |
| 14 | ulerythema ophryogenesis | 96.63% | DL |
| 15 | idiopathic and/or familial pulmonary arterial hypertension | 96.27% | DL |
| 16 | hypertrichosis (disease) | 96.25% | DL |
| 17 | gastrointestinal hamartoma | 96.19% | DL |
| 18 | pulmonary arterial hypertension | 96.07% | DL |
| 19 | malformation syndrome with odontal and/or periodontal component | 96.05% | DL |
| 20 | Ambras type hypertrichosis universalis congenita | 96.05% | DL |

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
