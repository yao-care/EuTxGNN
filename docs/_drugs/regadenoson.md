---
layout: default
title: Regadenoson
parent: AI Predictions (L5)
nav_order: 512
evidence_level: L5
indication_count: 10
---

# Regadenoson
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Regadenoson: From Diagnostic Stress Agent for Myocardial Perfusion Imaging to Anaphylaxis

## One-Sentence Summary

Regadenoson is a selective coronary vasodilator used as a pharmacological stress agent for radionuclide myocardial perfusion imaging (MPI) in adults who cannot exercise adequately.
The TxGNN model predicts it may be effective for **anaphylaxis**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on model output alone, and the drug's vasodilating and blood-pressure-lowering profile raises a safety concern in this setting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharmacological stress agent for radionuclide myocardial perfusion imaging (MPI) in adult patients unable to undergo adequate exercise stress (diagnostic use only) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data indicate that regadenoson is a selective A2A adenosine receptor agonist that also has binding records at the A1, A2B and A3 receptors. Its established effect is coronary vasodilation, which is why it is used as a stress agent in MPI.

A theoretical link to anaphylaxis exists through A2A signalling. In preclinical models this pathway has anti-inflammatory and mast-cell-stabilizing effects, which could plausibly relate to allergic reactions. The same applies, more weakly, to the related predictions of food-dependent exercise-induced anaphylaxis and pseudoallergy.

However, the original indication (a diagnostic imaging aid) has little in common with treating a severe allergic emergency. Regadenoson causes vasodilation and lowering of blood pressure, which could be harmful in anaphylactic shock. The high TxGNN score is therefore a model prediction only and is not supported by any trial or published study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for anaphylaxis.

Literature exists only for other lower-ranked predictions (headache disorder and migraine disorder), and it shows adverse effects rather than benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18513639](https://pubmed.ncbi.nlm.nih.gov/18513639/) | 2008 | Randomized, double-blind, placebo-controlled safety trial | J Nucl Cardiol | Safety of regadenoson in patients with mild and moderate asthma, who are at risk of adenosine-induced bronchoconstriction |
| [40142667](https://pubmed.ncbi.nlm.nih.gov/40142667/) | 2025 | Real-world safety analysis | J Clin Med | Disproportionality analysis of adverse event reports in the FDA Adverse Event Reporting System (FAERS) |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | Hemiplegic migraine episode triggered by regadenoson |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001176 (cancelled) | Rapiscan | Not specified | Diagnostic use only. Selective coronary vasodilator used as a pharmacological stress agent for radionuclide myocardial perfusion imaging (MPI) in adult patients unable to undergo adequate exercise stress. |

---

## Safety Considerations

**Contraindications (from knowledge graph, not label text):** The TxGNN knowledge graph lists contraindication links with the following conditions. These are model-derived and must be confirmed against the SmPC.
- Cardiovascular: atrioventricular block, sick sinus syndrome, hypotensive disorder, hypertension, aortic and mitral valve stenosis, coronary artery disease, carotid stenosis, pericarditis and pericardial effusion, transient ischemic attack, vertebrobasilar insufficiency
- Respiratory: asthma, chronic obstructive pulmonary disease, bronchial disease
- Neurological and autonomic: epilepsy, autonomic nervous system disease, Horner syndrome

**Drug Interactions:** Six moderate-level interactions were identified:
- Caffeine
- Dipyridamole
- Dyphylline
- Theophylline
- Aminophylline
- Oxtriphylline

Methylxanthines (caffeine, theophylline and related drugs) and dipyridamole act on the adenosine pathway and may alter the response to regadenoson.

**Additional signals from the literature:** Headache and a case of hemiplegic migraine have been reported after regadenoson. A randomized safety trial examined its use in mild and moderate asthma.

For label warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The anaphylaxis prediction has no clinical trial or literature support (Evidence Level L5). The drug's vasodilatory and hypotensive effects work against its use in a condition marked by circulatory collapse. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a clear rationale for how A2A agonism could benefit anaphylaxis without causing harmful hypotension
- Preclinical studies (mast cell and animal anaphylaxis models) showing a benefit
- Label warnings and contraindications from the EMA package insert, to allow a formal safety screen
- Assessment of whether a short-acting diagnostic agent is suitable for any therapeutic use, including route and dosing
- Reassessment of the lower-ranked predictions (such as headache and migraine), which currently indicate harm rather than benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

