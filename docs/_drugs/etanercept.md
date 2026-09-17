---
layout: default
title: Etanercept
parent: Medium Evidence (L3-L4)
nav_order: 238
evidence_level: L4
indication_count: 10
---

# Etanercept
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α receptor fusion protein originally approved for rheumatoid arthritis and related inflammatory joint diseases (juvenile idiopathic arthritis, ankylosing spondylitis, psoriatic arthritis). The TxGNN model's top-ranked prediction is **Rheumatoid Vasculitis**, but the available clinical and literature evidence is **contradictory** — the only directly relevant Phase 2 RCT (WGET, in ANCA-associated vasculitis) was negative, and multiple case reports describe etanercept **inducing** vasculitis rather than treating it. This is a Hold, not a Go.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis, Juvenile Idiopathic Arthritis, Ankylosing Spondylitis, Psoriatic Arthritis (approved indications referenced in the evidence pack; not currently marketed in this jurisdiction) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Market Status | Not marketed (0 licenses on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently a documented data gap (DG002) in this evidence pack. Based on the information available, etanercept is a soluble TNF-α receptor (p75) fusion protein that neutralizes TNF-α, a cytokine central to the inflammatory cascade in rheumatoid arthritis and related autoimmune joint diseases. Since TNF-α is also implicated in vasculitic inflammation of blood vessels, TxGNN's knowledge-graph similarity plausibly links etanercept to "rheumatoid vasculitis" through shared inflammatory pathway and disease-co-occurrence signals with rheumatoid arthritis.

However, the mechanistic story does not hold up under the evidence. The one adequately powered, disease-specific trial identified — the pivotal WGET study (NCT00001901, Phase 2, Wegener's granulomatosis / ANCA-associated vasculitis, n=60) — was **negative**: etanercept failed to improve remission rates and was associated with an *increased* risk of malignancy. Compounding this, ten independent case reports and case series (PMID 12209493, 15853915, 11792895, 15801034, 25544845, and others) document etanercept **inducing** cutaneous, renal, or large-vessel vasculitis in patients being treated for rheumatoid arthritis — a recognized paradoxical anti-TNF adverse effect, not a therapeutic signal.

In short, this looks like a case where TxGNN's link between etanercept and "rheumatoid vasculitis" reflects a **drug-induced adverse-event association** embedded in the knowledge graph rather than a genuine treatment opportunity. The direction of causality in the evidence is inverted relative to the repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 2 | Completed | 60 | Pivotal WGET trial of etanercept in Wegener's granulomatosis (ANCA-associated vasculitis) — **negative**: did not improve sustained remission and was associated with increased malignancy risk |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab (not etanercept) in general RA population; not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large registry study of incident immune-mediated inflammatory disease risk in patients on biologics/immunosuppressants; safety-signal relevant, not efficacy evidence |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; unrelated to vasculitis efficacy |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world RA treatment pathway comparison (etanercept vs. non-biologic); not vasculitis-specific |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biologic DMARD treatment patterns in China; not vasculitis-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological therapy in rheumatoid vasculitis; evidence base for biologics (including anti-TNF) in RV remains limited |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA cohort: quantifies drug-specific risk of lupus-like and **vasculitis-like events** in RA patients treated with TNF inhibitors |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | Reviews rationale and evidence for TNF-α blockade in ANCA-associated vasculitis and glomerulonephritis; effect remains unproven |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | The Journal of Rheumatology | Discusses TNF-α blockade and the **risk of vasculitis** as an adverse effect, not a treatment |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis and Rheumatism | Accelerated nodulosis and **vasculitis following etanercept therapy** for RA (adverse event) |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Report | Scandinavian Journal of Immunology | Cutaneous vasculitis associated with both etanercept and infliximab (adverse event) |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Report | Rheumatology (Oxford) | Etanercept and infliximab associated with cutaneous vasculitis (adverse event) |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | The Journal of Rheumatology | Proliferative lupus nephritis and leukocytoclastic vasculitis during etanercept treatment (adverse event) |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Reports in Medicine | Large vessel vasculitis occurring in an RA patient under anti-TNF therapy (adverse event) |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Case Report | Cureus | Etanercept-associated nephropathy, discussed in context of autoantibody formation and vasculitic complications |

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: the literature evidence above independently documents etanercept-induced vasculitis as a recognized paradoxical adverse effect (PMID 12209493, 15853915, 11792895, 15801034, 25544845) — this should be treated as a safety signal for the proposed indication, separate from the formal safety fields in this evidence pack, which are currently data-gapped (TFDA label/warnings, DG001).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only disease-specific RCT (WGET, ANCA-associated vasculitis) was negative and increased malignancy risk, and ten independent case reports show etanercept can *induce* vasculitis rather than treat it. The TxGNN signal for "Rheumatoid Vasculitis" likely reflects a drug-induced adverse-event association in the knowledge graph rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, currently Blocking) — required before any safety assessment
- Detailed mechanism of action data (DG002) to properly evaluate mechanistic plausibility
- If pursued at all, a mechanistic re-evaluation distinguishing anti-TNF-*induced* vasculitis from primary rheumatoid vasculitis pathophysiology, ideally via an independent expert vasculitis panel

**Editorial note:** within this same evidence pack, two *other* TxGNN-predicted indications for etanercept show materially stronger and more coherent evidence — **inflammatory spondylopathy** (rank 3, L1, multiple completed Phase 3 RCTs) and **polyarticular juvenile rheumatoid arthritis** (rank 5, L1, pivotal RCT PMID 10717011) — both of which align with etanercept's already-established mechanism and approved-indication family. These may warrant separate evaluation reports rather than further investment in the rheumatoid vasculitis signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

