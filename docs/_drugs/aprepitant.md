---
layout: default
title: Aprepitant
description: "Aprepitant drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 46
evidence_level: L5
indication_count: 50
---

# Aprepitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aprepitant |
| DrugBank ID | [DB00673](https://go.drugbank.com/drugs/DB00673) |
| Brand Names (EU) | Emend |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Emend 40 mg hard capsules is indicated for the prevention of postoperative nausea and vomiting (PONV) in adults. Emend is also available as 80 mg and 125 mg hard capsules for the prevention of nausea and vomiting associated with highly and moderately emetogenic cancer chemotherapy in adults and adolescents from the age of 12 (see separate Summary of Product Characteristics). Emend is also available as 165 mg hard capsules for the prevention of acute and delayed nausea and vomiting associated wit

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.97% | DL |
| 2 | hypertrichosis (disease) | 99.91% | DL |
| 3 | pulmonary hypertension | 99.90% | DL |
| 4 | leprosy | 99.90% | DL |
| 5 | Ambras type hypertrichosis universalis congenita | 99.87% | DL |
| 6 | malformation syndrome with odontal and/or periodontal component | 99.86% | DL |
| 7 | kyphoscoliotic heart disease | 99.86% | DL |
| 8 | syndrome with a Dandy-Walker malformation as major feature | 99.86% | DL |
| 9 | subarachnoid hemorrhage (disease) | 99.85% | DL |
| 10 | isolated genetic hair shaft abnormality | 99.85% | DL |
| 11 | persistent Mullerian duct syndrome | 99.63% | DL |
| 12 | multiple endocrine neoplasia | 99.61% | DL |
| 13 | nephrogenic diabetes insipidus | 99.47% | DL |
| 14 | pulmonary hypertension, primary, autosomal recessive | 99.42% | DL |
| 15 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 99.39% | DL |
| 16 | chromosome 17q23.1-q23.2 deletion syndrome | 99.28% | DL |
| 17 | familial clubfoot due to 17q23.1q23.2 microduplication | 99.28% | DL |
| 18 | acquired aneurysmal subarachnoid hemorrhage | 99.26% | DL |
| 19 | coxopodopatellar syndrome | 99.24% | DL |
| 20 | hypoalphalipoproteinemia | 99.19% | DL |

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
