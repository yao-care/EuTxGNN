---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: From C. difficile Infection Prevention to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab (brand name: Zinplava) is a human monoclonal IgG1 antibody that specifically neutralizes *Clostridioides difficile* Toxin B, approved in the United States and European Union for reducing recurrence of *C. difficile* infection (CDI) in adults — though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Acute Female Pelvic Peritonitis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The mechanistic plausibility for this prediction is assessed as extremely low; the high model score is most likely a knowledge graph topology artifact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reducing recurrence of *Clostridioides difficile* infection (CDI) in adults receiving antibacterial treatment |
| Predicted New Indication | Acute Female Pelvic Peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on published information, Bezlotoxumab is a highly selective human monoclonal antibody (IgG1 subclass) that binds with high affinity to *C. difficile* Toxin B, blocking its attachment to intestinal epithelial cells and thereby interrupting the toxin-mediated mucosal damage responsible for CDI recurrence. Its mechanism is pathogen-specific — it does not target the bacterium itself or broad inflammatory pathways, but solely the Toxin B protein.

Acute female pelvic peritonitis is a polymicrobial infectious condition arising from ascending spread of organisms from the lower genital tract to the pelvic peritoneum. The typical causative organisms include *Neisseria gonorrhoeae*, *Chlamydia trachomatis*, anaerobes, and Gram-negative *Enterobacteriaceae*. While bacterial toxins do contribute to inflammation in various forms of peritonitis, *C. difficile* Toxin B is not part of the established pathophysiology of pelvic peritonitis and plays no known role in this disease.

Given the foregoing, the mechanistic link between Bezlotoxumab and acute female pelvic peritonitis is essentially absent. The high TxGNN score (99.89%) despite negligible biological plausibility strongly suggests a knowledge graph topology artifact — likely driven by shared "abdominal/pelvic infectious disease" node proximity within the training graph — rather than a genuine repurposing signal. This interpretation is consistent across all 10 top-ranked predictions, which span structurally and functionally unrelated pelvic and abdominal conditions (ectopic pregnancy, lymphangioma, vascular anomalies, spinal stenosis) where no mechanistic link to anti-toxin biology exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Regulatory Status

Bezlotoxumab has no approved marketing authorizations in Taiwan (0 licenses; market status: 未上市). For reference, the drug is approved under the brand name **Zinplava** in:

- **United States** (FDA, October 2016): reducing recurrence of *C. difficile* infection in adults on antibacterial therapy
- **European Union** (EMA): same indication

Registration in Taiwan has not been pursued, likely reflecting the limited CDI hospitalization burden relative to other priority indications in the local market.

---

## Safety Considerations

Please refer to the official prescribing information (U.S. Prescribing Information or EMA SmPC for Zinplava) for safety data, as Taiwan-specific labeling is unavailable. Key areas to review include heart failure risk (noted in the U.S. label for patients with pre-existing cardiac disease) and infusion-related reactions, given the IV route of administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical trial evidence, zero supporting literature, and no credible mechanistic pathway connecting Bezlotoxumab's anti–Toxin B activity to acute female pelvic peritonitis. The high TxGNN score across all top-10 predictions — covering anatomically proximate but pathophysiologically unrelated pelvic conditions — is consistent with a graph topology confound rather than a real repurposing opportunity.

**To revisit this prediction, the following would be required:**
- A credible mechanistic hypothesis linking *C. difficile* Toxin B biology to pelvic peritonitis (e.g., evidence of CDI co-infection in documented pelvic peritonitis cases)
- At minimum one preclinical study, case report, or pharmacoepidemiological signal
- Knowledge graph audit to identify and correct pelvic/abdominal infectious disease node proximity artifacts that may be generating spurious high-score predictions across this cluster
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

