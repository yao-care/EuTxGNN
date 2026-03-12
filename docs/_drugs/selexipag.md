---
layout: default
title: Selexipag
description: "Selexipag drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 520
evidence_level: L5
indication_count: 50
---

# Selexipag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Selexipag |
| DrugBank ID | [DB11362](https://go.drugbank.com/drugs/DB11362) |
| Brand Names (EU) | Uptravi |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 98.03% |

---

## Approved Indication (EMA)

Uptravi is indicated for the long-term treatment of pulmonary arterial hypertension (PAH) in adult patients with WHO functional class (FC) II–III, either as combination therapy in patients insufficiently controlled with an endothelin receptor antagonist (ERA) and/or a phosphodiesterase type 5 (PDE-5) inhibitor, or as monotherapy in patients who are not candidates for these therapies. Efficacy has been shown in a PAH population including idiopathic and heritable PAH, PAH associated with connectiv

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | pulmonary arterial hypertension associated with congenital heart disease | 98.03% | DL |
| 2 | pulmonary arteriovenous malformation (disease) | 98.00% | DL |
| 3 | pulmonary arterial hypertension associated with connective tissue disease | 97.78% | DL |
| 4 | pulmonary arterial hypertension associated with HIV infection | 97.78% | DL |
| 5 | pulmonary arterial hypertension associated with chronic hemolytic anemia | 97.78% | DL |
| 6 | pulmonary arterial hypertension associated with schistosomiasis | 97.78% | DL |
| 7 | pulmonary arterial hypertension | 97.70% | DL |
| 8 | hypotrichosis simplex of the scalp | 97.11% | DL |
| 9 | congenital hypotrichosis milia | 96.30% | DL |
| 10 | diffuse alopecia areata | 96.00% | DL |
| 11 | malformation syndrome with odontal and/or periodontal component | 93.77% | DL |
| 12 | syndrome with a Dandy-Walker malformation as major feature | 93.31% | DL |
| 13 | isolated genetic hair shaft abnormality | 93.23% | DL |
| 14 | bilateral parasagittal parieto-occipital polymicrogyria | 93.19% | DL |
| 15 | telangiectasia, hereditary hemorrhagic, | 93.02% | DL |
| 16 | Ambras type hypertrichosis universalis congenita | 92.96% | DL |
| 17 | axial spondylometaphyseal dysplasia | 92.75% | DL |
| 18 | aleukemic mast cell leukemia | 92.73% | DL |
| 19 | hypertrichosis (disease) | 92.36% | DL |
| 20 | dermatofibrosarcoma protuberans | 92.28% | DL |

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
