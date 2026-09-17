---
layout: default
title: Infliximab
parent: High Evidence (L1-L2)
nav_order: 310
evidence_level: L1
indication_count: 10
---

# Infliximab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Infliximab: From TNF-α-Driven Autoimmune Disease to Expanded Immune-Mediated Indications

## Summary

Infliximab (DB00065) is a chimeric anti-TNF-α monoclonal antibody long used across the autoimmune/inflammatory disease spectrum (rheumatoid arthritis, Crohn's disease, ulcerative colitis, psoriatic arthritis, psoriasis, ankylosing spondylitis), though its formal original-indication and MOA text are missing from this evidence pack (**[Data Gap]**, DG001/DG002). This is a **multi-candidate** TxGNN run against 10 predicted indications; evidence quality varies enormously — from **L1** (Phase 3 RCT-backed) extensions of well-established anti-TNF biology (inflammatory spondylopathy, polyarticular juvenile RA) down to **L5** model-only hits for rare skeletal/ocular dysplasia syndromes that even the model's own rationale flags as mechanistically implausible. This report focuses evaluation effort on the 6 indications with actual trial/literature support and flags the 4 unsupported ones for immediate **Hold**.

## Quick Overview (Highest-Evidence Candidate)

| Item | Content |
|------|------|
| Original Indication | Not available in this pack (**[Data Gap]**) — publicly known anti-TNF indications: RA, Crohn's disease, UC, PsA, psoriasis, ankylosing spondylitis |
| Predicted New Indication (top actionable) | Inflammatory spondylopathy |
| TxGNN Prediction Score | 80.92% (rank 130,860) |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (Not currently marketed per this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## All Predicted Indications — Ranked Overview

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-----------|-----------------|-----------------|-----------------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 90.22% | L5 | S0 | **Hold** — no mechanistic link, model artifact |
| 2 | Brachydactyly-syndactyly syndrome | 89.88% | L5 | S0 | **Hold** — model artifact |
| 3 | Rheumatoid vasculitis | 85.32% | L3 | S1 | Research Question — conflicting signal (treats vs. induces) |
| 4 | Hypermobility of coccyx | 82.49% | L5 | S0 | **Hold** — model artifact |
| 5 | Anus disease (perianal Crohn's) | 81.21% | L2 | S3 | **Proceed with Guardrails** |
| 6 | Kummell disease | 81.15% | L5 | S0 | **Hold** — model artifact |
| 7 | Inflammatory spondylopathy | 80.92% | L1 | S3 | **Proceed with Guardrails** |
| 8 | Polyarticular juvenile rheumatoid arthritis | 80.14% | L1 | S3 | **Proceed with Guardrails** |
| 9 | Bronchitis | 77.87% | L4 | S0 | **Hold** — evidence shows adverse pulmonary events, not efficacy |
| 10 | Crohn disease of the esophagus | 77.58% | L3 | S2 | Research Question |

Ranks 1, 2, 4, 6 are rare structural/developmental or degenerative-bone conditions with **zero** clinical trial or literature hits and mechanism rationales that explicitly state "no reasonable connection to TNF-α" — these are excluded from further evaluation below.

## Why Are These Predictions Reasonable?

Detailed mechanism-of-action data for infliximab is currently unavailable in this pack (**[Data Gap]**, DG002). Based on known public information, infliximab is a chimeric IgG1 monoclonal antibody that neutralizes soluble and membrane-bound TNF-α, a cytokine central to synovial, enteric, entheseal, and vascular inflammation. Its established efficacy in RA, Crohn's disease, and ankylosing spondylitis-type diseases stems from interrupting this pathway.

The credible candidates in this pack are essentially **mechanistic line-extensions of already-approved anti-TNF biology**: inflammatory spondylopathy and polyarticular juvenile RA share the same TNF-α-driven synovitis/enthesitis pathway as adult RA and AS; anus disease (perianal fistulizing Crohn's) and esophageal Crohn's disease are anatomic sub-phenotypes of Crohn's disease itself. Rheumatoid vasculitis is mechanistically plausible (TNF-α contributes to vasculitic endothelial injury) but the literature is genuinely bidirectional — several case reports describe infliximab **inducing** vasculitis via anti-drug antibody/immune-complex mechanisms, which is an unusual and important caveat.

## Clinical Trial & Literature Evidence by Indication

### 7. Inflammatory Spondylopathy (L1, Proceed with Guardrails)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00051623](https://clinicaltrials.gov/study/NCT00051623) | Phase 3 | Completed | 70 | Multicenter double-blind RCT of infliximab in psoriatic/spondyloarthritic disease |
| [NCT00439283](https://clinicaltrials.gov/study/NCT00439283) | Phase 3 | Completed | 240 | Continuous vs. on-demand infliximab maintenance in ankylosing spondylitis; ± methotrexate |
| [NCT00207701](https://clinicaltrials.gov/study/NCT00207701) | Phase 3 | Completed | 279 | RCT of infliximab vs. placebo in ankylosing spondylitis on background NSAIDs |
| [NCT00367237](https://clinicaltrials.gov/study/NCT00367237) | Phase 3 | Completed | 115 | Infliximab + MTX vs. MTX alone in MTX-naïve active psoriatic arthritis |
| [NCT00591201](https://clinicaltrials.gov/study/NCT00591201) | Phase 2/3 | Completed | 26 | RCT + 52-week open extension of infliximab in juvenile spondyloarthropathies |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27650650](https://pubmed.ncbi.nlm.nih.gov/27650650/) | 2016 | Review | BioDrugs | Infliximab biosimilar CT-P13 review; PLANETAS pivotal trial data in AS |
| [24832835](https://pubmed.ncbi.nlm.nih.gov/24832835/) | 2014 | Meta-analysis | Eur J Health Econ | Systematic review/meta-analysis of infliximab-biosimilar efficacy/safety in AS |
| [17651658](https://pubmed.ncbi.nlm.nih.gov/17651658/) | 2007 | Systematic Review | Health Technol Assess | Comparative effectiveness/cost-effectiveness of anti-TNFs in AS |
| [17644552](https://pubmed.ncbi.nlm.nih.gov/17644552/) | 2008 | Cohort | Ann Rheum Dis | Inflammatory biomarkers correlate with infliximab response and MRI spinal inflammation in AS |
| [12379627](https://pubmed.ncbi.nlm.nih.gov/12379627/) | 2002 | Review | Ann Rheum Dis | Infliximab clinical/radiological efficacy in rheumatic disease |

### 8. Polyarticular Juvenile Rheumatoid Arthritis (L1, Proceed with Guardrails)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00036374](https://clinicaltrials.gov/study/NCT00036374) | Phase 3 | Completed | 123 | Randomized double-blind trial of infliximab + MTX in polyarticular JRA |
| [NCT01015547](https://clinicaltrials.gov/study/NCT01015547) | Phase 3 | Completed | 60 | Anti-TNF+MTX vs. combination DMARDs vs. MTX alone in very early polyarticular JIA |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17763439](https://pubmed.ncbi.nlm.nih.gov/17763439/) | 2007 | RCT | Arthritis Rheum | Placebo-controlled RCT of infliximab + MTX in polyarticular-course JRA |
| [20237125](https://pubmed.ncbi.nlm.nih.gov/20237125/) | 2010 | Cohort | Ann Rheum Dis | Long-term open-label extension confirming sustained efficacy/safety |
| [31612428](https://pubmed.ncbi.nlm.nih.gov/31612428/) | 2020 | Cohort | World J Pediatr | Single-center China study of infliximab outcomes in pJIA |
| [33626206](https://pubmed.ncbi.nlm.nih.gov/33626206/) | 2021 | Cohort | Clin Pharmacol Ther | Response-exposure similarity between pJIA and adult RA supports extrapolation |
| [23337074](https://pubmed.ncbi.nlm.nih.gov/23337074/) | 2013 | Systematic Review | Semin Arthritis Rheum | Systematic review of biologic response modifiers in polyarticular JIA |

### 5. Anus Disease / Perianal Crohn's (L2, Proceed with Guardrails)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02883296](https://clinicaltrials.gov/study/NCT02883296) | N/A | Completed | 15 | Long-term MRI follow-up of anal fistulae in Crohn's on infliximab/adalimumab |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Completed | 211 | Infliximab maintenance ± antimetabolites to sustain steroid-free remission |
| [NCT03801928](https://clinicaltrials.gov/study/NCT03801928) | N/A | Completed | 118 | Real-world observational study of Infliximab (Inflectra) in IBD, US/Canada |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | National real-world registry of Inflectra (infliximab biosimilar) use |
| [NCT02539368](https://clinicaltrials.gov/study/NCT02539368) | N/A | Completed | 2,565 | Post-marketing cohort of CT-P13 (infliximab) in IBD (CONNECT-IBD) |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20623697](https://pubmed.ncbi.nlm.nih.gov/20623697/) | 2011 | Cohort | Inflamm Bowel Dis | Combined infliximab + MTX + sphincter-sparing surgery in severe fistulizing anoperineal CD |
| [12641520](https://pubmed.ncbi.nlm.nih.gov/12641520/) | 2003 | Cohort | Aliment Pharmacol Ther | Mucosal immune regulation and relapse after infliximab in fistulating CD |
| [29126509](https://pubmed.ncbi.nlm.nih.gov/29126509/) | 2017 | Review | Semin Pediatr Surg | Treatment of perianal Crohn's disease |
| [17402327](https://pubmed.ncbi.nlm.nih.gov/17402327/) | 2007 | Review | Isr Med Assoc J | Overview of perianal Crohn's disease management |
| [39882221](https://pubmed.ncbi.nlm.nih.gov/39882221/) | 2025 | Review | J Anus Rectum Colon | Contemporary management of anal fistula with Crohn's disease |

### 3. Rheumatoid Vasculitis (L3, Research Question — mixed signal)

**Clinical Trials**: No trials directly target rheumatoid vasculitis; the 4 identified trials (NCT07138898, NCT05696106, NCT02590562, NCT01579006) are indirect RA/biologic-management studies graded C relevance — **not** included as supporting evidence.

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clin Rheumatol | Systematic review of biological drugs (incl. infliximab) in rheumatoid vasculitis treatment |
| [16078342](https://pubmed.ncbi.nlm.nih.gov/16078342/) | 2005 | Case Report | J Rheumatol | Rheumatoid vasculitis treated successfully with infliximab |
| [40385904](https://pubmed.ncbi.nlm.nih.gov/40385904/) | 2025 | Case Report | Cureus | **Infliximab-induced** leukocytoclastic vasculitis in an RA patient (paradoxical) |
| [35650123](https://pubmed.ncbi.nlm.nih.gov/35650123/) | 2023 | Case Report | Intern Med | IgA vasculitis nephritis after 11 years of infliximab in RA |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA cohort: risk of vasculitis-like events with TNF inhibitors |

⚠️ Evidence is **directionally mixed** — infliximab has case-report support for treating RV but also multiple case reports/cohort data showing it can **induce** vasculitis. This safety signal should be weighted heavily before pursuing this indication.

### 10. Crohn Disease of the Esophagus (L3, Research Question)

**Clinical Trials**: Currently no related clinical trials registered.

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41622053](https://pubmed.ncbi.nlm.nih.gov/41622053/) | 2026 | Cohort | Dig Liver Dis | Nationwide GETECCU cohort of esophageal/gastric/duodenal CD in the biologic era |
| [16954965](https://pubmed.ncbi.nlm.nih.gov/16954965/) | 2006 | Cohort | J Pediatr Gastroenterol Nutr | Infliximab as first-line therapy in severe pediatric Crohn's disease |
| [11907371](https://pubmed.ncbi.nlm.nih.gov/11907371/) | 2002 | Case Report | J Clin Gastroenterol | Infliximab treatment of esophagobronchial fistula in esophageal CD |
| [17298766](https://pubmed.ncbi.nlm.nih.gov/17298766/) | 2007 | Review | Curr Treat Options Gastroenterol | Overview of Crohn's disease of the esophagus |
| [40386539](https://pubmed.ncbi.nlm.nih.gov/40386539/) | 2025 | Case Report | ACG Case Rep J | Anti-TNF-refractory esophageal CD lesions requiring switch to upadacitinib — signals possible treatment failure in this niche |

### 9. Bronchitis (L4, Hold)

Literature is dominated by case reports of infliximab **causing or coinciding with** bronchial/pulmonary complications (tracheobronchitis, organizing pneumonia, granulomatous bronchiolitis) rather than treating bronchitis itself — the directional evidence does not support pursuing this candidate.

## EU/Taiwan Market Information

No authorization records are present in this dataset (`total_licenses: 0`, `market_status: Not marketed`). This does not reflect infliximab's actual global regulatory status (it is a long-marketed biologic, e.g., Remicade/CT-P13 biosimilars), but rather a data gap in this specific regulatory extract — TFDA label/license retrieval (DG001) is required before any safety or dosing claims can be finalized.

## Safety Considerations

Formal safety data (key warnings, contraindications, DDI) is entirely absent from this pack (**[Data Gap]**, DG001). Please refer to the SmPC/label for authoritative safety information.

**Literature-derived signal (not formal label data):** Across the rheumatoid vasculitis literature review, infliximab appears repeatedly both as a **treatment for** and a **trigger of** vasculitis (via anti-drug antibodies/immune complexes) and other paradoxical autoimmune events (drug-induced lupus, cutaneous vasculitis). This pattern should be explicitly flagged in any downstream clinical evaluation, particularly for the rheumatoid vasculitis indication.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for inflammatory spondylopathy, polyarticular JRA, and perianal Crohn's/anus disease) · **Research Question** (rheumatoid vasculitis, esophageal Crohn's) · **Hold** (bronchitis and the 4 mechanistically implausible L5 predictions)

**Rationale:**
- Three candidates (inflammatory spondylopathy, polyarticular JRA, anus disease) are backed by multiple completed Phase 2–4 RCTs and are essentially phenotype extensions of infliximab's already-established anti-TNF mechanism.
- Rheumatoid vasculitis and esophageal Crohn's have plausible mechanisms but evidence limited to case reports/reviews, and rheumatoid vasculitis carries a documented paradoxical-induction risk.
- The four L5 predictions (colobomatous microphthalmia-rhizomelic dysplasia, brachydactyly-syndactyly, coccyx hypermobility, Kummell disease) have zero supporting evidence and explicit mechanistic rationale against them — do not advance.

**To proceed, the following is needed:**
- TFDA label/SmPC retrieval to resolve DG001 (warnings, contraindications) before any S1+ safety evaluation
- DrugBank MOA confirmation to resolve DG002
- Route-compatibility and dosing data (currently "pending" for all candidates)
- For rheumatoid vasculitis: a dedicated benefit-risk review given the induction-vs-treatment paradox before further scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

