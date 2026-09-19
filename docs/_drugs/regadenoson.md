---
layout: default
title: Regadenoson
parent: AI Predictions (L5)
nav_order: 495
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

# Regadenoson: From Myocardial Perfusion Imaging Stress Agent to Systemic Anaphylaxis — Signal Credibility Questionable

## One-sentence Summary

Regadenoson currently lacks marketing authorization in the European Union (this database contains no data on approved indications and mechanism of action), and is used clinically as a pharmacological stress testing agent for myocardial perfusion imaging (MPI). The TxGNN model ranks **systemic anaphylactic reaction (Anaphylaxis)** as the predicted indication with the highest score (99.85%), but is currently supported by only **1 clinical trial (with no direct relevance)** and **0 publications**. Systematic interpretation suggests this signal most likely reflects the drug's known adverse reaction profile (allergic-like reaction) rather than a therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered (EU: Not marketed; based on clinical trial text context, clinical practice use is as pharmacological stress agent for myocardial perfusion imaging) |
| Predicted New Indication | Anaphylaxis (systemic anaphylactic reaction) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Approvals | 0 |
| Recommended Decision | **Hold** |

---

## Why This Prediction Requires High-Degree Skepticism?

Currently, no mechanism of action (MOA) data for regadenoson is available for query; this represents the first data gap in the present case and is flagged as a Blocking-level gap, meaning the standard safety preliminary assessment workflow cannot proceed until this gap is filled.

More critically, there is a **reversal in mechanism direction relative to the prediction direction**. Regadenoson is a selective adenosine A2A receptor agonist with known pharmacological properties capable of triggering mast cell degranulation and allergic-like (pseudoallergic) reactions—which are repeatedly documented in the literature as **adverse reactions** rather than diseases amenable to treatment with this drug. The same pattern also appears in other candidate indications in the current prediction list: headache disorder (ranked 5th) and migraine disorder (ranked 6th) have source evidence entirely derived from studies on "how to reduce regadenoson-induced headache/migraine adverse effects" in trials and case reports, rather than evidence for treating headache; pseudoallergy (ranked 4th) is similarly flagged as a known adverse effect rather than an indication.

This consistent reverse-causality pattern—the AI learning that "drug X and adverse effect Y are highly co-occurring," yet the ranking algorithm interpreting it as "drug X may treat Y"—strongly suggests that the present prediction results may be **false positives driven by adverse reaction signal pollution** rather than genuine drug repurposing opportunities. Progression to subsequent evaluation stages is not recommended until the MOA and safety data gaps are filled.

---

## Clinical Trial Evidence

| Trial ID | Phase | Status | Enrollment | Key Findings |
|----------|-------|--------|------------|--------------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | NA | Recruiting | 1,000 | Study subject is cardiac stress perfusion MRI imaging protocol to evaluate whether chest pain/dyspnea originates from coronary artery disease; **not studying regadenoson for treatment of anaphylaxis**, relevance rating: C (low relevance) |

No trials currently investigate regadenoson for treatment of systemic anaphylactic reaction.

---

## Literature Evidence

No relevant literature data available.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for safety information.

> Supplementary note: This database contains no critical safety information for regadenoson including warnings, contraindications, and drug-drug interactions; this is a Blocking-level data gap (DG001). No safety-related decisions should be made until this gap is addressed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (anaphylaxis) is mechanistically opposite to the drug's known adverse reaction profile; the evidence is most likely AE signal pollution rather than a genuine therapeutic signal.
- Mechanism of action (MOA) and TFDA/EMA safety labeling data represent Blocking-level gaps; S1 safety preliminary assessment cannot be performed at this time.
- The drug lacks marketing authorization in the European Union, providing no approved indication baseline against which to contextualize mechanistic extension.

**To advance further, the following gaps must be addressed:**
- Query regadenoson complete mechanism of action data via DrugBank API (DG002)
- Obtain full text of warnings and contraindications from TFDA/manufacturer labeling; analyze and populate into safety preliminary assessment (DG001)
- For all predicted indications for the present candidate drug, a manual mechanism-based review comparing "efficacy signal vs. adverse reaction signal" is recommended to exclude candidate items where known side effects may have been misinterpreted as indications, before deciding whether any item merits progression to the S1 stage.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

