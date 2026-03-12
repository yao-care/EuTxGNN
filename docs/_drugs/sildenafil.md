---
layout: default
title: Sildenafil
description: "Sildenafil drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 527
evidence_level: L5
indication_count: 53
---

# Sildenafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Sildenafil |
| DrugBank ID | [DB00203](https://go.drugbank.com/drugs/DB00203) |
| Brand Names (EU) | Mysildecard, Sildenafil ratiopharm, Vizarsin |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 98.41% |

---

## Approved Indication (EMA)

Treatment of men with erectile dysfunction, which is the inability to achieve or maintain a penile erection sufficient for satisfactory sexual performance. In order for sildenafil to be effective, sexual stimulation is required.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Ambras type hypertrichosis universalis congenita | 98.41% | DL |
| 2 | malformation syndrome with odontal and/or periodontal component | 98.23% | DL |
| 3 | syndrome with a Dandy-Walker malformation as major feature | 98.03% | DL |
| 4 | isolated genetic hair shaft abnormality | 97.86% | DL |
| 5 | hypertrichosis (disease) | 97.83% | DL |
| 6 | homozygous familial hypercholesterolemia | 93.77% | DL |
| 7 | hypoalphalipoproteinemia | 90.11% | DL |
| 8 | familial isolated trichomegaly | 79.78% | DL |
| 9 | genetic alopecia | 75.03% | DL |
| 10 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 70.00% | DL |
| 11 | hypotrichosis simplex of the scalp | 69.88% | DL |
| 12 | pulmonary hypertension, primary, autosomal recessive | 69.19% | DL |
| 13 | familial clubfoot due to 17q23.1q23.2 microduplication | 68.83% | DL |
| 14 | kyphoscoliotic heart disease | 68.49% | DL |
| 15 | pulmonary hypertension | 68.06% | DL |
| 16 | migraine with brainstem aura | 67.69% | DL |
| 17 | chromosome 17q23.1-q23.2 deletion syndrome | 66.76% | DL |
| 18 | pulmonary arterial hypertension associated with congenital heart disease | 66.60% | DL |
| 19 | congenital hypotrichosis milia | 66.08% | DL |
| 20 | coxopodopatellar syndrome | 65.68% | DL |

*Showing top 20 of 53 predictions.*

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
