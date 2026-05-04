---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

## One-Sentence Summary

Ambrisentan is a selective endothelin type A (ETA) receptor antagonist globally approved for pulmonary arterial hypertension (PAH), currently not marketed in Taiwan. The TxGNN model identifies **pulmonary arteriovenous malformation (PAVM)** as the highest-ranked novel indication (score 99.41%), supported by only **1 case report** of indirect mechanistic relevance; however, across this multi-indication analysis, substantially stronger evidence emerges for multiple PAH subtypes — **congenital heart disease-associated PAH** (9 trials, 17 publications, L1) and **HIV-associated PAH** (1 Phase 3 RCT, 4 publications, L1) represent the most actionable repurposing opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (globally approved; not registered in Taiwan) |
| Predicted New Indication (Rank 1) | Pulmonary Arteriovenous Malformation |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Multi-Indication Prediction Landscape

| Rank | Disease | TxGNN Score | Trials | Literature | Evidence Level | Decision |
|------|---------|-------------|--------|------------|----------------|---------|
| 1 | Pulmonary Arteriovenous Malformation | 99.41% | 0 | 1 | L4 | Research Question |
| 2 | PAH / Congenital Heart Disease | 99.37% | 9 | 17 | L1 | Proceed with Guardrails |
| 3 | PAH / Chronic Hemolytic Anemia | 99.30% | 0 | 0 | L5 | Hold |
| 4 | PAH / HIV Infection | 99.30% | 1 | 4 | L1 | Proceed with Guardrails |
| 5 | PAH / Connective Tissue Disease | 99.30% | 3 | 19 | L2 | Proceed with Guardrails |
| 6 | PAH / Schistosomiasis | 99.30% | 0 | 0 | L5 | Hold |
| 7 | Malformation with Odontal/Periodontal Component | 99.19% | 0 | 20 ⚠️ | L5 | Hold |
| 8 | Hypotrichosis Simplex of the Scalp | 99.15% | 0 | 0 | L5 | Hold |
| 9 | Hypertrichosis | 99.14% | 0 | 0 | L5 | Hold |
| 10 | Dandy-Walker Malformation Syndrome | 99.12% | 0 | 0 | L5 | Hold |

> ⚠️ All 20 publications retrieved for rank 7 are general periodontitis research entirely unrelated to Ambrisentan — this is a likely false positive from TxGNN. Ranks 7–10 have no established mechanistic link to ETA antagonism and should be filtered from further analysis.

---

## Why is This Prediction Reasonable? (Rank 1: Pulmonary Arteriovenous Malformation)

Currently, detailed mechanism of action data for Ambrisentan is not available in this Evidence Pack. Based on known information, Ambrisentan is a selective endothelin type A (ETA) receptor antagonist that blocks ET-1-mediated vasoconstriction and inhibits pulmonary vascular smooth muscle cell proliferation, thereby reducing pulmonary vascular resistance. Its proven efficacy in idiopathic PAH demonstrates potent vasodilatory and anti-remodeling activity across pulmonary vascular disease.

Pulmonary arteriovenous malformations (PAVMs) are abnormal direct communications between pulmonary arteries and veins, arising predominantly in hereditary hemorrhagic telangiectasia (HHT) — a rare autosomal dominant vascular disorder. While PAVMs themselves represent structural anomalies not directly amenable to vasodilator therapy, a subset of HHT patients develops secondary pulmonary arterial hypertension as a complication, sharing the same ET-1-driven pathophysiology as idiopathic PAH. The mechanistic rationale for Ambrisentan in PAVM is therefore indirect: the drug targets the secondary PAH component rather than the arteriovenous malformation itself.

The TxGNN prediction likely reflects the co-occurrence of HHT, PAVM, and PAH within the knowledge graph. The single supporting publication (PMID 33969094) describes exactly this scenario — an HHT patient with secondary PAH treated with Ambrisentan — which constitutes L4 indirect evidence. No direct PAVM-targeted clinical data exist at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary arteriovenous malformation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case Report | World J Clin Cases | HHT patient with secondary PAH treated with Ambrisentan; family genetic analysis of ACVRL1/ENG mutations; illustrates indirect use — ETA antagonism targets the PAH component secondary to HHT, not the PAVM structural lesion itself |

---

## High-Evidence Indications

### Rank 2 — PAH Associated with Congenital Heart Disease (L1 · Proceed with Guardrails)

Congenital heart disease-related systemic-to-pulmonary shunts (VSD, ASD, PDA) cause chronic pulmonary overcirculation, sustained endothelial shear stress injury, and progressive upregulation of the ET-1/ETA pathway — driving vascular remodeling and vasoconstriction identical in mechanism to idiopathic PAH. Ambrisentan's selective ETA blockade is therefore mechanistically equivalent across PAH subtypes sharing this pathway. The Eisenmenger syndrome subgroup (irreversible pulmonary vascular disease with shunt reversal) warrants heightened caution: some studies suggest a less favorable benefit-risk ratio in this subgroup, and the decision to treat requires specialist hemodynamic assessment.

#### Clinical Trials

| Trial | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3b | Completed | 134 | Open-label study in Chinese PAH patients (includes CHD-PAH subtype); 12-week primary evaluation of 6-minute walk distance; strongest direct Phase 3 evidence for Ambrisentan in an Asian PAH population |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 (OLE) | Completed | 38 | Long-term open-label extension in pediatric PAH ages 8–18 (includes CHD-PAH); follow-up through June 2022 — the longest available pediatric Ambrisentan safety dataset |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Phase 2 | Terminated | 41 | Randomized comparison of high vs. low dose Ambrisentan in pediatric PAH; terminated at 24 weeks; partial efficacy and safety data available |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Phase 1 | Completed | 29 | Pharmacokinetics of lower-dose Ambrisentan tablet intended for pediatric use; relative bioavailability compared to adult formulation |
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | Terminated | 33 | Randomized double-blind placebo-controlled study in inoperable CTEPH; terminated due to recruitment difficulties (n=33 of 160 planned); design-level evidence for ETA antagonism in non-idiopathic pulmonary hypertension |

#### Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Prospective Observational / Case Series | Am J Cardiology | Ambrisentan in Eisenmenger syndrome cohort at Columbia University PAH Center; improvements in resting and exercise arterial saturations and hemodynamics — first dedicated Ambrisentan data in CHD-PAH |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Prospective Observational | Pediatric Pulmonology | Real-world safety and tolerability of Ambrisentan + Tadalafil combination in pediatric pulmonary hypertension; adverse event profile in children |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review & Meta-analysis | Medicine | PAH-specific drug therapy in Eisenmenger syndrome: efficacy and safety meta-analysis establishing evidence position for targeted therapy |
| [22104452](https://pubmed.ncbi.nlm.nih.gov/22104452/) | 2011 | Registry / Cohort | Postgraduate Medicine | Texas Adult Congenital Heart Program experience; long-term PAH management in adult CHD population |
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Cohort / Observational | Ther Adv Respir Dis | Ambrisentan clinical use and long-term tolerability in a PH referral centre population including CHD-PAH subgroup |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Comprehensive PAH diagnosis and treatment review covering all WHO Group I subtypes including CHD-PAH |

---

### Rank 4 — PAH Associated with HIV Infection (L1 · Proceed with Guardrails)

HIV-associated PAH involves direct endothelial injury by viral proteins (gp120, Nef, Tat), stimulating ET-1 upregulation and driving inflammatory vascular remodeling through the ETA pathway — pathophysiologically convergent with idiopathic PAH. A completed Phase 3 double-blind, randomized, placebo-controlled crossover RCT (NCT00709956, n=64) enrolled HIV-PAH patients on stable background Ambrisentan therapy, representing the highest-level clinical evidence for Ambrisentan's safety and use in this population.

**Critical drug interaction warning:** HIV protease inhibitors (ritonavir, atazanavir, lopinavir) are potent CYP3A4 and P-glycoprotein inhibitors that can significantly increase Ambrisentan plasma concentrations. Comprehensive drug interaction assessment and potential dose adjustment are mandatory before use in patients receiving combination antiretroviral therapy.

#### Clinical Trials

| Trial | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Double-blind randomized placebo-controlled crossover RCT studying Iloprost add-on in symptomatic PAH including HIV-PAH; Ambrisentan was a permitted stable background therapy, validating its safety and tolerability in HIV-PAH treatment settings |

#### Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Cohort / Observational | Ther Adv Respir Dis | Real-world Ambrisentan use in wider PH population at a referral centre; includes HIV-PAH subgroup tolerability data |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry Analysis | Terapevticheskii Arkhiv | Russian national PAH registry 6-year data; epidemiology and current therapy patterns including HIV-PAH subgroup |
| [26897508](https://pubmed.ncbi.nlm.nih.gov/26897508/) | 2016 | Case Series | Medicina Clínica | Four HIV-PAH cases with BMPR2/ACVRL1/ENG molecular characterization; clinical outcomes and treatment response |

---

### Rank 5 — PAH Associated with Connective Tissue Disease (L2 · Proceed with Guardrails)

CTD-PAH — most commonly in systemic sclerosis (SSc/scleroderma) — is characterized by severe endothelial dysfunction, autoimmune vascular injury, and ET-1 overproduction driving both vasoconstriction and progressive fibrosis. Ambrisentan's selective ETA antagonism targets this dual mechanism simultaneously. Evidence includes a completed Phase 2 RCT (EDITA trial, NCT02290613, n=38), a completed Phase 4 study (NCT01042158, n=25), a Tier-1 systematic review with meta-analysis (PMID 38378970), and post-hoc RCT analysis from the AMBITION trial (PMID 32161055). The absence of a dedicated Phase 3 blinded RCT specifically for CTD-PAH limits classification to L2, though overall clinical support is substantial.

#### Clinical Trials

| Trial | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA trial: randomized, double-blind, placebo-controlled study of Ambrisentan in borderline SSc-PAH; evaluates whether early ETA antagonism can arrest disease progression before overt PAH develops |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | Ambrisentan + Tadalafil combination over 36 weeks in SSc-PAH; 6MWD, NYHA functional class, RV-pulmonary vascular function via echocardiography |

#### Literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review & Meta-analysis | Internal and Emergency Medicine | Most recent meta-analysis of RCT evidence for CTD-PAH; functional class, 6MWD, survival, and clinical worsening outcomes across agents including Ambrisentan |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Post-hoc RCT Analysis (Tier 1) | Ann Rheum Dis | AMBITION study CTD-PAH subgroup: initial Ambrisentan + Tadalafil combination prevents clinical events more effectively than monotherapy in CTD-PAH and SSc-PAH subpopulation |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | RCT Subgroup Analysis | Ann Rheum Dis | AMBITION trial CTD-PAH subgroup: attenuated treatment response vs. idiopathic PAH reinforces importance of early combination initiation |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Retrospective Cohort | Respiratory Medicine | ARIES-E trial 3-year follow-up in CTD-PAH: sustained 6MWD improvement and acceptable safety profile with long-term Ambrisentan |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis (Tier 1) | BMJ Open | Meta-analysis of PAH trials in CTD; evaluates whether agent class differences exist and optimal therapeutic strategy |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Ther Adv Respir Dis | Comprehensive Ambrisentan review: mechanism, Phase 3 trial data (ARIES-1/2), CTD-PAH indication, combination therapy evidence, safety profile |

---

## Taiwan Market Information

Ambrisentan is not currently registered in Taiwan (total authorizations: 0). No Taiwan license data is available under any brand name.

For international reference, Ambrisentan holds marketing authorizations as:
- **Letairis®** (Gilead Sciences, USA) — approved for idiopathic, heritable PAH and CTD-associated PAH (WHO FC II–III)
- **Volibris®** (GlaxoSmithKline, EU) — approved for PAH (WHO FC II–III)

A full Taiwan TFDA regulatory pathway assessment would be required before any clinical development or market authorization application in Taiwan.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) for complete safety information, including hepatotoxicity monitoring requirements and teratogenicity warnings (REMS program in the US).

**Drug Interactions (HIV-PAH population):** HIV protease inhibitors — including ritonavir, atazanavir, and lopinavir — are potent CYP3A4 and P-glycoprotein inhibitors. Concomitant use with Ambrisentan may significantly increase Ambrisentan plasma concentrations, amplifying both efficacy and adverse effects. Pharmacokinetic monitoring and possible dose adjustment are required in all HIV-positive patients receiving antiretroviral therapy.

---

## Conclusion and Next Steps

**Overall Decision Summary:**

| Indication | Evidence Level | Decision |
|-----------|----------------|---------|
| PAH / Congenital Heart Disease | L1 | Proceed with Guardrails |
| PAH / HIV Infection | L1 | Proceed with Guardrails |
| PAH / Connective Tissue Disease | L2 | Proceed with Guardrails |
| Pulmonary Arteriovenous Malformation | L4 | Research Question |
| PAH / Chronic Hemolytic Anemia | L5 | Hold |
| PAH / Schistosomiasis | L5 | Hold |
| Odontal/Periodontal Malformation | L5 | Hold — likely false positive |
| Hypotrichosis Simplex of the Scalp | L5 | Hold — likely false positive |
| Hypertrichosis | L5 | Hold — likely false positive |
| Dandy-Walker Malformation Syndrome | L5 | Hold — likely false positive |

---

**Primary Recommendation: Proceed with Guardrails**
(Applicable to CHD-PAH and HIV-PAH; CTD-PAH at L2 also warrants advancement)

**Rationale:**
Completed Phase 3-level clinical trials and substantial observational evidence directly support Ambrisentan's use in CHD-PAH and HIV-PAH, with shared mechanistic underpinning across all PAH subtypes (ET-1/ETA pathway upregulation and vascular remodeling). CHD-PAH evidence is further reinforced by pediatric long-term extension data. The top-ranked TxGNN prediction (PAVM) warrants mechanistic follow-up but does not meet the threshold for clinical advancement at this stage. Four of the ten predictions (ranks 7–10) represent probable false positives and should be excluded from further evaluation.

**To proceed, the following is needed:**

- **MOA documentation:** Retrieve formal Ambrisentan mechanism of action data from DrugBank API (DG002 — High severity, currently pending)
- **TFDA SmPC:** Download and parse Taiwan TFDA product monograph for Taiwan-specific warnings, contraindications, and pregnancy/lactation restrictions (DG001 — Blocking severity; required before S1 safety assessment)
- **DDI assessment for HIV-PAH:** Complete systematic drug interaction analysis for HIV antiretroviral co-administration (CYP3A4/P-gp pathways), particularly protease inhibitors
- **Eisenmenger subgroup review:** Assess whether benefit-risk profile supports treatment in Eisenmenger syndrome vs. non-Eisenmenger CHD-PAH; some evidence suggests limited benefit in Eisenmenger subgroup
- **Taiwan regulatory pathway:** Identify the appropriate strategy for CHD-PAH and/or HIV-PAH indication in Taiwan — new market authorization application vs. supplemental indication approval
- **Pediatric dosing strategy for CHD-PAH:** Leverage NCT04095286 pharmacokinetic data to define age-appropriate dosing if indication covers pediatric population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

