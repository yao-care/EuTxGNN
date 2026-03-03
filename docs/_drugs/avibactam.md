---
layout: default
title: Avibactam
description: "Avibactam drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 61
evidence_level: L5
indication_count: 50
---

# Avibactam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Avibactam |
| DrugBank ID | [DB09060](https://go.drugbank.com/drugs/DB09060) |
| Brand Names (EU) | Avibactam |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Emblaveo is indicated for the treatment of the following infections in adult patients (see sections 4.4 and 5.1):• Complicated intra-abdominal infection (cIAI)• Hospital-acquired pneumonia (HAP), including ventilator-associated pneumonia (VAP)&nbsp;• Complicated urinary tract infection (cUTI), including pyelonephritisEmblaveo is also indicated for the treatment of infections due to aerobic Gram-negative organisms in adult patients with limited treatment options (see sections 4.2, 4.4, and 5.1).C

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pyelonephritis | 99.98% | DL |
| 2 | streptococcal pneumonia | 99.70% | DL |
| 3 | influenza, severe, susceptibility to | 99.28% | DL |
| 4 | ureter tuberculosis | 99.11% | DL |
| 5 | urinary schistosomiasis | 99.06% | DL |
| 6 | polyclonal hyperviscosity syndrome | 99.01% | DL |
| 7 | hyperamylasemia | 99.01% | DL |
| 8 | staphylococcus aureus infection | 98.97% | DL |
| 9 | renal tuberculosis | 98.93% | DL |
| 10 | squamous cell lung carcinoma | 98.86% | DL |
| 11 | congenital analbuminemia | 98.84% | DL |
| 12 | influenza | 98.75% | DL |
| 13 | blood group incompatibility | 98.70% | DL |
| 14 | mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies | 98.68% | DL |
| 15 | premalignant hematological system disease | 98.61% | DL |
| 16 | monoclonal gammopathy | 98.58% | DL |
| 17 | cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency | 98.43% | DL |
| 18 | hematological disease associated with an acquired peripheral neuropathy | 98.39% | DL |
| 19 | congenital hematological disorder | 98.34% | DL |
| 20 | hematopoietic and lymphoid system neoplasm | 98.32% | DL |

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
