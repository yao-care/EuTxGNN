---
layout: default
title: Vaborbactam
description: "Vaborbactam drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 619
evidence_level: L5
indication_count: 50
---

# Vaborbactam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Vaborbactam |
| DrugBank ID | [DB12107](https://go.drugbank.com/drugs/DB12107) |
| Brand Names (EU) | Vaborbactam |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.52% |

---

## Approved Indication (EMA)

Vaborem is indicated for the treatment of the following infections in adults:  Complicated urinary tract infection (cUTI), including pyelonephritis Complicated intra-abdominal infection (cIAI) Hospital-acquired pneumonia (HAP), including ventilator associated pneumonia (VAP).  Treatment of patients with bacteraemia that occurs in association with, or is suspected to be associated with, any of the infections listed above. Vaborem is also indicated for the treatment of infections due to aerobic Gr

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | osteoarthritis | 98.52% | DL |
| 2 | osteoarthritis susceptibility | 98.35% | DL |
| 3 | rheumatoid arthritis | 98.35% | DL |
| 4 | gout | 97.78% | DL |
| 5 | pseudoachondroplasia | 97.74% | DL |
| 6 | hepatic porphyria | 97.67% | DL |
| 7 | brachyolmia | 97.56% | DL |
| 8 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.42% | DL |
| 9 | acromesomelic dysplasia, Hunter-Thompson type | 97.42% | DL |
| 10 | brachyolmia-amelogenesis imperfecta syndrome | 97.31% | DL |
| 11 | myosclerosis | 97.31% | DL |
| 12 | idiopathic copper-associated cirrhosis | 97.30% | DL |
| 13 | hepatoportal sclerosis | 97.30% | DL |
| 14 | primitive portal vein thrombosis | 97.30% | DL |
| 15 | early-onset familial noncirrhotic portal hypertension | 97.30% | DL |
| 16 | hepatopulmonary syndrome | 97.30% | DL |
| 17 | arthropathy | 96.99% | DL |
| 18 | hemoglobinopathy | 96.75% | DL |
| 19 | brachydactyly-syndactyly syndrome | 96.71% | DL |
| 20 | congestive heart failure | 96.67% | DL |

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
