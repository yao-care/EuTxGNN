---
layout: default
title: Choriogonadotropin Alfa
description: "Choriogonadotropin Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 134
evidence_level: L5
indication_count: 50
---

# Choriogonadotropin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Choriogonadotropin Alfa |
| DrugBank ID | [DB00097](https://go.drugbank.com/drugs/DB00097) |
| Brand Names (EU) | Ovitrelle |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.44% |

---

## Approved Indication (EMA)

Ovitrelle is indicated in the treatment of:  women undergoing superovulation prior to assisted reproductive techniques such as in vitro fertilisation (IVF): Ovitrelle is administered to trigger final follicular maturation and luteinisation after stimulation of follicular growth; anovulatory or oligo-ovulatory women: Ovitrelle is administered to trigger ovulation and luteinisation in anovulatory or oligo-ovulatory patients after stimulation of follicular growth.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | peptic esophagitis | 98.44% | DL |
| 2 | postural orthostatic tachycardia syndrome | 98.33% | DL |
| 3 | esophageal disease | 97.61% | DL |
| 4 | Raynaud disease | 97.43% | DL |
| 5 | non-syndromic esophageal malformation | 96.89% | DL |
| 6 | esophageal ulcer | 96.84% | DL |
| 7 | His bundle tachycardia | 95.95% | DL |
| 8 | sinoatrial block | 95.88% | DL |
| 9 | progressive familial heart block | 95.66% | DL |
| 10 | sinoatrial node disease | 95.47% | DL |
| 11 | restless legs syndrome | 95.43% | DL |
| 12 | esophageal atresia (disease) | 95.34% | DL |
| 13 | active peptic ulcer disease | 95.31% | DL |
| 14 | gastrojejunal ulcer | 95.30% | DL |
| 15 | peptic ulcer perforation | 95.30% | DL |
| 16 | migraine disorder | 95.28% | DL |
| 17 | esophageal leukoplakia (disease) | 95.23% | DL |
| 18 | acne (disease) | 95.16% | DL |
| 19 | dyskinesia of esophagus | 95.16% | DL |
| 20 | esophageal diverticulosis | 95.16% | DL |

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
