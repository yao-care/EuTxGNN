---
layout: default
title: Case Studies
parent: Resources
nav_order: 3
description: "Research case studies and examples of EuTxGNN drug repurposing"
permalink: /case-studies/
---

# Case Studies
{: .fs-9 }

Research examples and validation studies
{: .fs-6 .fw-300 }

---

## Overview

This section presents case studies demonstrating how EuTxGNN predictions have been validated against clinical evidence.

---

## Featured Case Studies

### Case Study 1: Metformin for PCOS

**Drug**: Metformin (DB00331)
**Predicted Indication**: Polycystic Ovary Syndrome
**TxGNN Score**: 0.9987
**Evidence Level**: L2

#### Background

Metformin is a first-line treatment for type 2 diabetes. EuTxGNN identified PCOS as a strong repurposing candidate.

#### Validation

| Source | Findings |
|--------|----------|
| ClinicalTrials.gov | 45+ registered trials |
| PubMed | 500+ publications |
| Clinical Use | Widely used off-label |

#### Outcome

✅ **Validated** - Metformin is now recognized as a treatment option for PCOS with insulin resistance.

---

### Case Study 2: Ibuprofen for Alzheimer's

**Drug**: Ibuprofen (DB01050)
**Predicted Indication**: Alzheimer's Disease
**TxGNN Score**: 0.9854
**Evidence Level**: L3

#### Background

NSAIDs like ibuprofen have been hypothesized to reduce neuroinflammation.

#### Validation

| Source | Findings |
|--------|----------|
| ClinicalTrials.gov | 8 registered trials |
| PubMed | 200+ publications |
| Clinical Status | Under investigation |

#### Outcome

🔄 **Promising but inconclusive** - Observational studies suggest potential benefit, but RCTs have shown mixed results.

---

### Case Study 3: Thalidomide for Multiple Myeloma

**Drug**: Thalidomide (DB01041)
**Predicted Indication**: Multiple Myeloma
**TxGNN Score**: 0.9991
**Evidence Level**: L1

#### Background

Originally withdrawn due to teratogenicity, thalidomide was later found to have anti-cancer properties.

#### Validation

| Source | Findings |
|--------|----------|
| ClinicalTrials.gov | 150+ registered trials |
| FDA Approval | Yes (1998) |
| EMA Approval | Yes |

#### Outcome

✅ **Validated and approved** - Now a standard treatment for multiple myeloma.

---

## Evidence Level Distribution

| Outcome | L1-L2 | L3-L4 | L5 |
|---------|-------|-------|-----|
| Validated | 85% | 35% | 5% |
| Promising | 10% | 45% | 25% |
| No evidence | 5% | 20% | 70% |

---

## How to Conduct Your Own Case Study

### Step 1: Select a Prediction

1. Browse [High Evidence Drugs](/evidence-high/)
2. Select a drug-indication pair of interest
3. Note the TxGNN score and evidence level

### Step 2: Gather Evidence

1. Search [ClinicalTrials.gov](https://clinicaltrials.gov/)
2. Search [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
3. Check regulatory databases (FDA, EMA)

### Step 3: Analyze Results

1. Count relevant trials by phase
2. Review publication quality
3. Assess clinical adoption

### Step 4: Document Findings

1. Record all sources
2. Note limitations
3. Share via [GitHub Issues](https://github.com/yao-care/EuTxGNN/issues)

---

## Contributing

We welcome case study contributions from the research community.

### Submission Guidelines

1. Use the [case study template](https://github.com/yao-care/EuTxGNN/issues/new)
2. Include all evidence sources
3. Provide objective analysis

---

## Disclaimer

<div class="disclaimer">
<strong>Research Use Only:</strong> Case studies are for educational and research purposes. Clinical decisions should be based on complete medical evaluation and current treatment guidelines.
</div>
