---
layout: default
title: Linaclotide
parent: Medium Evidence (L3-L4)
nav_order: 356
evidence_level: L3
indication_count: 10
---

# Linaclotide
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Linaclotide: From Constipation-Type Bowel Disorders to Large Intestine Disease

## Methodological Note

TxGNN scored 10 candidate indications for linaclotide. The top-ranked hits by raw score (cauda equina syndrome, obsolete neurogenic bladder, insomnia, mitral valve prolapse variants, rhinitis) were explicitly flagged in the evidence pack as **statistical artifacts with no plausible mechanism** — the pack itself labels them "predictive noise" (score 0.95–0.9996 despite zero mechanistic or evidentiary support). The only candidate that survived to evidence stage S2 with a "Proceed with Guardrails" call is **large intestine disease** (rank 9, score 95.14%), supported by 8 literature items including drug-specific and mechanistic studies. This report focuses on that candidate rather than the nominally top-ranked one, since reporting the top score without this context would be misleading.

---

## One-Sentence Summary

Linaclotide (DrugBank DB08890) is a minimally-absorbed guanylate cyclase-C (GC-C) agonist used internationally for constipation-predominant bowel disorders (IBS-C/CIC per the cited literature); it currently holds **no marketing authorization in this jurisdiction** (0 licenses, not marketed). The TxGNN model's only credibly-supported new signal points to broader **Large Intestine Disease**, backed by **8 publications** (no clinical trials) — largely mechanistic/preclinical rather than direct clinical evidence in this specific disease framing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local regulatory data (no licenses on file). Per cited literature, linaclotide is approved elsewhere for constipation-predominant IBS (IBS-C) and chronic idiopathic constipation (CIC). |
| Predicted New Indication | Large Intestine Disease |
| TxGNN Prediction Score | 95.14% (rank 9 of candidates) |
| Evidence Level | L3 |
| Market Status (local regulatory data) | Not marketed / Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action record exists in the drug-level fields (marked as a High-severity data gap, DG002). However, the evidence pack's literature-derived rationale is clear: linaclotide is a **guanylate cyclase-C (GC-C) receptor agonist** acting on intestinal epithelial apical receptors, increasing intracellular and extracellular cGMP. This drives chloride/bicarbonate secretion and accelerates intestinal transit, and separately reduces colonic nociceptor sensitization to relieve visceral pain (PMID 23958540).

"Large intestine disease" as a TxGNN-predicted category overlaps substantially with linaclotide's already-established pharmacology in IBS-C and chronic idiopathic constipation — this is best understood as an **adjacent extension of known activity**, not a mechanistically novel repurposing. Preclinical work also shows chronic linaclotide can reverse colitis-induced bladder and neuroplastic changes (PMID 30282832) and that GC-C/cGMP signaling is implicated in colitis and dysbiosis models (PMID 34546338), suggesting the drug's colonic action may extend to inflammatory large-bowel states beyond simple constipation. No data currently link linaclotide's local, non-absorbed GI action to any of the other 9 TxGNN-flagged candidates (autonomic nervous system disease has an indirect literature echo; the remainder — cauda equina syndrome, neurogenic bladder, insomnia, mitral valve prolapse/MVP1, gastroduodenitis, rhinitis — lack any mechanistic plausibility per the evidence pack's own assessment).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23464519](https://pubmed.ncbi.nlm.nih.gov/23464519/) | 2013 | Review (drug-specific) | Future Medicinal Chemistry | Overview of linaclotide's approval (Constella™/Linzess™) and clinical/biological profile for IBS-C and CIC |
| [23958540](https://pubmed.ncbi.nlm.nih.gov/23958540/) | 2013 | Preclinical (mechanistic, animal) | Gastroenterology | Linaclotide inhibits colonic nociceptors and relieves abdominal pain via GC-C/extracellular cGMP |
| [30282832](https://pubmed.ncbi.nlm.nih.gov/30282832/) | 2018 | Preclinical (animal) | JCI Insight | Chronic linaclotide reduces colitis-induced neuroplasticity and reverses persistent bladder dysfunction (gut-bladder axis) |
| [38923030](https://pubmed.ncbi.nlm.nih.gov/38923030/) | 2024 | Review | Alimentary Pharmacology & Therapeutics | Management approaches for refractory constipation in children |
| [34546338](https://pubmed.ncbi.nlm.nih.gov/34546338/) | 2021 | Preclinical (mouse model) | Journal of Experimental Medicine | Gut-associated cGMP mediates colitis and dysbiosis in a GUCY2C activating-mutation mouse model |
| [33849828](https://pubmed.ncbi.nlm.nih.gov/33849828/) | 2021 | Preclinical (rat model) | J. Southern Medical University | Changes in GC-C in colon tissue of rats with pancreatitis-associated intestinal injury |
| [23748116](https://pubmed.ncbi.nlm.nih.gov/23748116/) | 2013 | Review (mechanistic) | Pain | Uroguanylin/GC-C/cGMP pathway and visceral hypersensitivity in inflammation/stress models |
| [33751780](https://pubmed.ncbi.nlm.nih.gov/33751780/) | 2021 | Review | Neurogastroenterology and Motility | Pharmacology and clinical evidence for bisacodyl in constipation (comparator laxative context, not linaclotide-specific) |

**Note:** none of the above are randomized controlled trials of linaclotide specifically in "large intestine disease" as a standalone entity; they are mechanistic/preclinical studies plus one drug-specific pharmacology review, consistent with the assigned L3 evidence level.

---

## Market Information

Linaclotide currently holds **no marketing authorization on file** in this jurisdiction (market status: Not marketed; 0 licenses recorded). No dosage form or approved-indication text is available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data are currently on file (DDI query returned no results; a Blocking-severity data gap, DG001, notes that the local regulatory label has not yet been obtained/parsed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate indication with real (if indirect, preclinical-weighted) evidentiary support — Large Intestine Disease — reaches L3/S2 ("Proceed with Guardrails") on scientific grounds alone. However, a **Blocking** data gap (DG001: no local product label/warnings on file) currently prevents any safety initial assessment, and the drug has **zero marketing authorizations** in this jurisdiction, meaning there is no established local safety or regulatory foothold to build on. Until that gap is closed, no Go decision can responsibly be made regardless of the mechanistic plausibility.

**To proceed, the following is needed:**
- Obtain and parse the official product label/SmPC (warnings, contraindications) to resolve DG001 — required to even enter safety-stage (S1) review
- Formal mechanism-of-action documentation to close DG002, beyond the literature-inferred GC-C/cGMP pathway summarized above
- If pursuing the Large Intestine Disease signal specifically: clarify how it differs from linaclotide's already-marketed indications elsewhere (IBS-C/CIC), since this may be a market-access question rather than a genuine new-indication research question
- Given the other 9 TxGNN candidates lack any supporting evidence, no further action is recommended on those unless new clinical or mechanistic data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

