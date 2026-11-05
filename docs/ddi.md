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

| Source | Records | Drugs | Version |
|--------|---------|-------|---------|
| DDInter (`ddinter_code_*.csv` download files) | {{ site.data.ddi_sources.display.ddinter_rows }} drug–drug interaction rows ({{ site.data.ddi_sources.display.ddinter_unique_pairs }} unique drug pairs) | {{ site.data.ddi_sources.display.ddinter_drug_names }} drug names | Files in the EuTxGNN data release [data-20261031-060230](https://github.com/yao-care/EuTxGNN/releases/tag/data-20261031-060230) |
| Guide to PHARMACOLOGY | {{ site.data.ddi_sources.display.gtopdb_drug_target_records }} approved-drug target rows (drug–target data, not drug–drug interactions; no severity levels) | {{ site.data.ddi_sources.display.gtopdb_ligands }} ligands | GtoPdb {{ site.data.ddi_sources.gtopdb_version }} (published {{ site.data.ddi_sources.gtopdb_published }}) |

Counts are taken from the files in the EuTxGNN data release (`data/external/ddi/`).

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
