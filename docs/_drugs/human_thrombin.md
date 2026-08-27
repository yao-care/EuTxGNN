---
layout: default
title: Human Thrombin
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Human Thrombin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using the provided Evidence Pack, here is the evaluation report.

---

# Human Thrombin: From Topical Hemostasis to Primary Release Disorder of Platelets

## One-Sentence Summary

Human Thrombin is a coagulation-cascade enzyme whose established clinical use is topical/local hemostasis (e.g., surgical bleeding control, endoscopic injection for bleeding gastric varices — see supporting literature below).
The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets** (score **96.95%**), supported by **13 clinical trials** and **20 publications**, but the evidence is largely indirect: Thrombin appears mainly as a **laboratory agonist used to trigger and study platelet secretion**, not as a therapeutic agent for this disease.
No EU marketing authorization is on file for this product in the current dataset, so this candidate should be treated as an early-stage research signal rather than a near-term repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical hemostasis (control of surgical/procedural bleeding) — based on known pharmacological use; no formal EU authorization text is on record for this product |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 96.95% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this product is not available in DrugBank (data gap DG002). Based on known pharmacology, Human Thrombin is a serine protease that catalyzes the final step of the coagulation cascade — cleaving fibrinogen to fibrin — and is also a potent **platelet activator**, signaling through PAR1/PAR4 receptors to trigger platelet shape change, aggregation, and granule (release) secretion. Its efficacy as a topical hemostatic agent (e.g., endoscopic injection for bleeding gastric/esophageal varices, surgical sealants) is well documented in the literature captured in this evidence pack.

"Primary release disorder of platelets" refers to conditions (e.g., storage pool deficiencies) in which platelets fail to properly secrete granule contents upon activation. Because Thrombin is one of the strongest known platelet agonists, it is widely used *experimentally* to activate platelets and thereby reveal or characterize release-phase defects — this is the mechanistic basis for the TxGNN association. However, this is fundamentally a **diagnostic/research-tool relationship**, not a treatment mechanism: Thrombin activates the release pathway to expose a defect, but it does not correct or compensate for the underlying granule/secretion abnormality. None of the associated clinical trials or literature test Thrombin as a therapy for this disease; they use it as a functional assay reagent or study it in unrelated hemostatic contexts (COVID-19 pneumonia, portal hypertension, coagulation factor replacement, etc.).

Given this, the mechanistic plausibility of a *treatment* application is weak despite the high TxGNN score, and the evidence level is appropriately capped at L4 (mechanism/preclinical).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04619693](https://clinicaltrials.gov/study/NCT04619693) | N/A | Terminated | 79 | Biomarker study for dexamethasone response in COVID-19 pneumonia; not directly related to Thrombin or platelet release disorders (relevance grade C). |
| [NCT02850692](https://clinicaltrials.gov/study/NCT02850692) | N/A | Unknown | 60 | Systemic endothelial dysfunction in portal hypertension with cystic fibrosis; focuses on endothelium, not platelet release function (grade C). |
| [NCT03341156](https://clinicaltrials.gov/study/NCT03341156) | Phase 3 | Terminated | 14 | Compares prothrombin complex concentrate vs. standard transfusion in heart transplantation; involves coagulation factor replacement, not Thrombin therapy for this disease (grade C). |
| [NCT04492475](https://clinicaltrials.gov/study/NCT04492475) | Phase 3 | Completed | 969 | ACTT-3: interferon beta-1a + remdesivir vs. remdesivir alone for COVID-19; no direct Thrombin/disease link (grade C). |
| [NCT03603769](https://clinicaltrials.gov/study/NCT03603769) | N/A | Completed | 6 | In vitro/ex vivo anti-inflammatory activity of salmon polar lipids on platelet aggregation; unrelated to Thrombin (grade C). |
| [NCT02528253](https://clinicaltrials.gov/study/NCT02528253) | Phase 3 | Completed | 1832 | Tanezumab for chronic low back pain; no clear link to Thrombin or this disease (grade C). |
| [NCT04808895](https://clinicaltrials.gov/study/NCT04808895) | Phase 3 | Unknown | 204 | Aspirin for prevention of severe COVID-19 pneumonia; addresses platelet activation/thrombosis broadly, not Thrombin therapy (grade C). |
| [NCT05391412](https://clinicaltrials.gov/study/NCT05391412) | Phase 4 | Unknown | 32 | Prophylactic fibrinogen concentrate in pediatric scoliosis surgery; different hemostatic agent and surgical context (grade C). |
| [NCT04640168](https://clinicaltrials.gov/study/NCT04640168) | Phase 3 | Completed | 1010 | ACTT-4: baricitinib + remdesivir vs. dexamethasone + remdesivir for COVID-19; no Thrombin link (grade C). |
| [NCT04401579](https://clinicaltrials.gov/study/NCT04401579) | Phase 3 | Completed | 1033 | ACTT-2: baricitinib + remdesivir vs. remdesivir alone for COVID-19; no Thrombin link (grade C). |

*Note: none of the 13 trials associated with this predicted indication directly test Human Thrombin as a treatment for platelet release disorders — all graded C (low relevance) or pending in the source data.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Clinical Practice Update | Gastroenterology | AGA guidance on coagulation abnormalities in cirrhosis and appropriate use of pro-/anticoagulant agents. |
| [1321709](https://pubmed.ncbi.nlm.nih.gov/1321709/) | 1992 | Review | Disease-a-Month | Overview of platelet function disorders, including secretion/release-phase defects and thrombin's role in generating the procoagulant platelet surface. |
| [22841202](https://pubmed.ncbi.nlm.nih.gov/22841202/) | 2012 | Review | Transplantation Proceedings | Review of coagulopathy management, including thrombin-related clotting factor dynamics, during liver transplantation. |
| [984037](https://pubmed.ncbi.nlm.nih.gov/984037/) | 1976 | Basic Science | American Journal of Hematology | Demonstrates thrombin-induced platelet activation and release of arachidonic acid intermediates — foundational evidence of thrombin as a platelet secretagogue. |
| [2016486](https://pubmed.ncbi.nlm.nih.gov/2016486/) | 1991 | Review | Journal of the American College of Cardiology | Discusses the role of platelets and thrombin in hyperplasia/restenosis after coronary angioplasty. |
| [33749992](https://pubmed.ncbi.nlm.nih.gov/33749992/) | 2021 | Review | Wound Repair and Regeneration | Reviews thrombin/calcium-activated platelet gels for wound healing, highlighting thrombin's role in triggering platelet granule release. |
| [35226963](https://pubmed.ncbi.nlm.nih.gov/35226963/) | 2022 | Review | Hamostaseologie | Genetic diagnostic approaches for hereditary hemorrhagic, thrombotic, and platelet (release) disorders. |
| [12839267](https://pubmed.ncbi.nlm.nih.gov/12839267/) | 2003 | Review | Canadian Journal of Physiology and Pharmacology | Discusses thrombin as a stimulus for endothelin release in pulmonary embolism pathophysiology. |
| [35344028](https://pubmed.ncbi.nlm.nih.gov/35344028/) | 2022 | Review | The Biochemical Journal | Reviews immunothrombosis, including thrombin/tissue-factor pathways relevant to disseminated intravascular coagulation. |
| [23839295](https://pubmed.ncbi.nlm.nih.gov/23839295/) | 2013 | Basic Science | Current Opinion in Hematology | Characterizes tissue factor pathway inhibitor isoforms that modulate thrombin generation and platelet procoagulant activity. |

*Literature predominantly consists of mechanistic/basic-science reviews describing thrombin's biological role in platelet activation, rather than clinical evidence of therapeutic benefit for this specific disorder.*

---

## Other Candidate Indications (Context)

This Evidence Pack contains 10 TxGNN-predicted indications for Human Thrombin. Notably, the rank-1 prediction discussed above has the highest model score but the weakest treatment rationale. In contrast, **rank 8 ("esophageal disease," score 86.5%)** has the strongest real-world clinical evidence in this pack — evidence level **L2**, including a Phase 3 RCT ([NCT01717612](https://clinicaltrials.gov/study/NCT01717612): Histoacryl vs. Thrombin for acute gastric variceal bleeding) and a systematic review/meta-analysis ([PMID 33728506](https://pubmed.ncbi.nlm.nih.gov/33728506/): "Safety and Efficacy of Thrombin for Bleeding Gastric Varices"). This reflects Thrombin's already-established off-label/local use in endoscopic hemostasis rather than a genuinely novel repurposing hypothesis, and may warrant separate evaluation as a formulation/label-extension opportunity rather than a new-mechanism candidate.

Ranks 2–7, 9, and 10 (Glanzmann thrombasthenia, pseudo-von Willebrand disease, non-syndromic esophageal malformation, hereditary thrombocytopenia, collagen-receptor bleeding disorders, Scott syndrome, fetal/neonatal alloimmune thrombocytopenia, platelet-type bleeding disorder) are all evidence level L4–L5 and were assessed as "Hold" or "Research Question" in the source scoring — Thrombin appears in each mainly as a laboratory activation reagent used to characterize the underlying platelet defect, not as a proposed treatment.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for "Primary Release Disorder of Platelets" is high (96.95%), the supporting evidence is entirely mechanistic/laboratory-based (L4) and describes Thrombin as a platelet-activation reagent used to *reveal* release-phase defects, not as a therapy that corrects them. No clinical trial or publication in this pack tests Thrombin as a treatment for this disease, so the repurposing hypothesis is not yet clinically actionable.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official regulatory labeling (warnings, contraindications) before any safety pre-assessment (S1) can proceed
- Resolve DG002 (High): obtain confirmed mechanism-of-action data from DrugBank/product labeling
- A preclinical proof-of-concept study specifically testing whether Thrombin (or a thrombin-receptor agonist) can therapeutically compensate for platelet release/secretion deficits, rather than merely inducing/exposing them
- Clarification of achievable routes of administration and formulation, given the original established use is local/topical rather than systemic
- If pursuing a repurposing pathway, consider evaluating rank-8 "esophageal disease" (L2 evidence, existing Phase 3 RCT and systematic review) as a more mature and lower-risk candidate than the top TxGNN-scored indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

