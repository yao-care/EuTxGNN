---
layout: default
title: Flutemetamol (18F)
description: "Flutemetamol (18F) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 251
evidence_level: L5
indication_count: 50
---

# Flutemetamol (18F)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Flutemetamol (18F) |
| DrugBank ID | [DB09151](https://go.drugbank.com/drugs/DB09151) |
| Brand Names (EU) | Vizamyl |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.79% |

---

## Approved Indication (EMA)

This medicinal product is for diagnostic use only. Vizamyl is a radiopharmaceutical medicinal product indicated for Positron Emission Tomography (PET) imaging of ? amyloid neuritic plaque density in the brains of adult patients with cognitive impairment who are being evaluated for Alzheimer’s disease (AD) and other causes of cognitive impairment. Vizamyl should be used in conjunction with a clinical evaluation. A negative scan indicates sparse or no plaques, which is not consistent with a diagno

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | anaphylaxis | 98.79% | DL |
| 2 | food-dependent exercise-induced anaphylaxis | 98.38% | DL |
| 3 | dermatitis | 96.99% | DL |
| 4 | pseudoallergy | 96.39% | DL |
| 5 | acne keloid | 96.24% | DL |
| 6 | hydroa vacciniforme, familial | 96.23% | DL |
| 7 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 95.96% | DL |
| 8 | neonatal dermatomyositis | 95.95% | DL |
| 9 | amyopathic dermatomyositis | 95.87% | DL |
| 10 | acrodermatitis chronica atrophicans | 95.82% | DL |
| 11 | bronchitis | 95.29% | DL |
| 12 | exanthem (disease) | 94.41% | DL |
| 13 | dry eye syndrome | 94.25% | DL |
| 14 | autoimmune hemolytic anemia | 93.70% | DL |
| 15 | HER2 positive breast carcinoma | 92.76% | DL |
| 16 | esotropia | 92.44% | DL |
| 17 | acquired aplastic anemia | 92.27% | DL |
| 18 | xerophthalmia | 91.77% | DL |
| 19 | keratoconjunctivitis | 91.57% | DL |
| 20 | disorder of GPI anchor biosynthesis | 91.57% | DL |

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
