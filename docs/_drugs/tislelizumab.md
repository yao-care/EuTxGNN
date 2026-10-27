---
layout: default
title: Tislelizumab
parent: AI Predictions (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tislelizumab: predicted new indication Mixed-type autoimmune hemolytic anemia (evidence level L5). Approved use: Non-small cell lung cancer (NSCLC)…"
monitor_inn: "Tislelizumab"
predicted_indications: ["mixed-type autoimmune hemolytic anemia", "idiopathic aplastic anemia", "dermatitis", "paroxysmal nocturnal hemoglobinuria", "drug-induced autoimmune hemolytic anemia", "proteinuria", "acne keloid", "neonatal autoimmune hemolytic anemia", "primary CD59 deficiency", "amyopathic dermatomyositis"]
---

# Tislelizumab
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

## Tislelizumab: From Non-Small Cell Lung Cancer to Mixed-Type Autoimmune Hemolytic Anemia
{: .text-alpha }

## One-Sentence Summary

Tislelizumab is a PD-1 immune checkpoint inhibitor, originally used to treat several cancers including non-small cell lung cancer, small cell lung cancer, gastric/gastroesophageal junction adenocarcinoma, oesophageal squamous cell carcinoma and nasopharyngeal carcinoma.
The TxGNN model predicts it may be effective for **mixed-type autoimmune hemolytic anemia**, but **no clinical trials and no publications** currently support this prediction.
The mechanism also argues against it: PD-1 blockade boosts immune activity and is known to cause autoimmune hemolysis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (NSCLC), including resectable high-risk disease, first-line and previously treated advanced disease |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single EU authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tislelizumab is a humanized IgG4 antibody that blocks the PD-1 receptor (PDCD1) on T cells, which releases the brake on anti-tumour immunity. Its efficacy in cancer is established.

The predicted new indication does not follow from this mechanism. Autoimmune hemolytic anemia is driven by autoantibodies that destroy red blood cells. Enhancing T-cell activity through PD-1 blockade would be expected to worsen the disease, not treat it. Immune checkpoint inhibitors are already recognised to cause autoimmune hemolytic anemia as an immune-related adverse event.

The high TxGNN score (0.938) most likely reflects network-level associations in the knowledge graph, such as shared genes or immune pathways, rather than a plausible treatment effect. The same pattern appears in the other top-ranked predictions: other hemolytic anemias, aplastic anemia, paroxysmal nocturnal hemoglobinuria, dermatitis, proteinuria and dermatomyositis. The literature found for dermatitis and proteinuria consists mainly of adverse-event reports, and the others have no supporting evidence at all.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005919 (cancelled) | Tevimbra | Not specified | Non-small cell lung cancer (NSCLC): neoadjuvant/adjuvant treatment of resectable NSCLC at high risk of recurrence, first-line combination therapy for non-squamous and squamous NSCLC, and monotherapy after prior platinum-based therapy... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions. Case reports describe immune-related agranulocytosis. |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report, so please refer to the SmPC for full safety information.

The following points come from the wider literature and mechanism:
- **Immune-related adverse events**: PD-1 blockade can trigger autoimmune and inflammatory reactions. Reports describe severe cutaneous reactions with tislelizumab, including Stevens-Johnson syndrome/toxic epidermal necrolysis and DRESS syndrome, as well as renal toxicity.
- **Hematologic autoimmunity**: Checkpoint inhibitors are reported to cause drug-induced immune hemolysis, so using tislelizumab in autoimmune hemolytic conditions raises particular concern.
- **Drug interactions**: The only interaction record is its pharmacological target, PD-1 (PDCD1). No drug-drug interactions are listed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications. The mechanism points the wrong way, since PD-1 blockade is a plausible cause of autoimmune hemolysis rather than a treatment. The only EU authorization is also cancelled, which further limits any practical route.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that PD-1 blockade benefits autoimmune hemolytic anemia, which currently seems very unlikely
- Detailed mechanism of action data and SmPC safety information (warnings and contraindications)
- Clarification of the EU regulatory status, given that the authorization is cancelled
- If repurposing is still pursued, redirect attention to predictions with a plausible mechanism, and review the safety signals in the dermatitis and proteinuria literature before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

