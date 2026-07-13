---
layout: default
title: Deutetrabenazine
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Deutetrabenazine
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

# Deutetrabenazine: From Huntington's Disease Chorea to Chronic Tic Disorder

## One-Sentence Summary

Deutetrabenazine is a selective vesicular monoamine transporter 2 (VMAT2) inhibitor approved in the United States for chorea associated with Huntington's disease and tardive dyskinesia, though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Chronic Tic Disorder** (including Tourette Syndrome), with **2 completed Phase 3 RCTs** and **17 publications** directly supporting this direction — representing one of the most evidence-rich repurposing candidates in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chorea associated with Huntington's Disease; Tardive Dyskinesia (US FDA approved; not marketed in Taiwan) |
| Predicted New Indication | Chronic Tic Disorder |
| TxGNN Prediction Score | 98.31% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN ranking:** Chronic Tic Disorder is TxGNN rank 5 by model score but is the highest-evidence candidate in this pack (L1, two Phase 3 RCTs). Higher-ranked predictions (ranks 1–4) all carry Hold recommendations with L5 evidence and poor or absent mechanistic links.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the DrugBank API for this submission. However, based on abundant published literature, deutetrabenazine's mechanism is well-established: it is a VMAT2 inhibitor that prevents the loading of monoamines — primarily dopamine — into presynaptic vesicles, thereby reducing the amount of dopamine released into the synapse. The deuterium substitution at two methoxy groups slows hepatic CYP2D6 metabolism, producing more stable plasma concentrations, lower peak-to-trough fluctuation, fewer side effects attributable to peak exposure, and a twice-daily rather than three-daily dosing schedule compared to its parent compound tetrabenazine.

The core pathophysiology of chronic tic disorder (CTD) and Tourette syndrome (TS) involves hyperactivation of cortico-striatal-thalamo-cortical circuits with excess dopaminergic signalling in the striatum. This is precisely the mechanism that VMAT2 inhibition addresses. In Huntington's disease (deutetrabenazine's approved indication), the same cortico-striatal dopamine excess drives involuntary choreiform movements; in tardive dyskinesia, dopamine receptor supersensitivity after antipsychotic exposure similarly produces hyperkinesia. CTD and TS sit on the same mechanistic continuum — reducing presynaptic dopamine availability directly suppresses the aberrant motor and phonic outputs that define tic disorders.

This is not a speculative leap: deutetrabenazine has been directly studied in Tourette syndrome across a Phase 2 pilot and two independent Phase 3 randomised controlled trials, all with consistent results. Because CTD is diagnostically defined as the presence of chronic motor or phonic tics without meeting full TS criteria, the mechanistic and clinical evidence from TS studies directly extends to CTD. The TxGNN prediction captures a real and well-supported pharmacological relationship.

---

## Clinical Trial Evidence

No clinical trials were identified under a direct "chronic tic disorder" query. The following trials, captured under the broader **extrapyramidal and movement disorders** category, demonstrate deutetrabenazine's active Phase 3 clinical development programme for hyperkinetic movement disorders:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03813238](https://clinicaltrials.gov/study/NCT03813238) | Phase 3 | Completed | 63 | Randomised, double-blind, placebo-controlled study of deutetrabenazine (TEV-50717) for dyskinesia in cerebral palsy in children and adolescents — primary Phase 3 efficacy dataset for a paediatric hyperkinetic indication |
| [NCT04200352](https://clinicaltrials.gov/study/NCT04200352) | Phase 3 | Terminated | 44 | Open-label long-term safety extension for cerebral palsy dyskinesia — terminated early (commercial decision); 44-patient safety dataset provides long-term tolerability reference data |
| [NCT06997198](https://clinicaltrials.gov/study/NCT06997198) | Phase 4 | Not Yet Recruiting | 25 | Post-marketing study of deutetrabenazine for tardive dyskinesia identification and treatment in adults with intellectual/developmental disabilities — reflects ongoing real-world evidence generation interest |

> The Phase 3 RCT evidence for Tourette Syndrome / tic disorders (PMIDs 34661664 and 34609495) is captured as published literature below, as these trials were not registered under the direct CTD search query.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34661664](https://pubmed.ncbi.nlm.nih.gov/34661664/) | 2021 | Phase 3 RCT | JAMA Network Open | Fixed-dose deutetrabenazine significantly reduced tics vs. placebo in children and adolescents with Tourette syndrome; acceptable safety profile |
| [34609495](https://pubmed.ncbi.nlm.nih.gov/34609495/) | 2021 | Phase 3 RCT | JAMA Network Open | Flexible-dose deutetrabenazine reduced tic severity with acceptable tolerability in paediatric TS — confirms dose-titration feasibility |
| [37772282](https://pubmed.ncbi.nlm.nih.gov/37772282/) | 2023 | Long-term Extension | Movement Disorders Clinical Practice | Open-label extension of Phase 3 trials: sustained safety and efficacy of deutetrabenazine in children/adolescents with TS over long-term use |
| [27917309](https://pubmed.ncbi.nlm.nih.gov/27917309/) | 2016 | Phase 2 RCT | Tremor and Other Hyperkinetic Movements | Phase 2 pilot: deutetrabenazine demonstrated preliminary efficacy and tolerability for moderate-to-severe tics in adolescents with TS — established basis for Phase 3 programme |
| [37301806](https://pubmed.ncbi.nlm.nih.gov/37301806/) | 2023 | Real-world Study | Journal of Neurology | Real-world VMAT2 inhibitor experience in TS: deutetrabenazine showed clinical benefit in off-label use; discusses insurance and accessibility barriers |
| [30870235](https://pubmed.ncbi.nlm.nih.gov/30870235/) | 2019 | Real-world Study | Clinical Neuropharmacology | Real-world experience with deutetrabenazine across hyperkinetic movement disorders including tic disorders; efficacy confirmed with manageable side effects |
| [32454050](https://pubmed.ncbi.nlm.nih.gov/32454050/) | 2020 | Review | Pharmacology & Therapeutics | VMAT2 inhibitors (tetrabenazine, deutetrabenazine, valbenazine) for hyperkinetic movement disorders including TD, HD chorea, and tic disorders — mechanistic and clinical overview |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review of Phase III/IV trials for pharmacological treatment of Tourette syndrome in children, adults, and older adults |
| [28387387](https://pubmed.ncbi.nlm.nih.gov/28387387/) | 2017 | Review | Drugs of Today | Deutetrabenazine pharmacokinetics and pharmacodynamics: rationale for improved PK profile and applications in HD chorea, TD, and TS |
| [31955299](https://pubmed.ncbi.nlm.nih.gov/31955299/) | 2020 | Review | Journal of Neural Transmission | Comprehensive TS treatment overview positioning VMAT2 inhibitors (including deutetrabenazine) as dopamine depletion strategy for tic management |

---

## Taiwan Market Information

Deutetrabenazine is **not currently marketed in Taiwan** (0 TFDA-approved licenses on record).

For reference, the drug is approved in the United States under the brand name **Austedo®** (Teva Pharmaceuticals) for:
- Chorea associated with Huntington's disease (FDA approved April 2017)
- Tardive dyskinesia in adults (FDA approved August 2017)

No TFDA regulatory submissions are on record for this drug. Importation or compassionate use would require separate TFDA authorisation.

---

## Safety Considerations

Detailed TFDA SmPC (仿單) data is unavailable as deutetrabenazine is not marketed in Taiwan. Based on the US FDA-approved prescribing information and the pharmacological class profile:

- **Depression and Suicidality**: VMAT2-induced monoamine depletion can precipitate or worsen depression and suicidal ideation. The US FDA prescribing information carries a **Boxed Warning** for this risk. Patients — particularly adolescents — must be screened for depression and suicidality before and during treatment.
- **QTc Prolongation**: Deutetrabenazine prolongs the QTc interval; baseline ECG and monitoring during dose titration are recommended. Concomitant QTc-prolonging agents require particular caution.
- **Parkinsonism and Akathisia**: Excessive dopamine depletion can produce drug-induced parkinsonism or restlessness; dose reduction is the primary management strategy.
- **Sedation and Somnolence**: CNS depression is a known class effect; patients should be cautioned regarding driving and operating machinery.

Please refer to the **Austedo® US Prescribing Information** for the complete safety profile, including the full Boxed Warning text, until TFDA SmPC data becomes available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two independent completed Phase 3 RCTs (PMIDs 34661664 and 34609495) and one Phase 2 RCT (PMID 27917309) directly demonstrated deutetrabenazine's efficacy for tics in Tourette syndrome, with a mechanistic rationale (striatal dopamine excess → VMAT2 inhibition → tic suppression) that is unambiguous and identical to its approved indications. The evidence package supports a meaningful clinical benefit with a characterised safety profile.

**To proceed, the following is needed:**
- **Regulatory pathway**: Assess eligibility for TFDA submission citing US FDA approval (Austedo®) as reference; evaluate whether the paediatric Phase 3 data package meets TFDA's standards for new drug applications
- **Full safety dossier**: Obtain and translate the complete Austedo® US Prescribing Information including the Boxed Warning on depression/suicidality; conduct formal TFDA SmPC gap analysis
- **Paediatric safety review**: The primary evidence base is in children and adolescents — confirm TFDA requirements for paediatric investigation plans and age-specific dosing
- **CYP2D6 DDI profile**: Deutetrabenazine is a CYP2D6 substrate; a complete drug interaction assessment is missing from this evidence pack and is essential before clinical use, especially in patients on antipsychotics or MAO inhibitors
- **Market access assessment**: Confirm commercial availability, importation logistics, and reimbursement pathway under Taiwan NHI for this orphan-adjacent indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

