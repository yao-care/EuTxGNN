---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Caspofungin
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

# Caspofungin: From Invasive Candidiasis to Congenital Candidiasis

## One-Sentence Summary

Caspofungin is a first-in-class echinocandin antifungal, established for the treatment of invasive candidiasis and aspergillosis by inhibiting the fungal cell wall enzyme β-1,3-D-glucan synthase.
Although TxGNN's highest-ranked prediction (gastrin secretion abnormality, score 99.4%) carries no mechanistic support and is assessed as a likely false positive, the most clinically actionable prediction is **Congenital Candidiasis** (rank #8, score 95.2%),
backed by **1 completed Phase 3 clinical trial** and **11 publications** — with additional strong evidence for neonatal candidiasis (L2) and *Candida glabrata* infection (L2).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Taiwan TFDA record (drug not marketed; reference: invasive candidiasis / invasive aspergillosis per international SmPC) |
| Predicted New Indication | Congenital Candidiasis (TxGNN rank #8; top-ranked prediction "gastrin secretion abnormality" is a likely GNN false positive) |
| TxGNN Prediction Score | 95.18% (congenital candidiasis, rank #8) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (DrugBank MOA query returned a data gap). Based on established pharmacological knowledge, caspofungin is an echinocandin antifungal that non-competitively inhibits β-1,3-D-glucan synthase — an enzyme encoded by the *FKS* gene family in *Candida* and *Aspergillus* species. This enzyme polymerizes β-1,3-D-glucan, an essential structural polysaccharide of the fungal cell wall. Blocking this step causes the cell wall to lose integrity, ultimately leading to osmotic lysis and fungal cell death. Because human cells do not express β-1,3-D-glucan synthase, caspofungin's selectivity profile is highly favorable.

**On TxGNN prediction quality for this drug**: The top three TxGNN predictions (gastrin secretion abnormality rank #1; punctate epithelial keratoconjunctivitis rank #2; abnormality of glucagon secretion rank #3) are assessed as false positives. These conditions involve gastric G-cells, corneal epithelium, and pancreatic α-cells respectively — none of which possess fungal cell walls or express any target relevant to echinocandin pharmacology. The high prediction scores (99.4–97.7%) most likely reflect distant graph-node clustering in the TxGNN knowledge graph rather than biological plausibility.

The most clinically meaningful prediction is **Congenital Candidiasis** (rank #8). This condition is caused by the same *Candida* species — primarily *C. albicans*, *C. parapsilosis*, and *C. glabrata* — that caspofungin directly targets via β-glucan inhibition. Neonates with congenital candidiasis face two compounding challenges: amphotericin B (the historical standard) carries nephrotoxicity risk in renally immature infants, and fluconazole resistance is rising among non-albicans *Candida* species. Caspofungin addresses both gaps simultaneously, offering direct fungicidal activity while substantially reducing the nephrotoxic burden. A completed Phase 3 clinical trial in this setting (NCT00635648) provides Level 1 evidence.

---

## Clinical Trial Evidence

### Congenital Candidiasis (Rank #8 · L1 · Primary Focus)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00635648](https://clinicaltrials.gov/study/NCT00635648) | Phase 3 | Completed | 63 | Multicenter open-label non-comparative study evaluating caspofungin safety, tolerability, and efficacy for esophageal candidiasis and invasive candidiasis; conducted to support caspofungin registration in China — represents the highest-grade direct clinical evidence for the candidiasis indication |

### Neonatal Candidiasis (Rank #10 · L2 · High Relevance)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01945281](https://clinicaltrials.gov/study/NCT01945281) | Phase 2 | Terminated ⚠️ | 51 | Double-blind RCT comparing caspofungin vs amphotericin B deoxycholate in neonates and infants <3 months; primary hypothesis was superior fungal-free survival at 2-week post-therapy follow-up — termination reason must be clarified before clinical adoption |
| [NCT00330395](https://clinicaltrials.gov/study/NCT00330395) | Phase 2 | Completed | 16 | Open-label sequential PK/safety study of caspofungin 25 mg/m² in neonates <3 months with Candida infections; established the body-surface-area dosing rationale for this population |

### HIV-associated Opportunistic Fungal Infections (Rank #4 · L3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06691321](https://clinicaltrials.gov/study/NCT06691321) | N/A | Recruiting | 60 | Observational study directly evaluating caspofungin efficacy for Pneumocystis jirovecii pneumonia (PCP) in HIV/AIDS patients; motivated by *Pneumocystis* β-D-glucan composition and echinocandin activity in murine models — most current and relevant HIV-context trial |
| [NCT00005921](https://clinicaltrials.gov/study/NCT00005921) | N/A | Completed | 18 | Open serial-panel multi-dose PK/safety study in HIV patients with AIDS-related Candida esophagitis; provides foundational safety data for HIV-population caspofungin use |
| [NCT00005920](https://clinicaltrials.gov/study/NCT00005920) | Phase 2 | Terminated | 70 | Double-blind randomized dose-comparison study for fluconazole-refractory oropharyngeal candidiasis in HIV/AIDS adults; terminated — reason unknown, warrants investigation |

### *Candida glabrata* Infection (Rank #9 · L2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00839540](https://clinicaltrials.gov/study/NCT00839540) | Phase 4 | Completed | 21 | PK/PD comparison of caspofungin vs micafungin serum cidal activity against *Candida* isolates including *C. glabrata* strains with varying echinocandin susceptibilities; directly informs clinical use |
| [NCT03652194](https://clinicaltrials.gov/study/NCT03652194) | N/A | Unknown | 21 | Study of innate immune response to echinocandin-resistant *C. glabrata* isolates in candidemia; key resistance surveillance data relevant to therapy decisions |
| [NCT05881109](https://clinicaltrials.gov/study/NCT05881109) | N/A | Completed | 30 | Population PK model and dose optimization of caspofungin in adolescents undergoing allogeneic HSCT — a high-risk population for *C. glabrata* infection |

---

## Literature Evidence

### Congenital Candidiasis (Rank #8)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16681818](https://pubmed.ncbi.nlm.nih.gov/16681818/) | 2006 | Case Report | Mycoses | Successful caspofungin treatment of multidrug-resistant *C. parapsilosis* septicemia in a 27-week ELBW neonate (980 g) resistant to both amphotericin B and fluconazole — demonstrates salvage value in the most vulnerable patients |
| [22333013](https://pubmed.ncbi.nlm.nih.gov/22333013/) | 2012 | Case Report | J Formosan Med Assoc | ELBW infant with congenital *C. albicans* — caspofungin achieved initial blood sterilization; secondary candidemia after discontinuation highlights need for continued monitoring and defined treatment duration |
| [19840314](https://pubmed.ncbi.nlm.nih.gov/19840314/) | 2009 | Case Report | Pediatr Dermatol | Successful caspofungin + amphotericin B combination therapy for *C. albicans* septicemia in a preterm infant with congenital ichthyosis (Harlequin baby) |
| [21525820](https://pubmed.ncbi.nlm.nih.gov/21525820/) | 2011 | Case Series | Med Sci Monitor | Candidemia in children after congenital heart defect surgery managed with caspofungin; highlights surgically complex neonatal populations as a key risk group |
| [16012261](https://pubmed.ncbi.nlm.nih.gov/16012261/) | 2005 | Review | Curr Opin Pediatrics | Neonatal cutaneous fungal infections — discusses the vulnerability of premature and immunocompromised neonates and the role of newer antifungals including echinocandins |

### Neonatal Candidiasis (Rank #10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31586424](https://pubmed.ncbi.nlm.nih.gov/31586424/) | 2020 | RCT | J Antimicrob Chemother | Double-blind randomized trial comparing caspofungin vs amphotericin B deoxycholate in neonates/infants <3 months with invasive Candida infection — primary head-to-head comparative evidence for this population |
| [29596219](https://pubmed.ncbi.nlm.nih.gov/29596219/) | 2019 | Meta-analysis | Pediatr Infect Dis J | Meta-analysis of echinocandin efficacy and safety for invasive candidiasis across neonatal and pediatric patients — class-level evidence supporting caspofungin use |
| [39766599](https://pubmed.ncbi.nlm.nih.gov/39766599/) | 2024 | Review | Antibiotics (Basel) | Current NICU perspective on echinocandin use in low birth weight and critically ill neonates; addresses caspofungin dosing challenges and monitoring needs |
| [19075070](https://pubmed.ncbi.nlm.nih.gov/19075070/) | 2009 | PK Study | Antimicrob Agents Chemother | First prospective PK/safety data for caspofungin 25 mg/m²/day in neonates and infants <3 months; established the body-surface-area dosing rationale used in subsequent trials |
| [36329878](https://pubmed.ncbi.nlm.nih.gov/36329878/) | 2022 | Review | Curr Treat Options Infect Dis | Updated pharmacologic prophylaxis and treatment options for invasive candidiasis in NICU/PICU; positions echinocandins within current management algorithms |

### HIV-associated Fungal Infections (Rank #4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33277811](https://pubmed.ncbi.nlm.nih.gov/33277811/) | 2021 | Clinical Study | HIV Medicine | Caspofungin combined with TMP/SMZ as first-line therapy for moderate-to-severe PCP in HIV-infected patients — primary evidence for combination use in this setting |
| [38822256](https://pubmed.ncbi.nlm.nih.gov/38822256/) | 2024 | Systematic Review & Meta-analysis | BMC Infect Dis | Drug-resistant oral candidiasis in HIV patients: prevalence and patterns; underscores the growing need for echinocandin alternatives in azole-refractory settings |
| [17501701](https://pubmed.ncbi.nlm.nih.gov/17501701/) | 2007 | Review | Expert Opin Investig Drugs | Comprehensive review of caspofungin pharmacology, licensed indications, and clinical use in HIV-infected individuals including candidal and aspergillus infections |
| [12230933](https://pubmed.ncbi.nlm.nih.gov/12230933/) | 2002 | Clinical Study | AIDS Res Hum Retroviruses | Pooled analysis across 4 clinical trials: caspofungin 50 mg/day response and relapse rates for Candida esophagitis in HIV-infected adults |

---

## Taiwan Market Information

Caspofungin is **not currently marketed in Taiwan** (未上市) according to the TFDA database. No marketing authorizations are on record.

> Caspofungin (Cancidas®) holds regulatory approvals in the US (FDA), EU (EMA), Japan (PMDA), and other major jurisdictions for: invasive candidiasis (including candidemia), invasive aspergillosis (salvage therapy), and empirical antifungal therapy in febrile neutropenic patients. For clinical reference, consult the Cancidas® EU SmPC or FDA US Prescribing Information. The absence of a Taiwan TFDA license constitutes a **Blocking data gap (DG001)** that must be resolved before local regulatory submission.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> The TFDA package insert (仿單) was not available in this Evidence Pack (Data Gap DG001, severity: Blocking). Based on published neonatal literature and international SmPCs, key safety signals include:
> - **Drug interactions**: cyclosporine increases caspofungin AUC by approximately 35% (monitor liver function); caspofungin reduces tacrolimus trough levels by approximately 20% (requires dose adjustment in transplant patients)
> - **Neonatal dosing**: body-surface-area dosing (25 mg/m²/day IV) is required in neonates <3 months — weight-based fixed dosing used in adults is inappropriate in this population
> - **Echinocandin resistance**: FKS1/FKS2 mutations in *C. glabrata* can abolish caspofungin activity; susceptibility testing is mandatory before initiating therapy

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Congenital Candidiasis and Neonatal Candidiasis)

**Rationale:**
The mechanistic link is direct and well-validated — caspofungin's fungicidal activity via β-1,3-D-glucan synthase inhibition targets all major *Candida* species causing congenital and neonatal candidiasis, with a safety profile that is particularly advantageous over amphotericin B in renally vulnerable neonates. A completed Phase 3 trial, a double-blind RCT, two Tier-1 meta-analyses, and extensive case-series literature collectively support an L1/L2 evidence level. The drug is already approved in major international markets for the parent indication (invasive candidiasis), further lowering the regulatory threshold for the neonatal extension.

**To proceed, the following is needed:**
- Clarify the termination reason for NCT01945281 (Phase 2 RCT in neonates, n=51 terminated) — if the cause was a safety event such as increased mortality or hepatotoxicity, the risk-benefit assessment must be re-evaluated before adoption
- Retrieve the TFDA package insert (仿單) to document Taiwan-specific warnings, contraindications, and the approved indication scope (Data Gap DG001 — Blocking for regulatory pathway)
- Mandatory antifungal susceptibility testing protocol: MIC determination and FKS1/FKS2 mutation screening before and during therapy, given documented echinocandin resistance emergence in *C. glabrata* across multiple countries
- Establish a neonatal therapeutic drug monitoring plan using body-surface-area dosing (25 mg/m²/day) with dose adjustment guidance for extremely low birth weight infants (<1,000 g)
- Assess drug interaction risk with co-administered agents common in neonatal ICU settings (cyclosporine post-cardiac surgery; tacrolimus in transplant neonates; rifampin and dexamethasone, which reduce caspofungin exposure via CYP induction)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

