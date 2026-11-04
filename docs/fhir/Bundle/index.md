---
layout: default
title: Bundle Resources
nav_exclude: true
search_exclude: true
noindex: true
sitemap: false
description: "EuTxGNN does not publish FHIR Bundle resources; its static FHIR R4 API provides MedicationKnowledge and ClinicalUseDefinition resources."
permalink: /fhir/Bundle/
---

# Bundle Resources
{: .fs-9 }

EuTxGNN does not publish FHIR Bundle resources
{: .fs-6 .fw-300 }

---

## Overview

This site's static FHIR R4 API does not provide any Bundle resources, and there is no bulk Bundle download at this path. The [CapabilityStatement](/fhir/metadata) lists the two resource types that are actually available:

- **MedicationKnowledge** – one resource per drug: `/fhir/MedicationKnowledge/{drug}.json` (example: [metformin.json](/fhir/MedicationKnowledge/metformin.json))
- **ClinicalUseDefinition** – one resource per predicted drug–indication pair: `/fhir/ClinicalUseDefinition/{drug}-{disease}.json` (example: [metformin-classic-stiff-person-syndrome.json](/fhir/ClinicalUseDefinition/metformin-classic-stiff-person-syndrome.json))

To work with several drugs at once, request the individual resources above.

---

## Related Resources

- [FHIR CapabilityStatement](/fhir/metadata)
- [FHIR API Specification](/smart/fhir-api/)

---

*For research reference only; not medical advice. Predicted indications require clinical validation.*
