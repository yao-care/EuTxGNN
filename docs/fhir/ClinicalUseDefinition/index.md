---
layout: default
title: ClinicalUseDefinition Resources
nav_exclude: true
description: "FHIR R4 ClinicalUseDefinition resources for EuTxGNN predictions"
permalink: /fhir/ClinicalUseDefinition/
---

# ClinicalUseDefinition Resources
{: .fs-9 }

FHIR R4 ClinicalUseDefinition resources for drug repurposing predictions
{: .fs-6 .fw-300 }

---

## Overview

This directory contains FHIR R4 ClinicalUseDefinition resources representing drug repurposing predictions from EuTxGNN.

**Total Resources**: 32,368 predictions

---

## Access Individual Resources

Resources are available as JSON files:

```
/fhir/ClinicalUseDefinition/{drug-slug}-{disease-slug}.json
```

### Example

```bash
curl https://eutxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-type-2-diabetes-mellitus.json
```

---

## Resource Structure

Each ClinicalUseDefinition resource includes:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (drug-disease combination) |
| `type` | "indication" |
| `indication.diseaseSymptomProcedure` | Predicted disease/condition |
| `extension` | Prediction score and evidence level |

---

## Evidence Levels

| Level | Description |
|-------|-------------|
| L1 | Multiple RCTs supporting |
| L2 | Single RCT supporting |
| L3 | Observational studies |
| L4 | Preclinical evidence |
| L5 | AI prediction only |

---

## Query by Drug

To find all predictions for a specific drug, use the FHIR search syntax:

```
GET /fhir/ClinicalUseDefinition?subject=MedicationKnowledge/{drug-slug}
```

---

## Related Resources

- [FHIR CapabilityStatement](/fhir/metadata)
- [MedicationKnowledge Resources](/fhir/MedicationKnowledge/)
- [Drug Reports](/drug-reports/)
