---
layout: default
title: Fidaxomicin
description: "Fidaxomicin drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 244
evidence_level: L5
indication_count: 51
---

# Fidaxomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fidaxomicin |
| DrugBank ID | [DB08874](https://go.drugbank.com/drugs/DB08874) |
| Brand Names (EU) | Dificlir |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Dificlir film-coated tablets is indicated for the treatment of Clostridioides difficile infections (CDI) also known as C. difficile-associated diarrhoea (CDAD) in adult and paediatric patients with a body weight of at least 12.5 kg. Consideration should be given to official guidelines on the appropriate use of antibacterial agents. Dificlir granules for oral suspension is indicated for the treatment of Clostridioides  difficile infections (CDI) also known as C. difficile-associated diarrhoea (CD

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | staphylococcal scalded skin syndrome | 99.71% | DL |
| 2 | Clostridium infectious disease | 99.70% | DL |
| 3 | bullous impetigo | 99.70% | DL |
| 4 | inhalational botulism | 99.69% | DL |
| 5 | impetigo | 99.68% | DL |
| 6 | toxin-mediated infectious botulism | 99.66% | DL |
| 7 | vulvovaginal candidiasis | 99.65% | DL |
| 8 | hordeolum | 99.64% | DL |
| 9 | staphylococcus aureus pneumonia | 99.21% | DL |
| 10 | punctate epithelial keratoconjunctivitis | 99.02% | DL |
| 11 | parasitic skin disease | 98.62% | DL |
| 12 | aleutian mink disease | 98.45% | DL |
| 13 | feline panleukopenia | 98.42% | DL |
| 14 | hyperamylasemia | 98.41% | DL |
| 15 | polyclonal hyperviscosity syndrome | 98.41% | DL |
| 16 | pleural empyema (disease) | 98.33% | DL |
| 17 | fascioliasis | 98.32% | DL |
| 18 | erythema infectiosum | 98.30% | DL |
| 19 | congenital analbuminemia | 98.20% | DL |
| 20 | candidemia | 98.15% | DL |

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
