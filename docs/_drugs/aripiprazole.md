---
layout: default
title: Aripiprazole
description: "Aripiprazole drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 47
evidence_level: L5
indication_count: 50
---

# Aripiprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Aripiprazole |
| DrugBank ID | [DB01238](https://go.drugbank.com/drugs/DB01238) |
| Brand Names (EU) | Aripiprazole Accord |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Aripiprazole Accord is indicated for the treatment of schizophrenia in adults and in adolescents aged 15 years and older. Aripiprazole Accord is indicated for the treatment of moderate to severe manic episodes in Bipolar I Disorder and for the prevention of a new manic episode in adults who experienced predominantly manic episodes and whose manic episodes responded to aripiprazole treatment. Aripiprazole Accord is indicated for the treatment up to 12 weeks of moderate to severe manic episodes in

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.98% | DL |
| 2 | bipolar disorder | 99.72% | DL |
| 3 | autism spectrum disorder | 99.68% | DL |
| 4 | major affective disorder | 99.62% | DL |
| 5 | autism susceptibility 1 | 99.61% | DL |
| 6 | gaze palsy, familial horizontal, with progressive scoliosis | 99.60% | DL |
| 7 | schizophrenia | 99.58% | DL |
| 8 | asperger syndrome, susceptibility to | 99.52% | DL |
| 9 | Phelan-McDermid syndrome | 99.44% | DL |
| 10 | amelocerebrohypohidrotic syndrome | 99.34% | DL |
| 11 | distal 17p13.3 microdeletion syndrome | 99.34% | DL |
| 12 | trichotillomania | 99.26% | DL |
| 13 | Malan overgrowth syndrome | 99.26% | DL |
| 14 | retinal dystrophy with or without extraocular anomalies | 99.25% | DL |
| 15 | hydranencephaly (disease) | 99.21% | DL |
| 16 | congenital disorder of glycosylation with defective fucosylation | 99.17% | DL |
| 17 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.01% | DL |
| 18 | myopia X-linked | 99.00% | DL |
| 19 | syndromic myopia | 98.98% | DL |
| 20 | myopia 26, X-linked, female-limited | 98.95% | DL |

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
