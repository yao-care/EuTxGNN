---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Golimumab
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

# Golimumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody (marketed as Simponi), originally used for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis. The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, but the current evidence base is limited to **3 clinical trials** (none golimumab-specific for this indication) and **6 publications**, mostly case reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (per literature evidence, e.g. PMID 28530020, 20065639) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not directly available in this evidence pack (`original_moa: [Data Gap]`). Based on information found within the collected literature, golimumab is a fully human anti-TNF-α IgG1κ monoclonal antibody, approved in the EU for inflammatory arthritis (rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis) (PMID 20065639, 28530020).

Rheumatoid vasculitis is a severe extra-articular manifestation of rheumatoid arthritis, driven by the same TNF-α-mediated inflammatory pathways that golimumab already targets. One case report in this evidence pack (PMID 29075910) explicitly notes that "the introduction of biologic disease-modifying drugs, such as anti-TNFα agents, has attenuated the incidence of rheumatoid vasculitis." This provides a plausible mechanistic rationale for the TxGNN prediction.

However, the supporting evidence is mixed and largely indirect. On one hand, golimumab has been used successfully off-label for other vasculitic/inflammatory conditions, e.g. Behçet's disease-associated uveitis (PMID 23252659). On the other hand, a separate case report describes Takayasu's arteritis (a large-vessel vasculitis) *occurring under* anti-TNF therapy (PMID 22999907), suggesting the drug class's effect on vasculitis is not uniformly protective. No trial or publication in this pack directly evaluates golimumab as a treatment for rheumatoid vasculitis specifically — the connection remains mechanistic and anecdotal rather than proven.

## Clinical Trial Evidence

None of the 3 retrieved trials directly test golimumab for rheumatoid vasculitis; they are broader RA/immune-mediated disease registries returned by the search.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of **tocilizumab** (Actemra, not golimumab) in RA patients with inadequate response to non-biological DMARDs — not golimumab-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large epidemiological study on the risk of developing a second immune-mediated inflammatory disease (IMID) in patients already treated with biologics/immunosuppressants for one IMID |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Assesses rheumatologic flare/complication rates when holding immunosuppressants (general, not golimumab- or vasculitis-specific) perioperatively for shoulder arthroplasty |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatology International | Golimumab-treated RA patient developed pyoderma gangrenosum/pyogenic arthritis presenting as severe sepsis; notes anti-TNF agents have reduced rheumatoid vasculitis incidence |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (36 RCTs) | Int J Mol Sci | Original and biosimilar TNF inhibitors (incl. golimumab) similarly reduce joint destruction in RA vs. methotrexate; not vasculitis-specific |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Review | Semin Arthritis Rheum | Frequency, causes and RA treatment considerations in end-stage renal disease; general RA context |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Update on biologic therapy for autoimmune diseases generally |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel vasculitis) occurring **under** anti-TNF therapy — cautionary signal |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocular Immunol Inflamm | Behçet disease-associated uveitis successfully treated with golimumab, supporting off-label anti-inflammatory/vasculitic use |

## Safety Considerations

Please refer to the SmPC for safety information. (No warnings, contraindications, or drug interaction data were available in this evidence pack — DDI query returned `not_found`.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for golimumab in rheumatoid vasculitis is indirect and case-report level (L4) rather than trial-confirmed, with one case report even describing vasculitis onset under anti-TNF therapy — a mixed safety signal. The drug also has no current EU marketing authorization on file in this dataset, and critical safety data (warnings, contraindications) is entirely missing, which blocks a S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) with warnings and contraindications (blocking gap, per data gap DG001)
- Confirmed mechanism of action data via DrugBank API (data gap DG002)
- Targeted literature/trial search specifically for golimumab (or class-level anti-TNF) efficacy and safety in rheumatoid vasculitis, rather than general RA/IMID studies
- Clarification of the conflicting signal between anti-TNF therapy attenuating vs. potentially triggering vasculitis in select case reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

