---
layout: default
title: Methotrexate
description: "Methotrexate drug repurposing predictions from TxGNN. Evidence level L5 with 69 predicted indications."
parent: AI Predictions (L5)
nav_order: 372
evidence_level: L5
indication_count: 69
---

# Methotrexate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **69**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Methotrexate |
| DrugBank ID | [DB00563](https://go.drugbank.com/drugs/DB00563) |
| Brand Names (EU) | Jylamvo, Nordimet |
| Evidence Level | L5 |
| Predicted Indications | 69 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

In rheumatological and dermatological diseases  Active rheumatoid arthritis in adult patients. Polyarthritic forms of active, severe juvenile idiopathic arthritis (JIA) in adolescents and children aged 3 years and over when the response to non-steroidal anti-inflammatory drugs (NSAIDs) has been inadequate. Severe, treatment-refractory, disabling psoriasis which does not respond sufficiently to other forms of treatment such as phototherapy, psoralen and ultraviolet A radiation (PUVA) therapy and 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.46% | DL |
| 2 | pulmonary blastoma | 99.45% | DL |
| 3 | primary pulmonary lymphoma | 99.45% | DL |
| 4 | small cell lung carcinoma | 99.43% | DL |
| 5 | well-differentiated fetal adenocarcinoma of the lung | 99.42% | DL |
| 6 | acute lymphoblastic/lymphocytic leukemia | 99.36% | DL |
| 7 | Hodgkins lymphoma | 99.32% | DL |
| 8 | rhabdomyosarcoma (disease) | 99.25% | DL |
| 9 | folliculotropic mycosis fungoides | 99.23% | DL |
| 10 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 99.23% | DL |
| 11 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 99.23% | DL |
| 12 | parameningeal embryonal rhabdomyosarcoma | 99.21% | DL |
| 13 | acute lymphoblastic leukemia (disease) | 99.21% | DL |
| 14 | botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.21% | DL |
| 15 | embryonal extrahepatic bile duct rhabdomyosarcoma | 99.17% | DL |
| 16 | extrahepatic bile duct rhabdomyosarcoma | 99.15% | DL |
| 17 | prostate embryonal rhabdomyosarcoma | 99.14% | DL |
| 18 | mycosis fungoides and variants | 99.04% | DL |
| 19 | brachydactyly-syndactyly syndrome | 99.02% | DL |
| 20 | liver sarcoma | 98.99% | DL |

*Showing top 20 of 69 predictions.*

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
