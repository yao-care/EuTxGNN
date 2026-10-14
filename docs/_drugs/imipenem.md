---
layout: default
title: Imipenem
parent: AI Predictions (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: From Hospital-Acquired Pneumonia and Resistant Gram-Negative Infections to Diffuse Scleroderma

The prompt template uses the first-ranked prediction (diffuse scleroderma). That prediction has no supporting evidence. Because the rank 1 prediction is only a model output, the report also points to the better-supported candidates (typhoid fever and *Staphylococcus aureus* infection) in the sections below.

## One-Sentence Summary

Imipenem is a carbapenem antibiotic, originally used (as part of Recarbrio) for hospital-acquired pneumonia, bacteraemia and infections caused by aerobic Gram-negative organisms in adults with limited treatment options.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
Among the other predictions, typhoid fever and *Staphylococcus aureus* infection have the most relevant evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hospital-acquired pneumonia (including ventilator-associated pneumonia), associated bacteraemia, and infections due to aerobic Gram-negative organisms in adults with limited treatment options |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | ✗ Cancelled only |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, imipenem is a carbapenem antibacterial that inhibits bacterial cell wall synthesis, and its efficacy in serious Gram-negative infections is established.

For diffuse scleroderma, however, no plausible mechanistic link exists. Scleroderma is an autoimmune fibrotic disease, while imipenem acts on bacterial targets. The very high TxGNN score (99.99%) reflects a model prediction only, and no trials or literature support it. This prediction should be treated as a likely artefact rather than a real repurposing opportunity.

The more credible directions among the other predictions are:

- **Typhoid fever (L4):** Carbapenems are used as a last-line option for extensively drug-resistant (XDR) typhoid, where resistance to fluoroquinolones and third-generation cephalosporins limits alternatives. This is the strongest biological and practical rationale. Evidence is observational or surveillance-based, with no controlled imipenem trials.
- **Paratyphoid fever and salmonellosis (L4):** Imipenem is active against Enterobacterales including *Salmonella*, but the evidence is limited to susceptibility and resistance surveys.
- ***Staphylococcus aureus* infection (L3):** Imipenem alone has little activity against MRSA, but combinations (for example with fosfomycin) show synergy in vitro and in small clinical series.
- **Sinusitis, chronic rhinosinusitis, chronic ethmoidal sinusitis (L4–L5):** Imipenem has a broad spectrum, but these conditions are usually managed with narrower agents, and no imipenem-specific clinical evidence was found.
- **Paranasal sinus neoplasm and eosinophilia-myalgia syndrome (L5):** No plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered for diffuse scleroderma.

For reference, the only trials found among the predicted indications relate to *Staphylococcus aureus* infection (rank 9):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | Completed | 50 | Fosfomycin plus imipenem versus vancomycin for MRSA infective endocarditis |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone or combined with a carbapenem against MRSA in ventilator-associated pneumonia (carbapenem not necessarily imipenem) |

## Literature Evidence

Currently no related literature available for diffuse scleroderma.

For reference, the most relevant publications among the other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Cohort | Cureus | Carbapenems as the final line of defence in MDR/XDR typhoid fever in Peshawar |
| [36277244](https://pubmed.ncbi.nlm.nih.gov/36277244/) | 2022 | Observational | Infect Drug Resist | Single versus combination therapy in XDR *Salmonella* Typhi in Pakistan |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical study | Antimicrob Agents Chemother | Imipenem-cilastatin in 23 patients with MSSA and MRSA infections |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case commentary | Antimicrob Agents Chemother | Imipenem/cilastatin plus fosfomycin for refractory MRSA infection |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Case report and review | J Med Liban | Rhabdomyolysis in *Salmonella* Typhi infection successfully treated with imipenem/cilastatin |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | In vitro | J Med Microbiol | MIC of carbapenems and tigecycline against 210 *Salmonella* isolates |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004808 (cancelled) | Recarbrio | Not specified | Recarbrio is indicated for:- Treatment of hospital-acquired pneumonia (HAP), including ventilator associated pneumonia (VAP), in adults (see sections 4.4 and 5.1).... |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** epilepsy, kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions:** 15 interactions were identified. Major interactions: bupropion, iohexol, iopamidol. Moderate interactions include warfarin, dicoumarol, theophylline and other xanthines (aminophylline, dyphylline, oxtriphylline), cyclosporine, mycophenolic acid, ethinylestradiol, pemetrexed, lindane and polyethylene glycol (3350 with electrolytes).

Please refer to the SmPC for the approved warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diffuse scleroderma) has no mechanistic rationale, no trials and no literature, so it is supported by the model score alone. The EU authorization is also cancelled. Among the other predictions, typhoid fever (XDR cases) and *S. aureus* combination therapy are the most plausible research questions, but the evidence is observational or small-scale.

**To proceed, the following is needed:**
- Mechanism of action data for imipenem
- Package insert warnings and contraindications (SmPC), required before safety screening
- For typhoid fever: prospective or comparative clinical data on imipenem in MDR/XDR cases
- For *S. aureus*: confirmatory randomized data on imipenem-containing combinations
- Route and formulation compatibility assessment for any proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

