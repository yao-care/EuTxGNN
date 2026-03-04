---
layout: default
title: Tolvaptan
description: "tolvaptan drug repurposing predictions from TxGNN. Evidence level L1 with 51 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 595
evidence_level: L1
indication_count: 51
---

# Tolvaptan
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **51**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tolvaptan |
| DrugBank ID | [DB06212](https://go.drugbank.com/drugs/DB06212) |
| Brand Names (EU) | Samsca |
| Evidence Level | L1 |
| Predicted Indications | 51 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Treatment of adult patients with hyponatraemia secondary to syndrome of inappropriate antidiuretic-hormone secretion (SIADH).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | polycystic kidney disease 3 with or without polycystic liver disease | 99.99% | DL |
| 2 | renal-hepatic-pancreatic dysplasia | 99.98% | DL |
| 3 | karyomegalic interstitial nephritis | 99.98% | DL |
| 4 | thoracic malformation | 99.98% | DL |
| 5 | polycystic kidney disease | 99.98% | DL |
| 6 | Joubert syndrome with renal defect | 99.98% | DL |
| 7 | adult familial nephronophthisis-spastic quadriparesia syndrome | 99.98% | DL |
| 8 | Ambras type hypertrichosis universalis congenita | 99.96% | DL |
| 9 | hypertrichosis (disease) | 99.96% | DL |
| 10 | malformation syndrome with odontal and/or periodontal component | 99.96% | DL |
| 11 | syndrome with a Dandy-Walker malformation as major feature | 99.95% | DL |
| 12 | isolated genetic hair shaft abnormality | 99.95% | DL |
| 13 | nephrogenic syndrome of inappropriate antidiuresis | 99.94% | DL |
| 14 | homozygous familial hypercholesterolemia | 99.87% | DL |
| 15 | Joubert syndrome with oculorenal defect | 99.84% | DL |
| 16 | Meckel syndrome, | 99.84% | DL |
| 17 | syndrome with limb duplication, polydactyly, syndactyly, and/or hyperphalangy | 99.81% | DL |
| 18 | hypoalphalipoproteinemia | 99.79% | DL |
| 19 | autosomal dominant polycystic kidney disease type 1 with tuberous sclerosis | 99.74% | DL |
| 20 | congenital pulmonary lymphangiectasia | 99.63% | DL |

*Showing top 20 of 51 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| polycystic kidney disease | L1 | 20 | 18 | 8 Phase 3 trial(s), 5 Phase 2 trial(s), 4 RCT(s),  |

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
