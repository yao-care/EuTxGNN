---
layout: default
title: User Guide
parent: 🏥 SMART on FHIR
nav_order: 1
description: "How to use the EuTxGNN SMART on FHIR application"
permalink: /smart/guide/
---

# SMART App User Guide
{: .fs-9 }

Step-by-step guide for using EuTxGNN in your EHR
{: .fs-6 .fw-300 }

---

## Prerequisites

Before using the EuTxGNN SMART app:

1. Your organization must have registered the app
2. You need appropriate EHR access permissions
3. Patient context must be established

---

## Launching the App

### From Patient Chart

1. Open the patient's chart in your EHR
2. Navigate to the "Apps" or "SMART Apps" section
3. Select "EuTxGNN Drug Repurposing"
4. The app will launch with patient context

### Standalone Launch

1. Visit [https://eutxgnn.yao.care/smart/launch.html](https://eutxgnn.yao.care/smart/launch.html)
2. Select your EHR system
3. Authenticate with your credentials
4. Select patient context

---

## Using the App

### Medication Overview

After launch, the app displays:
- Patient's current medications
- DrugBank ID mappings
- Quick links to drug reports

### Viewing Predictions

For each medication:
1. Click on the drug name
2. View predicted new indications
3. Review evidence level (L1-L5)
4. Access supporting literature

### Filtering Results

Use the filters to:
- Show only high-evidence predictions (L1-L2)
- Filter by therapeutic area
- Sort by prediction confidence

---

## Interpreting Results

### Evidence Levels

| Level | Meaning | Clinical Action |
|-------|---------|-----------------|
| L1 | Multiple RCTs | Consider for evaluation |
| L2 | Single RCT | Further review needed |
| L3 | Observational | Research direction |
| L4 | Preclinical | Early-stage hypothesis |
| L5 | AI only | Requires validation |

### Prediction Scores

Higher scores indicate stronger model confidence, but clinical validation is always required.

---

## Troubleshooting

### App Won't Launch
- Verify app registration with IT
- Check EHR permissions
- Clear browser cache

### No Medications Displayed
- Ensure patient has active medications
- Check FHIR scope permissions

### Error Messages
- Contact IT support
- Report issues on [GitHub](https://github.com/yao-care/EuTxGNN/issues)

---

## Support

For technical support, please:
1. Check our [FAQ](/guide/)
2. Open a [GitHub Issue](https://github.com/yao-care/EuTxGNN/issues)
