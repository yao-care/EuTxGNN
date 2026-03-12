---
layout: default
title: CQL Syntax Notes
parent: 🏥 SMART on FHIR
nav_order: 9
description: "Clinical Quality Language syntax learning notes"
permalink: /smart/cql-notes/
---

# CQL Syntax Notes
{: .fs-9 }

Learning notes for Clinical Quality Language
{: .fs-6 .fw-300 }

---

## What is CQL?

Clinical Quality Language (CQL) is a domain-specific language for expressing clinical knowledge. It's used in:

- Clinical Decision Support (CDS)
- Electronic Clinical Quality Measures (eCQM)
- FHIR Clinical Reasoning

---

## Basic Syntax

### Library Declaration

```cql
library DrugRepurposingLogic version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

context Patient
```

### Data Retrieval

```cql
// Get all active medications
define "Active Medications":
  [MedicationRequest: status = 'active']

// Get specific drug
define "Metformin Orders":
  [MedicationRequest] M
    where M.medication.coding.code = 'DB00331'
```

---

## Value Sets and Code Systems

### Code System Definition

```cql
codesystem "DrugBank": 'https://go.drugbank.com'
codesystem "SNOMED": 'http://snomed.info/sct'
```

### Value Set Definition

```cql
valueset "Diabetes Medications": 'http://example.org/ValueSet/diabetes-meds'
```

### Code Definition

```cql
code "Metformin": 'DB00331' from "DrugBank"
code "Type 2 Diabetes": '44054006' from "SNOMED"
```

---

## Expressions

### Simple Expressions

```cql
// Boolean
define "Has Diabetes":
  exists([Condition: "Type 2 Diabetes"])

// Numeric
define "Age in Years":
  AgeInYears()

// String
define "Patient Name":
  Patient.name.first().given.first() + ' ' + Patient.name.first().family
```

### Conditional Logic

```cql
define "Diabetes Risk Level":
  case
    when "Has Diabetes" then 'High'
    when "Age in Years" > 45 then 'Medium'
    else 'Low'
  end
```

---

## Queries

### Basic Query

```cql
define "Recent Medications":
  [MedicationRequest] M
    where M.authoredOn during Interval[@2024-01-01, @2024-12-31]
```

### With Relationships

```cql
define "Medications with Conditions":
  [MedicationRequest] M
    with [Condition] C
      such that M.reasonReference.reference = 'Condition/' + C.id
```

### Sorting and Limiting

```cql
define "Last 5 Medications":
  (Last 5 from [MedicationRequest] M
    sort by authoredOn desc)
```

---

## Functions

### Built-in Functions

```cql
// Date functions
define "Days Since Last Medication":
  days between "Last Medication Date" and Today()

// String functions
define "Drug Name Upper":
  Upper("Drug Name")

// List functions
define "Medication Count":
  Count("Active Medications")
```

### Custom Functions

```cql
define function GetEvidenceLevel(score Decimal):
  case
    when score >= 0.9999 then 'L1'
    when score >= 0.999 then 'L2'
    when score >= 0.99 then 'L3'
    when score >= 0.9 then 'L4'
    else 'L5'
  end
```

---

## Drug Repurposing Example

### Complete Library

```cql
library DrugRepurposingCDS version '1.0.0'

using FHIR version '4.0.1'
include FHIRHelpers version '4.0.1'

codesystem "DrugBank": 'https://go.drugbank.com'

context Patient

// Get patient's current medications
define "Current Medications":
  [MedicationRequest: status = 'active']

// Get DrugBank IDs
define "DrugBank IDs":
  "Current Medications" M
    return M.medication.coding.where(system = 'https://go.drugbank.com').code

// Check if any medication has repurposing candidates
define "Has Repurposing Candidates":
  exists("DrugBank IDs")

// Recommendation text
define "Recommendation":
  if "Has Repurposing Candidates"
  then 'Review EuTxGNN for potential repurposing candidates for current medications.'
  else 'No medications available for repurposing analysis.'
```

---

## Testing CQL

### CQL Testing Framework

```cql
// Test case
define "Test Has Metformin":
  exists([MedicationRequest] M
    where M.medication.coding.code = 'DB00331')
```

### Tools

- [CQL Playground](https://cql-runner.dataphoria.org/)
- [Bonnie](https://bonnie.healthit.gov/) - eCQM testing
- [CQL Execution Engine](https://github.com/cqframework/cql-execution)

---

## Integration with EuTxGNN

### Potential Use Cases

1. **CDS Alert**: Alert when patient takes drug with L1/L2 repurposing evidence
2. **Quality Measure**: Track patients who might benefit from repurposed drugs
3. **Research Cohort**: Identify patients for clinical trials

### Example CDS Rule

```cql
define "Show Repurposing Alert":
  "Has Repurposing Candidates" and
  not exists("Recent Repurposing Review")
```

---

## Resources

- [CQL Specification](https://cql.hl7.org/)
- [CQL Author's Guide](https://cql.hl7.org/02-authorsguide.html)
- [FHIR Clinical Reasoning](https://www.hl7.org/fhir/clinicalreasoning-module.html)
- [CQFramework GitHub](https://github.com/cqframework)
