---
layout: default
title: Eliglustat (Tartrate)
description: "Eliglustat (Tartrate) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 200
evidence_level: L5
indication_count: 50
---

# Eliglustat (Tartrate)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eliglustat (Tartrate) |
| DrugBank ID | [DB09039](https://go.drugbank.com/drugs/DB09039) |
| Brand Names (EU) | Cerdelga |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.51% |

---

## Approved Indication (EMA)

AdultsCerdelga is indicated for the long-term treatment of adult patients with Gaucher disease type 1 (GD1), who are CYP2D6 poor metabolisers (PMs), intermediate metabolisers (IMs) or extensive metabolisers (EMs).Paediatric population (from 6 to &lt; 18 years of age) weighing ≥ 15 kgCerdelga is indicated for paediatric patients with GD1 who are 6 years and older with a minimum body weight of 15 kg, who are stable on enzyme replacement therapy (ERT), and who are CYP2D6 PMs, IMs or EMs.&nbsp;

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Gaucher disease | 98.51% | DL |
| 2 | autosomal ichthyosis syndrome with fatal disease course | 98.42% | DL |
| 3 | benign neoplasm of adrenal gland | 98.33% | DL |
| 4 | polycystic kidney disease 3 with or without polycystic liver disease | 96.91% | DL |
| 5 | gastrocutaneous syndrome | 96.67% | DL |
| 6 | familial generalized lentiginosis | 96.60% | DL |
| 7 | Moynahan syndrome | 96.40% | DL |
| 8 | rhabdoid tumor | 96.20% | DL |
| 9 | osteopathia striata-pigmentary dermopathy-white forelock syndrome | 96.06% | DL |
| 10 | congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome | 96.06% | DL |
| 11 | acromelanosis | 96.06% | DL |
| 12 | X-linked lymphoproliferative disease due to SH2D1A deficiency | 95.94% | DL |
| 13 | leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome | 95.86% | DL |
| 14 | renal-hepatic-pancreatic dysplasia | 95.75% | DL |
| 15 | Joubert syndrome with renal defect | 95.18% | DL |
| 16 | peripheral nerve schwannoma | 95.06% | DL |
| 17 | karyomegalic interstitial nephritis | 95.04% | DL |
| 18 | schwannoma of twelfth cranial nerve | 94.63% | DL |
| 19 | thoracic malformation | 94.62% | DL |
| 20 | sympathetic neurilemmoma | 94.61% | DL |

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
