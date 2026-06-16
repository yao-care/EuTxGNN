---
layout: default
title: Cholic Acid
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Cholic Acid
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

# Cholic Acid: From Bile Acid Synthesis Defect to HIV Infectious Disease

## One-Sentence Summary

Cholic acid is a primary bile acid approved internationally (US FDA Cholbam 2015; EMA Orphacol 2013) for treating bile acid synthesis defects (BASDs), though Taiwan regulatory records show no current authorization.
The TxGNN model ranks **HIV infectious disease** as its top novel repurposing candidate, with a prediction score of 99.79%.
However, supporting evidence is limited to **0 clinical trials** and **9 in vitro or review publications**, with one study demonstrating that cholic acid derivatives paradoxically enhance HIV replication — making the overall signal insufficient for further development at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bile acid synthesis defects (data gap in Taiwan registry; approved internationally for BASD) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cholic acid (sodium cholate) is a primary bile acid with amphiphilic, detergent-like properties. Its molecular structure — a steroid core bearing three hydroxyl groups and a carboxylic acid side chain — allows it to interact with and disrupt lipid bilayer membranes. This surfactant mechanism provided the theoretical basis for early exploration of cholic acid as an antiviral agent: HIV-1 is a lipid-enveloped virus that could theoretically be inactivated by membrane disruption at the point of mucosal entry.

Early in vitro work from the 1980s–1990s appeared to support this hypothesis. Psychoyos et al. (1993, PMID 7688380) demonstrated that sodium cholate inhibited HIV-1 reverse transcriptase activity in a dose-dependent manner and incorporated it as an active ingredient in the Protectaid contraceptive vaginal sponge alongside low-dose nonoxynol-9 and benzalkonium chloride. Prince et al. (1986, PMID 2870224) further showed that a tri(n-butyl)phosphate + sodium cholate combination could sterilize HTLV-III (HIV) and hepatitis B viruses in blood product preparations.

However, this hypothesis is critically undermined by a 2006 finding (PMID 16610808): amino-functionalized cholic acid derivatives — structurally related compounds — actually **induced** HIV-1 replication and syncytia (multinucleated giant cell) formation in T cells rather than inhibiting infection. This paradoxical result indicates that antiviral activity is highly sensitive to the precise chemical structure and concentration, and that even minor modifications may reverse the biological effect entirely. Detailed mechanism of action data for unmodified cholic acid is currently unavailable (Data Gap DG002). Based on its established pharmacology, cholic acid acts primarily as a bile acid in lipid emulsification and cholesterol catabolism regulation via FXR/SHP signaling — pathways with no direct mechanistic link to HIV therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cholic Acid in HIV infectious disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | In vitro / Animal | Human Reproduction | Sodium cholate shows dose-dependent in vitro inhibition of HIV-1 reverse transcriptase; basis for Protectaid contraceptive sponge development |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro | J Med Chem | Amino-functionalized cholic acid derivatives **enhance** HIV-1 replication and induce syncytia formation in T cells — key contradictory finding that undermines antiviral hypothesis |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro | Lancet | TNBP + sodium cholate sterilizes HBV and HTLV-III in blood product preparations; proof-of-concept for ex vivo antiviral surface activity |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Observational | Pharmacotherapy | HIV patients receiving protease inhibitor therapy show elevated plasma bile acid concentrations; explores hepatotoxicity prediction — cholic acid is a biomarker, not a therapeutic agent here |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | In vitro | Ann NY Acad Sci | Review of anti-STD vaginal contraceptive sponges; sodium cholate cited as active antiviral-spermicidal component |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust NZ J Obstet Gynaecol | Review of contraceptive methods with STD/HIV protection; cholic acid-based sponge among novel approaches discussed |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | Barrier methods and STD/HIV prevention review; Protectaid sponge with sodium cholate mentioned as candidate |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Review | Hepatology | New drugs for NASH in HIV co-infected patients; discusses drug-drug interactions with antiretroviral therapy — bile acids appear as metabolic context only, not as therapeutic agents |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | Methodological | ChemMedChem | Triton X-100 detergent effects on HIV-1 protease inhibitor binding assays; methodological paper — cholic acid not a study drug, minimal therapeutic relevance |

---

## Safety Considerations

Safety information for cholic acid is currently unavailable in the evidence pack (Data Gaps DG001 and DG002). Please refer to the US FDA Cholbam prescribing information or EMA Orphacol SmPC for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for cholic acid in HIV infectious disease consists entirely of in vitro and review literature from the 1980s–1990s, with no clinical trials and a critical 2006 finding demonstrating that structurally related derivatives can paradoxically enhance HIV replication. The conceptual leap from topical/ex vivo antiviral surfactant activity to clinically meaningful systemic HIV therapy has never been tested, and the contradictory mechanistic signals disqualify this from further priority development.

**To proceed, the following would be needed:**
- Resolution of the contradictory syncytia-induction finding (PMID 16610808): determine whether unmodified cholic acid at physiologically achievable concentrations is inhibitory or permissive for HIV replication
- MOA data from DrugBank (Data Gap DG002) to identify any plausible systemic antiviral pathway
- Dose-response in vitro studies with unmodified cholic acid under physiologically relevant conditions and against clinically relevant HIV strains
- Assessment of whether any systemically achievable plasma concentration of cholic acid could exert antiviral effects without hepatotoxicity
- **Priority consideration**: The Rank 5 prediction — **Vitamin Deficiency Disorder / BASD** (L3 evidence, "Proceed with Guardrails") — carries a well-established mechanism, existing regulatory approvals (Cholbam/Orphacol), and multiple observational cohort studies, and represents a far stronger repurposing opportunity for this drug in markets where it is currently unapproved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

