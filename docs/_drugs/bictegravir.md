---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Bictegravir is a second-generation integrase strand transfer inhibitor (INSTI) internationally approved as Biktarvy® (co-formulated with emtricitabine and tenofovir alafenamide) for HIV-1 treatment, though not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **no clinical trials** and **3 preclinical/structural biology publications** currently supporting this direction.
This prediction primarily reflects mechanistic cross-reactivity between HIV and SIV integrases, and represents a research question rather than a near-term clinical repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (international approval; not Taiwan-registered) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the current evidence pack (DG002). Based on known information from the retrieved literature, Bictegravir is a novel, once-daily, unboosted INSTI. It binds the HIV integrase enzyme active site and blocks the strand transfer step — the reaction that inserts viral DNA into the host chromosome. Compared to first-generation INSTIs (raltegravir and elvitegravir), Bictegravir carries a substantially higher genetic barrier to resistance and does not require pharmacokinetic boosting with cobicistat.

SIV and HIV-1 are both lentiviruses belonging to the primate immunodeficiency virus group and both replicate via the same integrase-dependent two-step mechanism: 3′-processing of viral DNA ends, followed by strand transfer into host chromatin. Because Bictegravir targets the conserved active-site metal-chelating pharmacophore of integrase, it retains theoretical antiviral activity across strains whose integrase pocket architecture resembles HIV-1. PMID 28923862 (2017) directly confirmed this by testing Bictegravir against INSTI-resistant SIVmac239 in vitro, and PMID 39559349 (2024) validated a humanized mouse model capable of testing antiviral strategies against SIV and HIV simultaneously.

That said, SIV infection is a disease of non-human primates with no corresponding human clinical indication. Its primary scientific value lies in serving as a preclinical model for HIV pathogenesis and cure research — not as a standalone drug repurposing target. The high TxGNN score likely reflects the deep structural and mechanistic overlap between HIV and SIV captured in the knowledge graph, rather than a signal for a new human indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bictegravir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro / Preclinical | Antimicrobial Agents and Chemotherapy | Direct in vitro testing of Bictegravir and Cabotegravir against INSTI-resistant SIVmac239 and HIV-1; demonstrates Bictegravir's superior genetic barrier to resistance compared to raltegravir and elvitegravir across both viruses |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Animal Model (Preclinical) | Frontiers in Immunology | Dual-purpose humanized mouse model simultaneously evaluating antiviral strategies against SIV and HIV; supports Bictegravir's use in cross-species preclinical efficacy testing |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Review | The FEBS Journal | Cryo-EM and X-ray crystal structures of HIV/SIV intasome complexes explain how INSTIs including Bictegravir and dolutegravir bind integrase and how viral escape mutations confer resistance; provides the structural rationale for cross-species inhibitory activity |

---

## Taiwan Market Information

Bictegravir is not currently registered in Taiwan (TFDA). No marketing authorizations are on record (0 licenses).

> **Reference context:** Internationally, Bictegravir is available as Biktarvy® (bictegravir 50 mg / emtricitabine 200 mg / tenofovir alafenamide 25 mg), approved by the US FDA (February 2018) and the EMA for HIV-1 treatment in adults and pediatric patients. Taiwan registration status should be confirmed directly via the TFDA online database.

---

## Safety Considerations

Please refer to the Biktarvy® SmPC or prescribing information for safety data.

> TFDA package insert warnings and contraindications are not available for this report (data gap DG001: TFDA 仿單 PDF not yet retrieved). DrugBank DDI data returned no results for Bictegravir in the current query. Until the TFDA SmPC is obtained, no Taiwan-specific safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is a non-human primate disease without a corresponding human clinical indication, making it an unsuitable direct repurposing target regardless of mechanistic plausibility. With L4 evidence (preclinical in vitro and animal models only, no human clinical trials), this prediction is best understood as a confirmation of Bictegravir's broad-spectrum INSTI activity rather than a clinical repurposing signal. Among all 10 TxGNN-ranked predictions in this evidence pack, the two most clinically actionable findings — both also mechanistically coherent — are **AIDS-related complex** (rank 5, L2, ARTISTRY-1 Phase 3 RCT; PMID 41763229) and **congenital HIV / pediatric HIV** (rank 6, L2, including Phase 1b neonatal PK study NCT07055451 and completed Phase 1b pregnant women study NCT03960645). These warrant separate focused reports.

**To proceed, the following is needed:**

- **Safety foundation (blocking):** Retrieve and parse the TFDA SmPC PDF (DG001) to enable Taiwan-specific safety evaluation before any further regulatory assessment
- **MOA documentation:** Query the DrugBank API for Bictegravir's full mechanism, categories, and toxicity profile (DG002) to support cytotoxicity and interaction analyses
- **For SIV specifically:** No further clinical development is warranted as a repurposing target; redirect mechanistic insights to support HIV cure and resistance research programs
- **For AIDS-related complex and congenital HIV:** Commission dedicated evidence reviews drawing on ARTISTRY-1 trial data and the accumulating pediatric/maternal B/F/TAF PK dataset before advancing to feasibility assessment
- **Taiwan regulatory pathway:** Confirm whether Biktarvy® has a pending or planned TFDA submission; if not, a full de novo regulatory pathway assessment is required before any Taiwan-specific clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

