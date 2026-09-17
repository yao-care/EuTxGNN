---
layout: default
title: Sebelipase Alfa
parent: AI Predictions (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase (LAL) enzyme replacement therapy, known from the evidence pack's own literature to be used for Lysosomal Acid Lipase Deficiency (Wolman disease / cholesteryl ester storage disease), though it is currently **not marketed** in this jurisdiction (0 licenses on file).
The TxGNN model's top-ranked prediction is **Scheie syndrome**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own mechanistic rationale states there is no biological overlap with the drug's known enzyme target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local registration data (0 licenses); literature in this pack indicates the drug's known global indication is Lysosomal Acid Lipase Deficiency (Wolman disease / CESD) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (Data Gap, High severity). Based on the literature contained in this evidence pack, sebelipase alfa is a recombinant human LAL enzyme that replaces the deficient lysosomal acid lipase activity in patients with LAL deficiency (LIPA gene defect), reducing lysosomal accumulation of cholesteryl esters and triglycerides in the liver and other tissues.

Scheie syndrome, by contrast, is the attenuated phenotype of Mucopolysaccharidosis type I (MPS I), caused by deficiency of α-L-iduronidase (IDUA), an entirely different lysosomal enzyme acting on a different substrate class (glycosaminoglycans, not cholesteryl esters/triglycerides). The model's own repurposing rationale explicitly states there is "no mechanistic overlap" between LAL and IDUA pathways, and that the association likely arises only because both conditions are broadly classified as lysosomal storage diseases in the knowledge graph embedding space — not from any shared molecular target.

Consequently, this specific prediction should be treated as an embedding-similarity artifact rather than a biologically grounded repurposing hypothesis. It is included in this report only because it is the top-ranked prediction in the evidence pack; the analysis below (Clinical Trial and Literature Evidence sections) confirms it has no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No marketing authorizations on record — the drug is currently not marketed in this jurisdiction (0 licenses).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Scheie syndrome) has zero clinical trial or literature evidence, and the model's own mechanistic rationale confirms there is no biological plausibility (LAL vs. IDUA are unrelated enzymes/substrates). Combined with missing MOA data and the drug's unmarketed status in this jurisdiction, there is no basis to advance this candidate beyond model-prediction-only status.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (Blocking data gap, DG001) before any safety assessment (S1) can begin
- Confirmed mechanism of action data via DrugBank API (High priority data gap, DG002)
- A biological plausibility review to formally exclude Scheie syndrome, or replace it with a mechanistically grounded candidate from this same prediction set
- **Pipeline note:** Ranks #4 (cholesteryl ester storage disease) and #5 (Wolman disease) in this prediction set are not novel repurposing candidates — they are the drug's already-established indication (LAL-D), each supported by a completed Phase 3 RCT (NCT01757184) and 15+ publications. This suggests the "known indication" filter did not trigger here (likely because `original_indications` is empty for this drug record) and should be corrected upstream before this candidate set is used for repurposing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

