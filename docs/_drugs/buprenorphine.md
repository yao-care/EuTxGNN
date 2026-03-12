---
layout: default
title: Buprenorphine
description: "Buprenorphine drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 100
evidence_level: L5
indication_count: 50
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Buprenorphine |
| DrugBank ID | [DB00921](https://go.drugbank.com/drugs/DB00921) |
| Brand Names (EU) | Buvidal |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.51% |

---

## Approved Indication (EMA)

Substitution treatment for opioid-drug dependence, within a framework of medical, social and psychological treatment. The intention of the naloxone component is to deter intravenous misuse. Treatment is intended for use in adults and adolescents over 15 years of age who have agreed to be treated for addiction.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opiate dependence | 99.51% | DL |
| 2 | morphine dependence | 99.42% | DL |
| 3 | acute intermittent porphyria | 99.41% | DL |
| 4 | lingual-facial-buccal dyskinesia | 99.32% | DL |
| 5 | chronic tic disorder | 99.13% | DL |
| 6 | continuous spikes and waves during sleep | 99.05% | DL |
| 7 | extrapyramidal and movement disease | 99.03% | DL |
| 8 | benign shuddering attacks | 99.03% | DL |
| 9 | schizophreniform disorder | 98.99% | DL |
| 10 | schizophrenia | 98.98% | DL |
| 11 | benign paroxysmal tonic upgaze of childhood with ataxia | 98.91% | DL |
| 12 | psychogenic movement disorders | 98.89% | DL |
| 13 | primary orthostatic tremor | 98.85% | DL |
| 14 | tremor-nystagmus-duodenal ulcer syndrome | 98.83% | DL |
| 15 | drug-induced dyskinesia | 98.76% | DL |
| 16 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 98.74% | DL |
| 17 | polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 98.74% | DL |
| 18 | retinal dystrophy with or without extraocular anomalies | 98.60% | DL |
| 19 | congenital disorder of glycosylation with defective fucosylation | 98.57% | DL |
| 20 | hydranencephaly (disease) | 98.56% | DL |

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
