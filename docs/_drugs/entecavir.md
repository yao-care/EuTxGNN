---
layout: default
title: Entecavir
parent: Medium Evidence (L3-L4)
nav_order: 229
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L4). Approved use: Chronic hepatitis B virus (HBV) infection in adults with compensated…"
monitor_inn: "Entecavir"
predicted_indications: ["HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Entecavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but the supporting evidence is **2 clinical trials** (both about HBV management in HCV/HBV co-infection) and **20 publications**, none showing anti-HCV efficacy.
This prediction is best read as a model artifact rather than a true repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus (HBV) infection in adults with compensated or decompensated liver disease, and in nucleoside-naive paediatric patients aged 2 to <18 years |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (all licenses are recorded as cancelled; this appears inconsistent with the generics and should be verified) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Entecavir is known to be a guanosine nucleoside analogue whose triphosphate form inhibits HBV polymerase (priming, reverse transcription and DNA synthesis). This is the basis of its established use in chronic hepatitis B.

The link to hepatitis C is weak. HCV is an RNA virus whose NS5B polymerase is not a target of entecavir, and entecavir has no recognised anti-HCV activity. The trials linked to this prediction concern patients co-infected with HCV and HBV, where entecavir prevents HBV reactivation during direct-acting antiviral (DAA) therapy for HCV. That is a supportive HBV indication, not treatment of HCV itself. The high TxGNN score most likely reflects network proximity to viral hepatitis in the knowledge graph.

Of note, a randomized trial (PMID 34864158) reports that entecavir prevents HBV reactivation during DAA treatment of HCV/HBV dual infection. This is clinically useful, but it concerns HBV, not HCV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Direct-acting antivirals in HCV/HBV co-infection; studies incidence and predisposing factors of HBV reactivation during anti-HCV therapy |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Randomized study of prophylactic nucleos(t)ide analogue (12 vs 24 weeks) to prevent HBV reactivation in HCV/HBV co-infected patients receiving DAAs |

Both trials address HBV control in co-infection, not entecavir efficacy against HCV.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Randomized trial | Clin Gastroenterol Hepatol | Entecavir prevents HBV reactivation during DAA therapy in HCV/HBV dual infection |
| [28321877](https://pubmed.ncbi.nlm.nih.gov/28321877/) | 2017 | Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of drug treatments for acute hepatitis B |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treatment of HBV/HCV co-infection |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | Management of viral hepatitis B and C in children |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort (66 patients) | Viruses | HCV reactivation in anti-HCV-positive chronic hepatitis B patients after anti-HBV therapy |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Observational | Dig Dis | HBV reactivation in patients treated with DAAs for hepatitis C |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World J Hepatol | Management of hepatitis B and C before and after liver and kidney transplantation |

The literature is centred on HBV and co-infection, and none of it shows entecavir treating HCV.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004377 | Entecavir Viatris (previously Entecavir Mylan) | Not specified | Chronic HBV infection in adults with compensated or decompensated liver disease; also nucleoside-naive paediatric patients aged 2 to <18 years... |
| EMEA/H/C/004458 | Entecavir Accord | Not specified | Chronic HBV infection in adults with compensated or decompensated liver disease; also nucleoside-naive paediatric patients aged 2 to <18 years... |
| EMEA/H/C/000623 | Baraclude | Not specified | Chronic HBV infection in adults with compensated liver disease and active viral replication, or decompensated liver disease... |

All three authorizations are recorded as cancelled, which should be verified against the current register.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): impaired renal function, fatty liver disease, non-alcoholic steatohepatitis, and lactic acidosis.
- **Drug Interactions**: 44 interactions are recorded. The ones listed are all Moderate, including:
  - Acid suppressants: famotidine, ranitidine, cimetidine
  - Metformin
  - Nephrotoxic or renally cleared agents: amphotericin B (including lipid, liposomal and cholesteryl sulfate forms), vancomycin, kanamycin, neomycin, polymyxin B
  - Amoxicillin and levofloxacin
  - Mesalazine, balsalazide, olsalazine and sulfasalazine
  - Orlistat
- **Class effects** noted in the literature: nucleoside analogues can cause myopathy, neuropathy and lactic acidosis, and a case report describes entecavir-associated thrombocytopenia.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir has no recognised activity against HCV, and the supporting trials and publications concern HBV reactivation prophylaxis in co-infection, not treatment of hepatitis C. The high TxGNN score appears to come from network proximity rather than a mechanistic link. Evidence is classed as L4.

**To proceed, the following is needed:**
- Preclinical or in vitro evidence of anti-HCV activity, if any exists
- Clarification of the discrepancy in EU market status (all licenses shown as cancelled)
- Mechanism of action data and SmPC warnings and contraindications
- Consideration of whether the HBV-reactivation-prophylaxis use in HCV/HBV co-infection should be assessed as a separate, supportive indication

---

### Note on Other Predicted Indications

The other predicted indications do not change this recommendation:
- **Hepatitis B virus infection** is the already-labelled indication and works as a positive control. It carries L1 evidence, including Phase 3 trials such as NCT00395018 (liver transplant) and NCT00410072 (entecavir plus tenofovir vs entecavir). It would be a **Proceed with Guardrails** case, but it is not a new indication.
- **HIV infection** has a resistance risk. Entecavir has weak HIV-1 activity and can select for the M184V mutation, so it should not be used as an HIV treatment.
- **Feline AIDS, simian immunodeficiency virus infection, a rare neurodevelopmental disorder, animal viral hepatitis, hepatitis E and hepatitis A** have no supporting evidence of treatment benefit (L5 or HBV-only trials) and remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

