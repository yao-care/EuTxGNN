---
layout: default
title: Onasemnogene Abeparvovec
description: "Onasemnogene Abeparvovec drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 422
evidence_level: L5
indication_count: 50
---

# Onasemnogene Abeparvovec
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Onasemnogene Abeparvovec |
| DrugBank ID | [DB15528](https://go.drugbank.com/drugs/DB15528) |
| Brand Names (EU) | Zolgensma |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 86.13% |

---

## Approved Indication (EMA)

Zolgensma is indicated for the treatment of:  patients with 5q spinal muscular atrophy (SMA) with a bi-allelic mutation in the SMN1 gene and a clinical diagnosis of SMA Type 1, or patients with 5q SMA with a bi-allelic mutation in the SMN1 gene and up to 3 copies of the SMN2 gene.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | bronchitis | 86.13% | DL |
| 2 | severe nonproliferative diabetic retinopathy | 79.85% | DL |
| 3 | diabetic retinopathy | 77.44% | DL |
| 4 | bronchial neoplasm (disease) | 77.10% | DL |
| 5 | non-seminomatous lesion | 76.78% | DL |
| 6 | chondroid hamartoma | 76.78% | DL |
| 7 | ductal or ductular proliferation | 76.78% | DL |
| 8 | bronchial adenomas/carcinoids childhood | 76.78% | DL |
| 9 | rectosigmoid junction neoplasm | 76.70% | DL |
| 10 | tumor of testis and paratestis | 76.67% | DL |
| 11 | colonic lymphangioma | 76.59% | DL |
| 12 | lipoma of colon | 76.51% | DL |
| 13 | odontogenic cyst | 76.46% | DL |
| 14 | cecum neuroendocrine tumor G1 | 76.44% | DL |
| 15 | thyroglossal duct cyst | 76.43% | DL |
| 16 | colonic neoplasm | 76.42% | DL |
| 17 | cecal disease | 76.39% | DL |
| 18 | cecum villous adenoma | 76.38% | DL |
| 19 | cystic neoplasm | 76.35% | DL |
| 20 | cavernous hemangioma of colon | 76.32% | DL |

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
