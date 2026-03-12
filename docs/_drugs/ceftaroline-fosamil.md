---
layout: default
title: Ceftaroline Fosamil
description: "Ceftaroline Fosamil drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 123
evidence_level: L5
indication_count: 50
---

# Ceftaroline Fosamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ceftaroline Fosamil |
| DrugBank ID | [DB06590](https://go.drugbank.com/drugs/DB06590) |
| Brand Names (EU) | Zinforo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.20% |

---

## Approved Indication (EMA)

Zinforo is indicated for the treatment of the following infections in neonates, infants, children, adolescents and adults:  Complicated skin and soft tissue infections (cSSTI) Community-acquired pneumonia (CAP)  Consideration should be given to official guidance on the appropriate use of antibacterial agents.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 98.20% | DL |
| 2 | osteoarthritis | 98.16% | DL |
| 3 | osteoarthritis susceptibility | 97.95% | DL |
| 4 | gout | 97.48% | DL |
| 5 | pseudoachondroplasia | 97.29% | DL |
| 6 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 97.16% | DL |
| 7 | hemoglobinopathy | 97.01% | DL |
| 8 | brachyolmia | 96.98% | DL |
| 9 | acromesomelic dysplasia, Hunter-Thompson type | 96.84% | DL |
| 10 | myosclerosis | 96.71% | DL |
| 11 | brachyolmia-amelogenesis imperfecta syndrome | 96.68% | DL |
| 12 | beta-thalassemia with other manifestations | 96.53% | DL |
| 13 | hepatic porphyria | 96.49% | DL |
| 14 | partial deletion of the short arm of chromosome 16 | 96.47% | DL |
| 15 | pyruvate kinase deficiency of red cells | 96.40% | DL |
| 16 | brachydactyly-syndactyly syndrome | 96.39% | DL |
| 17 | arthropathy | 96.33% | DL |
| 18 | hemolytic anemia due to glucophosphate isomerase deficiency | 96.19% | DL |
| 19 | pyropoikilocytosis, hereditary | 96.03% | DL |
| 20 | hepatoportal sclerosis | 96.03% | DL |

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
