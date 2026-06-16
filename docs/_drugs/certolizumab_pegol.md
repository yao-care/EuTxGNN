---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Certolizumab Pegol
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Certolizumab pegol (Cimzia) is a PEGylated anti-TNF-α biologic approved globally for rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis, and Crohn's disease, though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** (score 99.78%), with **1 directly relevant case report** documenting successful treatment of RV-related leg ulcers — however, the paradoxical finding that CZP can also *induce* vasculitis introduces significant clinical complexity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally approved for RA, PsA, axial SpA, Crohn's disease, and plaque psoriasis |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured MOA data is not available in this evidence pack. Based on information within the supporting literature, certolizumab pegol is a PEGylated Fab' fragment of a recombinant humanized monoclonal antibody that selectively neutralizes TNF-α. Its key structural distinction from other TNF inhibitors is the absence of an Fc region — it therefore does not activate complement or antibody-dependent cytotoxicity, and it does not actively cross the placenta. It is administered subcutaneously.

Rheumatoid vasculitis (RV) is a serious extra-articular complication of longstanding, seropositive rheumatoid arthritis, characterized by immune complex deposition in vessel walls, fibrinoid necrosis, and ischemia — most commonly manifesting as digital infarcts, leg ulcers, or mononeuritis multiplex. Because TNF-α is a principal driver of systemic RA inflammation, and its sustained elevation is thought to sustain the immune dysregulation underlying RV, anti-TNF therapy carries a mechanistic rationale for RV management.

However, the evidence picture is paradoxical and warrants caution: while CZP could theoretically suppress the TNF-driven inflammation underlying RV, multiple case reports in this pack document CZP itself *inducing* vasculitis — including leukocytoclastic vasculitis (PMID 28405087), hypocomplementemic urticarial vasculitis (PMID 31990069), and medium-vessel vasculitis (PMID 41158918). The distinction between therapeutic benefit in true RV and paradoxical drug-induced vasculitis requires careful clinical and immunological characterization before any repurposing can proceed.

---

## Clinical Trial Evidence

No clinical trials specifically evaluating certolizumab pegol as a treatment for rheumatoid vasculitis were identified. The three retrieved trials are all indirectly related:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab in general RA; no RV-specific subgroup — no direct evidence for RV treatment |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Epidemiological study on risk of incident IMIDs in biologic users; unrelated to RV as a therapeutic target |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in shoulder arthroplasty; not relevant to RV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | CZP successfully treated leg ulcers caused by rheumatoid vasculitis — the only direct therapeutic proof-of-concept for this indication |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Cohort Study | RMD Open | Long-term follow-up of CZP in uveitis due to IMIDs (80 patients); demonstrates sustained anti-inflammatory efficacy across immune-mediated vascular/ocular diseases |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Review | RMD Open | Infection profile comparison of immune-modulatory drugs from SmPC data; provides safety benchmarking for CZP in an already-immunocompromised RV population |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Retrospective Cohort | Clinical Medicine & Research | Single-center series of cutaneous adverse events from biologic agents, including CZP-associated vasculitic skin changes |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case Report / ADR Report | Cureus | Anti-TNF (CZP)-induced medium-vessel vasculitis in seronegative RA — confirms paradoxical vasculitis as a serious and rare adverse drug reaction |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case Report | J Clin Pharmacy & Therapeutics | Hypocomplementemic urticarial vasculitis that developed *during* CZP treatment for RA — illustrates the bidirectional risk |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case Report | Modern Rheumatology Case Reports | Rapidly progressive glomerulonephritis after CZP initiation in a 30-year-old RA patient — possible paradoxical renal vasculitis |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case Report | Proceedings (Baylor Univ. Med. Ctr.) | First reported case of leukocytoclastic vasculitis as a drug reaction to CZP — previously unreported for this specific TNF inhibitor |

---

## Safety Considerations

- **Paradoxical vasculitis**: Multiple case reports document CZP *inducing* vasculitis (leukocytoclastic, medium-vessel, hypocomplementemic urticarial subtypes). This is the central safety concern for this repurposing direction — the drug intended to treat RV may also precipitate or worsen vasculitic pathology.
- **Serious infection risk**: As with all TNF inhibitors, risks include serious bacterial infections, tuberculosis reactivation, and opportunistic fungal infections. Mandatory TB screening (PPD or IGRA) is required before initiation. This is especially critical in RV patients who are already often systemically unwell.
- **Renal safety**: One case of rapidly progressive glomerulonephritis was documented post-CZP (PMID 32687015) — particularly relevant for RV cases involving renal vasculitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single case report supporting CZP's therapeutic benefit in RV (PMID 34786446) is directly counterbalanced by multiple case reports documenting CZP-induced vasculitis as a paradoxical adverse reaction. With no completed Phase 2+ trials targeting RV, and a mechanistic ambiguity that creates both a theoretical benefit and a documented harm pathway, evidence is insufficient to support advancement beyond hypothesis generation.

**To proceed, the following is needed:**
- Prospective case series or an observational registry specifically enrolling RV patients treated with anti-TNF agents, with systematic immunological characterization (ANCA, complement levels, cryoglobulins, immune complex profiling) to distinguish responders from paradoxical reactors
- Mechanistic studies clarifying whether the RV subtype (small-vessel immune complex vs. medium-vessel ischemic) predicts anti-TNF response direction
- TFDA SmPC review to identify local contraindications and warnings applicable to Taiwan (Data Gap DG001 — currently blocking S1 safety evaluation)
- Regulatory pathway assessment for Taiwan market entry, given current 未上市 status and 0 local authorizations
- Formal MOA documentation from DrugBank API (Data Gap DG002) to support mechanistic rationale in future submissions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

