---
layout: default
title: Drug-Disease Interactions
parent: Safety Data
nav_order: 2
description: "Drug-Disease State Interaction (DDSI) database for EuTxGNN"
permalink: /ddsi/
---

# Drug-Disease Interactions (DDSI)
{: .fs-9 }

Drug-disease contraindication and precaution data
{: .fs-6 .fw-300 }

---

## Introduction

Drug-disease interactions occur when a medication may worsen an existing medical condition. This is especially important in drug repurposing, where the target patient population may have different comorbidities than the original indication.

---

## Severity Classification

| Level | Description | Example |
|-------|-------------|---------|
| **Contraindicated** | Should not be used | Beta-blockers in severe asthma |
| **Moderate** | Use with caution | NSAIDs in kidney disease |
| **Minor** | Monitor recommended | Statins in liver disease |

---

## Common Categories

### Cardiovascular Conditions
- Heart failure
- Arrhythmias
- Hypertension

### Renal/Hepatic
- Kidney disease
- Liver impairment

### Neurological
- Seizure disorders
- Parkinson's disease

### Metabolic
- Diabetes
- Thyroid disorders

---

## Usage in Drug Reports

Each drug report includes relevant DDSI warnings in the safety section, helping researchers identify contraindications for the proposed new indication.

---

## Related Pages

- [Drug-Drug Interactions](/ddi/)
- [Drug-Food Interactions](/dfi/)
- [Drug-Herb Interactions](/dhi/)
