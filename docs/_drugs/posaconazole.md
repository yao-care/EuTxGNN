---
layout: default
title: Posaconazole
description: "Posaconazole drug repurposing predictions from TxGNN. Evidence level L5 with 56 predicted indications."
parent: AI Predictions (L5)
nav_order: 466
evidence_level: L5
indication_count: 56
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **56**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Posaconazole |
| DrugBank ID | [DB01263](https://go.drugbank.com/drugs/DB01263) |
| Brand Names (EU) | Posaconazole AHCL, Posaconazole Accord |
| Evidence Level | L5 |
| Predicted Indications | 56 |
| Top Prediction Score | 99.77% |

---

## Approved Indication (EMA)

Posaconazole AHCL oral suspension is indicated for use in the treatment of the following fungal infections in adults:  Invasive aspergillosis in patients with disease that is refractory to amphotericin B or itraconazole or in patients who are intolerant of these medicinal products; Fusariosis in patients with disease that is refractory to amphotericin B or in patients who are intolerant of amphotericin B; Chromoblastomycosis and mycetoma in patients with disease that is refractory to itraconazol

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pneumocystosis | 99.77% | DL |
| 2 | mycetoma | 99.36% | DL |
| 3 | aspergillosis | 98.98% | DL |
| 4 | vulvovaginal candidiasis | 98.92% | DL |
| 5 | leprosy | 98.84% | DL |
| 6 | candidiasis | 98.73% | DL |
| 7 | multibacillary leprosy | 98.61% | DL |
| 8 | Ambras type hypertrichosis universalis congenita | 98.55% | DL |
| 9 | malformation syndrome with odontal and/or periodontal component | 98.46% | DL |
| 10 | isolated genetic hair shaft abnormality | 98.44% | DL |
| 11 | syndrome with a Dandy-Walker malformation as major feature | 98.43% | DL |
| 12 | hypertrichosis (disease) | 98.35% | DL |
| 13 | fusariosis | 98.08% | DL |
| 14 | paucibacillary leprosy | 97.98% | DL |
| 15 | lepromatous leprosy | 97.84% | DL |
| 16 | borderline leprosy | 97.84% | DL |
| 17 | multidrug-resistant tuberculosis | 97.77% | DL |
| 18 | hyperargininemia | 97.50% | DL |
| 19 | Cryptococcal meningitis | 97.36% | DL |
| 20 | geotrichosis | 97.01% | DL |

*Showing top 20 of 56 predictions.*

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
