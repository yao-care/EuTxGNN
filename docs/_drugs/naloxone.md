---
layout: default
title: Naloxone
description: "Naloxone drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 393
evidence_level: L5
indication_count: 50
---

# Naloxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Naloxone |
| DrugBank ID | [DB01183](https://go.drugbank.com/drugs/DB01183) |
| Brand Names (EU) | Naloxone |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 97.42% |

---

## Approved Indication (EMA)

Substitution treatment for opioid-drug dependence, within a framework of medical, social and psychological treatment. The intention of the naloxone component is to deter intravenous misuse. Treatment is intended for use in adults and adolescents over 15 years of age who have agreed to be treated for addiction.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | opiate dependence | 97.42% | DL |
| 2 | morphine dependence | 96.69% | DL |
| 3 | substance abuse/dependence | 91.45% | DL |
| 4 | continuous spikes and waves during sleep | 88.17% | DL |
| 5 | lissencephaly with cerebellar hypoplasia | 87.40% | DL |
| 6 | progressive encephalopathy with leukodystrophy due to DECR deficiency | 87.24% | DL |
| 7 | schizophreniform disorder | 86.35% | DL |
| 8 | nasal cavity disease | 84.84% | DL |
| 9 | psychotic disorder | 82.58% | DL |
| 10 | hypoglycemia | 81.53% | DL |
| 11 | acute pulmonary heart disease | 80.87% | DL |
| 12 | drug-induced dyskinesia | 80.64% | DL |
| 13 | acute laryngopharyngitis | 80.62% | DL |
| 14 | early-onset familial noncirrhotic portal hypertension | 80.19% | DL |
| 15 | idiopathic copper-associated cirrhosis | 80.19% | DL |
| 16 | primitive portal vein thrombosis | 80.19% | DL |
| 17 | hepatopulmonary syndrome | 80.19% | DL |
| 18 | hepatoportal sclerosis | 80.19% | DL |
| 19 | acute intermittent porphyria | 79.78% | DL |
| 20 | congestive heart failure | 79.60% | DL |

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
