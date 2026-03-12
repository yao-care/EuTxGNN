---
layout: default
title: 🏥 SMART on FHIR
nav_order: 2
has_children: true
description: "SMART on FHIR integration for EuTxGNN drug repurposing"
permalink: /smart/
---

# SMART on FHIR Integration
{: .fs-9 }

Integrate drug repurposing predictions into your EHR system
{: .fs-6 .fw-300 }

---

## Overview

EuTxGNN provides a SMART on FHIR application that allows healthcare institutions to query drug repurposing candidates directly from their Electronic Health Record (EHR) systems.

---

## Features

- **EHR Launch**: Launch from patient context in your EHR
- **Medication Query**: Automatic lookup of patient's current medications
- **Repurposing Candidates**: Display relevant predictions for each drug
- **Evidence Links**: Direct links to supporting evidence
- **FHIR R4 Compliance**: Full compliance with HL7 FHIR R4 standard

---

## Quick Start

### For Healthcare Organizations

1. Register EuTxGNN as a SMART app in your EHR
2. Configure OAuth2 credentials
3. Launch from patient chart

### For Developers

1. Review [FHIR API Specification](/smart/fhir-api/)
2. Implement SMART authorization flow
3. Query MedicationKnowledge and ClinicalUseDefinition resources

---

## App Registration

To register EuTxGNN with your EHR:

| Field | Value |
|-------|-------|
| **Launch URL** | `https://eutxgnn.yao.care/smart/launch.html` |
| **Redirect URL** | `https://eutxgnn.yao.care/smart/app.html` |
| **App Type** | Public client |

**Scopes Required**:
- `launch`
- `patient/Patient.read`
- `patient/MedicationRequest.read`

**Optional Scopes**:
- `patient/Condition.read`
- `patient/AllergyIntolerance.read`

---

## Documentation

| Guide | Description |
|-------|-------------|
| [User Guide](/smart/guide/) | How to use the SMART app |
| [Technical Documentation](/smart/setup/) | Implementation details |
| [Integration Resources](/smart/integration/) | Third-party integrations |
| [FHIR API Specification](/smart/fhir-api/) | API specifications |

---

## SMART App Gallery

EuTxGNN is designed to be compatible with the [SMART App Gallery](https://apps.smarthealthit.org/) specifications.

---

## Disclaimer

<div class="disclaimer">
<strong>Research Use Only:</strong> The SMART on FHIR application provides research-level predictions that require clinical validation before therapeutic use.
</div>
