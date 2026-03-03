---
layout: default
title: Caffeine Citrate
description: "Caffeine Citrate drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 107
evidence_level: L5
indication_count: 50
---

# Caffeine Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Caffeine Citrate |
| DrugBank ID | [DB00201](https://go.drugbank.com/drugs/DB00201) |
| Brand Names (EU) | Peyona (previously Nymusa) |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Treatment of primary apnoea of premature newborns.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pharyngitis | 99.92% | DL |
| 2 | nasal cavity disease | 99.91% | DL |
| 3 | thrombotic disease | 99.90% | DL |
| 4 | acute laryngopharyngitis | 99.89% | DL |
| 5 | papillary conjunctivitis | 99.79% | DL |
| 6 | headache disorder | 99.44% | DL |
| 7 | common cold | 99.42% | DL |
| 8 | neuralgia | 99.34% | DL |
| 9 | cluster headache syndrome | 99.29% | DL |
| 10 | hemicrania continua | 99.27% | DL |
| 11 | glossodynia | 99.26% | DL |
| 12 | coccygodynia | 99.22% | DL |
| 13 | nasopharyngitis | 99.22% | DL |
| 14 | trigeminal autonomic cephalalgia | 99.21% | DL |
| 15 | hypnic headache (disease) | 99.17% | DL |
| 16 | vein disease | 99.06% | DL |
| 17 | SUNCT syndrome | 98.99% | DL |
| 18 | faucial diphtheria | 98.81% | DL |
| 19 | cervical disc degenerative disorder | 98.78% | DL |
| 20 | rosacea conjunctivitis | 98.32% | DL |

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
