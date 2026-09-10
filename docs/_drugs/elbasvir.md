---
layout: default
title: Elbasvir
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Elbasvir is an HCV NS5A inhibitor, marketed in combination with grazoprevir (Zepatier®) for chronic hepatitis C genotypes 1, 4, and 6.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection**, with a **99.71% prediction score**,
but the **13 clinical trials** and **18 publications** retrieved are all existing HCV studies — none evaluate Elbasvir against HBV, and the evidence pack's own mechanistic review concludes there is **no direct mechanistic support** for this repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C (genotype 1, 4, 6) — as Elbasvir/Grazoprevir combination (Zepatier®); inferred from evidence-pack literature, not recorded in the regulatory dataset |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (per evidence-pack scoring; see caveat below) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced MOA data (e.g., from a DrugBank API query) is currently a flagged data gap (DG002). Based on information recoverable from the evidence pack's own literature and trial descriptions, Elbasvir is an **HCV NS5A protein inhibitor**, acting on the HCV replication complex; it is marketed only in fixed-dose combination with grazoprevir (Zepatier®) for chronic HCV genotype 1/4/6 infection.

Hepatitis B virus, however, belongs to the *Hepadnaviridae* family and replicates via reverse transcription of a covalently closed circular DNA (cccDNA) template — a mechanism entirely distinct from HCV's positive-strand RNA replication complex, and HBV has no NS5A-homologous target. The evidence pack's own repurposing rationale states this explicitly: *"HBV has no NS5A-homologous target; the replication mechanisms are entirely different. No direct mechanistic support exists."*

Consistent with this, all 13 clinical trials retrieved for this pairing are existing Elbasvir/Grazoprevir (or related MK-5172/MK-8742) HCV studies — none tested Elbasvir in HBV patients or HBV models. This is best read as a **TxGNN embedding-space association** (both are viral hepatitis targets in the knowledge graph) rather than a mechanism- or evidence-backed repurposing signal.

---

## Clinical Trial Evidence

*Note: relevance grading in the evidence pack marks these trials "C" (low relevance) — they are HCV studies retrieved under the HBV query and do not test Elbasvir against HBV. Included here for completeness/audit trail.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Phase 2 | Completed | 15 | Pembrolizumab (not Elbasvir) in HCV+/- HCC patients; unrelated to HBV |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | DAA safety database study in HCV patients; not an HBV study |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Completed | 301 | Grazoprevir/Elbasvir in HCV GT1/4/6 patients on opiate substitution therapy; HCV, not HBV |
| [NCT01932762](https://clinicaltrials.gov/study/NCT01932762) | Phase 2 | Completed | 98 | Grazoprevir ± Elbasvir ± ribavirin in chronic HCV GT2/4/5/6; HCV, not HBV |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Terminated | 13 | Zepatier (Grazoprevir/Elbasvir) point-of-care testing in homeless HCV patients; HCV, not HBV |
| [NCT03110055](https://clinicaltrials.gov/study/NCT03110055) | N/A | Unknown | 20 | Zepatier + TACE vs. TACE alone in HCV-related HCC; HCV, not HBV |
| [NCT02332707](https://clinicaltrials.gov/study/NCT02332707) | Phase 2 | Completed | 443 | Grazoprevir/Uprifosbuvir + Elbasvir/Ruzasvir in chronic HCV GT1/2; HCV, not HBV |
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Completed | 413 | Same regimen in chronic HCV GT3/4/5/6; HCV, not HBV |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV eradication in HIV/HCV patients; HCV, not HBV |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | Grazoprevir/Elbasvir in acute HCV GT1/4 (Dutch DAHHS-2 study); HCV, not HBV |

---

## Literature Evidence

*Note: none of the retrieved publications report direct evidence of Elbasvir efficacy in HBV; most are HCV-focused reviews that mention HBV only in passing (e.g., comparative epidemiology or drug-pricing context).*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver International | Discusses progress toward HCV eradication and a functional HBV cure as parallel but distinct goals; no Elbasvir–HBV data |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm. Sin. B | Explicitly contrasts HCV (curable via DAAs targeting NS3/4A, NS5B, NS5A) with HBV, which lacks these targets |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clinical Pharmacokinetics | 2019 update on licensed HCV DAA regimens including elbasvir/grazoprevir; no HBV content |
| [30049677](https://pubmed.ncbi.nlm.nih.gov/30049677/) | 2018 | Review/Case report | BMJ Case Reports | HCV extrahepatic manifestations (dermatomyositis case); unrelated to HBV |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Review | Annals of Hepatology | Cross-sectional comparison of HBV vs. HCV antiviral drug pricing; not an efficacy study |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective (pending classification) | Klin Mikrobiol Infekc Lek | Retrospective review of antiviral treatment for chronic HBV **and** HCV in children (Ostrava); does not isolate Elbasvir/HBV data |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Review (pending classification) | Cancers | HCC in chronic kidney disease, largely HCV-driven cohorts; not HBV/Elbasvir-specific |

---

## EU Market Information

No EU marketing authorization is on record for Elbasvir in this evidence pack (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). This is a significant data gap: it means no SmPC-derived safety, dosing, or indication text is available from the regulatory dataset for this candidate, and it should be independently verified before further evaluation (Elbasvir is known to have been marketed historically only as the fixed-dose combination Zepatier® with grazoprevir).

---

## Safety Considerations

Please refer to the SmPC for safety information. (No key warnings, contraindications, or drug-interaction data were returned in this evidence pack — DDI query status: not found.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack's own mechanistic review rules out a plausible pharmacological basis for this pairing — HBV has no NS5A-homologous target, and its reverse-transcription/cccDNA replication mechanism is fundamentally different from HCV. All 13 clinical trials and the literature retrieved are existing HCV (Elbasvir/Grazoprevir) studies misattributed to the HBV query, not genuine HBV evidence. Combined with the absence of any EU marketing authorization on file, there is no basis to advance this candidate beyond a Hold.

**To proceed, the following is needed:**
- Formal MOA confirmation via DrugBank API (currently blocking — DG002)
- TFDA/EMA label (SmPC) warnings and contraindications, currently a blocking data gap for safety screening (DG001)
- Verification of actual EU marketing-authorization status (the "not marketed" record here should be cross-checked against Zepatier's historical EU approval/withdrawal history)
- If pursued further: genuine preclinical or in-vitro evidence of NS5A-independent anti-HBV activity for Elbasvir, since no such studies currently exist in the collected evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

