---
layout: default
title: Carglumic Acid
description: "Carglumic Acid drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 117
evidence_level: L5
indication_count: 50
---

# Carglumic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Carglumic Acid |
| DrugBank ID | [DB06775](https://go.drugbank.com/drugs/DB06775) |
| Brand Names (EU) | Ucedane |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 86.61% |

---

## Approved Indication (EMA)

Ucedane is indicated in treatment of:  hyperammonaemia due to N-acetylglutamate synthase primary deficiency; Hyperammonaemia due to isovaleric acidaemia; Hyperammonaemia due to methymalonic acidaemia; Hyperammonaemia due to propionic acidaemia.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | cystic teratoma | 86.61% | DL |
| 2 | spinal cord dermoid cyst | 86.47% | DL |
| 3 | disease of orbital part of eye adnexa | 86.27% | DL |
| 4 | disease of orbital region | 86.06% | DL |
| 5 | dermoid cyst of ovary | 85.85% | DL |
| 6 | eye disease | 83.64% | DL |
| 7 | open-angle glaucoma | 83.33% | DL |
| 8 | primary hereditary glaucoma | 83.22% | DL |
| 9 | chronic relapsing inflammatory optic neuropathy | 83.21% | DL |
| 10 | isolated optic neuritis | 83.21% | DL |
| 11 | recurrent idiopathic neuroretinitis | 83.21% | DL |
| 12 | optic perineuritis | 83.21% | DL |
| 13 | conjunctival degeneration | 83.15% | DL |
| 14 | vitreous detachment | 83.14% | DL |
| 15 | total internal ophthalmoplegia | 83.12% | DL |
| 16 | cycloplegia | 83.12% | DL |
| 17 | accommodative spasm | 83.12% | DL |
| 18 | luxation of globe | 83.06% | DL |
| 19 | microcornea-corectopia-macular hypoplasia syndrome | 83.05% | DL |
| 20 | blepharophimosis-radioulnar synostosis syndrome | 83.05% | DL |

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
