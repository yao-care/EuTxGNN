---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Lamivudine
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

# Lamivudine: From HIV/Antiretroviral Therapy to Hepatitis B Virus Infection

## One-Sentence Summary

Lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor (NRTI) with established global approval for HIV-1 treatment and chronic hepatitis B, but currently not marketed in Taiwan.
The TxGNN model's highest-ranked human clinical prediction is **Hepatitis B Virus Infection** (rank 6, score 97.84%), supported by **50+ clinical trials** and **20+ publications**, reflecting a well-documented efficacy base that represents a regulatory introduction opportunity in Taiwan.

> **Note on top TxGNN predictions**: Ranks 1 and 2 are simian immunodeficiency virus (SIV, score 99.93%) and feline acquired immunodeficiency syndrome (FIV, score 99.93%) — both non-human veterinary indications with no applicable human repurposing value. Ranks 3, 4, 8, 9, and 10 carry Hold recommendations (L5 evidence or known mechanistic incompatibility). This report focuses on **Hepatitis B Virus Infection** (rank 6) as the highest-evidence, most clinically actionable human indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not licensed in Taiwan; globally approved for HIV-1 and chronic hepatitis B |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 97.84% (rank 6) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 (Taiwan) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lamivudine is a cytidine nucleoside analogue. After intracellular phosphorylation to its active triphosphate form (3TC-TP), it acts as a competitive inhibitor of reverse transcriptase — incorporating into the growing viral DNA chain and causing obligate chain termination. The key structural reason this works against both HIV and HBV is that **HIV reverse transcriptase and HBV DNA polymerase share homologous YMDD catalytic domains**, allowing the same molecule to inhibit both enzymes through the same mechanism.

HBV replicates via a pregenomic RNA (pgRNA) intermediate, which is reverse-transcribed into the viral relaxed circular DNA (rcDNA) by HBV polymerase. Lamivudine blocks this step precisely, which explains why it earned dual FDA approval as both Epivir® (HIV-1, 1995) and Epivir-HBV® (chronic hepatitis B, 1998). This mechanistic overlap is exactly what the TxGNN knowledge graph captures, producing a high prediction score (97.84%) that mirrors real-world clinical consensus.

The key clinical limitation is the YMDD-motif resistance mutation (rtM204V/I), which emerges in approximately 25% of patients by year 1 and exceeds 50% by year 3 of lamivudine monotherapy. Current EASL and AASLD guidelines consequently position tenofovir (TDF/TAF) and entecavir as preferred first-line agents, with lamivudine retained as a third-line or resource-limited alternative. In Taiwan, where lamivudine is presently unmarked, introducing it with a clear resistance monitoring plan and explicit guideline-concordant positioning represents the main guardrail required before proceeding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00001457](https://clinicaltrials.gov/study/NCT00001457) | Phase 2 | Completed | 60 | Foundational "Lamivudine for Chronic Hepatitis B" trial — directly compared with alpha interferon; established antiviral efficacy and tolerability benchmark for chronic HBV |
| [NCT00124241](https://clinicaltrials.gov/study/NCT00124241) | Phase 2b | Completed | N/A | Extension study: telbivudine vs lamivudine vs LdT+3TC beyond 1 year — directly evaluated lamivudine long-term comparative outcomes |
| [NCT03236584](https://clinicaltrials.gov/study/NCT03236584) | Phase 3 | Unknown | 76 | Tenofovir monotherapy vs lamivudine + adefovir in lamivudine-resistant CHB with prior viral suppression — informs resistance rescue strategy |
| [NCT01580202](https://clinicaltrials.gov/study/NCT01580202) | Phase 3 | Completed | 180 | Entecavir vs lamivudine prophylaxis to prevent HBV reactivation in HBV-positive patients undergoing cytotoxic chemotherapy |
| [NCT00076336](https://clinicaltrials.gov/study/NCT00076336) | Phase 3 | Completed | 232 | Telbivudine vs lamivudine in decompensated chronic hepatitis B with cirrhosis — safety and virological suppression in high-risk patients |
| [NCT00131742](https://clinicaltrials.gov/study/NCT00131742) | Phase 3 | Completed | N/A | Telbivudine vs lamivudine in Chinese adults with compensated CHB — relevant Asian population data |
| [NCT02202473](https://clinicaltrials.gov/study/NCT02202473) | Phase 4 | Completed | 192 | Oxymatrine + lamivudine vs lamivudine monotherapy — evaluated whether combination reduces long-term resistance incidence |
| [NCT00380614](https://clinicaltrials.gov/study/NCT00380614) | Phase 4 | Completed | N/A | Randomized trial of lamivudine in acute hepatitis B — rapid HBV DNA reduction to potentially prevent fulminant hepatitis |
| [NCT01046799](https://clinicaltrials.gov/study/NCT01046799) | Phase 3 | Completed | 20 | Post-liver transplant HBV reinfection prevention: short-term HBIG then entecavir vs lamivudine |
| [NCT00354653](https://clinicaltrials.gov/study/NCT00354653) | Phase 4 | Completed | 100 | Open-label lamivudine in HBeAg-negative chronic HBV in Iran — 2-year efficacy in pre-core mutant patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35499182](https://pubmed.ncbi.nlm.nih.gov/35499182/) | 2022 | Cochrane Review | Antiviral Therapy | Adefovir for lamivudine-resistant HBV: documents lamivudine's established initial efficacy and >50% year-3 resistance rate; defines rescue therapy paradigm |
| [31272463](https://pubmed.ncbi.nlm.nih.gov/31272463/) | 2019 | Meta-analysis | Virology Journal | Lamivudine in children with chronic HBV: meta-analysis confirms safety and efficacy of 3 mg/kg/day in pediatric population |
| [16984494](https://pubmed.ncbi.nlm.nih.gov/16984494/) | 2006 | Systematic Review | Alimentary Pharmacology & Therapeutics | Systematic review of lamivudine prophylaxis for chemotherapy-induced HBV reactivation; supports preemptive use in HBsAg-positive cancer patients |
| [22077578](https://pubmed.ncbi.nlm.nih.gov/22077578/) | 2011 | Cost-Effectiveness | PharmacoEconomics | Prophylactic lamivudine reduces HBV vertical transmission in high-viremia mothers; favorable cost-effectiveness ratio modeled for Taiwan context |
| [12269843](https://pubmed.ncbi.nlm.nih.gov/12269843/) | 2002 | Review | Paediatric Drugs | Dose-ranging data: lamivudine 3 mg/kg/day (max 100 mg) optimal for pediatric CHB; comprehensive tolerability review |
| [19207972](https://pubmed.ncbi.nlm.nih.gov/19207972/) | 2009 | Review | Liver International | Natural history of chronic HBV and long-term outcomes under treatment; lamivudine positioned as foundational antiviral comparator |
| [11231955](https://pubmed.ncbi.nlm.nih.gov/11231955/) | 2001 | Review | Gastroenterology | Molecular anatomy of YMDD resistance in HBV: mechanism of rtM204V/I emergence and its clinical implications for lamivudine long-term therapy |
| [12702032](https://pubmed.ncbi.nlm.nih.gov/12702032/) | 2003 | Cohort | Journal of Internal Medicine | Lamivudine before and after liver transplantation: effective HBV suppression reduces post-transplant graft reinfection risk |
| [16980024](https://pubmed.ncbi.nlm.nih.gov/16980024/) | 2006 | Cohort | Transplantation Proceedings | Successful lamivudine treatment of HBV after heart transplantation in Taiwan (N=18); supports use in immunosuppressed post-transplant patients |
| [21973301](https://pubmed.ncbi.nlm.nih.gov/21973301/) | 2011 | Review | Expert Review of Anti-infective Therapy | HBV management in hematopoietic stem cell transplantation: lamivudine prophylaxis for reactivation prevention in immunocompromised patients |

---

## Taiwan Market Information

Lamivudine is currently **not marketed in Taiwan**. No TFDA licenses are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No Taiwan authorizations | — | No Taiwan authorizations on record |

For reference, lamivudine holds approvals in other major jurisdictions:
- **FDA**: Epivir® (HIV-1 treatment); Epivir-HBV® (chronic hepatitis B with active viral replication and evidence of active hepatitis)
- **EMA**: Epivir® and multiple generic products approved for HIV-1 and chronic HBV

A TFDA regulatory submission would be required before lamivudine can be marketed in Taiwan. Given the extensive global evidence base, an abbreviated NDA or referencing international approval packages may accelerate the review process.

---

## Safety Considerations

No Taiwan-specific package insert data (warnings, contraindications) is available in this evidence pack. Based on established international safety profiles:

- **YMDD Resistance (Critical)**: The rtM204V/I mutation confers high-level resistance to lamivudine. Resistance emerges in ~25% at year 1, rising to >50% by year 3 of monotherapy. HBV DNA monitoring every 3–6 months is mandatory, with a pre-defined switch strategy upon virological breakthrough (HBV DNA rebound ≥1 log₁₀ IU/mL above nadir).
- **HBV Flare on Discontinuation**: Abrupt withdrawal triggers hepatitis exacerbation in a subset of patients; potentially life-threatening in those with underlying cirrhosis or impaired hepatic reserve. Discontinuation requires structured tapering and clinical monitoring.
- **Lactic Acidosis / Severe Hepatomegaly**: Rare but potentially fatal class effect of NRTIs; risk is elevated in patients with hepatic dysfunction or prolonged use.
- **Drug Interactions**: No DDI data was found in the database query for this evidence pack. Please refer to the FDA/EMA SmPC for complete interaction profile, particularly with TMP-SMX (increases lamivudine exposure) and other NRTIs.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lamivudine has Level 1 evidence for hepatitis B virus infection, underpinned by multiple completed Phase 3 RCTs, a Cochrane systematic review, and FDA approval dating to 1998. The TxGNN prediction (97.84%) accurately reflects the well-established mechanistic basis — HBV polymerase inhibition via the same YMDD-domain targeting used in HIV treatment. The absence of Taiwan marketing authorization represents a regulatory gap, not a scientific uncertainty, and there are specific patient populations (chemotherapy prophylaxis, liver transplant recipients, pregnancy, resource-limited settings) where lamivudine's clinical role remains current and relevant even within a guideline landscape that favors tenofovir and entecavir for treatment-naive patients.

**To proceed, the following is needed:**
- **Safety package**: Obtain full FDA/EMA SmPC or TFDA package insert; confirm warnings, contraindications, and DDI profile before any clinical evaluation
- **Guideline positioning**: Confirm lamivudine's current placement in EASL 2024 and AASLD guidelines; document that it is third-line for treatment-naive patients but may remain preferred in pregnancy, renal impairment, or specific co-infection scenarios
- **Resistance monitoring protocol**: Define HBV DNA monitoring intervals (every 3 months for first year, every 6 months thereafter), virological breakthrough threshold, and pre-planned entecavir or tenofovir switch criteria
- **Target population definition**: Identify the specific Taiwan patient segments where lamivudine provides added value over already-available alternatives (if any exist in Taiwan)
- **Regulatory pathway assessment**: Determine whether TFDA will accept an abbreviated NDA based on existing FDA/EMA dossiers, and estimate timeline and cost for market introduction
- **Commercial and supply chain review**: Assess whether generic lamivudine products can be sourced at competitive cost, given that tenofovir and entecavir generics are also widely available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

