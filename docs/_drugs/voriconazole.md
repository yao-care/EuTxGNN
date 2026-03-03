---
layout: default
title: Voriconazole
description: "Voriconazole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 641
evidence_level: L5
indication_count: 50
---

# Voriconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Voriconazole |
| DrugBank ID | [DB00582](https://go.drugbank.com/drugs/DB00582) |
| Brand Names (EU) | Voriconazole Accord |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.29% |

---

## Approved Indication (EMA)

Voriconazole is a broad-spectrum, triazole antifungal agent and is indicated in adults and children aged two years and above as follows:  treatment of invasive aspergillosis; treatment of candidaemia in non-neutropenic patients; treatment of fluconazole-resistant serious invasive Candida infections (including C. krusei); Treatment of serious fungal infections caused by Scedosporium spp. and Fusarium spp.  Voriconazole Accord should be administered primarily to patients with progressive, possibly

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | fusariosis | 99.29% | DL |
| 2 | multidrug-resistant tuberculosis | 98.67% | DL |
| 3 | cysticercosis | 98.34% | DL |
| 4 | Ambras type hypertrichosis universalis congenita | 98.28% | DL |
| 5 | syndrome with a Dandy-Walker malformation as major feature | 98.15% | DL |
| 6 | malformation syndrome with odontal and/or periodontal component | 98.13% | DL |
| 7 | tuberculosis, bovine | 98.10% | DL |
| 8 | isolated genetic hair shaft abnormality | 98.08% | DL |
| 9 | tuberculosis, avian | 98.04% | DL |
| 10 | tuberculoma | 98.04% | DL |
| 11 | tuberculous ascites | 98.04% | DL |
| 12 | inactive tuberculosis | 98.04% | DL |
| 13 | hypertrichosis (disease) | 98.00% | DL |
| 14 | esophageal candidiasis | 97.66% | DL |
| 15 | coenurosis | 97.64% | DL |
| 16 | trichosporonosis | 97.59% | DL |
| 17 | hyalohyphomycosis | 97.59% | DL |
| 18 | penicilliosis | 97.59% | DL |
| 19 | geotrichosis | 97.59% | DL |
| 20 | maple bark strippers' lung | 97.58% | DL |

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
