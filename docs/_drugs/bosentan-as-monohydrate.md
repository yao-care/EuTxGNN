---
layout: default
title: Bosentan (As Monohydrate)
description: "Bosentan (As Monohydrate) drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 87
evidence_level: L5
indication_count: 50
---

# Bosentan (As Monohydrate)
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Bosentan (As Monohydrate) |
| DrugBank ID | [DB00559](https://go.drugbank.com/drugs/DB00559) |
| Brand Names (EU) | Stayveer |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.96% |

---

## Approved Indication (EMA)

Treatment of pulmonary arterial hypertension (PAH) to improve exercise capacity and symptoms in patients with World Health Organization (WHO) functional class III. Efficacy has been shown in:  primary (idiopathic and familial) PAH; PAH secondary to scleroderma without significant interstitial pulmonary disease; PAH associated with congenital systemic-to-pulmonary shunts and Eisenmenger’s physiology.  Some improvements have also been shown in patients with PAH WHO functional class II. Stayveer is

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | scleroderma (disease) | 99.96% | DL |
| 2 | rheumatoid arthritis | 99.80% | DL |
| 3 | brachydactyly-syndactyly syndrome | 99.74% | DL |
| 4 | limited systemic sclerosis | 99.65% | DL |
| 5 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.62% | DL |
| 6 | localized scleroderma | 99.54% | DL |
| 7 | pulmonary hypertension | 99.50% | DL |
| 8 | pseudoxanthoma elasticum, forme fruste | 99.45% | DL |
| 9 | kyphoscoliotic heart disease | 99.43% | DL |
| 10 | elastoma | 99.35% | DL |
| 11 | systemic sclerosis | 99.28% | DL |
| 12 | gout | 99.21% | DL |
| 13 | hypertrichosis (disease) | 99.04% | DL |
| 14 | Ambras type hypertrichosis universalis congenita | 98.93% | DL |
| 15 | uterine polyp | 98.84% | DL |
| 16 | malformation syndrome with odontal and/or periodontal component | 98.81% | DL |
| 17 | epulis | 98.81% | DL |
| 18 | syndrome with a Dandy-Walker malformation as major feature | 98.77% | DL |
| 19 | diffuse cutaneous systemic sclerosis | 98.77% | DL |
| 20 | polyp of vocal cord | 98.77% | DL |

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
