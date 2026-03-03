---
layout: default
title: Glycerol Phenylbutyrate
description: "Glycerol Phenylbutyrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 273
evidence_level: L5
indication_count: 50
---

# Glycerol Phenylbutyrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Glycerol Phenylbutyrate |
| DrugBank ID | [DB08909](https://go.drugbank.com/drugs/DB08909) |
| Brand Names (EU) | Ravicti |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.67% |

---

## Approved Indication (EMA)

Ravicti is indicated for use as adjunctive therapy for chronic management of patients&nbsp;with urea cycle disorders (UCDs) including deficiencies of carbamoyl phosphate-synthase-I (CPS), ornithine carbamoyltransferase (OTC), argininosuccinate synthetase (ASS), argininosuccinate lyase (ASL), arginase I (ARG) and ornithine translocase deficiency hyperornithinaemia-hyperammonaemia homocitrullinuria syndrome (HHH) who cannot be managed by dietary protein restriction and/or amino acid supplementatio

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | urea cycle disorder | 98.67% | DL |
| 2 | argininosuccinic aciduria | 98.25% | DL |
| 3 | carbamoyl phosphate synthetase I deficiency disease | 97.92% | DL |
| 4 | acute neonatal citrullinemia type I | 97.24% | DL |
| 5 | adult-onset citrullinemia type I | 97.24% | DL |
| 6 | citrullinemia, type II, adult-onset | 97.13% | DL |
| 7 | 3-methylcrotonyl-CoA carboxylase 1 deficiency | 97.10% | DL |
| 8 | hyperinsulinism-hyperammonemia syndrome | 96.78% | DL |
| 9 | hyperammonemic encephalopathy due to carbonic anhydrase VA deficiency | 96.56% | DL |
| 10 | hyperargininemia | 94.98% | DL |
| 11 | citrullinemia | 94.31% | DL |
| 12 | citrin deficiency | 93.45% | DL |
| 13 | neonatal intrahepatic cholestasis due to citrin deficiency | 92.72% | DL |
| 14 | benign neoplasm of adrenal gland | 90.80% | DL |
| 15 | hyperammonemia due to N-acetylglutamate synthase deficiency | 89.01% | DL |
| 16 | familial apolipoprotein C-II deficiency | 86.32% | DL |
| 17 | polycystic kidney disease 3 with or without polycystic liver disease | 83.08% | DL |
| 18 | acute intermittent porphyria | 81.32% | DL |
| 19 | renal-hepatic-pancreatic dysplasia | 79.64% | DL |
| 20 | autosomal ichthyosis syndrome with fatal disease course | 79.47% | DL |

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
