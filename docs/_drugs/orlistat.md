---
layout: default
title: Orlistat
description: "Orlistat drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 425
evidence_level: L5
indication_count: 50
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Orlistat |
| DrugBank ID | [DB01083](https://go.drugbank.com/drugs/DB01083) |
| Brand Names (EU) | Xenical |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.46% |

---

## Approved Indication (EMA)

Xenical is indicated in conjunction with a mildly hypocaloric diet for the treatment of obese patients with a body mass index (BMI) greater or equal to 30 kg/m2, or overweight patients (BMI &gt; 28 kg/m2) with associated risk factors. Treatment with orlistat should be discontinued after 12 weeks if patients have been unable to lose at least 5% of the body weight as measured at the start of therapy.

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | obesity disorder | 99.46% | DL |
| 2 | hypervitaminosis | 99.42% | DL |
| 3 | proximal 16p11.2 microdeletion syndrome | 98.87% | DL |
| 4 | obsolete hypertelorism (disease) | 97.75% | DL |
| 5 | frontorhiny | 96.64% | DL |
| 6 | hypoalphalipoproteinemia | 96.47% | DL |
| 7 | monogenic obesity | 94.45% | DL |
| 8 | obsolete susceptibility to ischemic stroke | 92.00% | DL |
| 9 | ABri amyloidosis | 85.67% | DL |
| 10 | fatty liver disease | 85.26% | DL |
| 11 | homozygous familial hypercholesterolemia | 79.84% | DL |
| 12 | amenorrhea (disease) | 77.89% | DL |
| 13 | non-alcoholic steatohepatitis | 77.14% | DL |
| 14 | hypercarotenemia and vitamin A deficiency, autosomal recessive | 71.03% | DL |
| 15 | lethal polymalformative syndrome, Boissel type | 68.51% | DL |
| 16 | duodenogastric reflux | 68.39% | DL |
| 17 | pentosuria | 68.26% | DL |
| 18 | duodenal obstruction | 68.11% | DL |
| 19 | fibrosis of extraocular muscles, congenital, with synergistic divergence | 66.92% | DL |
| 20 | mitral valve prolapse, myxomatous | 66.79% | DL |

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
