---
layout: default
title: Pregabalin
description: "Pregabalin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 470
evidence_level: L5
indication_count: 51
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Pregabalin |
| DrugBank ID | [DB00230](https://go.drugbank.com/drugs/DB00230) |
| Brand Names (EU) | Pregabalin Accord, Pregabalin Zentiva |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Epilepsy  Pregabalin Accord is indicated as adjunctive therapy in adults with partial seizures with or without secondary generalisation.  Generalised Anxiety Disorder  Pregabalin Accord is indicated for the treatment of Generalised Anxiety Disorder (GAD) in adults.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | tendinitis | 99.71% | DL |
| 2 | idiopathic granulomatous myositis | 99.71% | DL |
| 3 | myositis fibrosa | 99.71% | DL |
| 4 | fibromyalgia | 99.65% | DL |
| 5 | inclusion body myositis | 99.52% | DL |
| 6 | migraine disorder | 99.47% | DL |
| 7 | migraine with brainstem aura | 99.43% | DL |
| 8 | osteoarthritis susceptibility | 98.74% | DL |
| 9 | myofascial pain syndrome | 98.64% | DL |
| 10 | osteoarthritis | 98.58% | DL |
| 11 | headache disorder | 97.63% | DL |
| 12 | atrophoderma vermiculata | 97.62% | DL |
| 13 | acromesomelic dysplasia, Hunter-Thompson type | 97.28% | DL |
| 14 | brachyolmia | 97.26% | DL |
| 15 | pseudoachondroplasia | 97.14% | DL |
| 16 | brachyolmia-amelogenesis imperfecta syndrome | 97.05% | DL |
| 17 | trigeminal autonomic cephalalgia | 97.01% | DL |
| 18 | ulerythema ophryogenesis | 97.01% | DL |
| 19 | myosclerosis | 96.69% | DL |
| 20 | migraine with or without aura, susceptibility to | 96.33% | DL |

*Showing top 20 of 51 predictions.*

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
