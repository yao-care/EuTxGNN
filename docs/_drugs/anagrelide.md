---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Anagrelide
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

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a selective PDE3 inhibitor used to reduce platelet counts in patients with essential thrombocythemia (ET), a clonal myeloproliferative neoplasm.
The TxGNN model predicts it may be effective for **Reactive Thrombocytosis**,
with **0 clinical trials** and **10 publications** currently supporting this direction — though existing literature discusses reactive thrombocytosis primarily as a differential diagnosis for ET, not as a direct therapeutic target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Essential Thrombocythemia (clonal myeloproliferative neoplasm) |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Anagrelide works by inhibiting phosphodiesterase type 3 (PDE3) in megakaryocytes. This raises intracellular cyclic AMP (cAMP) levels, which disrupts megakaryocyte maturation and differentiation, resulting in fewer platelets being released into circulation. Critically, this mechanism is fundamentally "platelet count–lowering" and does not distinguish between clonal and reactive origins of thrombocytosis — meaning that, in principle, the drug's action could extend to any condition involving abnormally elevated platelet counts.

The predicted new indication, reactive thrombocytosis, shares the core phenotype of elevated platelet counts with essential thrombocythemia. The biological plausibility is therefore not unreasonable: if cAMP-mediated inhibition of megakaryocyte maturation lowers platelet production in ET, it could theoretically do the same in reactive settings. One case report in the literature (PMID 29851840) even describes Anagrelide being administered peri-operatively to manage extreme post-splenectomy thrombocytosis — a reactive form — suggesting occasional off-label use in specific surgical contexts.

However, the clinical rationale is substantially different from ET. Reactive thrombocytosis is a secondary, typically self-limiting response to underlying triggers such as infection, inflammatory disease, iron deficiency, or tissue trauma. Standard clinical guidance does not recommend direct platelet-lowering therapy in this setting, as the elevated platelets rarely cause thrombotic events and resolve once the primary cause is treated. None of the 10 identified publications specifically evaluate Anagrelide as a treatment for reactive thrombocytosis as a primary indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | Drug profile of Anagrelide: PDE3 inhibition reduces platelet production; notes reactive thrombocytosis as a condition not requiring intervention, distinguishing it from clonal thrombocytosis |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Systematic Review | Leukemia & Lymphoma | Critical review of Anagrelide in ET; randomized trial showed hydroxyurea superior; reactive thrombocytosis discussed as distinct entity requiring no cytoreductive therapy |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Australia | ET management overview; diagnosis requires exclusion of reactive thrombocytosis; platelet-lowering therapy (including Anagrelide) recommended for ET with counts >1000×10⁹/L |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | Clinical spectrum of thrombocytosis; reviews cytokine regulation of megakaryopoiesis; distinguishes pseudothrombocytosis, reactive thrombocytosis, and essential thrombocythemia |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leukemia Research | Role of thrombocytapheresis for hyperthrombocytosis in myeloproliferative neoplasms; Anagrelide cited as cytoreductive maintenance option; thrombocytapheresis reserved for emergent platelet reduction |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective Cohort | Pediatric Blood & Cancer | Pediatric ET vs. reactive thrombocythemia in 12 cases; Anagrelide used as treatment for confirmed ET cases; reactive thrombocytosis managed conservatively |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | Eur J Case Rep Intern Med | Acute MI in ET patient on Anagrelide; highlights residual thrombotic risk despite platelet control; raises concern about cardiovascular safety of Anagrelide |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Digit replantation in post-splenectomy thrombocytosis patient; Anagrelide used peri-operatively to manage extreme reactive thrombocytosis in a surgical context — most direct example of reactive thrombocytosis use |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski arhiv | ET co-existing with ankylosing spondylitis; reactive mild thrombocytosis common in AS; Anagrelide used for the concurrent ET component |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | Japanese ET diagnosis and treatment guidelines; Anagrelide listed as megakaryocyte suppressor alongside busulfan, hydroxyurea, and IFN-α; reactive thrombocytosis delineated in differential diagnosis |

---

## Taiwan Market Information

Anagrelide is currently not approved for marketing in Taiwan (0 authorizations on record). No product licenses are available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Anagrelide's PDE3/cAMP mechanism is biologically capable of lowering platelet counts regardless of etiology, reactive thrombocytosis is a self-limiting secondary condition for which cytoreductive therapy is not standard practice — the priority is treating the underlying cause, not the platelet count itself. The available literature provides no clinical trial data and only indirect, differential-diagnosis–level discussion of reactive thrombocytosis in the context of Anagrelide use.

**To proceed, the following is needed:**
- Define a specific high-risk reactive thrombocytosis subpopulation where direct platelet reduction is clinically justified (e.g., extreme post-splenectomy thrombocytosis, prolonged reactive thrombocytosis with symptomatic thromboembolism risk, surgical/peri-operative settings)
- Obtain full MOA documentation from DrugBank (PDE3 inhibition pathway, cAMP cascade details)
- Obtain Taiwan prescribing information: key warnings, contraindications, and drug interactions (currently all absent)
- Conduct a targeted literature search for Anagrelide in post-splenectomy or surgery-related reactive thrombocytosis specifically, as PMID 29851840 suggests this niche may have precedent
- If niche is confirmed, design a small prospective case series before committing to a full clinical repurposing program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

