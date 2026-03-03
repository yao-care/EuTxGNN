---
layout: default
title: HL7 PDDI-CDS IG Notes
parent: 🏥 SMART on FHIR
nav_order: 10
description: "Technical notes on HL7 Potential Drug-Drug Interaction CDS Implementation Guide"
permalink: /smart/pddi-cds/
---

# HL7 PDDI-CDS IG Notes
{: .fs-9 }

Implementation guide for drug-drug interaction clinical decision support
{: .fs-6 .fw-300 }

---

## Overview

The HL7 PDDI-CDS Implementation Guide provides standards for implementing clinical decision support for potential drug-drug interactions (PDDIs) in healthcare systems.

---

## Key Concepts

### PDDI Types

| Type | Description | Example |
|------|-------------|---------|
| **Pharmacokinetic** | One drug affects absorption, distribution, metabolism, or excretion of another | Rifampin + oral contraceptives |
| **Pharmacodynamic** | Drugs have additive or opposing effects | Warfarin + aspirin |

### Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| **Contraindicated** | Should never be combined | Hard stop |
| **Serious** | Significant potential harm | Soft stop with override |
| **Moderate** | May cause problems | Warning |
| **Minor** | Limited clinical significance | Info only |

---

## CDS Hooks Integration

### Hook: order-select

Fired when a medication is selected for ordering:

```json
{
  "hook": "order-select",
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
  "context": {
    "userId": "Practitioner/example",
    "patientId": "Patient/example",
    "selections": ["MedicationRequest/medrx-new"],
    "draftOrders": {
      "resourceType": "Bundle",
      "entry": [...]
    }
  },
  "prefetch": {
    "patient": {...},
    "medications": {...}
  }
}
```

### Response: CDS Card

```json
{
  "cards": [{
    "uuid": "pddi-card-1",
    "summary": "Potential Drug-Drug Interaction",
    "detail": "Warfarin + Aspirin: Increased bleeding risk",
    "indicator": "warning",
    "source": {
      "label": "EuTxGNN Drug Interaction Database"
    },
    "suggestions": [{
      "label": "Review interaction details",
      "actions": [{
        "type": "create",
        "description": "Document interaction review"
      }]
    }],
    "links": [{
      "label": "Full interaction report",
      "url": "https://eutxgnn.yao.care/ddi/",
      "type": "absolute"
    }]
  }]
}
```

---

## FHIR Resources

### DetectedIssue

Used to record identified drug interactions:

```json
{
  "resourceType": "DetectedIssue",
  "status": "final",
  "code": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
      "code": "DRG",
      "display": "Drug Interaction Alert"
    }]
  },
  "severity": "high",
  "patient": {"reference": "Patient/example"},
  "implicated": [
    {"reference": "MedicationRequest/warfarin"},
    {"reference": "MedicationRequest/aspirin"}
  ],
  "detail": "Concurrent use may increase bleeding risk",
  "mitigation": [{
    "action": {
      "text": "Monitor INR more frequently"
    }
  }]
}
```

### ClinicalUseDefinition

For interaction knowledge base:

```json
{
  "resourceType": "ClinicalUseDefinition",
  "type": "interaction",
  "subject": [
    {"reference": "MedicationKnowledge/warfarin"},
    {"reference": "MedicationKnowledge/aspirin"}
  ],
  "interaction": {
    "interactant": [{
      "itemReference": {"reference": "MedicationKnowledge/aspirin"}
    }],
    "type": {
      "coding": [{
        "system": "http://hl7.org/fhir/interaction-type",
        "code": "pharmacodynamic"
      }]
    },
    "effect": {
      "text": "Increased bleeding risk"
    },
    "management": {
      "text": "Monitor INR closely; consider alternative analgesic"
    }
  }
}
```

---

## EuTxGNN DDI Integration

### Data Sources

| Source | Coverage | Update Frequency |
|--------|----------|------------------|
| DrugBank | 2.5M+ interactions | Quarterly |
| DDInter | 220,000+ pairs | Monthly |

### API Endpoint

```http
GET /fhir/ClinicalUseDefinition?type=interaction&subject=MedicationKnowledge/{drug1}
```

---

## Implementation Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   EHR System    │────▶│   CDS Service   │
│  (order-select) │     │   (EuTxGNN)     │
└─────────────────┘     └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │   Knowledge     │
                        │   Base (DDI)    │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │   CDS Cards     │
                        │   Response      │
                        └─────────────────┘
```

---

## Best Practices

### Alert Fatigue Mitigation

1. **Tiered Alerts**: Only hard stop for contraindicated
2. **Context-Aware**: Consider patient history
3. **Actionable**: Provide specific mitigation steps

### Documentation

1. **Log All Alerts**: For audit trail
2. **Track Overrides**: Monitor safety
3. **Feedback Loop**: Improve rules over time

---

## Resources

- [HL7 PDDI-CDS IG](https://hl7.org/fhir/uv/pddi/)
- [CDS Hooks Specification](https://cds-hooks.org/)
- [EuTxGNN DDI Data](/ddi/)
