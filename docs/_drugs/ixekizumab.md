---
layout: default
title: Ixekizumab
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: From Plaque Psoriasis / Ankylosing Spondylitis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab is a high-affinity monoclonal antibody targeting interleukin-17A (IL-17A), approved globally for plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis, though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
with **1 clinical trial** (indirectly related, Grade C) and **no published literature** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis, psoriatic arthritis, ankylosing spondylitis (global approvals; not registered in Taiwan) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, Ixekizumab is a high-affinity IgG4 monoclonal antibody that selectively binds and neutralizes IL-17A — a key pro-inflammatory cytokine central to Th17-mediated autoimmune responses. Its clinical efficacy in plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis has been extensively validated across multiple pivotal Phase 3 trials (SPIRIT-P1/P2, COAST-V/W/X).

Rheumatoid vasculitis (RV) is a severe extra-articular complication of long-standing seropositive rheumatoid arthritis, involving necrotizing inflammation of small- and medium-sized vessels. Because rheumatoid disease and spondyloarthritis share certain IL-17-mediated inflammatory pathways — and Ixekizumab has demonstrated broad anti-inflammatory activity — a theoretical rationale for immune modulation in RV exists.

However, the primary pathomechanism of rheumatoid vasculitis centers on immune complex deposition, complement activation, and neutrophil-mediated vessel wall injury. IL-17A plays a limited and indirect role in this process, making the mechanistic bridge to Ixekizumab considerably weaker than in spondyloarthritis. No direct preclinical or clinical evidence currently supports IL-17A inhibition as a therapeutic strategy for rheumatoid vasculitis. The TxGNN high score likely reflects indirect connectivity via shared rheumatoid arthritis and immune-cell nodes in the knowledge graph, rather than a direct disease-specific mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Assesses immunosuppressant management (holding vs. shorter interruption) in rheumatology patients — including potential Ixekizumab users — undergoing elective total shoulder arthroplasty. Primary outcomes are flare incidence, pain scores (VAS), functional outcomes (PROMIS), and wound complications. Not a vasculitis treatment trial; Ixekizumab is one of many immunosuppressants under evaluation. |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rheumatoid vasculitis pathology is driven primarily by immune complex deposition and complement activation — processes where IL-17A inhibition offers minimal mechanistic benefit. The only available trial (NCT07138898) addresses perioperative drug management, not vasculitis treatment, and no supporting literature exists. Evidence level L4 is insufficient to justify progression.

**To proceed, the following is needed:**

- Retrieval of Ixekizumab MOA data from DrugBank API to confirm or refute IL-17A relevance in vasculitis
- Preclinical data or case series documenting IL-17A upregulation specifically in rheumatoid vasculitis lesions
- Safety profile review from TFDA or EMA SmPC, particularly regarding immunosuppression depth in patients with systemic vasculitis
- Assessment of whether existing PsA/AS safety experience is transferable to the RV patient population (typically older, with more comorbidities)
- Consultation with rheumatology specialists to evaluate whether a mechanistic hypothesis is worth pursuing before initiating evidence search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

