---
layout: default
title: Fluticasone Furoate
description: "fluticasone furoate drug repurposing predictions from TxGNN. Evidence level L1 with 52 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 252
evidence_level: L1
indication_count: 52
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fluticasone Furoate |
| DrugBank ID | [DB08906](https://go.drugbank.com/drugs/DB08906) |
| Brand Names (EU) | Avamys, Relvar Ellipta, Revinty Ellipta |
| Evidence Level | L1 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Asthma Indication Revinty Ellipta is indicated in the regular treatment of asthma in adults and adolescents aged 12 years and older, where use of a combination product (long-acting beta2-agonist and inhaled corticosteroid) is appropriate:  patients not adequately controlled with inhaled corticosteroids and “as needed” inhaled short acting beta2-agonists.  COPD Indication Revinty Ellipta is indicated for the symptomatic treatment of adults with COPD with a FEV1 &lt;70% predicted normal (post-bron

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | atopic eczema | 99.98% | DL |
| 2 | allergic asthma | 99.98% | DL |
| 3 | intrinsic asthma | 99.97% | DL |
| 4 | bronchitis | 99.89% | DL |
| 5 | asthma | 99.88% | DL |
| 6 | 2-hydroxyethyl methacrylate sensitization | 99.87% | DL |
| 7 | dermatitis, atopic | 99.81% | DL |
| 8 | contact dermatitis | 99.46% | DL |
| 9 | asthma-related traits, susceptibility to | 99.37% | DL |
| 10 | occupational dermatitis | 99.33% | DL |
| 11 | phototoxic dermatitis | 99.12% | DL |
| 12 | obstructive lung disease | 98.90% | DL |
| 13 | polyp of vocal cord | 98.87% | DL |
| 14 | polyp of middle ear | 98.86% | DL |
| 15 | fibroepithelial polyp | 98.84% | DL |
| 16 | seborrheic dermatitis | 98.83% | DL |
| 17 | neoplastic polyp | 98.82% | DL |
| 18 | atopic dermatitis | 98.82% | DL |
| 19 | polyp of vulva | 98.81% | DL |
| 20 | polyp of frontal sinus | 98.81% | DL |

*Showing top 20 of 52 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| allergic asthma | L1 | 20 | 2 | 8 Phase 3 trial(s), 4 Phase 2 trial(s), 1 RCT(s) |
| atopic eczema | L1 | 11 | 0 | 1 Phase 3 trial(s), 2 Phase 2 trial(s) |

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
