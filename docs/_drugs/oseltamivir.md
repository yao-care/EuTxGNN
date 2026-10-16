---
layout: default
title: Oseltamivir
parent: AI Predictions (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Oseltamivir: predicted new indication Pyelonephritis (evidence level L5). Approved use: Treatment and post-exposure prevention of influenza in adults and chi…"
monitor_inn: "Oseltamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism", "teratogenic Pierre Robin syndrome", "disorder of phenylalanine metabolism", "tetrahydrobiopterin-responsive hyperphenylalaninemia/phenylketonuria", "staphylococcus aureus infection", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency", "pneumonia", "streptococcal pneumonia", "aspergillosis, susceptibility to"]
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Oseltamivir is an antiviral used to treat and prevent influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but **no clinical trials** and only **1 publication** (an unrelated review of influenza in pregnancy) support this prediction, so it is a model output only.
Among the other top-ranked predictions, only **pneumonia** has substantial trial and literature evidence, and that evidence reflects the existing influenza indication rather than a new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment and post-exposure prevention of influenza in adults and children, including infants during a pandemic |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Oseltamivir is known to be a viral neuraminidase inhibitor. It is effective against influenza, but it has no recognized antibacterial activity.

Pyelonephritis is usually a bacterial infection of the kidney and urinary tract. There is no plausible mechanistic link between inhibiting viral neuraminidase and treating it. The only article retrieved concerns influenza in pregnancy and does not address pyelonephritis. The high TxGNN score (97.85%) most likely reflects an indirect association in the knowledge graph rather than a real pharmacological signal.

The other top predictions follow the same pattern. Disorders of tyrosine and phenylalanine metabolism, Pierre Robin syndrome, phenylketonuria and mitochondrial cardioencephalomyopathy have no supporting trials and no plausible mechanism. Three predictions tied to infection have some indirect rationale:
- **Pneumonia** (rank 8): oseltamivir reduces influenza and its complications, including influenza-associated pneumonia, but this falls within the approved influenza indication. In COVID-19 pneumonia, oseltamivir appears only as a comparator or add-on arm, with no demonstrated benefit.
- **Streptococcal pneumonia** (rank 9) and ***Staphylococcus aureus* infection** (rank 6): these involve secondary bacterial superinfection after influenza. Antiviral treatment may reduce the viral trigger, but this supports treating influenza and not a new antibacterial indication.
- **Aspergillosis susceptibility** (rank 10): preclinical work suggests oseltamivir may increase susceptibility to pulmonary aspergillosis in mice, which points to potential harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials are registered for pyelonephritis.

For reference, the highest-ranked prediction with trials is pneumonia. Those trials mostly reflect the existing influenza indication or COVID-19 studies in which oseltamivir is a comparator:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00707941](https://clinicaltrials.gov/study/NCT00707941) | Phase 3 | Completed | 1190 | Oseltamivir for illness duration, viral shedding and household transmission in influenza (Dhaka, Bangladesh); within the existing influenza indication |
| [NCT01248715](https://clinicaltrials.gov/study/NCT01248715) | Phase 4 | Completed | 1107 | Empiric antiviral treatment for hospitalized community-acquired pneumonia during influenza season |
| [NCT04338698](https://clinicaltrials.gov/study/NCT04338698) | Phase 3 | Completed | 550 | COVID-19 platform trial comparing hydroxychloroquine, oseltamivir and azithromycin; oseltamivir is one of several arms |
| [NCT04255017](https://clinicaltrials.gov/study/NCT04255017) | Phase 4 | Unknown | 400 | Abidol, oseltamivir and lopinavir/ritonavir in COVID-19 pneumonia |
| [NCT00936013](https://clinicaltrials.gov/study/NCT00936013) | Phase 4 | Unknown | 400 | Chinese medicinal herbs plus oseltamivir vs oseltamivir alone in H1N1 pneumonia |
| [NCT04558463](https://clinicaltrials.gov/study/NCT04558463) | Phase 3 | Unknown | 100 | Favipiravir vs oseltamivir (comparator) as adjuvant therapy in COVID-19 |
| [NCT04973462](https://clinicaltrials.gov/study/NCT04973462) | Phase 4 | Unknown | 80 | Triazavirin vs oseltamivir (comparator) in COVID-19 |
| [NCT04516915](https://clinicaltrials.gov/study/NCT04516915) | Phase 2 | Completed | 38 | IMU-838 plus oseltamivir vs oseltamivir in COVID-19 |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20000 | REMAP-CAP adaptive platform trial in community-acquired pneumonia |
| [NCT04381936](https://clinicaltrials.gov/study/NCT04381936) | Phase 3 | Recruiting | 70000 | RECOVERY platform trial; includes an oseltamivir arm for influenza |

## Literature Evidence

For pyelonephritis, the only retrieved article is an unrelated review. For reference, the key publications for the pneumonia-related predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse Med | Influenza and pregnancy; does not address pyelonephritis (the only article for the top prediction) |
| [24718923](https://pubmed.ncbi.nlm.nih.gov/24718923/) | 2014 | Cochrane systematic review | Cochrane Database Syst Rev | Neuraminidase inhibitors for preventing and treating influenza in adults and children |
| [22513907](https://pubmed.ncbi.nlm.nih.gov/22513907/) | 2012 | Cochrane systematic review | Cochrane Database Syst Rev | Neuraminidase inhibitors for influenza in children (published trials only) |
| [23082123](https://pubmed.ncbi.nlm.nih.gov/23082123/) | 2012 | Cluster RCT | PLoS One | Treatment only vs treatment plus prophylaxis with oseltamivir during influenza outbreaks in aged care facilities |
| [40050867](https://pubmed.ncbi.nlm.nih.gov/40050867/) | 2025 | Review | Virol J | Antiviral treatment for viral pneumonia, including oseltamivir |
| [36752709](https://pubmed.ncbi.nlm.nih.gov/36752709/) | 2023 | Review | Curr Opin Infect Dis | Review of marketed influenza antivirals and their clinical effects |
| [15243927](https://pubmed.ncbi.nlm.nih.gov/15243927/) | 2004 | Mouse model study | J Infect Dis | Oseltamivir improved survival in a mouse model of secondary pneumococcal pneumonia after influenza |
| [12660947](https://pubmed.ncbi.nlm.nih.gov/12660947/) | 2003 | Mouse model study | J Infect Dis | Role of neuraminidase in lethal synergism between influenza virus and *S. pneumoniae* |
| [34095887](https://pubmed.ncbi.nlm.nih.gov/34095887/) | 2021 | Preclinical | Cell Rep Med | Oseltamivir increased susceptibility of mice to pulmonary aspergillosis |
| [21108186](https://pubmed.ncbi.nlm.nih.gov/21108186/) | 2010 | Case report | Ther Umsch | Oseltamivir-induced delirium in a hospitalized H1N1 patient |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000402 | Tamiflu (cancelled) | Not specified | Treatment of influenza in adults and children, including full term neonates, when influenza virus is circulating in the community. Efficacy has been dem... |
| EMEA/H/C/003717 | Ebilfumin (cancelled) | Not specified | Treatment of influenza in patients one year of age and older, and in infants under one year during a pandemic influenza outbreak. Post-exposure preven... |

## Safety Considerations

- **Contraindications (knowledge graph)**: The knowledge graph records a drug-disease contraindication signal with **delirium**. This comes from graph edges, not label text. A published case report of oseltamivir-associated delirium is consistent with this signal.
- **Drug Interactions**: 66 potential interactions were identified, all with an unspecified severity level. Examples include pantoprazole, vancomycin, lactulose, prednisone, simvastatin, metformin, clarithromycin, morphine and ondansetron.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pyelonephritis prediction rests on a model score alone (L5). There are no trials, no relevant literature and no plausible mechanism for a viral neuraminidase inhibitor in a bacterial kidney infection. The pneumonia prediction has an L1 grade, but that grade reflects Phase 3 evidence in influenza, which is the existing indication, and not a new use. Both EU authorizations are cancelled.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- EU SmPC warnings and contraindications (not yet reviewed)
- For any further consideration of pneumonia, a narrow scope limited to confirmed or suspected influenza pneumonia, with no extrapolation to COVID-19 or bacterial pneumonia
- Review of the delirium signal, especially in elderly and critically ill patients
- Verification of the cancelled EU authorization status and its reasons before any regulatory planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

