---
layout: default
title: Tecovirimat
description: "Tecovirimat drug repurposing predictions from TxGNN. Evidence level L5 with 53 predicted indications."
parent: AI Predictions (L5)
nav_order: 559
evidence_level: L5
indication_count: 53
---

# Tecovirimat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **53**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tecovirimat |
| DrugBank ID | [DB12020](https://go.drugbank.com/drugs/DB12020) |
| Brand Names (EU) | Tecovirimat SIGA |
| Evidence Level | L5 |
| Predicted Indications | 53 |
| Top Prediction Score | 99.71% |

---

## Approved Indication (EMA)

Tecovirimat SIGA is indicated for the treatment of the following viral infections in adults and children with body weight at least 13 kg:  Smallpox Monkeypox Cowpox  Tecovirimat SIGA is also indicated to treat complications due to replication of vaccinia virus following vaccination against smallpox in adults and children with body weight at least 13 kg (see sections 4.4 and 5.1). Tecovirimat SIGA should be used in accordance with official recommendations.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | smallpox | 99.71% | DL |
| 2 | cowpox | 99.69% | DL |
| 3 | contagious pustular dermatitis | 99.69% | DL |
| 4 | milker's nodule | 99.69% | DL |
| 5 | hordeolum | 99.66% | DL |
| 6 | vibrio infectious disease | 99.65% | DL |
| 7 | Klebsiella infectious disease | 99.64% | DL |
| 8 | noma | 99.62% | DL |
| 9 | Newcastle disease | 99.62% | DL |
| 10 | Proteus infectious disease | 99.62% | DL |
| 11 | lumpy skin disease | 99.62% | DL |
| 12 | Astroviridae infectious disease | 99.62% | DL |
| 13 | arbovirus infection | 99.62% | DL |
| 14 | escherichia coli infection | 99.62% | DL |
| 15 | molluscum contagiosum | 99.62% | DL |
| 16 | pneumonic pasteurellosis | 99.62% | DL |
| 17 | human infection by orthopoxvirus | 99.62% | DL |
| 18 | idiopathic severe pneumococcemia | 99.62% | DL |
| 19 | monkeypox | 99.62% | DL |
| 20 | coinfection | 99.62% | DL |

*Showing top 20 of 53 predictions.*

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
