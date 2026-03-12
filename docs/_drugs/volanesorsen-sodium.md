---
layout: default
title: Volanesorsen Sodium
description: "Volanesorsen Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 638
evidence_level: L5
indication_count: 50
---

# Volanesorsen Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Volanesorsen Sodium |
| DrugBank ID | [DB15067](https://go.drugbank.com/drugs/DB15067) |
| Brand Names (EU) | Waylivra |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 100.00% |

---

## Approved Indication (EMA)

Waylivra is indicated as an adjunct to diet in adult patients with genetically confirmed familial chylomicronemia syndrome (FCS) and at high risk for pancreatitis, in whom response to diet and triglyceride lowering therapy has been inadequate.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | megaloblastic anemia (disease) | 100.00% | DL |
| 2 | sclerosing cholangitis | 99.99% | DL |
| 3 | sickle cell disease and related diseases | 99.99% | DL |
| 4 | hereditary persistence of fetal hemoglobin-sickle cell disease syndrome | 99.99% | DL |
| 5 | sickle cell-hemoglobin d disease syndrome | 99.99% | DL |
| 6 | sickle cell-hemoglobin c disease syndrome | 99.99% | DL |
| 7 | sickle cell-hemoglobin E disease syndrome | 99.99% | DL |
| 8 | sickle cell-beta-thalassemia disease syndrome | 99.99% | DL |
| 9 | meningococcal infection | 99.99% | DL |
| 10 | paroxysmal nocturnal hemoglobinuria | 99.99% | DL |
| 11 | IgG4-related pachymeningitis | 99.99% | DL |
| 12 | IgG4-related retroperitoneal fibrosis | 99.99% | DL |
| 13 | mixed-type autoimmune hemolytic anemia | 99.99% | DL |
| 14 | non-infectious meningitis | 99.99% | DL |
| 15 | drug-induced autoimmune hemolytic anemia | 99.99% | DL |
| 16 | autosomal recessive severe congenital neutropenia due to G6PC3 deficiency | 99.98% | DL |
| 17 | infectious meningitis | 99.98% | DL |
| 18 | bone Paget disease | 99.98% | DL |
| 19 | psoriasis | 99.98% | DL |
| 20 | proteinuria | 99.98% | DL |

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
