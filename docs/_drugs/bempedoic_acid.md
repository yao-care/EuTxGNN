---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor approved internationally for LDL-C lowering in adults with heterozygous familial hypercholesterolemia (HeFH) or established atherosclerotic cardiovascular disease (ASCVD).
The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)** — a rarer, more severe form of FH where LDL receptor function is nearly absent.
**18 publications** currently support this direction, including 1 real-world retrospective study directly evaluating bempedoic acid in HoFH patients, though no dedicated registered clinical trials exist for this specific indication.

> **Note on prediction ranking**: TxGNN's top-scored predictions (ranks 1–5) include hyperthyroidism and two veterinary diseases, none with clinical evidence or mechanistic support for repurposing. The highest-evidence, clinically actionable prediction is **HoFH (rank 6)**, which is the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / LDL-C lowering (HeFH or established ASCVD) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase (ACL/ACLY), a cytoplasmic enzyme that converts citrate to acetyl-CoA — a key precursor for hepatic cholesterol synthesis. By acting upstream of HMG-CoA reductase (the target of statins), bempedoic acid reduces intracellular cholesterol availability. This secondarily upregulates LDL receptor (LDLR) expression, leading to increased clearance of circulating LDL-C. Critically, because the drug reduces cholesterol production rather than relying solely on receptor-mediated clearance, it retains partial activity even in receptor-compromised patients.

Homozygous familial hypercholesterolemia (HoFH) is a rare autosomal recessive disorder caused by biallelic mutations in the LDLR gene (or less commonly APOB, PCSK9, or LDLRAP1), resulting in severely impaired or absent LDL receptor function. This renders statins, ezetimibe, and PCSK9 inhibitors substantially less effective, as all three mechanisms depend partly or fully on intact LDL receptors. Bempedoic acid, by targeting the synthesis side of the cholesterol equation, can still reduce hepatic LDL-C output and lower plasma LDL-C even when receptor-mediated uptake is minimal — though the magnitude of reduction is expected to be smaller than in HeFH patients.

The step from HeFH (already an approved indication in the US and EU) to HoFH represents a mechanistically grounded but clinically challenging extension. A 2026 real-world retrospective study (PMID 41274797) specifically evaluated bempedoic acid in HoFH patients, and multiple review articles from 2021–2025 identify bempedoic acid as a candidate add-on agent in this difficult-to-treat population. Preclinical data in LDLR-deficient Yucatan miniature pigs (a large animal HoFH model) further demonstrated LDL-C reduction and attenuation of atherosclerosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-world retrospective study | J Clin Lipidol | Direct evaluation of bempedoic acid efficacy and tolerability specifically in HoFH patients — the most directly relevant clinical evidence available |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical study | Arterioscler Thromb Vasc Biol | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient (LDLR+/− and LDLR−/−) Yucatan miniature pigs; confirms receptor-independent activity |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Comprehensive review of HoFH treatment advances; discusses bempedoic acid as adjunctive option in patients with inadequate response to standard therapy |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Emerging therapies for HoFH covering ACL inhibition, gene therapy, and combination approaches; highlights unmet need in HoFH management |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Expert Review | J Am Coll Cardiol | JACC Focus Seminar on novel LDL-C lowering therapies; positions bempedoic acid within the broader lipid-lowering armamentarium including FH populations |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiol Rep | Updates in management of familial and refractory hypercholesterolemias; identifies bempedoic acid as a viable non-statin option in resistant cases |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiol Rev | Drug class review of novel lipid-lowering agents for FH; bempedoic acid discussed as adjunct to lomitapide and PCSK9 inhibitors in HoFH |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | Cumulative LDL-C exposure and ASCVD risk reduction; bempedoic acid identified as complementary therapy for patients not at goal |
| [39070027](https://pubmed.ncbi.nlm.nih.gov/39070027/) | 2024 | Review | Am J Prev Cardiol | Advances in LDL-C targeting beyond PCSK9 inhibitors; ACL inhibition discussed in the context of FH and ASCVD prevention |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid-lowering drugs for dyslipidaemia including statin-intolerant patients; bempedoic acid mechanism and clinical positioning reviewed |

---

## Taiwan Market Information

Bempedoic acid is **not currently approved or marketed in Taiwan** (0 authorizations on record as of 2026-06-02).

For reference, bempedoic acid is approved in the following major markets:

| Market | Brand Name | Approved Indication | Year |
|--------|-----------|---------------------|------|
| USA (FDA) | Nexletol | Adults with HeFH or established ASCVD requiring additional LDL-C reduction | 2020 |
| EU (EMA) | Nilemdo | Adults with primary hypercholesterolemia (HeFH and non-FH) or mixed dyslipidaemia, as adjunct to diet | 2020 |

Taiwan TFDA regulatory approval has not been obtained as of the data cutoff date. Any Taiwan-market development would require a separate NDA filing.

---

## Safety Considerations

Please refer to the SmPC (EMA) or FDA prescribing information (Nexletol) for full safety information.

> ⚠️ TFDA label data is unavailable (Data Gap DG001). Key known international safety signals include uric acid elevation and gout risk (a class effect of ACL inhibitors), as well as musculoskeletal side effects. Concomitant use with simvastatin or pravastatin may require dose limits due to transporter interactions. Confirm with the full prescribing information before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 2026 real-world retrospective study directly evaluated bempedoic acid in HoFH patients, and the ACL inhibition mechanism offers a receptor-independent LDL-C reduction pathway that addresses the core pharmacological limitation in HoFH. However, LDL-C lowering magnitude in HoFH is expected to be smaller than in HeFH, no dedicated RCT exists, and the drug is not yet approved in Taiwan, requiring regulatory development investment.

**To proceed, the following is needed:**

- **Clinical evidence**: Sponsor or join a dedicated Phase 2/3 RCT in HoFH patients to quantify LDL-C reduction, clinical outcomes, and safety profile in this specific population
- **Mechanistic documentation**: Retrieve full MOA data from DrugBank API (Data Gap DG002) to complete the mechanism-of-action analysis
- **Safety profile**: Download and parse TFDA SmPC equivalents (Data Gap DG001); review FDA/EMA labels for contraindications relevant to HoFH patients (who typically receive multiple lipid-lowering agents concurrently)
- **Competitive positioning**: Benchmark against lomitapide and evinacumab, which have specific HoFH approvals, and define the add-on niche (e.g., patients intolerant to or inadequately controlled by existing HoFH therapies)
- **Taiwan regulatory pathway**: Assess feasibility of TFDA NDA or orphan drug designation for HoFH, given the disease's rare status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

