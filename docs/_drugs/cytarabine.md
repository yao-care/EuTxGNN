---
layout: default
title: Cytarabine
description: "Cytarabine drug repurposing predictions from TxGNN. Evidence level L5 with 55 predicted indications."
parent: AI Predictions (L5)
nav_order: 148
evidence_level: L5
indication_count: 55
---

# Cytarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **55**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cytarabine |
| DrugBank ID | [DB00987](https://go.drugbank.com/drugs/DB00987) |
| Brand Names (EU) | Cytarabine, Vyxeos liposomal (previously Vyxeos) |
| Evidence Level | L5 |
| Predicted Indications | 55 |
| Top Prediction Score | 99.78% |

---

## Approved Indication (EMA)

Vyxeos liposomal is indicated for the treatment of adults with newly diagnosed, therapy-related acute myeloid leukaemia (t-AML) or AML with myelodysplasia-related changes (AML-MRC).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | small cell lung carcinoma | 99.78% | DL |
| 2 | primary pulmonary lymphoma | 99.78% | DL |
| 3 | well-differentiated fetal adenocarcinoma of the lung | 99.76% | DL |
| 4 | pulmonary blastoma | 99.76% | DL |
| 5 | myeloid leukemia | 99.61% | DL |
| 6 | upper aerodigestive tract neoplasm | 99.49% | DL |
| 7 | ganglioneuroblastoma (disease) | 99.36% | DL |
| 8 | vertebral anomalies and variable endocrine and T-cell dysfunction | 99.32% | DL |
| 9 | retroperitoneal neoplasm | 99.23% | DL |
| 10 | neuroblastoma | 99.19% | DL |
| 11 | acute lymphoblastic/lymphocytic leukemia | 99.16% | DL |
| 12 | chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation | 98.96% | DL |
| 13 | pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma | 98.96% | DL |
| 14 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 98.91% | DL |
| 15 | chronic myelogenous leukemia, BCR-ABL1 positive | 98.88% | DL |
| 16 | adenosarcoma | 98.81% | DL |
| 17 | Ewing sarcoma | 98.80% | DL |
| 18 | acute myeloid leukemia with CEBPA somatic mutations | 98.69% | DL |
| 19 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 98.69% | DL |
| 20 | uterine ligament adenosarcoma | 98.62% | DL |

*Showing top 20 of 55 predictions.*

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
