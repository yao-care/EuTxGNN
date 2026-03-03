---
layout: default
title: Netupitant
description: "Netupitant drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 401
evidence_level: L5
indication_count: 50
---

# Netupitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Netupitant |
| DrugBank ID | [DB09048](https://go.drugbank.com/drugs/DB09048) |
| Brand Names (EU) | Netupitant |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.35% |

---

## Approved Indication (EMA)

Akynzeo is indicated in adults for the:  Prevention of acute and delayed nausea and vomiting associated with highly emetogenic cisplatin based cancer chemotherapy. Prevention of acute and delayed nausea and vomiting associated with moderately emetogenic cancer chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 98.35% | DL |
| 2 | leprosy | 98.25% | DL |
| 3 | migraine disorder | 97.49% | DL |
| 4 | migraine with or without aura, susceptibility to | 97.27% | DL |
| 5 | pulmonary hypertension | 97.22% | DL |
| 6 | migraine with brainstem aura | 97.14% | DL |
| 7 | kyphoscoliotic heart disease | 96.96% | DL |
| 8 | hyperargininemia | 96.57% | DL |
| 9 | coronary artery disease | 96.39% | DL |
| 10 | hypertrichosis (disease) | 96.30% | DL |
| 11 | malformation syndrome with odontal and/or periodontal component | 95.81% | DL |
| 12 | anomalous left coronary artery from the pulmonary artery | 95.80% | DL |
| 13 | Ambras type hypertrichosis universalis congenita | 95.75% | DL |
| 14 | syndrome with a Dandy-Walker malformation as major feature | 95.73% | DL |
| 15 | isolated genetic hair shaft abnormality | 95.56% | DL |
| 16 | myocardial ischemia | 95.11% | DL |
| 17 | atrophoderma vermiculata | 94.86% | DL |
| 18 | persistent Mullerian duct syndrome | 94.21% | DL |
| 19 | ulerythema ophryogenesis | 93.95% | DL |
| 20 | genetic multiple congenital anomalies/dysmorphic syndrome without intellectual disability | 93.74% | DL |

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
