---
layout: default
title: Dibotermin Alfa
description: "Dibotermin Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 2 predicted indications."
parent: AI Predictions (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Dibotermin Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Dibotermin Alfa |
| DrugBank ID | [DB11639](https://go.drugbank.com/drugs/DB11639) |
| Brand Names (EU) | Inductos |
| Evidence Level | L5 |
| Predicted Indications | 2 |
| Top Prediction Score | 50.00% |

---

## Approved Indication (EMA)

Inductos is indicated for single level lumbar interbody spine fusion as a substitute for autogenous bone graft in adults with degenerative disc disease who have had at least 6 months of non operative treatment for this condition. Inductos is indicated for the treatment of acute tibia fractures in adults, as an adjunct to standard care using open fracture reduction and intramedullary unreamed nail fixation.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | tibia fracture | 50.00% | KG |
| 2 | intervertebral disc degenerative disorder | 50.00% | KG |

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
