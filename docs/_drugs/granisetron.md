---
layout: default
title: Granisetron
description: "Granisetron drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 276
evidence_level: L5
indication_count: 50
---

# Granisetron
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Granisetron |
| DrugBank ID | [DB00889](https://go.drugbank.com/drugs/DB00889) |
| Brand Names (EU) | Sancuso |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.62% |

---

## Approved Indication (EMA)

Prevention of nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy, with or without cisplatin, for up to five consecutive days. Sancuso may be used in patients receiving their first chemotherapy regimen or in patients who have previously received chemotherapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | manic bipolar affective disorder | 99.62% | DL |
| 2 | Tourette syndrome | 99.52% | DL |
| 3 | acute contagious conjunctivitis | 99.49% | DL |
| 4 | angioedema | 99.36% | DL |
| 5 | allergic urticaria | 99.32% | DL |
| 6 | nephrogenic syndrome of inappropriate antidiuresis | 99.32% | DL |
| 7 | trichotillomania | 99.23% | DL |
| 8 | bronchitis | 99.18% | DL |
| 9 | cold urticaria | 99.10% | DL |
| 10 | conjunctivitis | 99.09% | DL |
| 11 | punctate epithelial keratoconjunctivitis | 98.32% | DL |
| 12 | anaphylaxis | 98.24% | DL |
| 13 | common cold | 97.99% | DL |
| 14 | dysentery | 97.90% | DL |
| 15 | renin-angiotensin-aldosterone system-blocker-induced angioedema | 97.87% | DL |
| 16 | obsessive-compulsive disorder | 97.84% | DL |
| 17 | acquired angioedema | 97.76% | DL |
| 18 | schizotypal personality disorder | 97.72% | DL |
| 19 | paranoid personality disorder | 97.72% | DL |
| 20 | schizoid personality disorder | 97.72% | DL |

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
