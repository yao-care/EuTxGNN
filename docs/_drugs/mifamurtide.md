---
layout: default
title: Mifamurtide
description: "Mifamurtide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 382
evidence_level: L5
indication_count: 50
---

# Mifamurtide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Mifamurtide |
| DrugBank ID | [DB13615](https://go.drugbank.com/drugs/DB13615) |
| Brand Names (EU) | Mepact |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.06% |

---

## Approved Indication (EMA)

Mepact is indicated in children, adolescents and young adults for the treatment of high-grade resectable non-metastatic osteosarcoma after macroscopically complete surgical resection. It is used in combination with postoperative multi-agent chemotherapy. Safety and efficacy have been assessed in studies of patients two to 30 years of age at initial diagnosis.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | filariasis | 93.06% | DL |
| 2 | primary hereditary glaucoma | 86.67% | DL |
| 3 | autoimmune oophoritis | 85.19% | DL |
| 4 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 84.06% | DL |
| 5 | type 1 diabetes mellitus | 83.77% | DL |
| 6 | brain small vessel disease 1 with or without ocular anomalies | 83.34% | DL |
| 7 | open-angle glaucoma | 82.86% | DL |
| 8 | cholecystolithiasis | 81.83% | DL |
| 9 | trigeminal autonomic cephalalgia | 77.84% | DL |
| 10 | diabetic nephropathy | 77.64% | DL |
| 11 | headache disorder | 76.60% | DL |
| 12 | thromboangiitis obliterans | 75.41% | DL |
| 13 | unclassified myelodysplastic syndrome | 73.37% | DL |
| 14 | refractory cytopenia of childhood | 71.80% | DL |
| 15 | partial deletion of the long arm of chromosome 5 | 71.78% | DL |
| 16 | myelodysplastic syndrome | 71.05% | DL |
| 17 | aregenerative anemia | 70.86% | DL |
| 18 | severe congenital hypochromic anemia with ringed sideroblasts | 70.39% | DL |
| 19 | tendinitis | 70.00% | DL |
| 20 | congenital hypotrichosis milia | 69.84% | DL |

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
