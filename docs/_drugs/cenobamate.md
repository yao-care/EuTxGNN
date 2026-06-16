---
layout: default
title: Cenobamate
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Cenobamate
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

# Cenobamate: From Focal Seizures to Status Epilepticus

## One-Sentence Summary

Cenobamate (Xcopri®/Ontozry®) is a third-generation antiseizure medication with a novel dual mechanism, approved in the US (2019) and EU (2021) for adjunctive treatment of focal seizures in adults, but not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Status Epilepticus** (ranked #2, score 97.48%), with mechanistic plausibility grounded in its unique ability to modulate GABA-A receptors at a non-benzodiazepine site — directly addressing the receptor internalization that renders standard treatment ineffective in refractory SE.
This direction is currently supported by **1 early-phase clinical trial** (CENOBITE, NCT06352723) and **12 publications** including case series documenting off-label use in super-refractory SE.

> **⚠️ Prediction ranking note:** The highest-ranked TxGNN prediction (#1, score 97.83%) is Guanidinoacetate Methyltransferase Deficiency — a metabolic disorder where cenobamate may symptomatically address secondary epilepsy but has no effect on the underlying enzymatic defect, and carries a **Hold** recommendation with zero supporting clinical evidence. This report focuses on **Status Epilepticus** (#2), which presents the strongest clinical rationale and actionable evidence among all predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal seizures in adults (adjunctive; FDA-approved 2019, EMA-approved 2021; not registered in Taiwan) |
| Predicted New Indication | Status Epilepticus |
| TxGNN Prediction Score | 97.48% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cenobamate operates through a dual mechanism that is pharmacologically distinct from all other approved antiseizure medications. It preferentially inhibits the **persistent sodium current (INaP)** of voltage-gated sodium channels — the component responsible for sustained repetitive neuronal firing — while simultaneously acting as a **positive allosteric modulator (PAM) of GABA-A receptors at a non-benzodiazepine binding site**, enhancing inhibitory neurotransmission through a pathway that is independent of standard benzodiazepine targets. This combination is not incidental; it directly addresses two independent drivers of pathological neuronal excitability.

Status epilepticus (SE) is fundamentally defined by the failure of seizure self-termination, and the transition to benzodiazepine-resistant SE is driven at the molecular level by rapid **endocytosis of γ₂-subunit-containing synaptic GABA-A receptors** — precisely the receptor population that benzodiazepines require. Because cenobamate's GABA-A PAM activity acts at a distinct binding site (likely δ-subunit, expressed in extrasynaptic receptors that are not subject to the same trafficking), it is theoretically positioned to retain efficacy even when the benzodiazepine pathway has collapsed. INaP blockade provides an orthogonal mechanism against the sustained depolarization that maintains seizure activity. Together, these two mechanisms map onto both core molecular events of established SE — a pharmacological convergence that is rare among available agents.

This rationale has attracted clinical attention. The CENOBITE study (NCT06352723), initiated by the Critical Care EEG Monitoring Consortium, targets cenobamate specifically in ICU patients with acute seizure clusters and status epilepticus. Published case series (2023) document safe administration in super-refractory SE (SRSE) with controlled titration, and a 2025 safety correspondence provides early real-world clinical observations. The fact that academic critical care epileptologists have independently converged on this research question lends external validity to the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06352723](https://clinicaltrials.gov/study/NCT06352723) | Early Phase 1 | Not Yet Recruiting | 10 | **CENOBITE Study**: Multi-center ICU trial through the Critical Care EEG Monitoring Consortium (CCEMRC). Evaluates cenobamate for acute frequent seizures and status epilepticus under continuous EEG monitoring. Includes super-refractory SE (SRSE) subgroup. Safety and feasibility primary focus. Expected completion: June 2025. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37064924](https://pubmed.ncbi.nlm.nih.gov/37064924/) | 2023 | Case Series | The Neurohospitalist | Two SRSE cases treated safely with cenobamate as add-on therapy; slow up-titration protocol used to mitigate hypersensitivity risk; proof-of-concept for ICU neurological use |
| [39060539](https://pubmed.ncbi.nlm.nih.gov/39060539/) | 2025 | Safety Commentary | Neurological Sciences | Early safety observations from Italian neurological centers on cenobamate use in SE; practical guidance for critically ill patients |
| [36929735](https://pubmed.ncbi.nlm.nih.gov/36929735/) | 2023 | Narrative Review | Epilepsia Open | Comprehensive review of SE pharmacology — presynaptic, postsynaptic, and extrasynaptic mechanisms; frames mechanism-based ASM selection and contextualizes cenobamate's mechanistic positioning |
| [37458794](https://pubmed.ncbi.nlm.nih.gov/37458794/) | 2023 | Review | Journal of Neurology | Advances in epilepsy treatment; cenobamate highlighted as a third-generation ASM with broad-spectrum anticonvulsant activity |
| [40292823](https://pubmed.ncbi.nlm.nih.gov/40292823/) | 2025 | Retrospective Case Series | Epilepsia | ⚠️ **Safety signal**: Lack of effectiveness and seizure worsening in 6 pediatric Dravet syndrome (SCN1A loss-of-function) patients — highlights the need for genetic subgroup exclusion criteria in SE trials |
| [39388362](https://pubmed.ncbi.nlm.nih.gov/39388362/) | 2024 | Case Series | Epilepsia Open | Cenobamate add-on in Rasmussen's encephalitis (highly pharmacoresistant progressive epilepsy); informative model for pharmacoresistant SE populations |
| [40383002](https://pubmed.ncbi.nlm.nih.gov/40383002/) | 2025 | Observational Study | Epilepsy & Behavior | Single tertiary-center real-world experience; seizure-freedom rates at one year of cenobamate therapy |
| [41007820](https://pubmed.ncbi.nlm.nih.gov/41007820/) | 2025 | Review | Biomedicines | Potential for disease-modifying therapy in epilepsy; cenobamate discussed in context of reducing seizure burden and neuronal injury |
| [40763422](https://pubmed.ncbi.nlm.nih.gov/40763422/) | 2025 | Retrospective Cohort | Seizure | Italian multicenter study evaluating novel treatments in adults with severe epileptic phenotypes due to SSADHD |
| [39267763](https://pubmed.ncbi.nlm.nih.gov/39267763/) | 2024 | Case Report | Frontiers in Immunology | Drug-resistant epilepsy in seronegative limbic encephalitis; cenobamate included in management of refractory seizures in acute encephalitis — a clinically adjacent scenario to SE |

---

## Taiwan Market Information

Cenobamate is **not currently approved or marketed in Taiwan**. There are no TFDA-authorized products and no health insurance reimbursement listing.

For clinical reference, cenobamate is available globally under the following authorizations:

| Product Name | Region | Regulatory Body | Approved Indication | Approval Date |
|------|------|------|------|------|
| Xcopri® | United States | FDA | Adjunctive treatment of focal seizures in adults | November 2019 |
| Ontozry® | European Union | EMA | Adjunctive treatment of focal seizures in adults | March 2021 |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> ⚠️ **Key risk flagged from literature:** Three cases of **DRESS** (Drug Reaction with Eosinophilia and Systemic Symptoms) occurred during cenobamate clinical development, requiring implementation of a mandatory slow-titration protocol (start: 12.5 mg/day; target dose: 200 mg/day reached over months). In the acute SE/ICU context, where clinical urgency may pressure clinicians toward faster escalation, this represents a critical risk-benefit tension that any SE-specific protocol must explicitly address. Clinicians should review the DRESS mitigation strategy published in the Phase 3 open-label safety study (PMID 32396252) before any off-label SE use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cenobamate's dual mechanism — GABA-A PAM at a non-benzodiazepine site and persistent sodium channel blockade — maps directly onto the two molecular drivers of benzodiazepine-resistant status epilepticus, providing one of the strongest mechanistic arguments for any currently investigated SE candidate. The independent initiation of a dedicated clinical trial (CENOBITE, NCT06352723) by a leading academic critical care EEG consortium, combined with published case series confirming safe use in SRSE, justifies cautious forward movement.

**To proceed, the following is needed:**

- **CENOBITE trial results** (NCT06352723, target completion June 2025): the most critical near-term data point — primary safety and feasibility outcomes in ICU SE patients
- **TFDA SmPC / safety data resolution** (DG001): obtain and parse the cenobamate package insert to address Taiwan-specific warnings, contraindications, and DRESS management — currently a blocking gap for formal S1 safety evaluation
- **MOA documentation** (DG002): confirm the specific GABA-A receptor subunit selectivity (δ vs. γ) and INaP inhibition profile for mechanism-focused regulatory and scientific communication
- **SE-specific dosing protocol**: define a clinically feasible titration schedule that balances DRESS risk against the therapeutic urgency of refractory SE
- **Patient exclusion criteria**: pre-specify genetic epilepsy exclusions (especially SCN1A-related disorders) based on the Dravet safety signal (PMID 40292823) before any Taiwan pilot use
- **TFDA regulatory pathway assessment**: evaluate whether the existing US/EU approval for focal seizures can support an expedited NDA filing, and determine whether SE indication requires a separate clinical dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

