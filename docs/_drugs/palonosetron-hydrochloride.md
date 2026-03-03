---
layout: default
title: Palonosetron Hydrochloride
description: "Palonosetron Hydrochloride drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 436
evidence_level: L5
indication_count: 50
---

# Palonosetron Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Palonosetron Hydrochloride |
| DrugBank ID | [DB00377](https://go.drugbank.com/drugs/DB00377) |
| Brand Names (EU) | Aloxi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.74% |

---

## Approved Indication (EMA)

Aloxi is indicated in adults for:  the prevention of acute nausea and vomiting associated with highly emetogenic cancer chemotherapy, the prevention of nausea and vomiting associated with moderately emetogenic cancer chemotherapy.  Aloxi is indicated in paediatric patients 1 month of age and older for:  the prevention of acute nausea and vomiting associated with highly emetogenic cancer chemotherapy and prevention of nausea and vomiting associated with moderately emetogenic cancer chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | migraine disorder | 99.74% | DL |
| 2 | migraine with brainstem aura | 99.67% | DL |
| 3 | migraine with or without aura, susceptibility to | 99.44% | DL |
| 4 | atrophoderma vermiculata | 99.13% | DL |
| 5 | ulerythema ophryogenesis | 99.07% | DL |
| 6 | headache disorder | 97.91% | DL |
| 7 | trigeminal autonomic cephalalgia | 97.59% | DL |
| 8 | open-angle glaucoma | 96.46% | DL |
| 9 | sciatic neuropathy | 96.38% | DL |
| 10 | primary hereditary glaucoma | 96.36% | DL |
| 11 | dysthymic disorder | 96.11% | DL |
| 12 | nephrogenic syndrome of inappropriate antidiuresis | 95.84% | DL |
| 13 | insomnia (disease) | 95.33% | DL |
| 14 | congenital hypotrichosis milia | 95.15% | DL |
| 15 | multiple system atrophy | 95.09% | DL |
| 16 | diffuse alopecia areata | 95.09% | DL |
| 17 | hypotrichosis simplex of the scalp | 94.89% | DL |
| 18 | duodenum cancer | 94.73% | DL |
| 19 | phaeochromocytoma | 94.73% | DL |
| 20 | irritable bowel syndrome | 94.60% | DL |

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
