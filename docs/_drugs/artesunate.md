---
layout: default
title: Artesunate
description: "Artesunate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 50
evidence_level: L5
indication_count: 50
---

# Artesunate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Artesunate |
| DrugBank ID | [DB09274](https://go.drugbank.com/drugs/DB09274) |
| Brand Names (EU) | Artesunate Amivas |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 85.66% |

---

## Approved Indication (EMA)

Artesunate Amivas is indicated for the initial treatment of severe malaria in adults and children. Consideration should be given to official guidance on the appropriate use of antimalarial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malaria | 85.66% | DL |
| 2 | acne (disease) | 79.21% | DL |
| 3 | Smouldering systemic mastocytosis | 79.18% | DL |
| 4 | lymphoadenopathic mastocytosis with eosinophilia | 77.26% | DL |
| 5 | gastrin secretion abnormality | 76.71% | DL |
| 6 | systemic mastocytosis | 71.44% | DL |
| 7 | leishmaniasis, diffuse cutaneous | 66.16% | DL |
| 8 | abnormality of glucagon secretion | 61.77% | DL |
| 9 | pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 59.66% | DL |
| 10 | Wiskott-Aldrich syndrome 2 | 59.41% | DL |
| 11 | alacrima, achalasia, and intellectual disability syndrome | 59.33% | DL |
| 12 | GATA1-Related X-Linked Cytopenia | 57.09% | DL |
| 13 | inherited Fanconi renotubular syndrome | 57.00% | DL |
| 14 | acquired hypertrichosis lanuginosa | 56.96% | DL |
| 15 | ABetaL34V amyloidosis | 56.87% | DL |
| 16 | Ramon syndrome | 56.85% | DL |
| 17 | thiopurine immunosuppressant-induced pancreatitis | 56.72% | DL |
| 18 | Coronavinae infectious disease | 56.52% | DL |
| 19 | familial Mediterranean fever, autosomal dominant | 56.34% | DL |
| 20 | Zollinger-Ellison syndrome | 56.30% | DL |

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
