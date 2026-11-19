---
layout: default
title: Capecitabine
parent: AI Predictions (L5)
nav_order: 125
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-11-20
description: "Capecitabine: predicted new indication Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) (evidence level L5). Approved use: Adjuvant treatment of stage III (Dukes' stage C) colon c…"
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Capecitabine: From Colorectal, Gastric and Breast Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach
{: .text-alpha }

## One-Sentence Summary

Capecitabine is an oral chemotherapy drug licensed in the EU for colon cancer, metastatic colorectal cancer, advanced gastric cancer and breast cancer.
The TxGNN model predicts it may be useful for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**,
but the data compiled for this report contain **no clinical trials and no publications** on this condition, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjuvant treatment of stage III (Dukes' stage C) colon cancer; metastatic colorectal cancer; first-line advanced gastric cancer (with a platinum-based regimen); locally advanced or metastatic breast cancer |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 5 of 6) |
| Number of Authorizations | 6 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for capecitabine: "Capecitabine is metabolized to fluorouracil in vivo. Both normal and tumor cells metabolize fluorouracil to 5-fluoro-2'-deoxyuridine monophosphate (FdUMP) and 5-fluorouridine triphosphate (FUTP). These metabolites cause cell injury by two different mechanisms." ([DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5), label version 2026-02-05; accessed 2026-11-19.) Based on general knowledge, capecitabine is an oral prodrug of 5-fluorouracil. It is converted into the active drug and interferes with DNA and RNA synthesis in rapidly dividing cells, partly by inhibiting thymidylate synthase. Its efficacy in gastric cancer is established by its EU label, so mechanistically it may be applicable to gastric cancers more broadly.

The prediction should be read with caution. Gastric adenocarcinoma is already an approved use of capecitabine (first-line advanced gastric cancer in combination with a platinum-based regimen). The high score probably reflects this known activity, and it is likely inflated by ontology mapping, because the predicted disease name combines a cancer with a hereditary polyposis syndrome. GAPPS is a rare inherited condition linked to APC promoter 1B mutations, with fundic gland polyposis and a predisposition to gastric adenocarcinoma. Any benefit in GAPPS-associated cancer would be extrapolated from sporadic gastric adenocarcinoma, and no GAPPS-specific evidence is provided. This is therefore not a clearly new repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000316 | Xeloda | capecitabine | Valid |
| EMEA/H/C/002362 | Capecitabine Teva | capecitabine | Valid |
| EMEA/H/C/002386 | Capecitabine Accord | capecitabine | Valid |
| EMEA/H/C/002568 | Capecitabine Medac | capecitabine | Valid |
| EMEA/H/C/002605 | Ecansya | capecitabine | Valid |
| EMEA/H/C/002050 | Capecitabine SUN | capecitabine | Withdrawn |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class, oral 5-FU prodrug) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. The knowledge graph links the drug to neutropenia, thrombocytopenia and anaemia as contraindication-type relations. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count, liver and renal function (please confirm against the SmPC) |
| Handling Protection | Follow local cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (these come from the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anaemia, macrocytic anaemia, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, impaired renal function, sudden cardiac arrest, heart conduction disease, necrotizing enterocolitis, stomatitis, and dihydropyrimidine dehydrogenase deficiency.
- **Drug Interactions**: 100 interactions were found in total. The first 20 entries reviewed include two rated Moderate (metronidazole, tinidazole). Several are rated Minor (aluminium hydroxide, levofloxacin, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide). The rest have no rating (for example pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, doxycycline, morphine, atropine, prednisone, simvastatin, hydrocortisone, dolasetron).

The label warnings and contraindications were not available in the compiled data. Please refer to the SmPC for the authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. No trial or publication directly studies GAPPS, so the evidence level is L5. Gastric adenocarcinoma is already covered by the existing label, so the prediction adds little new information.

**To proceed, the following is needed:**
- Clinical or observational data on capecitabine in GAPPS-associated gastric cancer, or confirmation that the disease mapping is only an ontology artefact
- Mechanism of action data from DrugBank
- Label warnings and contraindications from the SmPC, so safety screening can be completed
- Review of the knowledge-graph contraindication relations (especially dihydropyrimidine dehydrogenase deficiency, hepatic and renal impairment) against the label

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

