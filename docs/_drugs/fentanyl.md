---
layout: default
title: Fentanyl
parent: AI Predictions (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Management of breakthrough pain in adults already receiving maintenan…"
---

# Fentanyl
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

# Fentanyl: From Cancer Breakthrough Pain to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a strong opioid painkiller, originally used in the EU to manage breakthrough pain in adults with cancer who already receive maintenance opioid therapy.
The TxGNN model's top-ranked prediction is **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but this is a computational signal only, with **0 clinical trials** and **0 publications** supporting it.
Among the other predictions, only myofascial pain syndrome has a related clinical trial (1 Phase 3 study), and it still requires verification.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Management of breakthrough pain in adults already receiving maintenance opioid therapy for chronic cancer pain |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all 3 authorizations cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is generally known as a mu-opioid receptor agonist, and its efficacy in cancer breakthrough pain is established through its authorized products.

For the top prediction, the link is weak. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2). Fentanyl has no established action on this pathway, so no plausible mechanistic link is apparent. The 99.46% score should be read as a model output, not as evidence of benefit.

Other predictions fit the drug's known pharmacology better, but with caveats:
- **Myofascial pain syndrome (score 98.09%)**: Mu-opioid analgesia is plausibly relevant to chronic musculoskeletal pain. One Phase 3 trial exists, but it covers breakthrough pain in non-cancer chronic pain, and its direct relevance to myofascial pain needs verification. Long-term opioid use carries risks of dependence, overdose and hyperalgesia.
- **Tendinitis (score 97.04%)**: The literature mostly concerns postoperative pain after shoulder surgery. This is already covered by fentanyl's analgesic role and is not a true repurposing signal.
- **Trichotillomania (score 98.87%)**: Opioid-system involvement is hypothesized in repetitive behaviors, but the one paper is an indirect opiate sensitivity test. Antagonists (such as naltrexone), not agonists like fentanyl, are used in this area.
- **Tourette syndrome, mania, migraine with brainstem aura, methemoglobinemia, myositis fibrosa and idiopathic granulomatous myositis**: No credible mechanistic or clinical support was found. The retrieved papers on mania and methemoglobinemia are about overdose, case reports or adverse events, not treatment benefit.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (NSIAD). The only trial in the top 10 predictions relates to rank 4, myofascial pain syndrome:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00343733](https://clinicaltrials.gov/study/NCT00343733) | Phase 3 | Completed | 120 | 12-week open-label study with three within-patient double-blind placebo-controlled periods of OraVescent fentanyl citrate for breakthrough pain in opioid-tolerant patients with non-cancer chronic pain. Relevance to myofascial pain needs verification. |

## Literature Evidence

No publications were found for NSIAD. The table below shows the most relevant publications across the other predictions, by priority (RCT > Review > Case report):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23809446](https://pubmed.ncbi.nlm.nih.gov/23809446/) | 2013 | RCT | Arthroscopy | Transdermal fentanyl patch vs subacromial bupivacaine infusion for pain after arthroscopic shoulder surgery (tendinitis prediction; postoperative pain, not the disease itself) |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence (myofascial pain prediction) |
| [12369265](https://pubmed.ncbi.nlm.nih.gov/12369265/) | 2002 | Pharmacological challenge study | Prog Neuropsychopharmacol Biol Psychiatry | Fentanyl-induced prolactin response used as an opiate receptor sensitivity test in stereotypic movement disorder and trichotillomania (indirect evidence) |
| [15102255](https://pubmed.ncbi.nlm.nih.gov/15102255/) | 2001 | Case report | Pain Med | Limited absorption of transdermal fentanyl in two patients with systemic sclerosis, one treated for deltoid tendinitis pain |
| [15839854](https://pubmed.ncbi.nlm.nih.gov/15839854/) | 2005 | Case report | Cephalalgia | Placebo response in chronic migraine with ergotamine overuse (does not support fentanyl efficacy) |
| [37871953](https://pubmed.ncbi.nlm.nih.gov/37871953/) | 2023 | Systematic review | CMAJ | Predictors of overdose after opioid prescription for chronic pain (safety context, not therapeutic evidence for mania) |
| [17923598](https://pubmed.ncbi.nlm.nih.gov/17923598/) | 2007 | Cohort | Arch Intern Med | Benzocaine-induced methemoglobinemia in transesophageal echocardiography (adverse event of another drug, not therapeutic evidence) |

## EU Market Information

All three authorizations are cancelled and none is currently valid.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000959 | Instanyl | Not specified | Management of breakthrough pain in adults already receiving maintenance opioid therapy for chronic cancer pain. Breakthrough pain is a transitory exacerbation... |
| EMEA/H/C/001164 | PecFent | Not specified | Management of breakthrough pain in adults who are already receiving maintenance opioid therapy for chronic cancer pain. Breakthrough pain is a transitory... |
| EMEA/H/C/000833 | Effentora | Not specified | Treatment of breakthrough pain (BTP) in adults with cancer who are already receiving maintenance opioid therapy for chronic cancer pain. BTP is a transitory... |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): hypertension and hypotensive disorders, orthostatic hypotension, long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, chronic obstructive pulmonary disease, asthma, pancreatitis, gallbladder disease, inflammatory bowel disease, benign prostatic hyperplasia, anxiety and related disorders, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were identified. Major-level examples include alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dolasetron, fenfluramine, dexfenfluramine, granisetron and lorcaserin. Moderate-level examples include atropine, cimetidine, dicyclomine, dronabinol, eluxadoline, glycopyrronium and hyoscyamine.
- **Condition-specific concerns**: Strong abuse liability, respiratory depression and overdose risk are particularly unfavorable for chronic or neurodevelopmental conditions such as Tourette syndrome.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (NSIAD) is supported only by a model score, and fentanyl has no plausible link to the AVPR2 pathway. Across the top 10 predictions, no indication has direct evidence of benefit. Myofascial pain syndrome is the most plausible candidate for further research, but its single Phase 3 trial is not yet confirmed as relevant. The drug's EU authorizations are all cancelled, and its safety burden is high.

**To proceed, the following is needed:**
- Mechanism of action data and the full SmPC warnings and contraindications
- Verification of NCT00343733 (intervention, population and results) to determine whether it supports myofascial pain
- For any further pursuit, a targeted literature review and a risk-benefit assessment covering dependence, respiratory depression and the interaction burden
- Confirmation of available formulations and routes of administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

