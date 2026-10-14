---
layout: default
title: Dantrolene
parent: AI Predictions (L5)
nav_order: 168
evidence_level: L5
indication_count: 9
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Dantrolene: From Malignant Hyperthermia to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant, originally authorised in the EU (as Agilus) for treating malignant hyperthermia in adults and children.
The TxGNN model predicts it for **malignant hyperthermia, susceptibility to**, with **0 clinical trials** and **18 publications** (mostly reviews and guidelines) in the data compiled for this report.
This predicted indication is essentially the same as the approved one, so it is not a true repurposing case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of malignant hyperthermia in adults and children of all ages, together with adequate support measures |
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 (based on guidelines and reviews; no Phase 3 RCT in the data) |
| EU Market Status | ✗ Cancelled only |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. From the literature, dantrolene binds the skeletal muscle ryanodine receptor type 1 (RyR1) and blocks calcium release from the sarcoplasmic reticulum. One 2017 study (PMID 28373535) reports that this action requires magnesium ions.

Malignant hyperthermia is mainly caused by RYR1 mutations that lead to uncontrolled calcium release in skeletal muscle when exposed to volatile anaesthetics or succinylcholine. Dantrolene directly counteracts this process. The "susceptibility" disease label is the genetic predisposition behind the approved crisis indication, so the prediction is consistent with existing practice.

Other predicted diseases, such as King-Denborough syndrome, central core myopathy and centronuclear myopathy, are RYR1-related. For these, the plausible benefit is managing malignant hyperthermia risk, not treating the underlying myopathy. Predictions for periodic paralysis conditions are speculative, with no supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists guideline on malignant hyperthermia (2020) |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Consensus guideline | Br J Anaesth | European MH Group consensus on perioperative management of suspected or susceptible patients; notes no interventional trial evidence exists |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative review of epidemiology and management of critically ill MH patients |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | Overview of MH as a pharmacogenetic skeletal muscle disorder |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | MH update; affects calcium release channels, mortality has improved |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanism study | PNAS | Dantrolene requires Mg2+ to arrest MH |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | Dantrolene sodium described as the definitive treatment for MH |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | MH incidence and pharmacogenetics |

Supporting evidence for other predicted diseases (all case-level or indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27918309](https://pubmed.ncbi.nlm.nih.gov/27918309/) | 2017 | Case report | A A Case Rep | Intraoperative MH with RYR1 mutation led to King-Denborough syndrome diagnosis |
| [9539627](https://pubmed.ncbi.nlm.nih.gov/9539627/) | 1998 | Case report | Anesth Analg | Prophylactic dantrolene use in a patient with central core disease |
| [36292611](https://pubmed.ncbi.nlm.nih.gov/36292611/) | 2022 | Genetic study | Genes | Novel RYR1 variant in MH with multi-minicore myopathy |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006009 (cancelled) | Agilus | Not specified | In combination with adequate support measures, Agilus is indicated for the treatment of malignant hyperthermia in adults and children of all ages. |

---

## Safety Considerations

- **Contraindications (from disease-association data, not label text)**: The knowledge graph links dantrolene with liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, lung disease and a rare pulmonary disease.
- **Drug Interactions**: 72 interactions were identified. The main ones are the **Major** interactions with morphine and liposomal morphine. **Moderate** interactions include dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol and promethazine.
- **Other considerations**: Dantrolene can cause muscle weakness, which is a concern for paralytic disorders such as periodic paralysis.

Please also refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication matches the approved, guideline-endorsed use of dantrolene in malignant hyperthermia, supported by reviews and guidelines. However, there are no registered trials in the data, and the only EU authorisation found is cancelled. The other predicted diseases (RYR1-related myopathies) are Research Questions with case-level evidence, and the periodic paralysis predictions should be held.

**To proceed, the following is needed:**
- Verification of current product availability in the EU, since the listed authorisation is cancelled
- Full SmPC warnings and contraindications
- Detailed mechanism of action data
- Prospective or registry data for RYR1-related myopathies before considering them for repurposing
- Safety review for patients with liver, muscle or pulmonary disease, and for opioid co-administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

