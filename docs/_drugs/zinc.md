---
layout: default
title: Zinc
parent: AI Predictions (L5)
nav_order: 659
evidence_level: L5
indication_count: 10
---

# Zinc
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

# Zinc: From Nutritional Supplementation to Filariasis

## One-Sentence Summary

Zinc (DrugBank ID DB01593) is an essential trace element with no single approved therapeutic indication on file in this dataset — it functions primarily as a nutritional/dietary supplement and enzymatic cofactor. The TxGNN model's top-ranked prediction links zinc to **Filariasis**, but this signal is currently supported only by AI prediction, with **1 clinical trial** and **20 publications** retrieved, none of which directly demonstrate antifilarial efficacy of zinc itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — zinc has no approved original indication on file (0 EU marketing licenses); included as an essential trace element/nutritional supplement |
| Predicted New Indication | Filariasis |
| TxGNN Prediction Score | 93.19% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for zinc is not available in this dataset, and no approved original indication is on file — zinc holds DrugBank ID DB01593 but has zero EU marketing authorizations. As an essential trace element, zinc is broadly known to act as a structural and catalytic cofactor for over 300 enzymes, and plays roles in immune function, wound healing, and epithelial/mucosal barrier integrity. These general biological properties are the basis on which TxGNN's knowledge-graph model draws associations to a wide range of diseases, including filariasis.

However, the retrieved evidence does not substantiate a specific mechanistic link between zinc and filariasis treatment. Per the evidence pack's own rationale: *"No clear mechanism supports a direct antiparasitic effect of zinc against filarial worms. The majority of the retrieved literature concerns zinc oxide nanoparticles used for mosquito vector control, or parasite molecular biology studies (e.g., zinc-dependent metalloenzymes in Setaria/Brugia species) that are unrelated to zinc as a therapeutic agent, and provide no direct evidence for zinc supplementation as a treatment for lymphatic filariasis."*

In short, the prediction score is driven by graph-level proximity (zinc's broad connectivity to enzyme/immune pathways) rather than by direct pharmacological or clinical evidence. This is a case where the AI signal and the underlying literature diverge materially, and it should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04695886](https://clinicaltrials.gov/study/NCT04695886) | N/A | Unknown | 6,440 | Community-delivered malaria elimination model trial in Myanmar; evaluates community health worker–based malaria services, not a zinc treatment intervention. Relevance graded **C** — weak/no direct link to filariasis or zinc therapy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40524903](https://pubmed.ncbi.nlm.nih.gov/40524903/) | 2025 | Review | Journal of Tropical Medicine | Systematic review of metal-based nanoparticles (including ZnO) against mosquito vectors of malaria, dengue, and filariasis — a vector-control, not a therapeutic, application |
| [40138337](https://pubmed.ncbi.nlm.nih.gov/40138337/) | 2025 | Cohort | PLoS One | Machine-learning study of nutritional predictors of lymphatic filariasis progression in Ghana; zinc not isolated as a specific factor |
| [29772240](https://pubmed.ncbi.nlm.nih.gov/29772240/) | 2018 | Preclinical | Biochem Biophys Res Commun | Characterization of a zinc finger protein in *Schistosoma japonicum* — parasite molecular biology, not a zinc treatment study |
| [40352769](https://pubmed.ncbi.nlm.nih.gov/40352769/) | 2025 | Preclinical | 3 Biotech | Green-synthesized ZnO nanoparticles evaluated for mosquito larvicidal/antibacterial activity — vector control application |
| [8522762](https://pubmed.ncbi.nlm.nih.gov/8522762/) | 1995 | Preclinical | Journal of Helminthology | Identifies a zinc-dependent cysteine proteinase as an allergen in the filarial parasite *Setaria digitata*; parasite biology, not zinc therapy |
| [30261054](https://pubmed.ncbi.nlm.nih.gov/30261054/) | 2018 | Preclinical | PLoS One | Characterization of *Wolbachia* Type IV secretion effectors in *Brugia malayi* — endosymbiont biology unrelated to zinc supplementation |
| [34666103](https://pubmed.ncbi.nlm.nih.gov/34666103/) | 2021 | Preclinical | Mol Biochem Parasitol | In-silico docking study targeting a *Wolbachia* (Brugia malayi) enzyme for novel antifilarial drug discovery — no zinc intervention tested |
| [18262499](https://pubmed.ncbi.nlm.nih.gov/18262499/) | 2008 | Preclinical | Acta Tropica | Characterizes a zinc-dependent metalloexopeptidase (leucine aminopeptidase) from the filarial parasite *Setaria cervi* — enzyme structure study, not treatment evidence |
| [19523248](https://pubmed.ncbi.nlm.nih.gov/19523248/) | 2009 | Preclinical | Parasitology | Characterizes a phosphatase from bovine filarial parasite *Setaria cervi* and its effect on eosinophil degranulation — parasite enzymology |
| [16870314](https://pubmed.ncbi.nlm.nih.gov/16870314/) | 2006 | Preclinical | Vaccine | Vaccination with a parasite-derived zinc-containing collagenase protects against *Brugia malayi* infection in jirds — a vaccine antigen study, not zinc supplementation |

**Note:** None of the retrieved literature is an RCT or directly tests zinc supplementation as a filariasis treatment. Most items describe zinc-containing parasite enzymes (as drug discovery targets) or zinc oxide nanoparticles for mosquito vector control — mechanistically distinct from zinc as a therapeutic agent.

---

## EU Market Information

Zinc (DB01593) currently has **no marketing authorization on file for the EU market** (0 licenses recorded in this dataset).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the supporting evidence base for filariasis is weak and largely off-target — dominated by zinc oxide nanoparticle vector-control studies and parasite enzyme characterization papers rather than any clinical or preclinical evidence of zinc's antifilarial therapeutic activity. This is classified as evidence level L5 (AI prediction only), and the evidence pack itself flags the mechanistic rationale as unsupported.

**To proceed, the following is needed:**
- Zinc's mechanism of action (MOA) data (currently a Data Gap, High severity)
- Regulatory safety label data — key warnings, contraindications, and TFDA/EMA SmPC information (currently a Blocking Data Gap; required before any Stage 1 safety review)
- Direct interventional evidence (preclinical or clinical) testing zinc supplementation specifically for filariasis prevention or treatment, rather than proxy studies on parasite zinc-dependent enzymes or ZnO nanoparticle vector control
- Given the stronger, more mechanistically coherent signals seen for other candidates in this evidence pack (e.g., dermatitis and enterocolitis, both rated L2/"Proceed with Guardrails"), consider re-prioritizing evaluation toward those indications rather than filariasis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

