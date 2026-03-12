---
layout: default
title: Fentanyl
description: "Fentanyl drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 241
evidence_level: L5
indication_count: 50
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Fentanyl |
| DrugBank ID | [DB00813](https://go.drugbank.com/drugs/DB00813) |
| Brand Names (EU) | PecFent |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

PecFent is indicated for the management of breakthrough pain in adults who are already receiving maintenance opioid therapy for chronic cancer pain. Breakthrough pain is a transitory exacerbation of pain that occurs on a background of otherwise controlled persistent pain. Patients receiving maintenance opioid therapy are those who are taking at least 60 mg of oral morphine daily, at least 25 micrograms of transdermal fentanyl per hour, at least 30 mg of oxycodone daily, at least 8 mg of oral hyd

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | nephrogenic syndrome of inappropriate antidiuresis | 99.46% | DL |
| 2 | Tourette syndrome | 99.05% | DL |
| 3 | trichotillomania | 98.87% | DL |
| 4 | myofascial pain syndrome | 98.09% | DL |
| 5 | migraine disorder | 98.06% | DL |
| 6 | manic bipolar affective disorder | 97.73% | DL |
| 7 | migraine with brainstem aura | 97.71% | DL |
| 8 | headache disorder | 97.26% | DL |
| 9 | methemoglobinemia | 97.22% | DL |
| 10 | idiopathic granulomatous myositis | 97.04% | DL |
| 11 | myositis fibrosa | 97.04% | DL |
| 12 | tendinitis | 97.04% | DL |
| 13 | fibromyalgia | 96.82% | DL |
| 14 | hypertrichosis (disease) | 96.54% | DL |
| 15 | trigeminal autonomic cephalalgia | 96.42% | DL |
| 16 | Ambras type hypertrichosis universalis congenita | 96.35% | DL |
| 17 | syndrome with a Dandy-Walker malformation as major feature | 96.21% | DL |
| 18 | inclusion body myositis | 96.18% | DL |
| 19 | restless legs syndrome | 96.17% | DL |
| 20 | malformation syndrome with odontal and/or periodontal component | 96.12% | DL |

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
