---
layout: default
title: Prasugrel
description: "Prasugrel drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 468
evidence_level: L5
indication_count: 50
---

# Prasugrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Prasugrel |
| DrugBank ID | [DB06209](https://go.drugbank.com/drugs/DB06209) |
| Brand Names (EU) | Efient |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.88% |

---

## Approved Indication (EMA)

Efient, co-administered with acetylsalicylic acid (ASA), is indicated for the prevention of atherothrombotic events in patients with acute coronary syndrome (i.e. unstable angina, non-ST-segment-elevation myocardial infarction [UA / NSTEMI] or ST-segment-elevation myocardial infarction [STEMI]) undergoing primary or delayed percutaneous coronary intervention (PCI).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary hypertension | 99.88% | DL |
| 2 | migraine disorder | 99.88% | DL |
| 3 | migraine with brainstem aura | 99.83% | DL |
| 4 | kyphoscoliotic heart disease | 99.81% | DL |
| 5 | rheumatoid arthritis | 99.74% | DL |
| 6 | homozygous familial hypercholesterolemia | 99.74% | DL |
| 7 | hypoalphalipoproteinemia | 99.72% | DL |
| 8 | migraine with or without aura, susceptibility to | 99.67% | DL |
| 9 | brachydactyly-syndactyly syndrome | 99.60% | DL |
| 10 | leprosy | 99.46% | DL |
| 11 | obsolete susceptibility to ischemic stroke | 99.46% | DL |
| 12 | atrophoderma vermiculata | 99.46% | DL |
| 13 | peripheral vascular disease | 99.43% | DL |
| 14 | hypertrichosis (disease) | 99.43% | DL |
| 15 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.42% | DL |
| 16 | pulmonary hypertension, primary, autosomal recessive | 99.38% | DL |
| 17 | Prinzmetal angina | 99.38% | DL |
| 18 | peripheral arterial disease | 99.38% | DL |
| 19 | obsolete familial combined hyperlipidemia | 99.32% | DL |
| 20 | ulerythema ophryogenesis | 99.31% | DL |

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
