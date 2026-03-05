---
layout: default
title: Risankizumab
description: "risankizumab drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 497
evidence_level: L1
indication_count: 50
---

# Risankizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Risankizumab |
| DrugBank ID | [DB14762](https://go.drugbank.com/drugs/DB14762) |
| Brand Names (EU) | Skyrizi |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.98% |

---

## Approved Indication (EMA)

Plaque PsoriasisSkyrizi is indicated for the treatment of moderate to severe plaque psoriasis in adults who are candidates for systemic therapy.Psoriatic ArthritisSkyrizi, alone or in combination with methotrexate (MTX), is indicated for the treatment of active psoriatic arthritis in adults who have had an inadequate response or who have been intolerant to one or more disease-modifying antirheumatic drugs (DMARDs). Crohn’s diseaseSkyrizi is indicated for the treatment of adult patients with mode

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | dermatitis | 99.98% | DL |
| 2 | neonatal dermatomyositis | 99.97% | DL |
| 3 | amyopathic dermatomyositis | 99.97% | DL |
| 4 | acrodermatitis chronica atrophicans | 99.97% | DL |
| 5 | acne keloid | 99.97% | DL |
| 6 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 99.97% | DL |
| 7 | psoriasis | 99.96% | DL |
| 8 | hydroa vacciniforme, familial | 99.96% | DL |
| 9 | severe nonproliferative diabetic retinopathy | 99.95% | DL |
| 10 | parapsoriasis | 99.95% | DL |
| 11 | pityriasis lichenoides | 99.91% | DL |
| 12 | acute lichenoid pityriasis | 99.89% | DL |
| 13 | diabetic retinopathy | 99.81% | DL |
| 14 | pustulosis palmaris et plantaris | 99.77% | DL |
| 15 | psoriasis 14, pustular | 99.74% | DL |
| 16 | primary release disorder of platelets | 99.47% | DL |
| 17 | pseudo-von Willebrand disease | 99.45% | DL |
| 18 | seborrheic dermatitis | 99.33% | DL |
| 19 | neurolymphomatosis | 99.24% | DL |
| 20 | polyp of middle ear | 99.04% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| dermatitis | L1 | 7 | 10 | 1 Phase 2 trial(s), 2 review(s)/meta-analysis |

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
