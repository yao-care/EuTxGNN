---
layout: default
title: Imiglucerase
parent: Medium Evidence (L3-L4)
nav_order: 303
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

> Imiglucerase is a recombinant human glucocerebrosidase used as enzyme replacement therapy (ERT), historically for Gaucher disease (the drug's structured `original_indications` field is empty — flagged as a data gap in this pack, not an absence of real-world use).
> The TxGNN model predicts it may be effective for **Hurler syndrome** (MPS I), with a **99.52% prediction score**, but only **0 clinical trials** and **2 general-review publications** support this direction — and the evidence pack's own analysis flags this as a likely **class-confusion false positive**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan regulatory data (drug not marketed in Taiwan); per the pack's evidence notes, imiglucerase's known use is Gaucher disease enzyme replacement therapy |
| Predicted New Indication | Hurler syndrome (Mucopolysaccharidosis type I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on information present elsewhere in the pack, imiglucerase is a recombinant form of human glucocerebrosidase, administered as enzyme replacement therapy (ERT) for Gaucher disease — a lysosomal storage disorder caused by glucocerebrosidase deficiency leading to glucocerebroside accumulation in macrophages.

Hurler syndrome, in contrast, is caused by deficiency of a completely different enzyme, alpha-L-iduronidase (IDUA), and its accumulated substrate (glycosaminoglycans) and pathway are unrelated to glucocerebrosidase. The standard ERT for Hurler syndrome is laronidase, not imiglucerase.

The evidence pack's own mechanistic assessment concludes that TxGNN's high score most likely reflects a **class-confusion effect**: the model's embedding space groups Gaucher disease and Hurler syndrome together under the broad category "lysosomal storage disease," inflating similarity without capturing that the two conditions involve distinct enzymes and substrates. The two supporting literature items are general reviews of ERT across lysosomal storage diseases as a class — neither specifically studies imiglucerase in Hurler syndrome patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | PNAS | General review of PET imaging for ERT effectiveness across lysosomal storage diseases (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); not specific to imiglucerase in Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT development history for lysosomal storage diseases, starting from imiglucerase's predecessor (alglucerase) for Gaucher disease; does not address Hurler syndrome specifically |

## Taiwan Market Information

Imiglucerase is not currently authorized or marketed in Taiwan (0 licenses on record), so no product/dosage-form/indication table is available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, there is no clinical trial evidence and no imiglucerase-specific literature for Hurler syndrome — only two general reviews of ERT as a drug class. The evidence pack's own mechanistic analysis identifies this as a probable class-confusion artifact, since Hurler syndrome (IDUA deficiency) and imiglucerase's target pathway (glucocerebrosidase deficiency in Gaucher disease) are mechanistically distinct.

**To proceed, the following is needed:**
- Preclinical or in vitro data testing imiglucerase specifically against alpha-L-iduronidase-pathway substrates, to confirm or rule out the class-confusion hypothesis
- Drug mechanism of action (MOA) documentation from DrugBank (data gap DG002)
- TFDA label warnings/contraindications (data gap DG001, currently blocking safety pre-screening)
- Correction of the `original_indications` data gap — the pack's own notes indicate imiglucerase's real original indication (Gaucher disease) is missing from structured fields, which should be fixed before further repurposing evaluation on this drug

*Note: within the same evidence pack, one other candidate for this drug ("lysosomal storage disease with skeletal involvement," rank 6) has strong evidence (L1, 2 clinical trials, 20 publications) — but that entry is essentially a re-confirmation of Gaucher disease itself (imiglucerase's known indication), not a genuinely new repurposing signal, and is not the subject of this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

