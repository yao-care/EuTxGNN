---
layout: default
title: SMART on FHIR
nav_order: 4
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

---

## Quick Start

### For Healthcare Organizations

1. Register EuTxGNN as a SMART app in your EHR
2. Configure OAuth2 credentials
3. Launch from patient chart

### For Developers

1. Review [FHIR API](/fhir/metadata) documentation
2. Implement SMART authorization flow
3. Query MedicationKnowledge and ClinicalUseDefinition resources

---

## Documentation

| Guide | Description |
|-------|-------------|
| [User Guide](/smart/guide/) | How to use the SMART app |
| [Technical Setup](/smart/setup/) | Implementation details |
| [FHIR API](/fhir/metadata) | API specifications |

---

## App Registration

To register EuTxGNN with your EHR:

**Launch URL**: `https://eutxgnn.yao.care/smart/launch.html`

**Redirect URL**: `https://eutxgnn.yao.care/smart/app.html`

**Scopes Required**:
- `patient/Patient.read`
- `patient/MedicationRequest.read`
- `launch`

---

## SMART App Gallery

EuTxGNN is designed to be compatible with the [SMART App Gallery](https://apps.smarthealthit.org/) specifications.

---

## Disclaimer

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>Research Use Only:</strong> The SMART on FHIR application provides research-level predictions that require clinical validation before therapeutic use.
</div>
