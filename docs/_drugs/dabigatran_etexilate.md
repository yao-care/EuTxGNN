---
layout: default
title: Dabigatran Etexilate
parent: AI Predictions (L5)
nav_order: 164
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dabigatran Etexilate: From Venous Thromboembolism Prevention to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate (Pradaxa) is an oral anticoagulant originally used to prevent venous thromboembolism and stroke in atrial fibrillation.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but there are currently **0 clinical trials** and only **1 loosely related publication** (a drug-interaction study of a different compound), so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary prevention of venous thromboembolic events in adults after elective total hip or knee replacement surgery; prevention of stroke and systemic embolism in non-valvular atrial fibrillation; treatment and prevention of recurrence of DVT and PE |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, dabigatran etexilate is a prodrug of dabigatran, a direct thrombin inhibitor. Its efficacy in preventing and treating thromboembolic disease is established.

No direct mechanistic link to sclerosing cholangitis has been established. A role for coagulation or fibrosis-related pathways in cholestatic liver disease is speculative. The one linked paper (PMID 36906733) concerns drug-interaction pharmacology of a different compound (cilofexor, an FXR agonist) and does not address dabigatran efficacy in this disease. The high TxGNN score (0.998) is a computational prediction only and should be treated as a hypothesis, not as evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Pharmacology / drug-interaction study | Clinical Pharmacokinetics | Evaluates cytochrome P450 and transporter-mediated drug-drug interactions of cilofexor, an FXR agonist in development for NASH and primary sclerosing cholangitis. It does not study dabigatran and offers no efficacy evidence for this indication. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000829 (cancelled) | Pradaxa | Not specified | Pradaxa 75 mg Primary prevention of venous thromboembolic events in adult patients who have undergone elective... |
| EMEA/H/C/005639 (cancelled) | Dabigatran Etexilate Accord | Not specified | Prevention of venous thromboembolic events |
| EMEA/H/C/005922 (cancelled) | Dabigatran etexilate Teva (previously Dabigatran etexilate Leon Farma) | Not specified | Dabigatran etexilate Leon Farma 75 mg Primary prevention of venous thromboembolic events (VTE) in adult pat... |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links with blood coagulation disease, anemia, macrocytic anemia, and intracerebral hemorrhage. These are consistent with the bleeding risk expected of an anticoagulant and should be verified against the official product information.

Please refer to the SmPC for the full warnings, contraindications, and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials, no direct literature, and no established mechanistic link. The only supporting element is the model score. Moreover, all EU authorizations for this drug are currently cancelled, and an anticoagulant carries bleeding risk that would need careful justification in patients with cholestatic liver disease.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking thrombin inhibition to sclerosing cholangitis
- Preclinical or observational studies in cholestatic or biliary disease models or patients
- Official warnings and contraindications from the product information, so a safety screening can be completed
- Clarification of the current EU regulatory status, given that all three authorizations are listed as cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

