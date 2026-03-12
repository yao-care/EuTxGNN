---
layout: default
title: Lumacaftor
description: "Lumacaftor drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 355
evidence_level: L5
indication_count: 50
---

# Lumacaftor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lumacaftor |
| DrugBank ID | [DB09280](https://go.drugbank.com/drugs/DB09280) |
| Brand Names (EU) | Lumacaftor |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.44% |

---

## Approved Indication (EMA)

Orkambi tablets are indicated for the treatment of cystic fibrosis (CF) in patients aged 6 years and older who are homozygous for the F508del mutation in the CFTR gene. Orkambi granules are indicated for the treatment of cystic fibrosis (CF) in children aged 1 year and older who are homozygous for the F508del mutation in the CFTR gene.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | leprosy | 99.44% | DL |
| 2 | migraine with or without aura, susceptibility to | 98.85% | DL |
| 3 | migraine disorder | 98.73% | DL |
| 4 | rheumatoid arthritis | 98.69% | DL |
| 5 | pulmonary hypertension | 98.67% | DL |
| 6 | kyphoscoliotic heart disease | 98.52% | DL |
| 7 | migraine with brainstem aura | 98.51% | DL |
| 8 | multiple endocrine neoplasia | 98.36% | DL |
| 9 | brachydactyly-syndactyly syndrome | 98.17% | DL |
| 10 | nephrogenic syndrome of inappropriate antidiuresis | 98.00% | DL |
| 11 | homozygous familial hypercholesterolemia | 97.95% | DL |
| 12 | Prinzmetal angina | 97.91% | DL |
| 13 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.84% | DL |
| 14 | atrophoderma vermiculata | 97.50% | DL |
| 15 | ulerythema ophryogenesis | 97.12% | DL |
| 16 | amyotrophic lateral sclerosis | 96.88% | DL |
| 17 | persistent Mullerian duct syndrome | 96.65% | DL |
| 18 | coronary artery disease | 96.56% | DL |
| 19 | pneumocystosis | 96.50% | DL |
| 20 | hypoalphalipoproteinemia | 96.50% | DL |

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
