---
layout: default
title: Drospirenone
description: "Drospirenone drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 184
evidence_level: L5
indication_count: 52
---

# Drospirenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Drospirenone |
| DrugBank ID | [DB01395](https://go.drugbank.com/drugs/DB01395) |
| Brand Names (EU) | Drospirenone, Lydisilka |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

oral contraceptive

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acne (disease) | 99.99% | DL |
| 2 | zinc, elevated plasma | 98.74% | DL |
| 3 | dyschondrosteosis-nephritis syndrome | 93.61% | DL |
| 4 | torticollis-keloids-cryptorchidism-renal dysplasia syndrome | 93.53% | DL |
| 5 | infundibulopelvic stenosis-multicystic kidney syndrome | 93.33% | DL |
| 6 | pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 93.18% | DL |
| 7 | 46,XX disorder of sex development-anorectal anomalies syndrome | 92.77% | DL |
| 8 | thyrocerebrorenal syndrome | 92.76% | DL |
| 9 | acrorenal syndrome | 92.75% | DL |
| 10 | radial hypoplasia-triphalangeal thumbs-hypospadias-maxillary diastema syndrome | 92.67% | DL |
| 11 | Mayer-Rokitansky-Kuster-Hauser syndrome | 92.65% | DL |
| 12 | Guttmacher syndrome | 92.63% | DL |
| 13 | renal nutcracker syndrome | 92.63% | DL |
| 14 | nephrosis-deafness-urinary tract-digital malformations syndrome | 92.53% | DL |
| 15 | trisomy 13 | 92.50% | DL |
| 16 | Mayer-Rokitansky-Küster-Hauser syndrome type 2 | 92.36% | DL |
| 17 | pericardial and diaphragmatic defect | 92.33% | DL |
| 18 | diaphragmatic defect-limb deficiency-skull defect syndrome | 92.27% | DL |
| 19 | renal-genital-middle ear anomalies | 92.26% | DL |
| 20 | monosomy 13q34 | 92.25% | DL |

*Showing top 20 of 52 predictions.*

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
