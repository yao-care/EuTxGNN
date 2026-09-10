---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
---

# Pretomanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pretomanid: From Drug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

> Pretomanid is a nitroimidazooxazine antimycobacterial agent, used as part of the BPaL regimen (bedaquiline + pretomanid + linezolid) for extensively drug-resistant tuberculosis (XDR-TB) and treatment-intolerant/non-responsive multidrug-resistant tuberculosis (MDR-TB).
> The TxGNN model predicts it may be effective for **Candidiasis**,
> but **0 clinical trials** and **0 publications** currently support this direction, and the evidence pack explicitly flags the mechanistic link as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Drug-resistant tuberculosis (XDR-TB / treatment-intolerant or non-responsive MDR-TB), as part of the BPaL regimen — *no formal marketing authorization text available; drug is not marketed in this jurisdiction* |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (marked as a data gap). However, based on mechanistic notes elsewhere in the evidence pack, pretomanid is a nitroimidazooxazine prodrug that requires activation by a mycobacteria-specific F420-coenzyme-dependent deazaflavin nitroreductase system. This activation pathway is unique to mycobacteria and is central to pretomanid's bactericidal activity against both replicating and non-replicating *M. tuberculosis*.

Candida species are fungi and do not possess this mycobacterial F420-dependent activation system. The evidence pack's own rationale for this prediction states explicitly: **"No plausible mechanism: Pretomanid's antimicrobial activity depends on the mycobacteria-specific F420 coenzyme reductase system; Candida (a fungus) does not have this metabolic pathway, and there is no clinical or preclinical evidence supporting this."**

Given the complete absence of clinical trials, literature, or mechanistic rationale, this prediction should be treated as a likely embedding-similarity artifact of the TxGNN model rather than a genuine repurposing signal. For context, two other predictions in this evidence pack (leprosy, rank 2; HIV infectious disease, rank 6) did generate clinical trial and literature hits, but both were also found to lack support on closer review: a direct in vitro study (PMID 17005816) shows *M. leprae* is naturally resistant to pretomanid (PA-824), and the HIV-related trials/literature concern TB treatment *in* HIV-co-infected patients rather than any direct antiretroviral activity of pretomanid. No candidate in this evidence pack currently clears the bar for further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Pretomanid is currently **not marketed** in this jurisdiction (total authorizations: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `key_warnings`, `contraindications`, and drug-drug interaction data are all marked as data gaps in this evidence pack, including a Blocking-severity gap for TFDA label warnings/contraindications.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (candidiasis) has no supporting clinical trials, no literature, and an explicitly stated implausible mechanism (fungal vs. mycobacteria-specific drug activation pathway). This is best interpreted as model noise rather than a genuine repurposing signal.
- The only two predictions in this evidence pack with actual trial/literature support (leprosy, HIV) were independently found to be non-viable — one due to direct evidence of natural drug resistance, the other due to a data-labeling mismatch (TB treatment in HIV+ patients, not anti-HIV activity).

**To proceed, the following is needed:**
- Resolve the Blocking-severity data gap (DG001): TFDA/official label warnings and contraindications must be obtained before any safety pre-screening (S1) can begin for any candidate.
- Resolve the High-severity data gap (DG002): formal MOA data from DrugBank API to support or refute mechanistic plausibility assessments.
- If candidiasis repurposing is to be pursued further, in vitro antifungal susceptibility data for pretomanid against *Candida* spp. would be the minimum evidence needed to justify moving past S0.
- No further action recommended on this candidate set without new primary evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

