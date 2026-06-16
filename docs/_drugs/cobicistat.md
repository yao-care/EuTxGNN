---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Cobicistat
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

# Cobicistat: From Adult HIV Treatment to Congenital HIV Management

## One-Sentence Summary

Cobicistat is a selective CYP3A inhibitor approved as a pharmacokinetic booster within HIV fixed-dose combination regimens (E/C/F/TAF and D/C/F/TAF), used to amplify plasma concentrations of co-administered antiretrovirals in adult HIV therapy.
TxGNN predicts it may contribute to the management of **Congenital Human Immunodeficiency Virus** — vertically acquired HIV infection in neonates and children — with **12 clinical trials** and **2 publications** currently supporting this direction, including multiple large-scale Phase 3 RCTs (Evidence Level: **L1**).

> TxGNN's rank #1 prediction was simian immunodeficiency virus infection (SIV, 99.92%), a non-human primate disease with no human clinical applicability. This report focuses on the most clinically actionable prediction: Rank #5 — Congenital HIV (98.33%, L1, Proceed with Guardrails).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV treatment (pharmacokinetic booster component in E/C/F/TAF and D/C/F/TAF regimens) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus |
| TxGNN Prediction Score | 98.33% (Rank #5; Rank #1 SIV is a non-human primate disease — clinically inapplicable) |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this report. Based on established clinical pharmacology, cobicistat is a mechanistic inhibitor of CYP3A4 and intestinal P-glycoprotein (P-gp) with no intrinsic antiretroviral activity of its own. Its sole clinical purpose is pharmacokinetic boosting: by blocking the metabolic enzymes that would otherwise rapidly eliminate co-administered drugs, cobicistat dramatically increases their plasma exposure — raising darunavir Cmin by approximately 10-fold and elvitegravir AUC by approximately 20-fold — thereby enabling effective once-daily dosing regimens.

Congenital HIV results from mother-to-child vertical transmission during pregnancy, delivery, or breastfeeding. Prevention depends critically on sustained maternal HIV RNA suppression throughout gestation. For infants and children who are already infected, cobicistat-containing fixed-dose combinations (particularly E/C/F/TAF [Genvoya] in adolescents ≥12 years) provide an effective single-tablet regimen option. Multiple Phase 3 RCTs — NCT02269917 (n=1,149) and NCT02431247 (n=725) — establish robust virological suppression data for D/C/F/TAF in adults, directly applicable to maternal HIV management to prevent vertical transmission. Dedicated Phase 2/3 data from NCT01854775 (n=129) specifically evaluated E/C/F/TAF in HIV-infected adolescents and children, bridging adult data to younger populations.

The key mechanistic caveat is that cobicistat's own pharmacokinetics change substantially during pregnancy: increased hepatic and intestinal metabolic activity in the second and third trimesters reduces cobicistat plasma levels, potentially compromising its boosting function and leading to subtherapeutic antiretroviral concentrations. This pregnancy-related PK vulnerability is the primary guardrail — not lack of efficacy. Current DHHS Perinatal HIV Guidelines advise against initiating cobicistat-boosted regimens in pregnant patients who are not already stably maintained on them; patients who conceive while virologically suppressed may continue with enhanced therapeutic drug monitoring.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | Randomized switch study: D/C/F/TAF vs boosted PI + FTC/TDF in virologically-suppressed HIV-1 patients; demonstrated non-inferiority in HIV-1 RNA suppression (<50 copies/mL) at Week 48 with improved renal and bone safety profile |
| [NCT02431247](https://clinicaltrials.gov/study/NCT02431247) | Phase 3 | Completed | 725 | Double-blind RCT: D/C/F/TAF vs DRV/COBI + FTC/TDF in treatment-naive HIV-1 adults; confirmed non-inferior virological efficacy, establishing cobicistat-boosted D/C/F/TAF as a first-line HIV treatment option |
| [NCT01854775](https://clinicaltrials.gov/study/NCT01854775) | Phase 2/3 | Completed | 129 | E/C/F/TAF PK, safety, and antiviral activity in HIV-1 infected treatment-naive adolescents (≥12 years) and virologically-suppressed children; confirmed dose selection and efficacy at Week 24, directly supporting cobicistat use in pediatric HIV populations |
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | Single-arm PK comparison of darunavir/ritonavir vs darunavir/cobicistat in HIV-1 infected pregnant women; key dataset for understanding cobicistat's pregnancy-related PK changes and their implications for vertical transmission prevention |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | Longitudinal ARV and anti-TB drug PK study across pregnancy trimesters and postpartum; provides cobicistat PK trajectory data critical for maternal HIV management strategy design |
| [NCT03577470](https://clinicaltrials.gov/study/NCT03577470) | N/A | Completed | 246 | DIAMANTE: Italian retrospective + prospective real-world observational study of D/C/F/TAF effectiveness (n=246); 48-week virological response data confirm real-world durability of cobicistat-boosted regimen |
| [NCT04442737](https://clinicaltrials.gov/study/NCT04442737) | Phase 4 | Completed | 103 | Switch to D/C/F/TAF in virologically-suppressed patients with rapid weight gain on INI+TAF/FTC regimens; safety and metabolic profile data with cobicistat-containing regimen at Week 48 |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A | Completed | 1,578 | IMPAACT P1026s: large-scale prospective PK study of ARV drugs in pregnant women and infants; includes cobicistat-containing regimens, directly informing perinatal HIV management and congenital HIV prevention strategies |
| [NCT03045861](https://clinicaltrials.gov/study/NCT03045861) | Phase 2 | Completed | 33 | Cobicistat-boosted GSK2838232 (novel HIV-1 maturation inhibitor) 10-day dose-ranging monotherapy; confirms cobicistat's expandable role as a PK booster for emerging HIV agents beyond darunavir and elvitegravir |
| [NCT02397096](https://clinicaltrials.gov/study/NCT02397096) | Phase 3 | Completed | 673 | Doravirine switch study from ritonavir/cobicistat-boosted PI regimens; cobicistat serves as background control, providing comparative safety and virological reference data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33048878](https://pubmed.ncbi.nlm.nih.gov/33048878/) | 2021 | Cohort | AIDS | Risk of birth defects and adverse perinatal outcomes in HIV-infected women exposed to integrase strand transfer inhibitors (INSTIs) at conception; contextualizes safety trade-offs when selecting between INSTI- vs cobicistat-boosted regimens for women of childbearing potential and pregnant patients |
| [35809963](https://pubmed.ncbi.nlm.nih.gov/35809963/) | 2022 | Case Report | Chest | 28-year-old man with congenital HIV presenting with diffuse bilateral pulmonary nodules and encephalopathy; illustrates long-term complications of vertically acquired HIV and the ongoing clinical need for effective, durable ARV regimen selection across the entire lifespan |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 RCTs establish robust virological suppression data for cobicistat-containing fixed-dose combinations (D/C/F/TAF, E/C/F/TAF) in adults — directly relevant to maternal HIV management for preventing vertical transmission — and Phase 2/3 data specifically support use in adolescents ≥12 years; the primary barrier to broader application in congenital HIV is cobicistat's own pregnancy-related PK vulnerability, not insufficient evidence of antiretroviral efficacy in the target population.

**To proceed, the following is needed:**
- Trimester-specific PK studies confirming adequate cobicistat boosting effect throughout pregnancy, with therapeutic drug monitoring protocols and defined viral load thresholds for regimen reassessment
- Weight-band–based pediatric dosing studies for children <12 years receiving cobicistat-boosted regimens
- Neonatal PK characterization of cobicistat and boosted antiretrovirals in HIV-exposed newborns
- Taiwan (TFDA) regulatory submission for cobicistat-containing fixed-dose combination products (currently 0 domestic authorizations)
- Safety monitoring plan addressing renal function, bone mineral density (especially in pediatric populations), extensive DDI screening given cobicistat's potent CYP3A4/P-gp inhibition, and trimester-specific viral load tracking during pregnancy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

