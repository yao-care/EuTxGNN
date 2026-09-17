---
layout: default
title: Entecavir
parent: Medium Evidence (L3-L4)
nav_order: 222
evidence_level: L4
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a guanosine nucleoside analogue approved for chronic hepatitis B virus (HBV) infection, where it directly inhibits HBV reverse transcriptase. The TxGNN model's top-ranked prediction is **chronic hepatitis C virus infection (HCV)**, but this evidence pack's own mechanistic and trial review flags the prediction as **biologically implausible** — HCV uses an entirely different (NS5B RNA-dependent RNA polymerase) replication machinery, and none of the 40 retrieved clinical trials or 20 publications provide direct support for anti-HCV activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection *(not present in `taiwan_regulatory.licenses` — this evidence pack shows 0 licenses/Not marketed; inferred from the pack's own rank-2 entry, which is explicitly described as "the approved drug mechanism, not a speculative link," supported by Phase 3 trial NCT01046799)* |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data for entecavir is not available in this evidence pack (`original_moa: [Data Gap]`). However, the pack's own repurposing rationale for this candidate does contain mechanistic detail, and it argues **against** plausibility rather than for it: entecavir is a deoxyguanosine nucleoside analogue that, after intracellular phosphorylation, competitively inhibits HBV polymerase/reverse transcriptase at three steps (priming, negative-strand reverse transcription, and positive-strand DNA synthesis). This is its approved, non-speculative mechanism against HBV.

HCV, by contrast, is a *Flaviviridae* RNA virus whose replication depends on the NS5B RNA-dependent RNA polymerase — a structurally and functionally distinct enzyme family from the HBV reverse transcriptase that entecavir targets. The evidence pack explicitly states: *"HCV 為黃病毒科 RNA 病毒...與 entecavir 抑制的 HBV 逆轉錄酶完全不同機轉家族。無合理生物學基礎支持 entecavir 對 HCV 有抗病毒活性"* (no reasonable biological basis supports antiviral activity against HCV).

Consistent with this, none of the 40 clinical trials returned for the HCV query are entecavir-in-HCV efficacy studies — the graded ones (NCT00371150, NCT00096785) were confirmed as HBV studies mismatched by keyword overlap ("hepatitis," "antiviral," "viral load"), and the remainder are HBV trials that merely mention HCV in background text (e.g., as a historical comparator for combination-therapy rationale). The high TxGNN score most likely reflects embedding-space proximity between "chronic viral hepatitis" disease concepts rather than a validated pharmacological link.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | **Mismatch** — actual subject is entecavir antiviral effect in Black/Hispanic patients with chronic HBV, not HCV |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | **Mismatch** — entecavir vs. adefovir in nucleoside-naive chronic HBV patients, not HCV |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Unknown | 420 | Entecavir for chronic hepatitis B in HCC patients post-RFA; HCV mentioned only as background rationale for antiviral therapy reducing tumor recurrence |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Phase 4 | Unknown | 294 | Pegasys + entecavir vs. entecavir alone for HBeAg-positive chronic HBV; HCV/HIV combination-therapy experience cited only as conceptual background |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Arabinoxylan rice bran (not entecavir) for HCC and hepatitis B/C infection — different investigational drug |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Studies HBV reactivation risk during direct-acting anti-HCV therapy in HBV/HCV coinfected patients — evaluates HBV-side risk, not entecavir efficacy against HCV |
| [NCT02532413](https://clinicaltrials.gov/study/NCT02532413) | Phase 4 | Unknown | 180 | Entecavir + Poly IC vs. entecavir monotherapy for chronic hepatitis B (not HCV) |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Nucleoside analogue combinations for chronic hepatitis B (not HCV) |

No trial in this evidence pack directly tests entecavir's efficacy against HCV.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics and Research in Hepatology and Gastroenterology | Discusses HBV/HCV coinfection as a therapeutic challenge; does not report entecavir activity against HCV |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | — | Journal of Gastroenterology and Hepatology | HBV reactivation risk during direct-acting antiviral (DAA) therapy for HCV in coinfected patients — HBV-side safety signal, not HCV efficacy |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | — | Journal of Viral Hepatitis | Low incidence of HBV reactivation during DAA therapy for HCV — again an HBV safety observation |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics and Research in Hepatology and Gastroenterology | HBV/HCV dual infection is associated with more severe liver injury; therapeutic challenge overview |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | — | Expert Opinion on Pharmacotherapy | Advances in treatment of HBV/HCV coinfection — reviews combination management strategy, not entecavir monotherapy for HCV |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | — | Wiener Medizinische Wochenschrift | Current/future therapy overview for chronic hepatitis B and C — general review, no entecavir-HCV efficacy data |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | — | Minerva Gastroenterologica e Dietologica | Reviews antiviral medications for HBV (including entecavir) and HCV separately and their renal effects — not combined efficacy |

None of the retrieved literature reports entecavir as an anti-HCV therapeutic agent; all HCV-related mentions concern coinfection management or HBV reactivation during HCV-directed DAA therapy.

---

## EU Market Information

This drug is currently **not marketed** under this evidence pack's regulatory dataset (`market_status: Not marketed`, 0 authorizations on record).

---

## Safety Considerations

Please refer to the SmPC for safety information. *(This evidence pack recorded no key warnings, contraindications, or drug-drug interaction data — DDI query status: not found, 0 interactions.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (chronic HCV, score 99.98%) is contradicted by the evidence pack's own mechanistic analysis: HCV's NS5B RNA-dependent RNA polymerase is unrelated to the HBV reverse transcriptase that entecavir inhibits, and none of the 40 clinical trials or 20 publications retrieved provide direct efficacy evidence for entecavir against HCV.
- Evidence level is L4 (mechanism/preclinical-grade at best) with a system-assigned decision stage of S0.
- Note: this evidence pack's rank-2 candidate (hepatitis B virus infection, L1, "Proceed with Guardrails") recovers entecavir's already-known, approved indication with strong Phase 3/Phase 4 trial support — this reflects a validated use rather than a novel repurposing opportunity, and should not be conflated with the rank-1 HCV signal being evaluated here.

**To proceed, the following is needed:**
- In vitro/in vivo evidence of direct anti-HCV activity for entecavir (none currently exists in this pack)
- Regulatory/marketing data (TFDA label, warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank-sourced mechanism-of-action record (currently a High-severity data gap, DG002)
- If pursuing further, reclassify this candidate as low priority relative to the HBV-confirming signal, or investigate whether the TxGNN score reflects embedding proximity rather than a genuine pharmacological hypothesis before committing further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

