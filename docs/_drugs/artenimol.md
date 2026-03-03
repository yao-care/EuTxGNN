---
layout: default
title: Artenimol
description: "Artenimol drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 49
evidence_level: L5
indication_count: 50
---

# Artenimol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Artenimol |
| DrugBank ID | [DB11638](https://go.drugbank.com/drugs/DB11638) |
| Brand Names (EU) | Artenimol |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.87% |

---

## Approved Indication (EMA)

Eurartesim is indicated for the treatment of uncomplicated Plasmodium falciparum malaria in adults, children and infants 6 months and over and weighing 5 kg or more. Consideration should be given to official guidance on the appropriate use of antimalarial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | malaria | 99.87% | DL |
| 2 | Smouldering systemic mastocytosis | 98.67% | DL |
| 3 | lymphoadenopathic mastocytosis with eosinophilia | 98.42% | DL |
| 4 | systemic mastocytosis | 98.28% | DL |
| 5 | Plasmodium vivax malaria | 97.30% | DL |
| 6 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 97.17% | DL |
| 7 | juvenile chronic polyarthritis | 96.61% | DL |
| 8 | rheumatoid nodulosis | 96.57% | DL |
| 9 | juvenile idiopathic arthritis | 96.57% | DL |
| 10 | West syndrome | 96.33% | DL |
| 11 | intellectual disability, X-linked, with or without seizures, arx-related | 95.87% | DL |
| 12 | echinococcus granulosus infectious disease | 94.27% | DL |
| 13 | alveolar echinococcosis | 93.21% | DL |
| 14 | gastrin secretion abnormality | 93.02% | DL |
| 15 | cystic echinococcosis | 93.00% | DL |
| 16 | enterobiasis | 92.44% | DL |
| 17 | pseudoachondroplasia | 92.11% | DL |
| 18 | juvenile arthritis due to defect in LACC1 | 91.98% | DL |
| 19 | acne (disease) | 90.97% | DL |
| 20 | monosomy X | 90.56% | DL |

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
