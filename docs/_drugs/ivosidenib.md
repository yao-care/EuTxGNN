---
layout: default
title: Ivosidenib
description: "Ivosidenib drug repurposing predictions from TxGNN. Evidence level L5 with 50 predicted indications."
parent: AI Predictions (L5)
nav_order: 319
evidence_level: L5
indication_count: 50
---

# Ivosidenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **50**
{: .fs-6 .fw-300 }

---

## Quick Overview

| Item | Value |
|------|-------|
| Drug Name | Ivosidenib |
| DrugBank ID | [DB14568](https://go.drugbank.com/drugs/DB14568) |
| Brand Names (EU) | Tibsovo |
| Evidence Level | L5 |
| Predicted Indications | 50 |
| Top Prediction Score | 99.54% |

---

## Approved Indication (EMA)

Tibsovo in combination with azacitidine is indicated for the treatment of adult patients with newly diagnosed acute myeloid leukaemia (AML) with an isocitrate dehydrogenase-1 (IDH1) R132 mutation who are not eligible to receive standard induction chemotherapy (see section 5.1). Tibsovo monotherapy is indicated for the treatment of adult patients with locally advanced or metastatic cholangiocarcinoma with an IDH1 R132 mutation who were previously treated by at least one prior line of systemic the

---

## Predicted New Indications

TxGNN model predictions for potential drug repurposing:

| Rank | Indication | Score | Source |
|:----:|------------|------:|--------|
| 1 | acute myeloid leukemia with t(8;21)(q22;q22) translocation | 99.54% | DL |
| 2 | acute myeloid leukemia with CEBPA somatic mutations | 99.53% | DL |
| 3 | acute myeloid leukemia and myelodysplastic syndromes related to topoisomerase type 2 inhibitor | 99.52% | DL |
| 4 | acute myeloid leukemia with inv3(p21;q26.2) or t(3;3)(p21;q26.2) | 99.51% | DL |
| 5 | therapy related acute myeloid leukemia and myelodysplastic syndrome | 99.36% | DL |
| 6 | bulbar polio | 99.31% | DL |
| 7 | acute myeloid leukemia with t(8;16)(p11;p13) translocation | 99.26% | DL |
| 8 | acute myeloid leukemia and myelodysplastic syndromes related to radiation | 99.26% | DL |
| 9 | acute myeloid leukemia and myelodysplastic syndromes related to alkylating agent | 99.26% | DL |
| 10 | acute myeloid leukemia with t(9;11)(p22;q23) | 99.16% | DL |
| 11 | inherited acute myeloid leukemia | 99.13% | DL |
| 12 | unclassified acute myeloid leukemia | 99.11% | DL |
| 13 | acute myeloid leukemia with t(6;9)(p23;q34) | 99.08% | DL |
| 14 | acute myeloblastic leukemia with maturation | 99.04% | DL |
| 15 | acute myeloblastic leukemia without maturation | 98.99% | DL |
| 16 | 5q35 microduplication syndrome | 98.97% | DL |
| 17 | acute myeloid leukemia with minimal differentiation | 98.86% | DL |
| 18 | neuralgic amyotrophy | 98.80% | DL |
| 19 | acute myeloid leukemia with NPM1 somatic mutations | 98.76% | DL |
| 20 | amyotrophic neuralgia | 98.73% | DL |

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
