---
layout: default
title: Darifenacin
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Darifenacin
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

# Darifenacin: From Overactive Bladder to Polycystic Kidney Disease 3 with Polycystic Liver Disease

## One-Sentence Summary

Darifenacin is a selective M3 muscarinic receptor antagonist, originally approved for treating overactive bladder (OAB) — a condition marked by urinary urgency, frequency, and urge incontinence.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease (PKD3/PCLD)**, with a prediction score of **96.93%**;
however, **0 clinical trials** specifically address this combination, and the **20 identified publications** describe disease biology broadly rather than testing Darifenacin in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Overactive bladder (urgency, frequency, urge urinary incontinence) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not currently marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacology, Darifenacin acts as a **highly selective M3 muscarinic acetylcholine receptor antagonist**. Its approved use in overactive bladder works by blocking M3 receptors on bladder detrusor muscle, suppressing involuntary contractions and reducing urinary urgency.

The proposed mechanistic connection to PKD3 (caused primarily by *GANAB* gene mutations) rests on an indirect hypothesis: **M3 receptor signaling may modulate cAMP/PKA-dependent pathways in renal tubular epithelial cells**. In polycystic kidney disease, dysregulated cAMP is a central driver of cyst epithelial proliferation and fluid secretion — the same axis targeted by the approved PKD drug tolvaptan (a vasopressin V2 receptor antagonist). A 2025 review further notes that cholinergic signaling intersects with extracellular matrix remodeling and matrix metalloprotease activity, both implicated in cyst progression ([PMID 40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/)).

That said, the biological case remains entirely speculative. No published study has tested Darifenacin in any PKD model — in vitro, in vivo, or clinical. The high TxGNN score likely reflects **topological proximity in the knowledge graph** between M3 receptor nodes and ciliopathy/cystogenesis gene networks (PKD1, PKD2, GANAB share network neighborhoods). Whether M3 antagonism achieves meaningful cAMP suppression in collecting duct cells, or whether it complements tolvaptan's mechanism, requires experimental validation before any development decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darifenacin in polycystic kidney disease 3 with or without polycystic liver disease.

> **Note — higher-priority signal identified:** A Phase 2 trial ([NCT06249867](https://clinicaltrials.gov/study/NCT06249867)) is currently **recruiting** patients to evaluate Darifenacin 15 mg/day in amyotrophic lateral sclerosis (ALS), where respiratory failure is a major downstream outcome (indication rank #10 in this evidence pack, evidence level L2). This is the **only registered trial** for any novel repurposing of Darifenacin, and its results (expected September 2027) represent a more actionable near-term monitoring target.

---

## Literature Evidence

The following publications address polycystic kidney/liver disease biology that is mechanistically relevant to the TxGNN prediction. **None directly study Darifenacin in this indication.**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Clinical Guideline | Am J Gastroenterology | ACG guideline on focal liver lesions; covers diagnosis and management of polycystic liver disease including surgical and transplant thresholds |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Guideline | J Hepatology | EASL Clinical Practice Guidelines on cystic liver disease; addresses ADPKD-associated PCLD, somatostatin analogs, and surgical options |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Landmark ADPKD review; covers systemic complications (liver cysts, intracranial aneurysms, cardiac valvular disease) and emerging cAMP-targeted therapies |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | ADPKD and PCLD genetics and clinical course; tolvaptan slows renal function decline; isolated PCLD vs ADPKD-associated PCLD compared |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | JASN | Eight genes across ADPKD/ADPLD spectrum; GANAB (PKD3-related) associated with both kidney and liver cysts; genetic testing utility discussion |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Expanded genetic spectrum of PKD; PKD1/PKD2 account for ~80% of cases; minor loci including GANAB and their phenotypic severity |
| [40081770](https://pubmed.ncbi.nlm.nih.gov/40081770/) | 2025 | Review | Biochem Pharmacology | ECM dynamics and MMP activity as novel therapeutic targets in ADPKD/ARPKD; cholinergic signaling noted in fibrosis-cyst interaction — most mechanistically relevant to this prediction |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Review | Adv Kidney Dis Health | Polycystic liver disease as most common extrarenal ADPKD manifestation; symptomatic PLD management overview (aspiration, fenestration, transplant) |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annu Rev Pathol | PLD mechanisms from gene mutation → cyst initiation → progression; cAMP, mTOR, and VEGF pathway interactions reviewed |
| [37208103](https://pubmed.ncbi.nlm.nih.gov/37208103/) | 2023 | Review | J Hepatology | Multi-organ (liver + kidney) transplantation outcomes in polycystic liver-kidney disease; immunological considerations and patient selection |

---

## EU Market Status

Darifenacin is **not currently marketed** in this regulatory dataset (market status: 未上市; 0 authorizations on record). No marketing authorization entries were retrieved.

For contextual reference: Darifenacin (brand name Emselex®) previously held EMA authorization for overactive bladder; availability in individual EU markets should be verified against current EMA product databases. The absence of active licensing data means no SmPC-derived safety information was accessible through this pipeline.

---

## Safety Considerations

No formal safety data (TFDA/EMA SmPC warnings or contraindications) was available in this evidence pack (Data Gap DG001). Please refer to the current SmPC for complete safety information.

Based on pharmacological class effects of M3 muscarinic antagonists, the following are relevant to any future development decision:

- **Anticholinergic class effects**: Dry mouth, constipation, blurred vision, urinary retention, cognitive effects (especially in elderly patients)
- **Glaucoma risk**: Anticholinergic-induced mydriasis can precipitate acute angle-closure glaucoma — use with extreme caution or contraindicated in patients with narrow-angle glaucoma; notably relevant given indication rank #9 (primary hereditary glaucoma) carries an explicit safety flag in this evidence pack
- **Respiratory secretion concern**: For the ALS/respiratory failure indication specifically, systemic M3 antagonism may thicken airway secretions by suppressing glandular secretion — a clinically meaningful risk in patients with already-impaired respiratory clearance
- **Drug interactions**: No DDI data was found for Darifenacin in this evidence pack; CYP2D6 and CYP3A4 metabolic interactions are known class concerns and must be evaluated formally

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a high prediction score (96.93%) for Darifenacin in PKD3/PCLD, but this appears to reflect knowledge graph topology rather than direct pharmacological evidence — the M3/cAMP/PKD mechanistic link is biologically plausible but entirely unvalidated. With no preclinical studies, no clinical trials, no direct literature, and no MOA data confirmed, this indication cannot advance beyond a theoretical research question at this stage.

**To proceed, the following is needed:**

- **Preclinical validation (essential first step):** Test Darifenacin in established PKD mouse models (e.g., *Pkd1* or *Ganab* conditional knockouts) to assess cyst volume, kidney weight, and renal function outcomes
- **MOA confirmation:** Verify whether M3 receptor antagonism meaningfully modulates cAMP levels in renal collecting duct cells — this is the core mechanistic premise and must be confirmed in cell-based assays before animal studies (addresses Data Gap DG002)
- **Safety gate:** Retrieve the current EMA SmPC / TFDA package insert for Darifenacin to complete the S1 safety screening before any development investment (addresses Data Gap DG001)
- **Differentiation from tolvaptan:** Determine whether M3 antagonism offers mechanistically additive, complementary, or redundant benefit versus the approved V2 antagonist, and whether combination therapy is feasible
- **Parallel monitoring (higher priority):** The ALS/respiratory failure Phase 2 trial (NCT06249867, recruiting, n=30, expected completion September 2027) represents the only active clinical signal for Darifenacin repurposing. **Monitoring this trial should be prioritized over PKD3 preclinical investment**, as its safety/PK/PD readout will also inform any future novel-indication program.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

