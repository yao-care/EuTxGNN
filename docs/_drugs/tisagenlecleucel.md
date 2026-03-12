---
layout: default
title: Tisagenlecleucel
description: "Tisagenlecleucel drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 587
evidence_level: L5
indication_count: 50
---

# Tisagenlecleucel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tisagenlecleucel |
| DrugBank ID | [DB13881](https://go.drugbank.com/drugs/DB13881) |
| Brand Names (EU) | Kymriah |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 91.39% |

---

## Approved Indication (EMA)

Kymriah is indicated for the treatment of: • Paediatric and young adult patients up to and including 25 years of age with B cell acute lymphoblastic leukaemia (ALL) that is refractory, in relapse post transplant or in second or later relapse. • Adult patients with relapsed or refractory diffuse large B cell lymphoma (DLBCL) after two or more lines of systemic therapy. • Adult patients with relapsed or refractory follicular lymphoma (FL) after two or more lines of systemic therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Crohn's colitis | 91.39% | DL |
| 2 | multiple endocrine neoplasia | 91.34% | DL |
| 3 | idiopathic aplastic anemia | 89.69% | DL |
| 4 | adrenal gland hyperfunction | 88.34% | DL |
| 5 | HER2 positive breast carcinoma | 88.02% | DL |
| 6 | ankylosing spondylitis | 87.11% | DL |
| 7 | lymphoadenopathic mastocytosis with eosinophilia | 87.04% | DL |
| 8 | systemic mastocytosis | 87.00% | DL |
| 9 | Smouldering systemic mastocytosis | 86.83% | DL |
| 10 | rheumatoid vasculitis | 86.24% | DL |
| 11 | normal breast-like subtype of breast carcinoma | 85.85% | DL |
| 12 | progesterone-receptor positive breast cancer | 85.85% | DL |
| 13 | breast tumor luminal A or B | 85.64% | DL |
| 14 | hypermobility of coccyx | 85.64% | DL |
| 15 | polyarticular juvenile rheumatoid arthritis | 85.59% | DL |
| 16 | inflammatory spondylopathy | 85.54% | DL |
| 17 | multifocal choroiditis | 85.49% | DL |
| 18 | drug-induced osteoporosis | 85.45% | DL |
| 19 | progesterone-receptor negative breast cancer | 85.12% | DL |
| 20 | psoriasis | 85.06% | DL |

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
