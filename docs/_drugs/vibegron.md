---
layout: default
title: Vibegron
description: "Vibegron drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 631
evidence_level: L5
indication_count: 50
---

# Vibegron
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vibegron |
| DrugBank ID | [DB14895](https://go.drugbank.com/drugs/DB14895) |
| Brand Names (EU) | Obgemsa |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.86% |

---

## Approved Indication (EMA)

Obgemsa is indicated in symptomatic treatment of adult patients with overactive bladder (OAB) syndrome.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | overactive bladder (disease) | 95.86% | DL |
| 2 | polycystic kidney disease 3 with or without polycystic liver disease | 94.50% | DL |
| 3 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 94.47% | DL |
| 4 | renal-hepatic-pancreatic dysplasia | 92.47% | DL |
| 5 | Joubert syndrome with renal defect | 91.53% | DL |
| 6 | thoracic malformation | 91.33% | DL |
| 7 | esophageal varices with bleeding | 91.29% | DL |
| 8 | esophageal varices without bleeding | 91.29% | DL |
| 9 | karyomegalic interstitial nephritis | 90.30% | DL |
| 10 | adult familial nephronophthisis-spastic quadriparesia syndrome | 90.15% | DL |
| 11 | hypotrichosis simplex of the scalp | 90.03% | DL |
| 12 | 16q24.1 microdeletion syndrome | 88.97% | DL |
| 13 | congenital hypotrichosis milia | 88.42% | DL |
| 14 | primary interstitial lung disease specific to childhood | 88.37% | DL |
| 15 | isolated pulmonary capillaritis | 88.04% | DL |
| 16 | congenital pulmonary lymphangiectasia | 86.33% | DL |
| 17 | psychogenic movement disorders | 85.59% | DL |
| 18 | chronic tic disorder | 84.56% | DL |
| 19 | tremor-nystagmus-duodenal ulcer syndrome | 84.09% | DL |
| 20 | primary orthostatic tremor | 84.04% | DL |

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
