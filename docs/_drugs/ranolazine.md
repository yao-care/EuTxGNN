---
layout: default
title: Ranolazine
description: "Ranolazine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 479
evidence_level: L5
indication_count: 50
---

# Ranolazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ranolazine |
| DrugBank ID | [DB00243](https://go.drugbank.com/drugs/DB00243) |
| Brand Names (EU) | Ranexa (previously Latixa) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.65% |

---

## Approved Indication (EMA)

Ranexa is indicated as add-on therapy for the symptomatic treatment of patients with stable angina pectoris who are inadequately controlled or intolerant to first-line anti-anginal therapies (such as beta-blockers and / or calcium antagonists).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.65% | DL |
| 2 | rheumatoid arthritis | 99.00% | DL |
| 3 | brachydactyly-syndactyly syndrome | 98.26% | DL |
| 4 | myositis fibrosa | 97.80% | DL |
| 5 | idiopathic granulomatous myositis | 97.80% | DL |
| 6 | tendinitis | 97.76% | DL |
| 7 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.64% | DL |
| 8 | fibromyalgia | 97.63% | DL |
| 9 | headache disorder | 97.36% | DL |
| 10 | conjunctivitis | 97.26% | DL |
| 11 | gout | 97.05% | DL |
| 12 | nephrogenic diabetes insipidus | 96.90% | DL |
| 13 | trigeminal autonomic cephalalgia | 96.76% | DL |
| 14 | duodenal obstruction | 96.67% | DL |
| 15 | pulmonary hypertension | 96.34% | DL |
| 16 | gastrin secretion abnormality | 96.33% | DL |
| 17 | bronchitis | 96.28% | DL |
| 18 | duodenal ulcer (disease) | 96.25% | DL |
| 19 | inclusion body myositis | 96.25% | DL |
| 20 | kyphoscoliotic heart disease | 96.23% | DL |

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
