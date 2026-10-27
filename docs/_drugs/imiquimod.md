---
layout: default
title: Imiquimod
parent: AI Predictions (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imiquimod: predicted new indication Pre-malignant neoplasm (evidence level L5). Approved use: External genital and perianal warts (condylomata acuminata)…"
monitor_inn: "Imiquimod"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

## Imiquimod: From Actinic Keratosis and Genital Warts to Pre-malignant Neoplasm
{: .text-alpha }

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for external genital and perianal warts, small superficial basal cell carcinomas and actinic keratosis.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**,
with **2 clinical trials** (one small and completed, one terminated early) and **9 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | External genital and perianal warts (condylomata acuminata), small superficial basal cell carcinomas, and actinic keratoses on the face or scalp in adults |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 (see note below) |
| EU Market Status | ✗ Cancelled only (no currently valid authorization) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Under the strict rule (≥2 completed Phase 3 RCTs), the evidence is weaker than L1. Only one Phase 3 trial is completed, and it is open-label and not randomized. The second Phase 3 RCT was terminated after 9 participants. The L1 label comes from the upstream scoring, but a conservative reading would place this closer to L2–L3. The decision below reflects that caution.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in the data compiled for this report. Based on the published rationale, imiquimod is a Toll-like receptor 7 (TLR7) agonist. It triggers local innate and adaptive immune activation (interferon-alpha, TNF-alpha, IL-12), which promotes clearance of dysplastic and virally transformed epithelium.

Its approved uses, actinic keratosis (itself a pre-malignant skin lesion), superficial basal cell carcinoma and HPV-related warts, already sit close to "pre-malignant neoplasm". The same immune-driven mechanism could plausibly act on other intraepithelial neoplasias (cervical, vulvar, anal, penile). The literature includes Cochrane reviews of anal and vulval intraepithelial neoplasia and case reports of success in vulvar intraepithelial neoplasia and Bowenoid papulosis.

The supporting trials are small, and one was terminated early. Confirmatory evidence outside the approved indications is therefore limited.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream applied 3 days per week in 1 or 2 cycles for actinic keratoses on the head, assessing how long the effect lasts. Small, and overlaps the approved indication. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod versus standard excision (LLETZ) for high-grade cervical intraepithelial neoplasia. Terminated with only 9 participants, so it cannot support efficacy conclusions. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant, HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant skin lesion, including topical options |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including imiquimod |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade vulval intra-epithelial neoplasia with imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Clearance of Bowenoid papulosis of the penis with topical imiquimod 5% |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical (animal) | Urol Oncol | Pharmacokinetics of two investigational TLR7 agonists in a rat bladder model |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000179 (cancelled) | Aldara | Cream | Imiquimod cream is indicated for the topical treatment of: External genital and perianal warts (condylomata acuminata) in adults. Small superficial basal... |
| EMEA/H/C/002387 (cancelled) | Zyclara | Cream | Zyclara is indicated for the topical treatment of clinically typical, non-hyperkeratotic, non-hypertrophic, visible or palpable actinic keratosis of the... |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** photoparoxysmal response, photosensitivity disease, autoimmune disease, graft versus host disease and sunburn. These come from drug-disease contraindication links in the TxGNN knowledge graph and should be verified against the SmPC.
- **Drug Interactions:** 59 potential interactions were identified in the DDI database, none with a graded severity. Examples include pantoprazole, omeprazole, prednisone, prednisolone, warfarin, clopidogrel, simvastatin and hydroxychloroquine. Clinical significance needs confirmation.
- **Literature safety signals:** Case reports describe lichen planopilaris and erythema multiforme after topical imiquimod. These come from other indications but are relevant to safety monitoring.

Please refer to the SmPC for the full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score is very high and the mechanism is plausible. Pre-malignant lesions, such as actinic keratosis, are already within the approved use. However, the direct trial evidence is thin: one small open-label Phase 3 study that is largely an approved-indication trial, and one randomized trial terminated at 9 patients. Both EU authorizations are cancelled, so any development would need a new regulatory pathway.

**To proceed, the following is needed:**
- Adequately powered randomized trials in a defined off-label pre-malignant setting (for example, high-grade cervical, vulvar or anal intraepithelial neoplasia)
- Mechanism-of-action data from DrugBank to complete the mechanistic analysis
- EMA label warnings and contraindications, which are required for safety screening
- Review of the knowledge-graph contraindication flags (photosensitivity, autoimmune disease, graft versus host disease)
- Clarification of the regulatory route, given the cancelled EU status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

