---
layout: default
title: Lomitapide
description: "Lomitapide drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 349
evidence_level: L5
indication_count: 50
---

# Lomitapide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Lomitapide |
| DrugBank ID | [DB08827](https://go.drugbank.com/drugs/DB08827) |
| Brand Names (EU) | Lojuxta |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.92% |

---

## Approved Indication (EMA)

Lojuxta is indicated as an adjunct to a low?fat diet and other lipid?lowering medicinal products with or without low-density-lipoprotein (LDL) apheresis in adult patients with homozygous familial hypercholesterolaemia (HoFH). Genetic confirmation of HoFH should be obtained whenever possible. Other forms of primary hyperlipoproteinaemia and secondary causes of hypercholesterolaemia (e.g. nephrotic syndrome, hypothyroidism) must be excluded.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | marcothrombocytopenia with mitral valve insufficiency | 99.92% | DL |
| 2 | hereditary thrombocytopenia with normal platelets | 99.92% | DL |
| 3 | dense granule disease | 99.92% | DL |
| 4 | transient neonatal thrombocytopenia | 99.92% | DL |
| 5 | homozygous familial hypercholesterolemia | 99.91% | DL |
| 6 | thrombocytopenia | 99.88% | DL |
| 7 | primary release disorder of platelets | 99.85% | DL |
| 8 | pseudo-von Willebrand disease | 99.85% | DL |
| 9 | Glanzmann thrombasthenia | 99.76% | DL |
| 10 | hyperlipoproteinemia | 99.74% | DL |
| 11 | platelet storage pool deficiency | 99.54% | DL |
| 12 | hyperlipidemia, familial combined, LPL related | 99.46% | DL |
| 13 | primary hyperoxaluria | 98.97% | DL |
| 14 | Scott syndrome | 98.67% | DL |
| 15 | obsolete familial combined hyperlipidemia | 98.59% | DL |
| 16 | fibroma of prostate | 98.52% | DL |
| 17 | fetal and neonatal alloimmune thrombocytopenia | 98.38% | DL |
| 18 | cholesterol-ester transfer protein deficiency | 98.35% | DL |
| 19 | benign reproductive system neoplasm | 98.29% | DL |
| 20 | prostate cancer/brain cancer susceptibility | 98.21% | DL |

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
