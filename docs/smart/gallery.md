---
layout: default
title: SMART App Gallery Reference
parent: 🏥 SMART on FHIR
nav_order: 4
description: "SMART App Gallery compatibility and reference"
permalink: /smart/gallery/
---

# SMART App Gallery Reference
{: .fs-9 }

Compatibility with SMART Health IT ecosystem
{: .fs-6 .fw-300 }

---

## SMART App Gallery

The [SMART App Gallery](https://apps.smarthealthit.org/) is a curated collection of healthcare applications that meet SMART on FHIR standards.

---

## EuTxGNN Compatibility

### Core Requirements

| Requirement | Status | Notes |
|-------------|--------|-------|
| SMART on FHIR Launch | ✅ | EHR and standalone |
| OAuth 2.0 | ✅ | Authorization code flow |
| FHIR R4 | ✅ | Full compliance |
| Patient Context | ✅ | Required for EHR launch |

### Supported Launch Modes

- **EHR Launch**: Integrated with patient chart
- **Standalone Launch**: Direct access with authentication
- **Patient Portal**: Consumer-facing access (planned)

---

## Similar Apps in Gallery

### Drug Information Apps

| App | Focus | FHIR Resources |
|-----|-------|----------------|
| Lexicomp | Drug reference | MedicationKnowledge |
| Micromedex | Drug interactions | ClinicalUseDefinition |
| **EuTxGNN** | Drug repurposing | MedicationKnowledge, ClinicalUseDefinition |

### Clinical Decision Support

| App | Focus | Integration |
|-----|-------|-------------|
| Isabel | Diagnosis support | CDS Hooks |
| DynaMed | Evidence review | SMART Launch |
| **EuTxGNN** | Repurposing evidence | SMART Launch, FHIR API |

---

## Submission Guidelines

To submit an app to the SMART App Gallery:

1. **Complete Testing**: Use SMART App Launcher
2. **Documentation**: Provide user and technical guides
3. **Security Review**: Complete security questionnaire
4. **Submit**: Apply via [SMART Health IT](https://smarthealthit.org/)

### EuTxGNN Submission Status

| Step | Status |
|------|--------|
| Technical Implementation | ✅ Complete |
| Documentation | ✅ Complete |
| Security Review | 🔄 In Progress |
| Gallery Submission | ⏳ Pending |

---

## Best Practices from Gallery Apps

### User Experience

1. **Fast Load Time**: < 3 seconds initial load
2. **Responsive Design**: Works on tablets and desktops
3. **Clear Actions**: Obvious next steps for users

### Clinical Workflow

1. **Minimal Clicks**: Essential information upfront
2. **Context Awareness**: Use patient data appropriately
3. **Evidence Display**: Show source of recommendations

### Security

1. **Minimal Scopes**: Only request needed permissions
2. **Token Security**: Never expose tokens
3. **Audit Logging**: Log all data access

---

## Resources

- [SMART App Gallery](https://apps.smarthealthit.org/)
- [SMART on FHIR Documentation](https://docs.smarthealthit.org/)
- [HL7 SMART App Launch IG](https://hl7.org/fhir/smart-app-launch/)
