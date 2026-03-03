---
layout: default
title: Drug-Drug Interactions
parent: Safety Data
nav_order: 1
description: "Drug-Drug Interaction (DDI) database for EuTxGNN drug repurposing safety assessment"
permalink: /ddi/
---

# Drug-Drug Interactions (DDI)
{: .fs-9 }

Comprehensive DDI data for drug repurposing safety evaluation
{: .fs-6 .fw-300 }

---

## Introduction

Drug-drug interactions are a critical consideration in drug repurposing. When a drug is considered for a new indication, it may be used alongside different medications than originally intended, potentially creating new interaction risks.

---

## Data Sources

| Source | Records | Drugs | Last Updated |
|--------|---------|-------|--------------|
| DDInter 2.0 | ~190,000 | 1,833 | 2023 |
| Guide to PHARMACOLOGY | ~32,000 | 477 | 2024 |

---

## Severity Classification

| Level | Description | Action |
|-------|-------------|--------|
| **Major** | Potentially life-threatening | Avoid combination |
| **Moderate** | May require monitoring | Use with caution |
| **Minor** | Generally safe | Monitor if necessary |

---

## Usage

DDI information is integrated into individual drug reports. For each drug in EuTxGNN:

1. Navigate to the drug report page
2. Check the "Safety Considerations" section
3. Review major and moderate interactions

---

## External Resources

- [DDInter 2.0](https://ddinter2.scbdd.com/) - Drug-Drug Interaction database
- [DrugBank Interactions](https://go.drugbank.com/) - Commercial drug database
- [Drugs.com Interaction Checker](https://www.drugs.com/drug_interactions.html) - Consumer resource

---

## Data Download

DDI datasets are available for research use:

- [GitHub Repository](https://github.com/yao-care/EuTxGNN)

---

## Related Pages

- [Drug-Disease Interactions](/ddsi/)
- [Drug-Food Interactions](/dfi/)
- [Drug-Herb Interactions](/dhi/)
- [Drug List](/drugs/)
