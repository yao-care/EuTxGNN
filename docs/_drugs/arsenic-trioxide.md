---
layout: default
title: Arsenic Trioxide
description: "Arsenic Trioxide drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 48
evidence_level: L5
indication_count: 52
---

# Arsenic Trioxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Arsenic Trioxide |
| DrugBank ID | [DB01169](https://go.drugbank.com/drugs/DB01169) |
| Brand Names (EU) | Arsenic trioxide Accord, Arsenic trioxide medac |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.93% |

---

## Approved Indication (EMA)

Arsenic trioxide medac is indicated for induction of remission, and consolidation in adult patients with:  Newly diagnosed low-to-intermediate risk acute promyelocytic leukaemia (APL) (white blood cell count, ? 10 x 10³/?l) in combination with all-trans-retinoic acid (ATRA) Relapsed/refractory APL (previous treatment should have included a retinoid and chemotherapy) characterised by the presence of the t(15;17) translocation and/or the presence of the pro-myelocytic leukaemia/retinoic-acid-recep

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | unclassified myelodysplastic syndrome | 99.93% | DL |
| 2 | refractory cytopenia of childhood | 99.93% | DL |
| 3 | severe congenital hypochromic anemia with ringed sideroblasts | 99.93% | DL |
| 4 | aregenerative anemia | 99.92% | DL |
| 5 | partial deletion of the long arm of chromosome 5 | 99.92% | DL |
| 6 | myelodysplastic syndrome | 99.91% | DL |
| 7 | Ewing sarcoma | 99.89% | DL |
| 8 | dermatofibrosarcoma protuberans | 99.77% | DL |
| 9 | liposarcoma | 99.75% | DL |
| 10 | ovarian myxoid liposarcoma | 99.70% | DL |
| 11 | uterine corpus sarcoma | 99.44% | DL |
| 12 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 99.25% | DL |
| 13 | osteoarthritis | 99.21% | DL |
| 14 | acute myeloid leukemia with CEBPA somatic mutations | 99.17% | DL |
| 15 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 99.14% | DL |
| 16 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.04% | DL |
| 17 | parameningeal embryonal rhabdomyosarcoma | 99.01% | DL |
| 18 | osteoarthritis susceptibility | 99.01% | DL |
| 19 | extrahepatic bile duct rhabdomyosarcoma | 98.98% | DL |
| 20 | embryonal extrahepatic bile duct rhabdomyosarcoma | 98.95% | DL |

*Showing top 20 of 52 predictions.*

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
