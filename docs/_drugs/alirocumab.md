---
layout: default
title: Alirocumab
description: "Alirocumab drug repurposing predictions from TxGNN. Evidence level L5 with 52 predicted indications."
parent: AI Predictions (L5)
nav_order: 29
evidence_level: L5
indication_count: 52
---

# Alirocumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **52**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Alirocumab |
| DrugBank ID | [DB09302](https://go.drugbank.com/drugs/DB09302) |
| Brand Names (EU) | Praluent |
| Evidence Level | L5 |
| Predicted Indications | 52 |
| Top Prediction Score | 99.43% |

---

## Approved Indication (EMA)

Primary hypercholesterolaemia and mixed dyslipidaemia Praluent is indicated in adults with primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia, and in paediatric patients 8 years of age and older with heterozygous familial hypercholesterolaemia (HeFH) as an adjunct to diet: - in combination with a statin or statin with other lipid lowering therapies in patients unable to reach LDL-C goals with the maximum tolerated dose of a statin or, - alone or in comb

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ichthyosis, X-linked, without steroid sulfatase deficiency | 99.43% | DL |
| 2 | disorder of other vitamins and cofactors metabolism and transport | 99.41% | DL |
| 3 | xanthomatosis (disease) | 99.37% | DL |
| 4 | 46,XY disorder of sexual development due to dihydrotestosterone backdoor pathway biosynthesis defect | 99.37% | DL |
| 5 | cholesterol catabolic process disease | 99.36% | DL |
| 6 | 46,XY disorder of sex development due to a cholesterol synthesis defect | 99.35% | DL |
| 7 | dappled diaphyseal dysplasia | 99.30% | DL |
| 8 | neutral lipid storage disease | 99.29% | DL |
| 9 | 3-hydroxyacyl-CoA dehydrogenase deficiency | 99.29% | DL |
| 10 | spastic paraplegia-optic atrophy-neuropathy and spastic paraplegia-optic atrophy-neuropathy-related disorder | 99.26% | DL |
| 11 | thrombocytopenic purpura | 99.21% | DL |
| 12 | chondrodysplasia punctata, brachytelephalangic, autosomal | 99.20% | DL |
| 13 | chondrodysplasia punctata, tibial-metacarpal type | 99.16% | DL |
| 14 | Astley-Kendall dysplasia | 99.15% | DL |
| 15 | spastic paraplegia | 99.01% | DL |
| 16 | adenosine deaminase deficiency | 98.95% | DL |
| 17 | syndromic dyslipidemia | 98.85% | DL |
| 18 | hemorrhagic disease of newborn | 98.73% | DL |
| 19 | familial apolipoprotein C-II deficiency | 98.70% | DL |
| 20 | severe combined immunodeficiency due to LCK deficiency | 98.48% | DL |

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
