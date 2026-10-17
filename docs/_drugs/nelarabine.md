---
layout: default
title: Nelarabine
parent: AI Predictions (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nelarabine: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). Approved use: T-cell acute lymphoblastic leukaemia (T-ALL) and T-cell lymphoblastic…"
monitor_inn: "Nelarabine"
predicted_indications: ["relapsing-remitting multiple sclerosis", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "extrahepatic bile duct rhabdomyosarcoma", "pancreatic adenocarcinoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Nelarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Nelarabine: From T-Cell Acute Lymphoblastic Leukaemia to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine is a purine nucleoside analogue originally used to treat relapsed or refractory T-cell acute lymphoblastic leukaemia (T-ALL) and T-cell lymphoblastic lymphoma (T-LBL).
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukaemia (T-ALL) and T-cell lymphoblastic lymphoma (T-LBL) that has not responded to, or has relapsed after, at least two chemotherapy regimens |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Nelarabine is known to be a purine nucleoside analogue that is selectively toxic to T-lymphoblasts, and its efficacy in T-cell malignancies has been established.

The only plausible link is class-level. Other lymphocyte-depleting purine analogues, such as cladribine, are used in multiple sclerosis, so a drug that depletes lymphocytes could in theory resemble them. The prediction is therefore best viewed as a graph-based hypothesis, not a mechanistically supported one.

The hypothesis also has a serious problem. Nelarabine carries a known severe neurotoxicity warning, including demyelination and Guillain-Barré-like ascending neuropathy. Applying it to a demyelinating disease of the central nervous system is highly unfavourable, and the knowledge graph also lists demyelinating disease and inflammatory demyelinating polyradiculoneuropathy among its contraindication-related conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered for relapsing-remitting multiple sclerosis.

## Literature Evidence

Currently no related literature available for relapsing-remitting multiple sclerosis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000752 (cancelled) | Atriance | Not specified | Nelarabine is indicated for the treatment of patients with T-cell acute lymphoblastic leukaemia (T-ALL) and T-cell lymphoblastic lymphoma (T-LBL) whose d... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside antimetabolite) |
| Myelosuppression Risk | High (the knowledge graph links the drug to neutropenia, thrombocytopenia, anaemia and agranulocytosis) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function, and neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions linked to the drug in the knowledge graph (contraindication edges, not label text)**: liver failure, epilepsy, thrombocytopenia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anaemia, macrocytic anaemia, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), impaired renal function, learning disability, intellectual disability, demyelinating disease, and inflammatory demyelinating polyradiculoneuropathy.
- **Drug Interactions**: The interaction query returned 100 records. Among those listed, the **Major** interactions are bupropion, deferiprone, iopamidol, iohexol and samarium (153Sm) lexidronam. **Moderate** interactions include metronidazole, tinidazole, secnidazole, benznidazole, disulfiram, chloroquine, hydroxychloroquine, rosuvastatin, simvastatin, palifermin, strontium-89 chloride, lindane, and the bowel-preparation products picosulfuric acid, sodium sulfate and polyethylene glycol with electrolytes.

Label-based warnings and contraindications are not available in the compiled data. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or literature. Nelarabine's neurotoxicity, including demyelination, runs directly against the proposed use in multiple sclerosis. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Label warnings and contraindications from the EMA product information
- Mechanism of action data
- Preclinical evidence that nelarabine is neurologically safe and active in demyelinating disease models
- A benefit-risk comparison against approved lymphocyte-depleting MS therapies

## Other Predictions (For Reference)

Nine further predictions were reviewed. All are rated **Hold**.

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Hodgkin lymphoma | 98.23% | L4 | Three Phase 2 trials of nelarabine (506U78) in other lymphomas give only indirect support, and none studied Hodgkin lymphoma. Reed-Sternberg cells are B-cell derived. |
| Chronic lymphocytic leukaemia/small lymphocytic lymphoma (two entries) | 98.65% | L5 | Purine analogues are active in CLL as a class, but nelarabine is T-cell selective and CLL is a B-cell disease. The two entries are likely redundant. |
| Rhabdomyosarcoma and its subtypes (vaginal botryoid, extrahepatic bile duct, parameningeal) | 98.0–98.3% | L5 | No mechanistic link or evidence. Parameningeal disease adds concern given the neurotoxicity. |
| Pancreatic adenocarcinoma | 98.07% | L5 | The one linked publication is unrelated to nelarabine, so it provides no support. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

