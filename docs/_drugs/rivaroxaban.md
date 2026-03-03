---
layout: default
title: Rivaroxaban
description: "Rivaroxaban drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 502
evidence_level: L5
indication_count: 50
---

# Rivaroxaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Rivaroxaban |
| DrugBank ID | [DB06228](https://go.drugbank.com/drugs/DB06228) |
| Brand Names (EU) | Xarelto |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.57% |

---

## Approved Indication (EMA)

Xarelto, co-administered with acetylsalicylic acid (ASA) alone or with ASA plus clopidogrel or ticlopidine, is indicated for the prevention of atherothrombotic events in adult patients after an acute coronary syndrome (ACS) with elevated cardiac biomarkers. Xarelto, co-administered with acetylsalicylic acid (ASA), is indicated for the prevention of atherothrombotic events in adult patients with coronary artery disease (CAD) or symptomatic peripheral artery disease (PAD) at high risk of ischaemic

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.57% | DL |
| 2 | gout | 99.51% | DL |
| 3 | HIV infectious disease | 99.17% | DL |
| 4 | brachydactyly-syndactyly syndrome | 99.10% | DL |
| 5 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.95% | DL |
| 6 | sclerosing cholangitis | 98.88% | DL |
| 7 | systemic mastocytosis | 98.82% | DL |
| 8 | Smouldering systemic mastocytosis | 98.78% | DL |
| 9 | feline acquired immunodeficiency syndrome | 98.67% | DL |
| 10 | simian immunodeficiency virus infection | 98.67% | DL |
| 11 | neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 98.67% | DL |
| 12 | multiple endocrine neoplasia | 98.66% | DL |
| 13 | lymphoadenopathic mastocytosis with eosinophilia | 98.60% | DL |
| 14 | Plasmodium falciparum malaria | 98.10% | DL |
| 15 | leprosy | 97.91% | DL |
| 16 | infectious otitis media | 97.73% | DL |
| 17 | pneumonia | 97.52% | DL |
| 18 | middle ear cholesterol granuloma | 97.39% | DL |
| 19 | nephrogenic syndrome of inappropriate antidiuresis | 97.35% | DL |
| 20 | otosalpingitis | 97.28% | DL |

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
