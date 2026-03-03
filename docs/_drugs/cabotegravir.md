---
layout: default
title: Cabotegravir
description: "Cabotegravir drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 105
evidence_level: L5
indication_count: 50
---

# Cabotegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Cabotegravir |
| DrugBank ID | [DB11751](https://go.drugbank.com/drugs/DB11751) |
| Brand Names (EU) | Apretude |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.45% |

---

## Approved Indication (EMA)

Apretude is indicated in combination with safer sex practices for pre-exposure prophylaxis (PrEP) to reduce the risk of sexually acquired HIV-1 infection in high-risk adults and adolescents, weighing at least 35 kg (see sections 4.2, 4.4 and 5.1).

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | rheumatoid arthritis | 99.45% | DL |
| 2 | sclerosing cholangitis | 99.22% | DL |
| 3 | bronchitis | 99.19% | DL |
| 4 | colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.16% | DL |
| 5 | severe nonproliferative diabetic retinopathy | 99.03% | DL |
| 6 | brachydactyly-syndactyly syndrome | 98.67% | DL |
| 7 | diabetic retinopathy | 98.17% | DL |
| 8 | non-syndromic visceral malformation | 97.86% | DL |
| 9 | autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 97.83% | DL |
| 10 | brain small vessel disease 1 with or without ocular anomalies | 97.82% | DL |
| 11 | biliary atresia intrahepatic | 97.71% | DL |
| 12 | cholestasis | 97.46% | DL |
| 13 | colonic neoplasm | 97.38% | DL |
| 14 | Mirizzi syndrome | 97.30% | DL |
| 15 | diabetic nephropathy | 97.25% | DL |
| 16 | rectosigmoid junction neoplasm | 97.13% | DL |
| 17 | lipoma of colon | 97.09% | DL |
| 18 | colonic lymphangioma | 97.06% | DL |
| 19 | colon leiomyoma | 97.05% | DL |
| 20 | cavernous hemangioma of colon | 97.04% | DL |

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
