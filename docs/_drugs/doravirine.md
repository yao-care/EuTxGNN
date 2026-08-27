---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine (DrugBank DB12301) is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used to treat HIV-1 infection. The TxGNN model predicts it may also be active against **Simian Immunodeficiency Virus (SIV) infection**, a related primate lentivirus, but this direction is currently supported by only **1 indirectly related publication** and **no clinical trials**, making it a low-confidence, model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection *(inferred from clinical trial context in this evidence pack; not a TFDA-approved indication, as the drug is not marketed in Taiwan)* |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record for Doravirine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale attached to its predicted indications, Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that binds and blocks the reverse transcriptase enzyme of HIV-1, preventing conversion of viral RNA into DNA and halting viral replication.

SIV (Simian Immunodeficiency Virus) is a lentivirus closely related to HIV-1 that infects non-human primates and is widely used as an animal model for HIV research. Because SIV reverse transcriptase shares structural similarity with HIV-1 reverse transcriptase, there is a theoretical basis for NNRTI activity extending across the two viruses. This is, however, an indirect taxonomic analogy rather than a finding derived from direct preclinical or clinical testing of Doravirine against SIV.

It is also important to note that the single supporting literature record (PMID 31658118) is a 2020 review discussing **Islatravir**, a different investigational NNRTI-class antiretroviral — not Doravirine itself. The evidence therefore reflects thematic relevance to the reverse-transcriptase-inhibitor drug class rather than a direct study of Doravirine in an SIV context. This substantially weakens confidence in the prediction despite its mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Discusses islatravir, a related NNRTI-class investigational agent, in the treatment/prevention of HIV-1; does not directly study Doravirine or SIV. |

---

## Taiwan Market Information

Doravirine is currently **not marketed in Taiwan** (0 authorizations on record), so no license/product information is available.

---

## Safety Considerations

Please refer to the SmPC / TFDA package insert for safety information (key warnings, contraindications, and drug-interaction data were not available in this evidence pack — DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the supporting evidence is weak and indirect — there are no clinical trials, and the single literature citation concerns a different drug (Islatravir) rather than Doravirine. Without direct preclinical or clinical data linking Doravirine to SIV, this candidate cannot advance past an initial research hypothesis stage.

**To proceed, the following is needed:**
- Doravirine MOA confirmation via DrugBank/primary literature (DG002)
- TFDA label warnings/contraindications for baseline safety screening (DG001, Blocking — currently prevents any S1 safety evaluation)
- Direct in-vitro or preclinical evidence of Doravirine activity against SIV reverse transcriptase
- Drug-drug interaction (DDI) data, currently unavailable (query returned "not_found")

**Additional note:** Within this same evidence pack, a different predicted indication — **congenital human immunodeficiency virus** (rank 5, TxGNN score 98.75%, Evidence Level **L2**, decision stage S2, "Research Question") — is supported by 5 clinical trials, including a completed Phase 3 pivotal trial (NCT02397096) and a dedicated pregnancy pharmacokinetics study (NCT04518228). This candidate, addressing mother-to-child HIV transmission prevention, is considerably more clinically mature than the SIV signal and may warrant separate, prioritized evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

