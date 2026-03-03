---
layout: default
title: Abemaciclib
description: "Abemaciclib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 13
evidence_level: L5
indication_count: 50
---

# Abemaciclib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Abemaciclib |
| DrugBank ID | [DB12001](https://go.drugbank.com/drugs/DB12001) |
| Brand Names (EU) | Verzenios |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.32% |

---

## Approved Indication (EMA)

Early Breast Cancer Verzenios in combination with endocrine therapy is indicated for the adjuvant treatment of adult patients with hormone receptor (HR) positive, human epidermal growth factor receptor 2 (HER2) negative, node positive early breast cancer at high risk of recurrence (see section 5.1). In pre or perimenopausal women, aromatase inhibitor endocrine therapy should be combined with a luteinising hormone-releasing hormone (LHRH) agonist. Advanced or Metastatic Breast Cancer Verzenios is

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 97.32% | DL |
| 2 | hyperthyroidism | 97.17% | DL |
| 3 | multiple endocrine neoplasia | 97.07% | DL |
| 4 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 96.88% | DL |
| 5 | homozygous familial hypercholesterolemia | 96.56% | DL |
| 6 | heart disease | 96.30% | DL |
| 7 | Laubry-Pezzi syndrome | 96.30% | DL |
| 8 | Pierre Robin syndrome associated with a chromosomal anomaly | 96.29% | DL |
| 9 | Jeune syndrome situs inversus | 96.23% | DL |
| 10 | amyotrophic lateral sclerosis | 96.23% | DL |
| 11 | genetic syndromic Pierre Robin syndrome | 96.21% | DL |
| 12 | orofacial clefting syndrome | 96.17% | DL |
| 13 | interventricular septum aneurysm | 96.17% | DL |
| 14 | partial deletion of the long arm of chromosome 7 | 96.16% | DL |
| 15 | disorder of fucoglycosan synthesis | 96.12% | DL |
| 16 | partial deletion of the long arm of chromosome 22 | 96.02% | DL |
| 17 | pulmonary valve disease | 96.01% | DL |
| 18 | brachydactyly-syndactyly syndrome | 95.99% | DL |
| 19 | mitral valve disease | 95.82% | DL |
| 20 | amyotrophic lateral sclerosis, susceptibility to | 95.70% | DL |

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
