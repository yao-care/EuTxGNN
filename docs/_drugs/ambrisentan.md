---
layout: default
title: Ambrisentan
description: "Ambrisentan drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 33
evidence_level: L5
indication_count: 50
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ambrisentan |
| DrugBank ID | [DB06403](https://go.drugbank.com/drugs/DB06403) |
| Brand Names (EU) | Volibris |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.41% |

---

## Approved Indication (EMA)

Volibris is indicated for treatment of pulmonary arterial hypertension (PAH) in adult patients of WHO Functional Class (FC) II to III, including use in combination treatment (see section 5.1).  Efficacy has been shown in idiopathic PAH (IPAH) and in PAH associated with connective tissue disease. Volibris is indicated for treatment of PAH in adolescents and children (aged 8 to less than 18 years) of WHO Functional Class (FC) II to III including use in combination treatment. Efficacy has been show

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary arteriovenous malformation (disease) | 99.41% | DL |
| 2 | pulmonary arterial hypertension associated with congenital heart disease | 99.37% | DL |
| 3 | pulmonary arterial hypertension | 99.37% | DL |
| 4 | pulmonary arterial hypertension associated with schistosomiasis | 99.30% | DL |
| 5 | pulmonary arterial hypertension associated with HIV infection | 99.30% | DL |
| 6 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 99.30% | DL |
| 7 | pulmonary arterial hypertension associated with connective tissue disease | 99.30% | DL |
| 8 | malformation syndrome with odontal and/or periodontal component | 99.19% | DL |
| 9 | hypotrichosis simplex of the scalp | 99.15% | DL |
| 10 | hypertrichosis (disease) | 99.14% | DL |
| 11 | syndrome with a Dandy-Walker malformation as major feature | 99.12% | DL |
| 12 | isolated genetic hair shaft abnormality | 99.04% | DL |
| 13 | Ambras type hypertrichosis universalis congenita | 99.02% | DL |
| 14 | congenital hypotrichosis milia | 98.77% | DL |
| 15 | diffuse alopecia areata | 98.62% | DL |
| 16 | alopecia | 96.98% | DL |
| 17 | telangiectasia, hereditary hemorrhagic, | 95.48% | DL |
| 18 | pulmonary hypertension, primary | 92.60% | DL |
| 19 | genetic alopecia | 92.46% | DL |
| 20 | obsolete patella aplasia, coxa vara, and tarsal synostosis | 92.40% | DL |

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
