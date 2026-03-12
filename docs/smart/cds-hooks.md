---
layout: default
title: CDS Hooks Architecture
parent: 🏥 SMART on FHIR
nav_order: 11
description: "CDS Hooks architecture and implementation guide"
permalink: /smart/cds-hooks/
---

# CDS Hooks Architecture
{: .fs-9 }

Clinical Decision Support integration via CDS Hooks
{: .fs-6 .fw-300 }

---

## What is CDS Hooks?

CDS Hooks is a specification for integrating clinical decision support (CDS) services with EHR systems. It enables real-time alerts and recommendations at the point of care.

---

## Core Concepts

### Hooks

Predefined moments in clinical workflow when CDS can be invoked:

| Hook | Trigger | Use Case |
|------|---------|----------|
| `patient-view` | Patient chart opened | General alerts |
| `order-select` | Order being composed | Drug interactions |
| `order-sign` | Order about to be signed | Final validation |
| `encounter-start` | Encounter begins | Care gaps |
| `encounter-discharge` | Discharge process | Follow-up reminders |

### Cards

Response format containing recommendations:

| Element | Purpose |
|---------|---------|
| `summary` | Brief description (≤140 chars) |
| `detail` | Full explanation |
| `indicator` | Urgency (info, warning, critical) |
| `source` | Attribution |
| `suggestions` | Actionable options |
| `links` | External resources |

---

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│                        EHR System                         │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐     │
│  │  Workflow  │───▶│   Hook     │───▶│   Cards    │     │
│  │  Trigger   │    │  Dispatch  │    │  Display   │     │
│  └────────────┘    └─────┬──────┘    └────────────┘     │
└──────────────────────────┼───────────────────────────────┘
                           │ HTTP POST
                           ▼
┌──────────────────────────────────────────────────────────┐
│                     CDS Service                          │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐     │
│  │  Request   │───▶│  Decision  │───▶│  Response  │     │
│  │  Handler   │    │   Logic    │    │  Builder   │     │
│  └────────────┘    └─────┬──────┘    └────────────┘     │
│                          │                               │
│                    ┌─────▼──────┐                        │
│                    │ Knowledge  │                        │
│                    │   Base     │                        │
│                    └────────────┘                        │
└──────────────────────────────────────────────────────────┘
```

---

## EuTxGNN CDS Service

### Service Discovery

```json
{
  "services": [{
    "hook": "order-select",
    "title": "EuTxGNN Drug Repurposing",
    "description": "Provides drug repurposing predictions for selected medications",
    "id": "eutxgnn-repurposing",
    "prefetch": {
      "patient": "Patient/{{context.patientId}}",
      "medications": "MedicationRequest?patient={{context.patientId}}&status=active"
    }
  }]
}
```

### Request Example

```json
{
  "hook": "order-select",
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
  "fhirServer": "https://ehr.example.org/fhir",
  "fhirAuthorization": {
    "access_token": "...",
    "token_type": "Bearer",
    "scope": "patient/*.read"
  },
  "context": {
    "userId": "Practitioner/123",
    "patientId": "Patient/456",
    "selections": ["MedicationRequest/789"],
    "draftOrders": {
      "resourceType": "Bundle",
      "entry": [{
        "resource": {
          "resourceType": "MedicationRequest",
          "id": "789",
          "medicationCodeableConcept": {
            "coding": [{
              "system": "https://go.drugbank.com",
              "code": "DB00331",
              "display": "Metformin"
            }]
          }
        }
      }]
    }
  },
  "prefetch": {
    "patient": {...},
    "medications": {...}
  }
}
```

### Response Example

```json
{
  "cards": [{
    "uuid": "eutxgnn-1",
    "summary": "Metformin: 50 potential repurposing candidates identified",
    "detail": "EuTxGNN has identified 50 potential new therapeutic uses for Metformin, including:\n- Polycystic Ovary Syndrome (L2 evidence)\n- Cancer prevention (L3 evidence)\n\nThese are research-level predictions requiring clinical validation.",
    "indicator": "info",
    "source": {
      "label": "EuTxGNN Drug Repurposing",
      "url": "https://eutxgnn.yao.care",
      "icon": "https://eutxgnn.yao.care/assets/images/icon.png"
    },
    "links": [{
      "label": "View full report",
      "url": "https://eutxgnn.yao.care/drugs/metformin/",
      "type": "absolute"
    }, {
      "label": "FHIR Resource",
      "url": "https://eutxgnn.yao.care/fhir/MedicationKnowledge/metformin.json",
      "type": "absolute"
    }]
  }]
}
```

---

## Implementation Guide

### Step 1: Register Service

```bash
# POST to EHR's CDS service registry
curl -X POST https://ehr.example.org/cds-services \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://eutxgnn.yao.care/cds-services",
    "hook": "order-select"
  }'
```

### Step 2: Implement Handler

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cds-services', methods=['GET'])
def discovery():
    return jsonify({
        "services": [{
            "hook": "order-select",
            "id": "eutxgnn-repurposing",
            "title": "EuTxGNN Drug Repurposing"
        }]
    })

@app.route('/cds-services/eutxgnn-repurposing', methods=['POST'])
def repurposing_hook():
    data = request.json
    drug_code = extract_drug_code(data)
    predictions = get_predictions(drug_code)

    return jsonify({
        "cards": build_cards(predictions)
    })
```

### Step 3: Test with Sandbox

Use the [CDS Hooks Sandbox](https://sandbox.cds-hooks.org/) to test your service.

---

## Security Considerations

### Authentication

- Use OAuth 2.0 tokens from `fhirAuthorization`
- Validate tokens before processing

### Data Handling

- Only access data needed for decision
- Don't store patient information
- Log access for audit

### CORS

Enable CORS for EHR domains:

```python
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response
```

---

## Best Practices

### Card Design

1. **Be Concise**: Summary ≤140 characters
2. **Be Actionable**: Provide clear next steps
3. **Be Relevant**: Filter low-value alerts

### Performance

1. **Use Prefetch**: Reduce FHIR calls
2. **Cache Knowledge**: Update periodically
3. **Respond Quickly**: <500ms target

### Alert Fatigue

1. **Prioritize**: Only surface critical items
2. **Deduplicate**: Avoid repeat alerts
3. **Allow Dismissal**: Learn from feedback

---

## Resources

- [CDS Hooks Specification](https://cds-hooks.org/)
- [CDS Hooks Sandbox](https://sandbox.cds-hooks.org/)
- [HL7 CDS Implementation Guide](https://hl7.org/fhir/clinicalreasoning-cds-on-fhir.html)
