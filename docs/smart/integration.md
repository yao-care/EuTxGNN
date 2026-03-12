---
layout: default
title: Integration Resources
parent: 🏥 SMART on FHIR
nav_order: 3
description: "Third-party integration resources for EuTxGNN"
permalink: /smart/integration/
---

# Integration Resources
{: .fs-9 }

Resources for integrating EuTxGNN with healthcare systems
{: .fs-6 .fw-300 }

---

## Supported EHR Systems

EuTxGNN is compatible with any EHR that supports SMART on FHIR:

| EHR System | Status | Notes |
|------------|--------|-------|
| Epic | Compatible | Requires app registration |
| Cerner | Compatible | Millennium platform |
| MEDITECH | Compatible | Expanse platform |
| Allscripts | Compatible | TouchWorks/Professional |
| athenahealth | Compatible | athenaClinicals |

---

## Integration Patterns

### Pattern 1: EHR-Embedded Launch

The most common pattern where the app launches from within the EHR:

```
1. User opens patient chart
2. Selects EuTxGNN from app menu
3. EHR passes launch context
4. App displays predictions for patient's medications
```

### Pattern 2: Standalone with Patient Selection

For research or administrative use:

```
1. User accesses EuTxGNN directly
2. Authenticates with EHR credentials
3. Selects patient from search
4. Views predictions
```

### Pattern 3: CDS Integration

Clinical Decision Support integration via CDS Hooks:

```
1. Clinician orders medication
2. CDS Hook fires
3. EuTxGNN returns relevant predictions
4. Decision support card displayed
```

---

## API Endpoints

### FHIR Resources

| Resource | Endpoint | Description |
|----------|----------|-------------|
| CapabilityStatement | `/fhir/metadata` | Server capabilities |
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` | Drug information |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` | Predictions |

### Bulk Data

For research use, bulk data access is available:

- [Drug Mapping CSV](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/drug_mapping.csv)
- [All Predictions CSV](https://github.com/yao-care/EuTxGNN/raw/main/data/processed/repurposing_candidates.csv)

---

## Authentication

### Public Client

EuTxGNN operates as a public client (no client secret):

```javascript
const clientId = 'eutxgnn-public';
// No client_secret required
```

### Token Refresh

Access tokens expire after 1 hour. Refresh tokens (if provided) can be used:

```
POST {token_url}
grant_type=refresh_token
&refresh_token={refresh_token}
```

---

## Testing Environment

### Sandbox Servers

| Server | URL | Description |
|--------|-----|-------------|
| SMART Launcher | https://launch.smarthealthit.org | Testing sandbox |
| HAPI FHIR | https://hapi.fhir.org/baseR4 | Public FHIR server |

### Test Credentials

Use the SMART App Launcher with synthetic data for testing.

---

## Support

- [GitHub Repository](https://github.com/yao-care/EuTxGNN)
- [Technical Documentation](/smart/setup/)
- [FHIR API Specification](/smart/fhir-api/)
