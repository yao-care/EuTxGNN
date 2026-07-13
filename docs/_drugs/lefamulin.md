---
layout: default
title: Lefamulin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Lefamulin
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

# Lefamulin: From Community-Acquired Bacterial Pneumonia to Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Lefamulin (Xenleta) is a first-in-class pleuromutilin antibiotic approved in the United States in 2019 for community-acquired bacterial pneumonia (CABP), but currently not marketed in Taiwan.
The TxGNN model predicts it may have potential activity against **Diffuse Cutaneous Leishmaniasis** — a chronic parasitic skin infection caused by *Leishmania* species — with a high model confidence score of **99.24%**.
However, **0 clinical trials** and **0 publications** currently support this direction; this prediction remains a purely AI-generated hypothesis without any experimental validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Community-Acquired Bacterial Pneumonia (CABP) |
| Predicted New Indication | Leishmaniasis, Diffuse Cutaneous |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lefamulin belongs to the pleuromutilin class of antibiotics — a novel mechanism of action distinct from all other antibiotic classes. It works by binding to the peptidyl transferase center (PTC) of the bacterial **50S ribosomal subunit**, blocking both A- and P-site substrate binding and thereby shutting down protein synthesis. Crucially, this binding site differs structurally from that targeted by macrolides, lincosamides, or oxazolidinones, which means lefamulin retains activity against many multi-drug-resistant organisms.

The theoretical basis for the leishmaniasis prediction rests on an important biological observation: *Leishmania* parasites possess **prokaryotic-type (70S) mitochondrial ribosomes** — not the eukaryotic 80S ribosomes typical of human cells. Since pleuromutilins target the 70S ribosomal PTC, there exists a mechanistic argument that lefamulin could theoretically disrupt *Leishmania* mitochondrial protein synthesis in a manner analogous to its antibacterial effect. This is a biologically coherent hypothesis and represents the most scientifically grounded rationale among Lefamulin's top TxGNN predictions.

That said, significant uncertainty remains. Diffuse cutaneous leishmaniasis and CABP are mechanistically very distant: one is a chronic intracellular parasitic infection of macrophages, the other a community-acquired bacterial respiratory illness. While the ribosomal target hypothesis is intellectually attractive, **no in vitro susceptibility data, animal model studies, or clinical observations** have been published to confirm whether lefamulin can penetrate host macrophages, reach adequate intracellular concentrations, or achieve meaningful anti-leishmanial activity at clinically relevant doses. The prediction score reflects knowledge graph topology, not empirical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Lefamulin is not currently marketed in Taiwan and holds no TFDA authorizations. It is approved by the US FDA (August 2019) and EMA (February 2020) for CABP in adults, available in both intravenous and oral formulations (brand name: Xenleta). Regulatory filings in Taiwan have not been identified as of the data cutoff.

---

## Safety Considerations

Detailed TFDA prescribing information (包裝仿單) has not been retrieved for this report. Based on the drug's known profile from US/EU approval:

- **Key known concerns**: QTc prolongation (contraindicated with QT-prolonging drugs), embryo-fetal toxicity (avoid in pregnancy), hepatotoxicity risk with IV formulation
- **Drug Interactions**: Strong CYP3A4 inhibitors/inducers may significantly alter lefamulin exposure; co-administration with QTc-prolonging agents (e.g., fluoroquinolones, certain antifungals) is contraindicated

Please refer to the full SmPC or FDA prescribing information for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Lefamulin are rated L5 (AI model prediction only), with zero supporting clinical trials or literature across any predicted target. The top prediction — diffuse cutaneous leishmaniasis — has a plausible mechanistic hypothesis (70S mitochondrial ribosome targeting), but this remains entirely unvalidated; the remaining 9 predictions carry weak-to-absent biological rationale and most likely reflect knowledge graph network topology rather than true therapeutic potential.

**To proceed, the following is needed:**

- **In vitro anti-leishmanial activity testing**: Establish MIC/IC₅₀ against *Leishmania major*, *L. braziliensis*, and *L. donovani* amastigote/promastigote forms before any further investment
- **Intracellular penetration data**: Confirm whether lefamulin achieves effective concentrations inside infected macrophages (the primary host cell for *Leishmania*)
- **Mechanism of action clarification**: Retrieve full MOA data from DrugBank (DG002) to formally characterize pleuromutilin binding selectivity for parasite vs. host ribosomes
- **Safety profile for the target population**: Leishmaniasis is endemic in immunocompromised and resource-limited settings — QTc and hepatotoxicity risks require specific assessment in these populations
- **TFDA prescribing information**: Retrieve and parse the SmPC/仿單 (DG001) to complete the safety gate (S1) before any clinical feasibility assessment
- **Regulatory pathway assessment**: Since Lefamulin is not marketed in Taiwan, a full NDA/505(b)(2) equivalent pathway would be required even for an approved indication — the repurposing regulatory burden is correspondingly higher

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

