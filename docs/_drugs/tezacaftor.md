---
layout: default
title: Tezacaftor
parent: AI Predictions (L5)
nav_order: 585
evidence_level: L5
indication_count: 10
---

# Tezacaftor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

> Tezacaftor is a CFTR corrector believed to be used in the treatment of cystic fibrosis, acting on chloride channel protein folding.
> The TxGNN model's top-ranked prediction suggests possible relevance to **HIV Infectious Disease**,
> but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly states there is no known biological plausibility for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic Fibrosis (inferred from CFTR corrector mechanism referenced throughout the evidence pack; not confirmed via a formal regulatory license record) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available — this is flagged as a High-severity data gap in the evidence pack. Based on the contextual information available (repeated references to "CFTR corrector" and "cystic fibrosis patients" across the prediction rationales and the one associated clinical trial), Tezacaftor appears to work by correcting the folding and trafficking of the CFTR chloride channel protein.

For the top-ranked prediction, HIV Infectious Disease, the evidence pack's own mechanistic assessment states there is **no known biological connection**: "Tezacaftor is a CFTR corrector acting on chloride channel folding correction; there is no known relationship to the HIV replication cycle or host immune mechanisms — this is a knowledge-graph embedding similarity inference without biological plausibility." This prediction should be interpreted as a statistical artifact of the knowledge graph rather than a genuine repurposing signal.

This pattern extends across the full top-10 prediction list: nearly all candidates (leprosy, multiple endocrine neoplasia, female breast carcinoma, homozygous familial hypercholesterolemia, amyotrophic lateral sclerosis) are noted as having no known mechanistic link to CFTR correction, and two entries (simian immunodeficiency virus infection, feline acquired immunodeficiency syndrome) are non-human/veterinary disease models with no clinical translation value. The one partial exception is rank 7, rheumatoid arthritis (L4), where CFTR dysfunction has a theoretical, indirect connection to neutrophil-driven inflammation — though the only supporting trial is a descriptive neutrophil-phenotyping study in cystic fibrosis patients, not a test of tezacaftor's efficacy in RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV Infectious Disease (the top-ranked predicted indication).

*Note: One low-relevance (Grade C) trial exists for a lower-ranked candidate — see rank 7, rheumatoid arthritis, below.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | NA | Completed | 47 | Descriptive study of blood neutrophil function/phenotype in cystic fibrosis patients, including effects of CFTR modulator treatment and *Pseudomonas aeruginosa* infection. Provides indirect immune-mechanism background but does not test tezacaftor efficacy in rheumatoid arthritis. |

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations are recorded for this drug in the evidence pack (market status: Not Marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (HIV Infectious Disease, 99.24% score) is an L5 pure AI prediction with no clinical trials, no literature, and the evidence pack's own analysis explicitly states there is no known mechanistic plausibility.
- The drug is not currently marketed in the region, and a Blocking-severity data gap (missing label warnings/contraindications) prevents any formal safety review (S1 stage) from being initiated.

**To proceed, the following is needed:**
- Regulatory label (SmPC) warnings and contraindications — currently a Blocking data gap
- Confirmed mechanism of action data — currently a High-severity data gap
- If further repurposing evaluation is pursued, prioritize the rank 7 candidate (rheumatoid arthritis, L4 evidence, indirect CFTR–neutrophil inflammation rationale) over the top-ranked HIV signal, since it carries relatively stronger mechanistic and evidentiary support despite still requiring dedicated clinical validation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

