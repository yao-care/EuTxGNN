---
layout: default
title: Midazolam
parent: Medium Evidence (L3-L4)
nav_order: 406
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Midazolam: predicted new indication Insomnia (evidence level L3). Approved use: Treatment of prolonged, acute…"
monitor_inn: "Midazolam"
predicted_indications: ["insomnia (disease)", "myofascial pain syndrome", "obsessive-compulsive disorder", "tendinitis", "benign paroxysmal torticollis of infancy", "anxiety disorder", "agoraphobia", "myositis fibrosa", "idiopathic granulomatous myositis", "dysthymic disorder"]
---

# Midazolam
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Midazolam: From Prolonged Acute Convulsive Seizures to Insomnia

## One-Sentence Summary

Midazolam is a benzodiazepine, authorised in the EU (as Buccolam) for prolonged, acute convulsive seizures in infants, children and adults.
The TxGNN model predicts it may be effective for **insomnia**, supported by **2 registered clinical trials** (both indirect) and **10 publications**, several of which are older studies of oral midazolam as a hypnotic.
The evidence is suggestive but dated, and it does not yet support a development decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of prolonged, acute, convulsive seizures in infants from 3 months to adults (Buccolam) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Midazolam is a short-acting benzodiazepine that enhances GABA-A receptor signalling, and this class has sedative, hypnotic, anxiolytic and anticonvulsant effects.

The original indication, seizure control, and the predicted indication, insomnia, both depend on dampening excessive neuronal activity through GABA-A receptors. Oral midazolam was studied as a sleep medication in the 1980s and 1990s, including a dose-finding study and a 14-day comparison with flurazepam in chronic insomnia patients. This makes the prediction mechanistically plausible.

There are limits. Midazolam has a short half-life, and benzodiazepines carry tolerance and dependence risks. Better-studied hypnotics are also available, which reduces its current relevance for insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Dexmedetomidine vs midazolam sedation during spinal anaesthesia for transurethral prostatic resection, comparing postoperative sleep quality. This is perioperative sleep, so the link to chronic insomnia is indirect. |
| [NCT00886314](https://clinicaltrials.gov/study/NCT00886314) | NA | Unknown | 80 | Clown doctors vs sedative premedication for anxiety in children undergoing surgery. It addresses preoperative anxiety, not insomnia. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | J Clin Psychopharmacol | Randomised, double-blind, multicentre study of sleep, performance and mood during 14-day use of flurazepam and midazolam in chronic insomnia patients. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | J Clin Psychopharmacol | Executive summary of the same multicentre flurazepam/midazolam study in chronic insomniacs (no abstract available). |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | Clinical study | Br J Clin Pharmacol | Double-blind study of midazolam 15 mg vs Vesparax in 30 patients with insomnia secondary to neuromuscular disease. Both were effective hypnotics, and midazolam was better tolerated. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Dose-finding study | Arzneimittel-Forschung | Multicentre pilot study of oral midazolam 10–30 mg in 75 hospitalised patients with mild to moderate insomnia. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Review of the clinical use of hypnotics and the need for a variety of agents. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orv Hetil | Review of insomnia and cerebral hypoperfusion (general insomnia background). |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002267 (cancelled) | Buccolam | Not specified | Treatment of prolonged, acute, convulsive seizures in infants from 3 months to adults. BUCCOLAM must only be used by parents/carers where the patient has been d... |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: Contraindication links were recorded for chronic obstructive pulmonary disease, liver cirrhosis, angle-closure glaucoma, and chronic kidney disease or renal failure (including end-stage).
- **Drug Interactions**: The interaction query returned 100 entries; the 20 reviewed include these.
  - Moderate: ranitidine, bupropion, aprepitant, morphine, omeprazole, cimetidine, clarithromycin, dronabinol, eluxadoline, nabilone, metoclopramide, miconazole, clotrimazole.
  - Minor: dexamethasone, betamethasone, magnesium oxide, aluminium hydroxide, calcium carbonate.
  - Concomitant opioids and other central nervous system depressants deserve particular attention.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Insomnia has the highest TxGNN score and some direct human data, but the studies are from the 1980s–1990s and the registered trials concern perioperative sleep, not insomnia treatment.
- The only EU authorisation is cancelled, and safety label data are missing.
- Dependence risk and the availability of better-studied hypnotics reduce the case for repurposing.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the SmPC.
- Mechanism of action data from DrugBank.
- A critical review of the 1980s–1990s hypnotic studies against current insomnia treatments.
- Consideration of whether a suitable oral or other hypnotic formulation and route exist.

**Other predicted indications (for reference):** Anxiety disorder has the strongest clinical trial base (L2, many procedural-anxiolysis trials), but this reflects situational perioperative anxiety, not chronic anxiety disorders. Obsessive-compulsive disorder, agoraphobia and dysthymic disorder have only indirect evidence. Myofascial pain syndrome, tendinitis, benign paroxysmal torticollis of infancy, myositis fibrosa and idiopathic granulomatous myositis rest on model prediction alone and have no supporting studies.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

