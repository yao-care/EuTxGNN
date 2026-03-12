---
layout: default
title: ClinicalTrials.gov API v2 Notes
parent: 🏥 SMART on FHIR
nav_order: 8
description: "Technical notes on ClinicalTrials.gov API v2 integration"
permalink: /smart/clinicaltrials-api/
---

# ClinicalTrials.gov API v2 Notes
{: .fs-9 }

Technical documentation for clinical trials data integration
{: .fs-6 .fw-300 }

---

## Overview

ClinicalTrials.gov provides a comprehensive database of clinical studies. The API v2 offers improved functionality over v1 with better filtering and response formats.

---

## API Endpoints

### Base URL

```
https://clinicaltrials.gov/api/v2
```

### Studies Search

```http
GET /studies?query.term={drug}+{disease}&filter.overallStatus=RECRUITING
```

### Single Study

```http
GET /studies/{nctId}
```

---

## Query Parameters

### Search Terms

| Parameter | Description | Example |
|-----------|-------------|---------|
| `query.term` | Free text search | `metformin diabetes` |
| `query.cond` | Condition/disease | `type 2 diabetes` |
| `query.intr` | Intervention/drug | `metformin` |

### Filters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `filter.overallStatus` | RECRUITING, COMPLETED, etc. | Study status |
| `filter.phase` | PHASE1, PHASE2, PHASE3, PHASE4 | Trial phase |
| `filter.studyType` | INTERVENTIONAL, OBSERVATIONAL | Study type |

### Pagination

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pageSize` | 10 | Results per page (max 1000) |
| `pageToken` | - | Continuation token |

---

## Response Format

### JSON Structure

```json
{
  "studies": [
    {
      "protocolSection": {
        "identificationModule": {
          "nctId": "NCT01234567",
          "briefTitle": "Study Title"
        },
        "statusModule": {
          "overallStatus": "RECRUITING"
        },
        "designModule": {
          "phases": ["PHASE3"]
        },
        "armsInterventionsModule": {
          "interventions": [...]
        }
      }
    }
  ],
  "nextPageToken": "..."
}
```

---

## EuTxGNN Integration

### Drug-Disease Query

```python
def search_trials(drug: str, disease: str) -> list:
    url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "query.term": f"{drug} {disease}",
        "filter.overallStatus": "RECRUITING,COMPLETED",
        "pageSize": 100
    }
    response = requests.get(url, params=params)
    return response.json()["studies"]
```

### Evidence Level Mapping

| Trial Phase | Evidence Level |
|-------------|----------------|
| Phase 3 (multiple) | L1 |
| Phase 3 (single) | L2 |
| Phase 2 | L2-L3 |
| Phase 1 | L3-L4 |
| Observational | L3 |

---

## Rate Limiting

| Tier | Requests/sec | Notes |
|------|--------------|-------|
| Default | 3 | No API key needed |
| Registered | 10 | With API key |

---

## Example Queries

### Find Metformin Repurposing Trials

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.intr=metformin&filter.overallStatus=RECRUITING&pageSize=20"
```

### Find Cancer Drug Trials

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.cond=cancer&query.intr=ibuprofen&filter.phase=PHASE2,PHASE3"
```

---

## Data Fields Used

### For Evidence Collection

| Field | Path | Use |
|-------|------|-----|
| NCT ID | `identificationModule.nctId` | Unique identifier |
| Title | `identificationModule.briefTitle` | Display |
| Phase | `designModule.phases` | Evidence level |
| Status | `statusModule.overallStatus` | Filtering |
| Enrollment | `designModule.enrollmentInfo.count` | Sample size |

---

## Best Practices

1. **Combine Terms**: Use both drug and disease for specific results
2. **Filter Status**: Focus on COMPLETED for evidence, RECRUITING for ongoing
3. **Cache Results**: API responses are relatively static
4. **Handle Pagination**: Use pageToken for complete results

---

## Resources

- [ClinicalTrials.gov API Documentation](https://clinicaltrials.gov/data-api/api)
- [API v2 Migration Guide](https://clinicaltrials.gov/data-api/about-api/api-migration)
- [Study Data Structure](https://clinicaltrials.gov/data-api/about-api/study-data-structure)
