---
layout: default
title: Cerliponase Alfa
description: "Cerliponase Alfa drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 128
evidence_level: L5
indication_count: 50
---

# Cerliponase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cerliponase Alfa |
| DrugBank ID | [DB13173](https://go.drugbank.com/drugs/DB13173) |
| Brand Names (EU) | Brineura |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Brineura is indicated for the treatment of neuronal ceroid lipofuscinosis type 2 (CLN2) disease, also known as tripeptidyl peptidase 1 (TPP1) deficiency

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | Scheie syndrome | 99.98% | DL |
| 2 | Hurler syndrome | 99.97% | DL |
| 3 | lysosomal storage disease with skeletal involvement | 99.95% | DL |
| 4 | cholesteryl ester storage disease | 99.93% | DL |
| 5 | Gaucher disease | 99.93% | DL |
| 6 | familial encephalopathy with neuroserpin inclusion bodies | 99.93% | DL |
| 7 | infantile neuronal ceroid lipofuscinosis | 99.92% | DL |
| 8 | Wolman disease with hypolipoproteinemia and acanthocytosis | 99.92% | DL |
| 9 | myoclonic epilepsy, juvenile, susceptibility to | 99.92% | DL |
| 10 | proximal myopathy with extrapyramidal signs | 99.92% | DL |
| 11 | autosomal ichthyosis syndrome with fatal disease course | 99.90% | DL |
| 12 | Wolman disease | 99.89% | DL |
| 13 | adolescent/adult-onset epilepsy syndrome | 99.89% | DL |
| 14 | Tay-Sachs disease | 99.88% | DL |
| 15 | adolescence-adult electroclinical syndrome | 99.88% | DL |
| 16 | growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant | 99.88% | DL |
| 17 | adult Krabbe disease | 99.88% | DL |
| 18 | Sanfilippo syndrome | 99.85% | DL |
| 19 | lysosomal acid lipase deficiency | 99.85% | DL |
| 20 | skeletal muscle disease | 99.85% | DL |

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
