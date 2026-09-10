---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Epinephrine
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

# Epinephrine: From Anaphylaxis and Acute Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine is the classic first-line agent for anaphylaxis, cardiac arrest, and acute bronchospasm (this evidence pack does not itself document an EU-approved indication text, but this is standard, well-established pharmacology).
The TxGNN model predicts it may also be effective for **Obstructive Lung Disease**,
with **50 clinical trials** and **20 publications** returned by evidence search, including direct Phase 3 RCTs of epinephrine in bronchiolitis and asthma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (0 EU licenses on file). Based on established pharmacology: anaphylaxis, cardiac arrest, acute bronchospasm/asthma |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| EU Market Status | 未上市 (Not Marketed — per this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on known pharmacology, epinephrine is a non-selective adrenergic agonist acting on α1, β1, and β2 receptors. Its β2-agonist activity produces direct bronchial smooth muscle relaxation (bronchodilation), while α1-mediated vasoconstriction reduces airway mucosal edema — both mechanisms are directly relevant to obstructive airway pathophysiology.

Obstructive lung disease (encompassing asthma, COPD, and bronchiolitis in the evidence pool below) is mechanistically continuous with epinephrine's established emergency use in acute bronchospasm. Epinephrine (racemic or L-isomer, nebulized, inhaled, or systemic) has long been used off-label/adjunctively in acute severe asthma exacerbations and viral bronchiolitis in children, and an epinephrine metered-dose inhaler (e.g., Primatene Mist/E004 formulations) has historical and renewed OTC approval specifically for asthma in some markets.

This TxGNN prediction is therefore not a novel mechanistic leap but largely a formal recognition of an already-practiced clinical use pattern, which is reflected in the depth of clinical trial and systematic-review evidence retrieved below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Phase 3 | Completed | 864 | Inhaled epinephrine + oral dexamethasone vs. placebo in infant bronchiolitis in the ED; primary outcome hospitalization within 7 days |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Randomized, double-blind, placebo-controlled, crossover single-dose study of E004 epinephrine inhalation aerosol in children (4–11y) with asthma |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | Intramuscular epinephrine as adjunct to inhaled β2-agonists for severe pediatric asthma exacerbation |
| [NCT00619918](https://clinicaltrials.gov/study/NCT00619918) | Phase 2/3 | Completed | 447 | Nebulized hypertonic saline vs. standard therapy (including epinephrine/albuterol comparators) for viral bronchiolitis |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | NA | Unknown | 600 | RCT comparing nebulized epinephrine vs. albuterol for bronchiolitis |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Home oxygen therapy in bronchiolitis; nebulized treatment arm used 0.1% epinephrine diluted in bromhexine |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Pharmacokinetics and augmented-dose safety of Epinephrine Inhalation Aerosol USP (HFA-MDI, E004) |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | PK profile of proposed Epinephrine Inhalation Aerosol USP (E004) using deuterium-labeled epinephrine |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Phase 1/2 | Terminated | 21 | PK profile of E004 HFA-MDI epinephrine inhaler, complementing an earlier PK study |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | NA | Completed | 65 | Double-blind RCT: adrenaline inhalation vs. nasal decongestant drops for bronchiolitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review "Epinephrine for bronchiolitis" — evaluates bronchodilator effectiveness of epinephrine |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Earlier Cochrane review confirming modest short-term benefit of epinephrine in mild-moderate bronchiolitis |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Therapeutic strategies for pediatric bronchiolitis, focused on racemic epinephrine, steroids, hypertonic saline, HFOT |
| [19444115](https://pubmed.ncbi.nlm.nih.gov/19444115/) | 2009 | Review | Curr Opin Pediatr | Update on epinephrine (adrenaline) use across pediatric emergencies including respiratory indications |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clin Pharmacol Ther | Direct comparison of bronchodilator effects of terbutaline and epinephrine in obstructive lung disease |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Review | Annals of Allergy | "Nebulized bronchodilators in obstructive lung disease" — epinephrine among agents reviewed |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Bronchiolitis clinical evidence overview, including bronchodilator/epinephrine use |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | Bronchiolitis clinical evidence overview (earlier edition) |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Acute bronchiolitis and croup — evidence for nebulized adrenaline benefit |
| [11339733](https://pubmed.ncbi.nlm.nih.gov/11339733/) | 2001 | Systematic Review | Prehosp Emerg Care | Subcutaneous epinephrine in the prehospital setting for asthma/anaphylaxis in older patients |

---

## EU Market Information

Currently no EU marketing authorization records are available in this dataset for this DrugBank entry (`total_licenses: 0`). Given epinephrine's global ubiquity (autoinjectors, nebulizer solutions, inhalers), this most likely reflects a data-collection gap in this evidence pack rather than genuine absence from the EU market — this should be verified directly against EMA/national registries before final decision-making.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence quality is high (L1) — two completed Phase 3 RCTs testing epinephrine directly in bronchiolitis/asthma plus two Cochrane systematic reviews support a bronchodilator effect consistent with the "obstructive lung disease" prediction. However, TFDA/EMA label warnings (DG001, Blocking) and mechanism-of-action documentation (DG002, High) are missing from this pack, which blocks formal S1 safety sign-off.

**To proceed, the following is needed:**
- TFDA/EMA-approved product label (SmPC) with warnings, contraindications, and DDI data for epinephrine
- Confirmed DrugBank/literature-sourced mechanism of action (MOA) documentation
- Verification of actual EU marketing authorization status (the "0 licenses" result in this pack appears inconsistent with epinephrine's known global availability and should be reconciled)
- Route-of-administration compatibility assessment (nebulized/inhaled vs. IM/SC) specific to obstructive lung disease use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

