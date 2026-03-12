---
layout: default
title: Oteracil
description: "oteracil drug repurposing predictions from TxGNN. Evidence level L1 with 50 predicted indications."
parent: Phase 3+ Evidence (L1)
nav_order: 429
evidence_level: L1
indication_count: 50
---

# Oteracil
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Oteracil |
| DrugBank ID | [DB03209](https://go.drugbank.com/drugs/DB03209) |
| Brand Names (EU) | Oteracil |
| Evidence Level | L1 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.99% |

---

## Approved Indication (EMA)

Teysuno is indicated in adults: - for the treatment of advanced gastric cancer when given in combination with cisplatin (see section 5.1). - as monotherapy or in combination with oxaliplatin or irinotecan, with or without bevacizumab, for the treatment of patients with metastatic colorectal cancer for whom it is not possible to continue treatment with another fluoropyrimidine due to hand-foot syndrome or cardiovascular toxicity that developed in the adjuvant or metastatic setting.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | colonic neoplasm | 99.99% | DL |
| 2 | cecum villous adenoma | 99.98% | DL |
| 3 | cecum neuroendocrine tumor G1 | 99.98% | DL |
| 4 | lipoma of colon | 99.98% | DL |
| 5 | cecal disease | 99.98% | DL |
| 6 | rectosigmoid junction neoplasm | 99.98% | DL |
| 7 | benign neoplasm of cecum | 99.98% | DL |
| 8 | colonic lymphangioma | 99.98% | DL |
| 9 | colon leiomyoma | 99.98% | DL |
| 10 | cavernous hemangioma of colon | 99.98% | DL |
| 11 | colorectal gastrointestinal stromal tumor | 99.96% | DL |
| 12 | colorectal hamartoma | 99.95% | DL |
| 13 | gastric carcinoma | 99.95% | DL |
| 14 | colorectal leiomyoma | 99.95% | DL |
| 15 | squamous cell carcinoma of colon | 99.93% | DL |
| 16 | diffuse gastric adenocarcinoma | 99.93% | DL |
| 17 | malignant gastric granular cell tumor | 99.92% | DL |
| 18 | cardia cancer | 99.91% | DL |
| 19 | gastric lymphoma | 99.91% | DL |
| 20 | carcinoma in situ of gastric body | 99.91% | DL |

*Showing top 20 of 50 predictions.*

---


---
## Clinical Evidence

The following indications have supporting clinical evidence:

| Indication | Level | Trials | Articles | Summary |
|------------|:-----:|:------:|:--------:|---------|
| colonic neoplasm | L1 | 8 | 0 | 3 Phase 3 trial(s), 4 Phase 2 trial(s) |

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
