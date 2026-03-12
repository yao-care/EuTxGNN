---
layout: default
title: Basiliximab
description: "Basiliximab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 70
evidence_level: L5
indication_count: 50
---

# Basiliximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Basiliximab |
| DrugBank ID | [DB00074](https://go.drugbank.com/drugs/DB00074) |
| Brand Names (EU) | Simulect |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 95.61% |

---

## Approved Indication (EMA)

Simulect is indicated for the prophylaxis of acute organ rejection in de-novo allogeneic renal transplantation in adult and paediatric patients (1-17 years). It is to be used concomitantly with ciclosporin for microemulsion- and corticosteroid-based immunosuppression, in patients with panel reactive antibodies less than 80%, or in a triple maintenance immunosuppressive regimen containing ciclosporin for microemulsion, corticosteroids and either azathioprine or mycophenolate mofetil.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | plasma cell myeloma | 95.61% | DL |
| 2 | bronchitis | 95.54% | DL |
| 3 | indolent plasma cell myeloma | 95.29% | DL |
| 4 | hemoglobinopathy | 94.28% | DL |
| 5 | gastric carcinoma | 93.89% | DL |
| 6 | diffuse gastric adenocarcinoma | 93.75% | DL |
| 7 | partial deletion of the short arm of chromosome 16 | 93.52% | DL |
| 8 | beta-thalassemia with other manifestations | 93.29% | DL |
| 9 | hemolytic anemia due to glucophosphate isomerase deficiency | 92.93% | DL |
| 10 | Jeune syndrome situs inversus | 92.86% | DL |
| 11 | orofacial clefting syndrome | 92.81% | DL |
| 12 | gastric linitis plastica | 92.74% | DL |
| 13 | interventricular septum aneurysm | 92.72% | DL |
| 14 | pyruvate kinase deficiency of red cells | 92.70% | DL |
| 15 | Pierre Robin syndrome associated with a chromosomal anomaly | 92.68% | DL |
| 16 | pulmonary valve disease | 92.62% | DL |
| 17 | partial deletion of the long arm of chromosome 7 | 92.60% | DL |
| 18 | disorder of fucoglycosan synthesis | 92.60% | DL |
| 19 | partial deletion of the long arm of chromosome 22 | 92.56% | DL |
| 20 | genetic syndromic Pierre Robin syndrome | 92.56% | DL |

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
