---
layout: default
title: Nusinersen
parent: Medium Evidence (L3-L4)
nav_order: 425
evidence_level: L4
indication_count: 10
---

# Nusinersen
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

Using no additional skill — this is a direct report-writing task per the given template; proceeding directly.

# Nusinersen: From Spinal Muscular Atrophy to Skin Atrophy

## One-Sentence Summary

> Nusinersen is an antisense oligonucleotide administered intrathecally to restore SMN protein production in Spinal Muscular Atrophy (SMA). The TxGNN model flags a possible link to **Skin Atrophy**, but the **3 clinical trials** and **6 publications** returned as "evidence" are not actually studies of nusinersen for skin atrophy — they concern SMA lumbar-puncture technique and incidental injection-site skin necrosis, meaning this candidate is currently unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) — per embedded trial descriptions ("first treatment approved by FDA and EMA for all SMA subtypes"); not present in this market's regulatory data |
| Predicted New Indication | Skin atrophy |
| TxGNN Prediction Score | 50% (raw score 0.5; global rank 1,181,204 — very low priority among all predictions) |
| Evidence Level | L4 |
| Market Status | ✗ Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for nusinersen is not available in the structured `original_moa` field (Data Gap). However, the evidence pack's own analysis identifies nusinersen as an antisense oligonucleotide that targets *SMN2* pre-mRNA splicing, given intrathecally to increase functional SMN protein for the treatment of SMA — a neuromuscular, not dermatologic, mechanism.

There is no established or plausible mechanistic link between *SMN2* splicing modulation and skin atrophy. Skin atrophy is typically driven by dermal collagen/elastin loss (e.g., corticosteroid use, aging, connective tissue disease) — pathways unrelated to motor neuron RNA splicing.

The apparent "evidence" behind this prediction is a keyword-co-occurrence artifact: retrieved trials and literature describe SMA patients receiving nusinersen via lumbar puncture (some with scoliosis or spinal instrumentation), and one case report describes resolution of localized injection-site skin necrosis — not therapeutic use of nusinersen for a skin-atrophy indication. The evidence pack's own relevance grading (Grade C) and rationale text explicitly flag this as a likely false-positive pairing rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04674618](https://clinicaltrials.gov/study/NCT04674618) | N/A | Completed | 58 | Compares ultrasound-assisted vs. landmark-based intrathecal nusinersen administration in adult SMA patients; addresses injection technique, not skin atrophy (relevance: Grade C) |
| [NCT05644899](https://clinicaltrials.gov/study/NCT05644899) | N/A | Completed | 51 | Retrospective analysis of >500 intrathecal nusinersen administrations in SMA adults with scoliosis; procedural study, not a skin-atrophy trial (relevance: Grade C) |
| [NCT06555419](https://clinicaltrials.gov/study/NCT06555419) | Phase 1 | Recruiting | 58 | Pharmacokinetic study of nusinersen delivered via the ThecaFlex DRx™ implantable system vs. lumbar puncture in SMA patients; not related to skin atrophy (relevance: Grade C) |

**Note:** None of the above trials evaluate nusinersen as a treatment for skin atrophy; all concern intrathecal delivery technique in SMA.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40241365](https://pubmed.ncbi.nlm.nih.gov/40241365/) | 2025 | Case series | Zhongguo Dang Dai Er Ke Za Zhi | Nusinersen + risdiplam combination therapy in 10 SMA patients; efficacy/adverse reactions, not skin atrophy |
| [39010073](https://pubmed.ncbi.nlm.nih.gov/39010073/) | 2024 | Technique report | Orphanet J Rare Dis | Novel interlaminar approach for intrathecal nusinersen injection in SMA patients with scoliosis |
| [30811610](https://pubmed.ncbi.nlm.nih.gov/30811610/) | 2019 | Case report | Muscle & Nerve | Resolution of localized skin necrosis at injection site in an infant treated with nusinersen — an adverse event report, not a treatment-efficacy finding for skin atrophy |
| [32515646](https://pubmed.ncbi.nlm.nih.gov/32515646/) | 2020 | Case report | J Child Neurol | SMA Type 0 patient treated with nusinersen and onasemnogene abeparvovec; motor outcome case report |
| [37155209](https://pubmed.ncbi.nlm.nih.gov/37155209/) | 2023 | Case series/technique | Minerva Pediatrics | Surgical technique enabling intrathecal nusinersen injection after spinal fusion in SMA patients |
| [39344612](https://pubmed.ncbi.nlm.nih.gov/39344612/) | 2024 | Case report | Zhonghua Yi Xue Yi Chuan Xue Za Zhi | Genetic/functional analysis of SMN1 variants in two SMA children |

**Note:** All retrieved literature concerns SMA management or intrathecal-injection technique/complications; none evaluates nusinersen as a treatment for skin atrophy.

---

## Market Information

No marketing authorizations are on file for this market — nusinersen's status here is **"Not marketed" (Not marketed)**, with 0 recorded licenses. No approved indication text is available from this dataset.

---

## Safety Considerations

Please refer to the SmPC for safety information (product labeling, warnings, and drug-interaction data were not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (0.5) corresponds to an extremely low global rank (~1.18 million), and every supporting clinical trial and publication is unrelated to skin atrophy — they concern SMA injection technique or incidental injection-site skin necrosis. There is no mechanistic or clinical rationale connecting *SMN2* splicing modulation to skin atrophy; this candidate is best characterized as a keyword-co-occurrence false positive rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Independent, disease-specific mechanistic rationale linking nusinersen to a dermatologic atrophic process (none currently exists)
- Nusinersen product label / MOA data (currently a Blocking data gap per DG001/DG002) before any safety evaluation can begin
- Any genuine preclinical or clinical study directly testing nusinersen in skin atrophy — none currently exists in this evidence pack
- Given the absence of supporting rationale, deprioritize this candidate in favor of other predicted indications with stronger mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

