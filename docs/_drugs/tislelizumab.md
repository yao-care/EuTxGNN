---
layout: default
title: Tislelizumab
description: "Tislelizumab drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 588
evidence_level: L5
indication_count: 50
---

# Tislelizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Tislelizumab |
| DrugBank ID | [DB14922](https://go.drugbank.com/drugs/DB14922) |
| Brand Names (EU) | Tevimbra |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 93.76% |

---

## Approved Indication (EMA)

Non-small cell lung cancer (NSCLC) Tevimbra, in combination with platinum-containing chemotherapy as neoadjuvant treatment and then continued as monotherapy as adjuvant treatment, is indicated for the treatment of adult patients with resectable NSCLC at high risk of recurrence (for selection criteria, see section 5.1).Tevimbra in combination with pemetrexed and platinum containing chemotherapy is indicated for the first-line treatment of adult patients with non-squamous NSCLC&nbsp; whose tumours

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | mixed-type autoimmune hemolytic anemia | 93.76% | DL |
| 2 | idiopathic aplastic anemia | 93.76% | DL |
| 3 | dermatitis | 93.69% | DL |
| 4 | paroxysmal nocturnal hemoglobinuria | 93.67% | DL |
| 5 | drug-induced autoimmune hemolytic anemia | 93.67% | DL |
| 6 | proteinuria | 93.07% | DL |
| 7 | acne keloid | 93.05% | DL |
| 8 | neonatal autoimmune hemolytic anemia | 93.03% | DL |
| 9 | primary CD59 deficiency | 92.84% | DL |
| 10 | amyopathic dermatomyositis | 92.79% | DL |
| 11 | neonatal dermatomyositis | 92.74% | DL |
| 12 | cold agglutinin disease | 92.47% | DL |
| 13 | hydroa vacciniforme, familial | 92.41% | DL |
| 14 | secondary interstitial lung disease specific to childhood associated with a connective tissue disease | 92.36% | DL |
| 15 | acrodermatitis chronica atrophicans | 92.25% | DL |
| 16 | hepatic veno-occlusive disease-immunodeficiency syndrome | 91.69% | DL |
| 17 | pancytopenia due to IKZF1 mutations | 91.04% | DL |
| 18 | chromhidrosis | 90.97% | DL |
| 19 | adult idiopathic neutropenia | 90.78% | DL |
| 20 | congenital neutropenia-myelofibrosis-nephromegaly syndrome | 90.78% | DL |

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
