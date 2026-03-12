---
layout: default
title: Eculizumab
description: "Eculizumab drug repurposing predictions from TxGNN. Evidence level L5 with 51 predicted indications."
parent: AI Predictions (L5)
nav_order: 191
evidence_level: L5
indication_count: 51
---

# Eculizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Eculizumab |
| DrugBank ID | [DB01257](https://go.drugbank.com/drugs/DB01257) |
| Brand Names (EU) | Bekemv, Epysqli |
| Evidence Level | L5 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Bekemv is indicated in adults and children for the treatment of paroxysmal nocturnal haemoglobinuria (PNH). Evidence of clinical benefit is demonstrated in patients with haemolysis with clinical symptom(s) indicative of high disease activity, regardless of transfusion history (see section 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | cyclic hematopoiesis | 99.97% | DL |
| 2 | autosomal recessive severe congenital neutropenia due to JAGN1 deficiency | 99.96% | DL |
| 3 | X-linked severe congenital neutropenia | 99.96% | DL |
| 4 | congenital neutropenia-myelofibrosis-nephromegaly syndrome | 99.96% | DL |
| 5 | adult idiopathic neutropenia | 99.96% | DL |
| 6 | autosomal recessive severe congenital neutropenia due to CXCR2 deficiency | 99.96% | DL |
| 7 | primary immunodeficiency syndrome due to p14 deficiency | 99.95% | DL |
| 8 | autosomal recessive severe congenital neutropenia due to CSF3R deficiency | 99.95% | DL |
| 9 | severe congenital neutropenia | 99.95% | DL |
| 10 | primary release disorder of platelets | 99.94% | DL |
| 11 | pseudo-von Willebrand disease | 99.94% | DL |
| 12 | Barth syndrome | 99.91% | DL |
| 13 | Glanzmann thrombasthenia | 99.90% | DL |
| 14 | mixed-type autoimmune hemolytic anemia | 99.89% | DL |
| 15 | drug-induced autoimmune hemolytic anemia | 99.89% | DL |
| 16 | constitutional neutropenia | 99.88% | DL |
| 17 | primary CD59 deficiency | 99.88% | DL |
| 18 | cold agglutinin disease | 99.87% | DL |
| 19 | neonatal autoimmune hemolytic anemia | 99.86% | DL |
| 20 | autosomal recessive severe congenital neutropenia due to G6PC3 deficiency | 99.86% | DL |

*Showing top 20 of 51 predictions.*

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
