---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Bosentan
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist (ETA/ETB) globally approved for pulmonary arterial hypertension (PAH) and prevention of digital ulcers in systemic sclerosis, though it is not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (score 99.80%),
with **1 indirectly relevant clinical trial** and **16 publications** — primarily animal models and mechanistic reviews — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary Arterial Hypertension (globally approved; not registered in Taiwan) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Bosentan is a competitive dual antagonist of both ETA and ETB endothelin receptors, blocking the vasoconstrictor and mitogenic actions of endothelin-1 (ET-1). In its approved indications, bosentan reduces pulmonary vascular resistance in PAH and prevents new digital ulcers in systemic sclerosis by reversing ET-1-mediated vascular dysfunction and fibrosis.

The mechanistic case for rheumatoid arthritis rests on ET-1's role in synovial inflammation. ET-1 levels are significantly elevated in the synovial fluid and plasma of RA patients, where ET-1 acts synergistically with TNF-α to promote synovial fibroblast proliferation, joint angiogenesis, and secretion of pro-inflammatory cytokines (IL-1β, IL-6). Bosentan's dual ETA/ETB blockade may disrupt this cycle by inhibiting ET-1-mediated NF-κB activation and TNF-α signaling within the inflamed joint. The most direct preclinical validation comes from a murine collagen-induced arthritis (CIA) model, which confirmed that bosentan ameliorated experimental arthritis and showed that TNF-α upregulates endothelin system genes in diseased joints (PMID 22249931). Complementary animal studies further identified ET-1 as a downstream mediator of IL-15-induced inflammatory hypernociception (PMID 16766656) and neutrophil accumulation/edema in arthritic joints (PMID 18515326).

However, the gap between these preclinical signals and clinical validation in RA remains wide. The only registered clinical trial using bosentan in an inflammatory arthritis context (NCT06957002) targets giant cell arteritis (GCA) — a large-vessel vasculitis that shares ET-1-driven vascular inflammation with RA but differs substantially in target organ, disease mechanism, and patient population. Direct human evidence in RA synovial tissue is entirely absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Bosentan + standard glucocorticoids vs. glucocorticoids alone in Giant Cell Arteritis; primary endpoint is failure-free survival at 12 months (2025–2029). **Indirect relevance only** — target indication is GCA (large-vessel vasculitis), not RA; both share ET-1-driven vascular inflammation but differ in pathophysiology and organ tropism (grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Animal Model (CIA) | Inflammation Research | **Core preclinical evidence**: Bosentan (dual ETA/ETB antagonist) ameliorates collagen-induced arthritis in mice; TNF-α upregulates endothelin system genes in diseased joints, confirming the ET-1/bosentan axis as a therapeutic target in arthritis |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Animal Model | Journal of Leukocyte Biology | ETA/ETB receptors mediate neutrophil accumulation and joint edema in murine zymosan-induced arthritis; ET-1 levels elevated in RA synovial membrane, supporting ET-1 as a joint inflammation driver |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Animal Model | PNAS | IL-15-induced inflammatory hypernociception requires sequential ET-1 release; dual ET receptor blockade inhibits this signaling cascade — directly relevant to RA pain pathophysiology |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Animal Model | Pain | IL-17-mediated articular hypernociception in antigen-induced arthritis; ET-1 implicated as a downstream mediator, linking RA cytokine biology to the endothelin axis |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | PAH associated with connective tissue diseases including RA; contextualizes bosentan use in the broader rheumatic disease landscape and discusses functional impairment burden |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH as a complication of CTDs including RA; ET-1 elevated in pulmonary vasculature; endothelin receptor antagonism discussed as a treatment class for CTD-associated vascular disease |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in SLE and Sjögren's syndrome; reviews clinical management including endothelin blockade, providing contextual framework for ET-1 targeting in rheumatic diseases |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia Polska | Child with Eisenmenger syndrome on bosentan subsequently diagnosed with juvenile RA and started on naproxen; demonstrates clinical co-existence and tolerability of bosentan alongside RA management |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | Rheumatic manifestations of skin disease; outcome measures and emerging therapies; background context for rheumatic disease evaluation |
| [21165350](https://pubmed.ncbi.nlm.nih.gov/21165350/) | 2010 | Observational Study | Canadian Respiratory Journal | Targeted PAH therapies in CTD patients with concurrent interstitial lung disease; bosentan efficacy in CTD-PH context with implications for RA-associated pulmonary complications |

---

## Safety Considerations

Taiwan TFDA prescribing information for Bosentan is not available in this dataset. Please refer to the EMA SmPC (Tracleer®) for complete safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Bosentan's dual ET receptor blockade has demonstrated proof-of-concept in the murine CIA model (PMID 22249931) and aligns with established ET-1 elevations in RA synovial fluid, building a biologically coherent mechanistic hypothesis. However, with no completed human clinical trial in RA and the only registered trial targeting a different indication (GCA, NCT06957002), the evidence sits firmly at L4 — insufficient to recommend development investment without a dedicated human proof-of-concept study.

It is also worth noting that the rank 3 predicted indication, **limited systemic sclerosis**, carries substantially stronger evidence (L2) and overlaps with bosentan's existing EU approval for SSc-related digital ulcer prevention — making SSc the more actionable near-term repurposing opportunity if Taiwan market entry is being considered.

**To proceed toward an RA indication, the following is needed:**

- **Proof-of-concept Phase 2 trial** in RA patients who are inadequate responders to conventional DMARDs (methotrexate ± biologics), using synovial inflammation biomarkers (e.g., DAS28-CRP, synovial biopsy) as endpoints
- **Biomarker qualification**: Quantify ET-1 and ETA/ETB receptor expression in RA synovial tissue vs. controls to identify likely-responsive patient subgroups and establish pharmacodynamic markers
- **Drug interaction profiling**: Bosentan is a potent CYP3A4/CYP2C9 inducer; formal DDI assessment with common RA co-medications (methotrexate, JAK inhibitors, TNF inhibitors) is essential before any clinical use
- **TFDA SmPC retrieval** (DG001): Download and parse the Tracleer® prescribing information PDF to complete the safety profiling required for Taiwan regulatory pathway assessment
- **MOA data retrieval** (DG002): Query DrugBank API to formally document the mechanism of action and complete the mechanistic gap
- **GCA trial monitoring**: Track NCT06957002 for mechanistic signals (e.g., synovial/vascular ET-1 changes, biomarker readouts) that may support or refute the RA hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

