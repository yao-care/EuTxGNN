---
layout: default
title: FHIR API Specification
parent: 🏥 SMART on FHIR
nav_order: 6
description: "FHIR R4 API specification for EuTxGNN"
permalink: /smart/fhir-api/
---

# FHIR API Specification
{: .fs-9 }

Complete FHIR R4 API documentation for EuTxGNN
{: .fs-6 .fw-300 }

---

## Base URL

```
https://eutxgnn.yao.care/fhir
```

---

## CapabilityStatement

### Request

```http
GET /fhir/metadata
Accept: application/fhir+json
```

### Response

Returns a FHIR CapabilityStatement describing server capabilities.

---

## Resources

### MedicationKnowledge

Drug information resources for 642 EMA-approved medications.

#### Read

```http
GET /fhir/MedicationKnowledge/{id}.json
```

**Example**:
```bash
curl https://eutxgnn.yao.care/fhir/MedicationKnowledge/metformin.json
```

#### Resource Structure

```json
{
  "resourceType": "MedicationKnowledge",
  "id": "metformin",
  "code": {
    "coding": [{
      "system": "https://go.drugbank.com",
      "code": "DB00331",
      "display": "Metformin"
    }]
  },
  "status": "active",
  "indicationGuideline": [{
    "indication": [{
      "reference": "ClinicalUseDefinition/metformin-type-2-diabetes-mellitus"
    }]
  }]
}
```

---

### ClinicalUseDefinition

Drug repurposing predictions with evidence levels.

#### Read

```http
GET /fhir/ClinicalUseDefinition/{drug}-{disease}.json
```

**Example**:
```bash
curl https://eutxgnn.yao.care/fhir/ClinicalUseDefinition/metformin-polycystic-ovary-syndrome.json
```

#### Resource Structure

```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "metformin-polycystic-ovary-syndrome",
  "type": "indication",
  "subject": [{
    "reference": "MedicationKnowledge/metformin"
  }],
  "indication": {
    "diseaseSymptomProcedure": {
      "coding": [{
        "system": "http://snomed.info/sct",
        "display": "Polycystic ovary syndrome"
      }]
    }
  },
  "extension": [{
    "url": "https://eutxgnn.yao.care/fhir/StructureDefinition/prediction-score",
    "valueDecimal": 0.9987
  }, {
    "url": "https://eutxgnn.yao.care/fhir/StructureDefinition/evidence-level",
    "valueCode": "L2"
  }]
}
```

---

## Search Parameters

### MedicationKnowledge

| Parameter | Type | Description |
|-----------|------|-------------|
| `_id` | token | Resource ID |
| `code` | token | DrugBank code |
| `status` | token | active \| inactive |

### ClinicalUseDefinition

| Parameter | Type | Description |
|-----------|------|-------------|
| `_id` | token | Resource ID |
| `subject` | reference | MedicationKnowledge reference |
| `type` | token | indication |

---

## Extensions

### Prediction Score

```
URL: https://eutxgnn.yao.care/fhir/StructureDefinition/prediction-score
Type: decimal
Range: 0.0 - 1.0
```

### Evidence Level

```
URL: https://eutxgnn.yao.care/fhir/StructureDefinition/evidence-level
Type: code
Values: L1 | L2 | L3 | L4 | L5
```

| Code | Description |
|------|-------------|
| L1 | Multiple Phase 3 RCTs |
| L2 | Single RCT or multiple Phase 2 |
| L3 | Observational studies |
| L4 | Preclinical evidence |
| L5 | AI prediction only |

---

## Error Responses

### 404 Not Found

```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "not-found",
    "diagnostics": "Resource not found"
  }]
}
```

---

## Rate Limiting

| Tier | Requests/min | Notes |
|------|--------------|-------|
| Public | 60 | Default |
| Research | 300 | Contact us |

---

## Code Examples

### JavaScript (fhir.js)

```javascript
const client = FHIR.client({
  serverUrl: 'https://eutxgnn.yao.care/fhir'
});

// Get drug information
const drug = await client.read({
  resourceType: 'MedicationKnowledge',
  id: 'metformin'
});

// Get predictions for drug
const predictions = await client.search({
  resourceType: 'ClinicalUseDefinition',
  searchParams: {
    subject: 'MedicationKnowledge/metformin'
  }
});
```

### Python (fhir.resources)

```python
import requests

base_url = "https://eutxgnn.yao.care/fhir"

# Get drug information
response = requests.get(f"{base_url}/MedicationKnowledge/metformin.json")
drug = response.json()

# Get specific prediction
response = requests.get(
    f"{base_url}/ClinicalUseDefinition/metformin-type-2-diabetes-mellitus.json"
)
prediction = response.json()
```

### cURL

```bash
# Get CapabilityStatement
curl https://eutxgnn.yao.care/fhir/metadata

# Get drug
curl https://eutxgnn.yao.care/fhir/MedicationKnowledge/ibuprofen.json

# Get prediction
curl https://eutxgnn.yao.care/fhir/ClinicalUseDefinition/ibuprofen-rheumatoid-arthritis.json
```

---

## Resources

- [HL7 FHIR R4](https://www.hl7.org/fhir/R4/)
- [MedicationKnowledge Resource](https://www.hl7.org/fhir/medicationknowledge.html)
- [ClinicalUseDefinition Resource](https://www.hl7.org/fhir/clinicalusedefinition.html)
