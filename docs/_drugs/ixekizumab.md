---
layout: default
title: Ixekizumab
description: "Ixekizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 321
evidence_level: L5
indication_count: 50
---

# Ixekizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ixekizumab |
| DrugBank ID | [DB11569](https://go.drugbank.com/drugs/DB11569) |
| Brand Names (EU) | Taltz |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.41% |

---

## Approved Indication (EMA)

Plaque psoriasisTaltz is indicated for the treatment of moderate to severe plaque psoriasis in adults who are candidates for systemic therapy.Paediatric plaque psoriasisTaltz is indicated for the treatment of moderate to severe plaque psoriasis in children from the age of 6 years and with a body weight of at least 25 kg and adolescents who are candidates for systemic therapy.Psoriatic arthritisTaltz, alone or in combination with methotrexate, is indicated for the treatment of active psoriatic ar

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | spondyloarthropathy, susceptibility to | 98.41% | DL |
| 2 | ankylosing spondylitis | 97.56% | DL |
| 3 | rheumatoid vasculitis | 97.53% | DL |
| 4 | acute lymphoblastic/lymphocytic leukemia | 97.35% | DL |
| 5 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 97.07% | DL |
| 6 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 97.07% | DL |
| 7 | hypermobility of coccyx | 96.87% | DL |
| 8 | inflammatory spondylopathy | 96.77% | DL |
| 9 | Kummell disease | 96.70% | DL |
| 10 | polyarticular juvenile rheumatoid arthritis | 96.42% | DL |
| 11 | vertebral disease | 95.13% | DL |
| 12 | fibromatosis, gingival | 92.21% | DL |
| 13 | rheumatoid nodulosis | 91.92% | DL |
| 14 | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis | 91.71% | DL |
| 15 | juvenile idiopathic arthritis | 91.65% | DL |
| 16 | hamartoma of lung | 91.62% | DL |
| 17 | Richter syndrome | 91.44% | DL |
| 18 | lung benign neoplasm | 91.30% | DL |
| 19 | lung hilum carcinoma | 91.20% | DL |
| 20 | juvenile chronic polyarthritis | 91.10% | DL |

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
