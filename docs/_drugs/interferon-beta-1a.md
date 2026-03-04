---
layout: default
title: Interferon Beta-1A
description: "interferon beta-1a drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 311
evidence_level: L1
indication_count: 50
---

# Interferon Beta-1A
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Interferon Beta-1A |
| DrugBank ID | [DB00060](https://go.drugbank.com/drugs/DB00060) |
| Brand Names (EU) | Rebif |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.97% |

---

## Approved Indication (EMA)

Rebif is indicated for the treatment of:  patients with a single demyelinating event with an active inflammatory process, if alternative diagnoses have been excluded, and if they are determined to be at high risk of developing clinically definite multiple sclerosis; patients with relapsing multiple sclerosis. In clinical trials, this was characterised by two or more acute exacerbations in the previous two years.  Efficacy has not been demonstrated in patients with secondary progressive multiple 

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | relapsing-remitting multiple sclerosis | 99.97% | DL |
| 2 | Jeune syndrome situs inversus | 97.47% | DL |
| 3 | Pierre Robin syndrome associated with a chromosomal anomaly | 97.31% | DL |
| 4 | partial deletion of the long arm of chromosome 22 | 97.25% | DL |
| 5 | disorder of fucoglycosan synthesis | 97.21% | DL |
| 6 | Laubry-Pezzi syndrome | 97.21% | DL |
| 7 | partial deletion of the long arm of chromosome 7 | 97.17% | DL |
| 8 | orofacial clefting syndrome | 97.14% | DL |
| 9 | genetic syndromic Pierre Robin syndrome | 97.14% | DL |
| 10 | rete ovarii cystadenoma | 97.11% | DL |
| 11 | borderline ovarian serous tumor | 97.08% | DL |
| 12 | ovarian benign neoplasm | 97.01% | DL |
| 13 | ovarian papillary cystadenoma | 96.99% | DL |
| 14 | ovarian mucinous cystadenofibroma | 96.97% | DL |
| 15 | hairy cell leukemia | 96.90% | DL |
| 16 | serous neoplasm | 96.89% | DL |
| 17 | mucinous ovarian cystadenoma | 96.82% | DL |
| 18 | malignant ovarian Brenner tumor | 96.82% | DL |
| 19 | ovarian surface papilloma | 96.79% | DL |
| 20 | autoimmune disease of central nervous system | 96.79% | DL |

*Showing top 20 of 50 predictions.*

---

## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| relapsing-remitting multiple sclerosis | L1 | 20 | 20 | 5 Phase 3 trial(s), 2 Phase 2 trial(s), 3 RCT(s),  |

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
