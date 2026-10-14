---
layout: default
title: Capecitabine
parent: AI Predictions (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal, Gastric and Breast Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)

## One-Sentence Summary

Capecitabine is an oral chemotherapy drug that the body converts to 5-FU. It was originally authorised in the EU for colon, colorectal, gastric and breast cancer.
The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach**, but there are currently **0 clinical trials** and **0 publications** linked to this specific condition. The high score mostly reflects capecitabine's existing approval for advanced gastric cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjuvant treatment of stage III (Dukes' stage C) colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), and locally advanced or metastatic breast cancer |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 5 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, capecitabine is a prodrug of 5-FU that inhibits thymidylate synthase, blocking DNA synthesis in rapidly dividing tumour cells. Its efficacy in gastric cancer is already established, so it may mechanistically apply to related gastric tumours.

The predicted condition is a syndromic form of gastric adenocarcinoma. The model's high score largely reflects this overlap with the approved gastric cancer indication, so this is closer to on-label use than true repurposing. No trials or publications address this rare subtype, so nothing shows that capecitabine works specifically in it.

For context, the data compiled for this report also cover other gastric subtypes with more support:
- **Gastric tubular adenocarcinoma** has L1 evidence, including Phase 3 trials such as CLASSIC (adjuvant capecitabine plus oxaliplatin).
- **Gastric cardia adenocarcinoma** has L2 evidence from completed Phase 2 trials.
- **Gastric body carcinoma** has L1 evidence, including a Phase 3 trial with a fluoropyrimidine/platinum backbone.

All of these largely reflect the labelled gastric use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

All five EU authorisations are cancelled, so none is currently valid.

| Authorization Number | Product Name | Approved Indication |
|---------|------|-----------|
| EMEA/H/C/000316 | Xeloda | Adjuvant stage III colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), breast cancer (with docetaxel or as monotherapy)... |
| EMEA/H/C/002605 | Ecansya (previously Capecitabine Krka) | Adjuvant stage-III colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), breast cancer... |
| EMEA/H/C/002568 | Capecitabine Medac | Adjuvant stage-III colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), breast cancer... |
| EMEA/H/C/002386 | Capecitabine Accord | Adjuvant stage-III colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), breast cancer... |
| EMEA/H/C/002362 | Capecitabine Teva | Adjuvant stage III colon cancer, metastatic colorectal cancer, first-line advanced gastric cancer (with platinum), breast cancer... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Medium (neutropenia and thrombocytopenia are possible; please refer to the SmPC warnings and precautions) |
| Emetogenicity Classification | Low to medium |
| Monitoring Items | Complete blood count with differential, liver and renal function, bilirubin; DPYD (DPD deficiency) status before treatment |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions flagged in the knowledge graph:** The TxGNN knowledge graph links capecitabine to the following conditions as contraindication-type relationships. This comes from the graph, not from label text, so it needs confirmation against the SmPC.
  - Liver disease and hyperbilirubinaemia (including Gilbert syndrome)
  - Gallbladder disease
  - Thrombocytopenia, neutropenia, agranulocytosis and anaemia (including macrocytic anaemia)
  - Impaired renal function
  - Infectious disease
  - Coronary artery disease, sudden cardiac arrest and heart conduction disease
  - Necrotising enterocolitis
  - Stomatitis
  - Dihydropyrimidine dehydrogenase (DPD) deficiency
- **Drug interactions:** The interaction screening returned 100 records. The main ones listed in the data are:
  - Moderate: metronidazole and tinidazole.
  - Minor: antacids (aluminium hydroxide, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide) and levofloxacin.
  - Unknown severity: pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, doxycycline, morphine, atropine, prednisone, hydrocortisone, simvastatin and dolasetron.
  - Warfarin interaction should also be considered, as noted in the supporting rationale.

Please refer to the SmPC for the full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For this specific condition there are no linked trials or publications, the evidence level is L5, and the high model score mainly reflects capecitabine's existing gastric cancer approval. In addition, all five EU authorisations are currently cancelled.

**To proceed, the following is needed:**
- Subtype-specific clinical or case evidence for GAPPS-type gastric adenocarcinoma
- Confirmation of the current EU authorisation status and available products
- Mechanism of action data and the SmPC warnings and contraindications
- A safety plan covering DPYD testing, renal and liver function, and warfarin interaction
- Consideration of better-supported gastric subtypes (tubular adenocarcinoma, cardia adenocarcinoma) as higher-priority candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

