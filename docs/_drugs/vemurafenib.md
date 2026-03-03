---
layout: default
title: Vemurafenib
description: "Vemurafenib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 627
evidence_level: L5
indication_count: 50
---

# Vemurafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vemurafenib |
| DrugBank ID | [DB08881](https://go.drugbank.com/drugs/DB08881) |
| Brand Names (EU) | Zelboraf |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.65% |

---

## Approved Indication (EMA)

Vemurafenib is indicated in monotherapy for the treatment of adult patients with BRAF-V600-mutation-positive unresectable or metastatic melanoma.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | HIV infectious disease | 97.65% | DL |
| 2 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 96.73% | DL |
| 3 | simian immunodeficiency virus infection | 96.56% | DL |
| 4 | feline acquired immunodeficiency syndrome | 96.56% | DL |
| 5 | acute intermittent porphyria | 96.21% | DL |
| 6 | collagenopathy | 95.32% | DL |
| 7 | paratenonitis | 95.25% | DL |
| 8 | female breast carcinoma | 95.15% | DL |
| 9 | calcific tendinitis | 95.13% | DL |
| 10 | lymphocytic hypereosinophilic syndrome | 95.00% | DL |
| 11 | Plasmodium falciparum malaria | 94.78% | DL |
| 12 | homozygous familial hypercholesterolemia | 94.58% | DL |
| 13 | gout | 94.30% | DL |
| 14 | obsolete familial combined hyperlipidemia | 94.29% | DL |
| 15 | dermatofibrosarcoma protuberans | 93.80% | DL |
| 16 | myositis | 93.64% | DL |
| 17 | headache disorder | 93.47% | DL |
| 18 | rheumatoid arthritis | 93.43% | DL |
| 19 | trigeminal autonomic cephalalgia | 93.26% | DL |
| 20 | arteriosclerosis disorder | 91.93% | DL |

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
