---
layout: default
title: Technical Documentation
parent: 🏥 SMART on FHIR
nav_order: 2
description: "Technical implementation guide for EuTxGNN SMART on FHIR"
permalink: /smart/setup/
---

# Technical Documentation
{: .fs-9 }

Implementation details for EHR integration
{: .fs-6 .fw-300 }

---

## Architecture Overview

```
EHR System → SMART Authorization → EuTxGNN App → FHIR API
```

---

## Registration Requirements

### App Metadata

| Field | Value |
|-------|-------|
| App Name | EuTxGNN Drug Repurposing |
| Launch URL | `https://eutxgnn.yao.care/smart/launch.html` |
| Redirect URL | `https://eutxgnn.yao.care/smart/app.html` |
| App Type | Public client |

### Required Scopes

```
launch
patient/Patient.read
patient/MedicationRequest.read
```

### Optional Scopes

```
patient/Condition.read
patient/AllergyIntolerance.read
```

---

## OAuth 2.0 Flow

### 1. Launch Request

```
GET /smart/launch.html?iss={ehr_fhir_url}&launch={launch_token}
```

### 2. Authorization

The app redirects to the EHR's authorization endpoint:

```
GET {authorize_url}?
  response_type=code
  &client_id={client_id}
  &redirect_uri=https://eutxgnn.yao.care/smart/app.html
  &scope=launch patient/Patient.read patient/MedicationRequest.read
  &state={state}
  &aud={fhir_url}
```

### 3. Token Exchange

```
POST {token_url}
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code={authorization_code}
&redirect_uri={redirect_uri}
```

---

## FHIR Resources Used

### MedicationRequest

Query patient's active medications:

```
GET {fhir_url}/MedicationRequest?patient={patient_id}&status=active
```

### Patient

Get patient demographics:

```
GET {fhir_url}/Patient/{patient_id}
```

---

## EuTxGNN API Integration

### Query Drug Predictions

```
GET https://eutxgnn.yao.care/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/{drugbank_id}
```

### Response Format

FHIR R4 ClinicalUseDefinition resources containing:
- Predicted indication
- Evidence level
- Prediction confidence score

---

## Security Considerations

1. **HTTPS Required**: All communications must use TLS
2. **Token Handling**: Access tokens are not stored server-side
3. **Data Minimization**: Only required patient data is accessed
4. **Audit Logging**: All accesses are logged for compliance

---

## Testing

### SMART App Launcher

Use the [SMART App Launcher](https://launch.smarthealthit.org/) for testing:

1. Select "Launch App"
2. Enter EuTxGNN launch URL
3. Select sample patient
4. Verify app functionality

---

## Support

For implementation support:
- [GitHub Issues](https://github.com/yao-care/EuTxGNN/issues)
- [FHIR API Documentation](/smart/fhir-api/)
