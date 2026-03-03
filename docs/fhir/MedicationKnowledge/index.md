---
layout: default
title: MedicationKnowledge Resources
nav_exclude: true
description: "FHIR R4 MedicationKnowledge resources for EuTxGNN"
permalink: /fhir/MedicationKnowledge/
---

# MedicationKnowledge Resources
{: .fs-9 }

FHIR R4 MedicationKnowledge resources for EMA-approved drugs
{: .fs-6 .fw-300 }

---

## Overview

This directory contains FHIR R4 MedicationKnowledge resources for drugs analyzed by EuTxGNN.

**Total Resources**: 642 drugs

---

## Access Individual Resources

Resources are available as JSON files:

```
/fhir/MedicationKnowledge/{drug-slug}.json
```

### Example

```bash
curl https://eutxgnn.yao.care/fhir/MedicationKnowledge/metformin.json
```

---

## Resource Structure

Each MedicationKnowledge resource includes:

| Field | Description |
|-------|-------------|
| `id` | Drug slug (e.g., "metformin") |
| `code` | Drug name and DrugBank coding |
| `indicationGuideline` | Reference to ClinicalUseDefinition resources |

---

## Sample Drugs

| Drug | Resource |
|------|----------|
| Metformin | [metformin.json](/fhir/MedicationKnowledge/metformin.json) |
| Amlodipine | [amlodipine.json](/fhir/MedicationKnowledge/amlodipine.json) |
| Ibuprofen | [ibuprofen.json](/fhir/MedicationKnowledge/ibuprofen.json) |
| Apixaban | [apixaban.json](/fhir/MedicationKnowledge/apixaban.json) |

---

## Related Resources

- [FHIR CapabilityStatement](/fhir/metadata)
- [ClinicalUseDefinition Resources](/fhir/ClinicalUseDefinition/)
- [Downloads](/downloads/)
