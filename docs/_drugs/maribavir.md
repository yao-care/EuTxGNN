---
layout: default
title: Maribavir
description: "Maribavir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 364
evidence_level: L5
indication_count: 50
---

# Maribavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Maribavir |
| DrugBank ID | [DB06234](https://go.drugbank.com/drugs/DB06234) |
| Brand Names (EU) | Livtencity |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 87.79% |

---

## Approved Indication (EMA)

LIVTENCITY is indicated for the treatment of cytomegalovirus (CMV) infection and/or disease that are refractory (with or without resistance) to one or more prior therapies, including ganciclovir, valganciclovir, cidofovir or foscarnet in adult patients who have undergone a haematopoietic stem cell transplant (HSCT) or solid organ transplant (SOT). Consideration should be given to official guidance on the appropriate use of antiviral agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 87.79% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 79.11% | DL |
| 3 | bronchial neoplasm (disease) | 77.78% | DL |
| 4 | diabetic retinopathy | 76.24% | DL |
| 5 | filariasis | 74.26% | DL |
| 6 | rectosigmoid junction neoplasm | 73.41% | DL |
| 7 | colonic lymphangioma | 73.32% | DL |
| 8 | lipoma of colon | 73.23% | DL |
| 9 | cecum neuroendocrine tumor G1 | 73.13% | DL |
| 10 | cecum villous adenoma | 73.07% | DL |
| 11 | cecal disease | 73.07% | DL |
| 12 | colonic neoplasm | 72.96% | DL |
| 13 | cavernous hemangioma of colon | 72.95% | DL |
| 14 | colon leiomyoma | 72.94% | DL |
| 15 | benign neoplasm of cecum | 72.92% | DL |
| 16 | indolent plasma cell myeloma | 72.73% | DL |
| 17 | dermatitis | 72.65% | DL |
| 18 | plasma cell myeloma | 72.38% | DL |
| 19 | diabetic cataract | 71.82% | DL |
| 20 | ductal or ductular proliferation | 71.70% | DL |

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
