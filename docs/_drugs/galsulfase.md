---
layout: default
title: Galsulfase
description: "Galsulfase drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 260
evidence_level: L5
indication_count: 50
---

# Galsulfase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Galsulfase |
| DrugBank ID | [DB01279](https://go.drugbank.com/drugs/DB01279) |
| Brand Names (EU) | Naglazyme |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.89% |

---

## Approved Indication (EMA)

Naglazyme is indicated for long-term enzyme-replacement therapy in patients with a confirmed diagnosis of mucopolysaccharidosis VI (MPS VI; N-acetylgalactosamine-4-sulfatase deficiency; Maroteaux-Lamy syndrome) (see section 5.1). As for all lysosomal genetic disorders, it is of primary importance, especially in severe forms, to initiate treatment as early as possible, before appearance of non-reversible clinical manifestations of the disease. A key issue is to treat young patients aged &lt;5 yea

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | ptosis-strabismus-ectopic pupils syndrome | 97.89% | DL |
| 2 | camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye | 97.87% | DL |
| 3 | congenital Horner syndrome (disease) | 97.84% | DL |
| 4 | ptosis-vocal cord paralysis syndrome | 97.83% | DL |
| 5 | ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome | 97.67% | DL |
| 6 | jaw-winking syndrome | 97.65% | DL |
| 7 | congenital entropion | 97.64% | DL |
| 8 | epiblepharon | 97.55% | DL |
| 9 | congenital ectropion | 97.48% | DL |
| 10 | mucopolysaccharidosis | 96.93% | DL |
| 11 | Scheie syndrome | 94.79% | DL |
| 12 | Steel syndrome | 93.88% | DL |
| 13 | inborn disorder of lysosomal amino acid transport | 92.43% | DL |
| 14 | proximal myopathy with extrapyramidal signs | 91.31% | DL |
| 15 | Hurler syndrome | 90.23% | DL |
| 16 | Charcot-Marie-Tooth disease | 90.05% | DL |
| 17 | Sanfilippo syndrome | 88.67% | DL |
| 18 | lysosomal storage disease with skeletal involvement | 87.99% | DL |
| 19 | alpha-mannosidosis | 87.23% | DL |
| 20 | skeletal muscle disease | 86.19% | DL |

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
