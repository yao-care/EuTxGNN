---
layout: default
title: Colesevelam (As Hydrochloride)
description: "Colesevelam (As Hydrochloride) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 143
evidence_level: L5
indication_count: 50
---

# Colesevelam (As Hydrochloride)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Colesevelam (As Hydrochloride) |
| DrugBank ID | [DB00930](https://go.drugbank.com/drugs/DB00930) |
| Brand Names (EU) | Cholestagel |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.37% |

---

## Approved Indication (EMA)

Cholestagel co-administered with a 3-hydroxy-3-methyl-glutaryl-coenzyme-A (HMG-CoA)-reductase inhibitor (statin) is indicated as adjunctive therapy to diet to provide an additive reduction in low-density-lipoprotein-cholesterol (LDL-C) levels in adult patients with primary hypercholesterolaemia who are not adequately controlled with a statin alone. Cholestagel as monotherapy is indicated as adjunctive therapy to diet for reduction of elevated total cholesterol and LDL-C in adult patients with pr

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | gout | 93.37% | DL |
| 2 | congestive heart failure | 89.76% | DL |
| 3 | acute pulmonary heart disease | 88.61% | DL |
| 4 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 87.09% | DL |
| 5 | brain small vessel disease 1 with or without ocular anomalies | 86.91% | DL |
| 6 | infectious otitis media | 86.33% | DL |
| 7 | diabetic nephropathy | 86.16% | DL |
| 8 | phosphorus metabolism disease | 84.83% | DL |
| 9 | middle ear cholesterol granuloma | 84.80% | DL |
| 10 | otosalpingitis | 84.60% | DL |
| 11 | endocardial fibroelastosis | 84.49% | DL |
| 12 | middle ear disease | 84.25% | DL |
| 13 | allergic otitis media | 84.12% | DL |
| 14 | non-suppurative otitis media | 84.04% | DL |
| 15 | chronic otitis media | 83.89% | DL |
| 16 | endocarditis | 83.69% | DL |
| 17 | epiglottitis | 83.45% | DL |
| 18 | suppurative otitis media | 83.24% | DL |
| 19 | dyspepsia | 83.12% | DL |
| 20 | HIV infectious disease | 79.90% | DL |

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
