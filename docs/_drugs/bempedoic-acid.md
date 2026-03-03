---
layout: default
title: Bempedoic Acid
description: "Bempedoic Acid drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 75
evidence_level: L5
indication_count: 50
---

# Bempedoic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bempedoic Acid |
| DrugBank ID | [DB11936](https://go.drugbank.com/drugs/DB11936) |
| Brand Names (EU) | Nilemdo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.61% |

---

## Approved Indication (EMA)

Hypercholesterolaemia and mixed dyslipidaemiaNilemdo is indicated in adults with primary hypercholesterolaemia (heterozygous familial and non familial) or mixed dyslipidaemia, as an adjunct to diet:• in combination with a statin or statin with other lipid-lowering therapies in patients unable to reach LDL C goals with the maximum tolerated dose of a statin (see sections 4.2, 4.3, and 4.4) or,• alone or in combination with other lipid-lowering therapies in patients who are statin intolerant, or f

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | hyperthyroidism | 99.61% | DL |
| 2 | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta | 99.58% | DL |
| 3 | malignant catarrh | 99.58% | DL |
| 4 | infectious bovine rhinotracheitis | 99.58% | DL |
| 5 | cytomegalovirus infection | 99.53% | DL |
| 6 | homozygous familial hypercholesterolemia | 99.48% | DL |
| 7 | hyperthyroxinemia | 99.34% | DL |
| 8 | drug-induced osteoporosis | 99.21% | DL |
| 9 | multiple endocrine neoplasia | 99.18% | DL |
| 10 | pregnancy associated osteoporosis | 99.17% | DL |
| 11 | postmenopausal osteoporosis | 99.12% | DL |
| 12 | acne (disease) | 98.98% | DL |
| 13 | autosomal dominant neovascular inflammatory vitreoretinopathy | 98.95% | DL |
| 14 | Worth syndrome | 98.88% | DL |
| 15 | Graves disease | 98.70% | DL |
| 16 | hypoalphalipoproteinemia | 98.70% | DL |
| 17 | succinyl-CoA:3-ketoacid CoA transferase deficiency | 98.69% | DL |
| 18 | cholestasis | 98.66% | DL |
| 19 | non-syndromic visceral malformation | 98.63% | DL |
| 20 | biliary atresia intrahepatic | 98.55% | DL |

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
