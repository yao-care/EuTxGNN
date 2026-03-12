---
layout: default
title: Colistimethate Sodium
description: "Colistimethate Sodium drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 144
evidence_level: L5
indication_count: 50
---

# Colistimethate Sodium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Colistimethate Sodium |
| DrugBank ID | [DB01111](https://go.drugbank.com/drugs/DB01111) |
| Brand Names (EU) | Colobreathe |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.78% |

---

## Approved Indication (EMA)

Colobreathe is indicated for the management of chronic pulmonary infections due to Pseudomonas aeruginosa in patients with cystic fibrosis (CF) aged six years and older. Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | osteoarthritis | 97.78% | DL |
| 2 | rheumatoid arthritis | 97.48% | DL |
| 3 | osteoarthritis susceptibility | 97.41% | DL |
| 4 | gout | 96.85% | DL |
| 5 | pseudoachondroplasia | 96.74% | DL |
| 6 | hepatic porphyria | 96.71% | DL |
| 7 | brachyolmia | 96.40% | DL |
| 8 | early-onset familial noncirrhotic portal hypertension | 96.27% | DL |
| 9 | idiopathic copper-associated cirrhosis | 96.27% | DL |
| 10 | primitive portal vein thrombosis | 96.27% | DL |
| 11 | hepatopulmonary syndrome | 96.27% | DL |
| 12 | hepatoportal sclerosis | 96.27% | DL |
| 13 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 96.26% | DL |
| 14 | acromesomelic dysplasia, Hunter-Thompson type | 96.21% | DL |
| 15 | brachyolmia-amelogenesis imperfecta syndrome | 96.05% | DL |
| 16 | myosclerosis | 96.04% | DL |
| 17 | arthropathy | 95.66% | DL |
| 18 | congestive heart failure | 95.32% | DL |
| 19 | brachydactyly-syndactyly syndrome | 95.20% | DL |
| 20 | acute pulmonary heart disease | 94.80% | DL |

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
